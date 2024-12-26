# 두 정수 a, b를 입력받아 최대 공약수를 반환하는 함수
# 1. r1, r2에 a, b를 대입한다.
# 2. r2가 0이 아닌 동안 다음을 반복한다.
# 3. r1에는 r2를, r2에는 r1 % r2를 저장한다.
# 4. r2가 0이 되면 r1이 최대 공약수가 된다.

def euclidean_gcd(a, b):
    r1, r2 = a, b
    while r2 != 0:
        r1, r2 = r2, r1 % r2
    return r1

print(euclidean_gcd(12, 15))