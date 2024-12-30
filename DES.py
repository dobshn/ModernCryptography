# 초기 순열 테이블
IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# 최종 순열 테이블
FP_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# 확장 P-box 테이블
EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# 단순 P-box 테이블
STRAIGHT_PBOX_TABLE = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# Parity Drop P-box 테이블
PARITY_DROP_TABLE = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Compression P-box 테이블
COMPRESSION_PBOX_TABLE = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# S1
S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

# S2
S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

# S3
S3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

# S4
S4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

# S5
S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

# S6
S6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

# S7
S7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

# S8
S8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]

def permutation(data, table):
    result = ""

    for i in table:
        result += data[i - 1]

    return result

def initial_permutation(data):
    return permutation(data, IP_TABLE)

def final_permutation(data):
    return permutation(data, FP_TABLE)

def expansion_permutation(data):
    return permutation(data, EXPANSION_TABLE)

def straight_pbox_permutation(data):
    return permutation(data, STRAIGHT_PBOX_TABLE)

def parity_drop_permutation(data):
    return permutation(data, PARITY_DROP_TABLE)

def compression_permutation(data):
    return permutation(data, COMPRESSION_PBOX_TABLE)

def S_Box(data, table):
    col_index = int(data[1:5], 2)
    row_index = int(data[0] + data[5], 2)
    return bin(table[row_index][col_index])[2:].zfill(4)

def F(half_data, key):
    # Step 1: Perform expansion permutation on half_data
    expanded_data = expansion_permutation(half_data)
    
    # Step 2: XOR the expanded data with the key
    xor_result = bin(int(expanded_data, 2) ^ int(key, 2))[2:].zfill(len(expanded_data))
    
    # Step 3: Divide the XOR result into 8 segments of 6 bits each and pass through S-Boxes
    sbox_result = ""
    sboxes = [S1, S2, S3, S4, S5, S6, S7, S8]
    for i in range(8):
        six_bits = xor_result[i * 6:(i + 1) * 6]
        sbox_result += S_Box(six_bits, sboxes[i])
    
    # Step 4: Perform straight P-box permutation on the S-box result
    result = straight_pbox_permutation(sbox_result)
    
    return result

def key_generator(initial_key):
    def left_shift(key, shifts):
        return key[shifts:] + key[:shifts]

    # Step 1: Apply Parity Drop P-box permutation
    key_56 = parity_drop_permutation(initial_key)

    # Step 2: Divide the key into left and right halves
    left_half = key_56[:28]
    right_half = key_56[28:]

    # Schedule of left shifts for 16 rounds
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    round_keys = []
    for shifts in shift_schedule:
        # Step 3: Perform left shifts on both halves
        left_half = left_shift(left_half, shifts)
        right_half = left_shift(right_half, shifts)

        # Step 4: Combine halves and apply Compression P-box permutation
        round_key = compression_permutation(left_half + right_half)
        round_keys.append(round_key)

    return round_keys

def des_encrypt(data, key):

    # Generate the round keys
    round_keys = key_generator(key)

    # Step 1: Perform the Initial Permutation
    permuted_data = initial_permutation(data)

    # Step 2: Split the data into two halves (L0 and R0)
    left, right = permuted_data[:32], permuted_data[32:]

    # Steps 3-18: DES rounds (16 times)
    for i in range(16):
        temp = right
        # Pass right half through F function
        right = bin(int(left, 2) ^ int(F(right, round_keys[i]), 2))[2:].zfill(32)
        left = temp  # Swap halves

    # Step 19: Combine halves (R16 + L16)
    combined_data = right + left

    # Step 20: Apply the Final Permutation
    encrypted_data = final_permutation(combined_data)

    return encrypted_data



hex_data = "4E6F772069732074"
bin_data = bin(int(hex_data, 16))[2:].zfill(64)

hex_key = "0123456789ABCDEF"
bin_key = bin(int(hex_key, 16))[2:].zfill(64)

hex_out = "3FA40E8A984D4815"
bin_out = bin(int(hex_out, 16))[2:].zfill(64)

print(hex_data, hex_key, hex_out)
print(bin_data, bin_key, bin_out)
print(len(bin_data), len(bin_key), len(bin_out))
print(des_encrypt(bin_data, bin_key) == bin_out)