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
EXPANSION_PBOX_TABLE = [
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

# 압축 P-box 테이블
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

# Parity Drop 테이블
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

# S-box
S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

S3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

S4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

S6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

S7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

S8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]


def substitution(data, table):
    # 가운데 네 비트가 열을 결정
    col_index = int(data[1:5], 2)

    # 앞 뒤 두 비트가 행을 결정
    row_index = int(data[0] + data[5], 2)

    return bin(table[row_index][col_index])[2:].zfill(4) # table 에서 10진수 값을 2진수 문자열로 반환


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
    return permutation(data, EXPANSION_PBOX_TABLE)


def straight_pbox_permutation(data):
    return permutation(data, STRAIGHT_PBOX_TABLE)


def parity_drop_permutation(data):
    return permutation(data, PARITY_DROP_TABLE)


def compression_permutation(data):
    return permutation(data, COMPRESSION_PBOX_TABLE)


def F(half_data, key):
    # Step 1: 48 bit key 와 연산 가능하도록 32 bit 를 48 bit 로 확장
    expanded_data = expansion_permutation(half_data)
    
    # Step 2: key와 xor 연산 수행
    xor_result = bin(int(expanded_data, 2) ^ int(key, 2))[2:].zfill(len(expanded_data))
    
    # Step 3: XOR 연산의 결과를 8부분으로 나눈 뒤 s_box에 입력 후 출력 결과를 모아 32 bit 출력
    s_box_result = ""
    s_boxes = [S1, S2, S3, S4, S5, S6, S7, S8]
    for i in range(8):
        six_bits = xor_result[i * 6:(i + 1) * 6]
        s_box_result += substitution(six_bits, s_boxes[i])
    
    # Step 4: 단순 P-box 연산 수행
    result = straight_pbox_permutation(s_box_result)
    
    return result


def key_generator(initial_key):
    # shifts 칸 만큼 왼쪽으로 이동하는 shift 연산(순환 이동)
    def left_shift(key, shifts):
        return key[shifts:] + key[:shifts]

    # Step 1: Parity Drop 연산 수행
    key_56 = parity_drop_permutation(initial_key)

    # Step 2: 56 bit의 key를 절반으로 나눔
    left_half = key_56[:28]
    right_half = key_56[28:]

    # 1, 2, 9, 16 라운드에서만 1비트 이동; 나머지 2비트 이동
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    round_keys = []
    for shifts in shift_schedule:
        # Step 3: 나누어진 부분에 각각 shift 연산 적용
        left_half = left_shift(left_half, shifts)
        right_half = left_shift(right_half, shifts)

        # Step 4: shift 연산이 적용된 각 부분을 합한 뒤 마지막 전치 연산 수행 후 반환
        round_key = compression_permutation(left_half + right_half)
        round_keys.append(round_key)

    return round_keys

def des_encrypt(data, key):

    # 16개의 Round Key 생성
    round_keys = key_generator(key)

    # Step 1: 초기 순열 수행
    permuted_data = initial_permutation(data)

    # Step 2: 데이터를 왼쪽, 오른쪽으로 나눔
    L0, R0 = permuted_data[:32], permuted_data[32:]

    # Steps 3-18: 라운드 반복 (16번)
    for i in range(16):
        # 1라운드 페이스텔 구조 적용
        R1 = R0
        L1 = bin(int(L0, 2) ^ int(F(R0, round_keys[i]), 2))[2:].zfill(32)

        # 다음 라운드에선 엇갈려서 들어감
        R0, L0 = L1, R1

    # Step 19: 나누어진 부분 결합
    combined_data = L1 + R1

    # Step 20: 최종 순열 적용
    encrypted_data = final_permutation(combined_data)

    return encrypted_data

def des_decrypt(data, key):

    # 16개의 Round Key 생성
    round_keys = key_generator(key)

    # Step 1: 초기 순열 수행
    permuted_data = initial_permutation(data)

    # Step 2: 데이터를 왼쪽, 오른쪽으로 나눔
    L1, R1 = permuted_data[:32], permuted_data[32:]

    # Steps 3-18: 라운드 반복 (16번)
    for i in range(15, -1, -1):
        R0 = R1
        L0 = bin(int(L1, 2) ^ int(F(R1, round_keys[i]), 2))[2:].zfill(32)
        L1, R1 = R0, L0

    # Step 19: 나누어진 부분 결합
    combined_data = L0 + R0

    # Step 20: 최종 순열 적용
    decrypted_data = final_permutation(combined_data)

    return decrypted_data


hex_data = "4E6F772069732074"
bin_data = bin(int(hex_data, 16))[2:].zfill(64)

hex_key = "0123456789ABCDEF"
bin_key = bin(int(hex_key, 16))[2:].zfill(64)

hex_out = "3FA40E8A984D4815"
bin_out = bin(int(hex_out, 16))[2:].zfill(64)

print(f"암호화 전 데이터:  {bin_data}")
print(f"암호화 예상 데이터: {bin_out}")
print(f"암호화 후 데이터:  {des_encrypt(bin_data, bin_key)}")
print(f"암호화 예측 결과 일치 여부: {des_encrypt(bin_data, bin_key) == bin_out}")
print(f"암호화 후 복호화 성공 여부: {des_decrypt(des_encrypt(bin_data, bin_key), bin_key) == bin_data}")
