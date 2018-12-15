# 파이썬 팩토리얼 - 재귀함수 사용

def factorial(n):
    # 1일 경우
    if n <= 1:
        return 1
    # 재귀 함수
    return n * factorial(n - 1)

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

print(factorial(int(input('입  력: '))))
