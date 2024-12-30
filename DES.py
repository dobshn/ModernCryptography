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

def initial_permutation(data):
    """
    초기 순열을 수행
    :param data: 64 bit 데이터를 문자열로 입력 받음
    :return: IP_TABLE 에 의해 순열이 적용된 64 bit 문자열
    """
    return permutation(data, IP_TABLE)

def permutation(data, table):
    result = ""

    for i in table:
        result += data[i - 1]

    return result