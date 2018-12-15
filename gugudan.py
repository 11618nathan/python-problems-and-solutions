print('구구단 python')
print('----------------------------------------------')
print('1. 1단 ~ 9단 전체 출력')
print('2. 특정 단 출력')
print('----------------------------------------------')

m= int(input('입력: '))
while m <1 or m>2:
    m = int(input('선택 오류 || 입력:'))
if m==1:
    for m in range(1,10):
        print('='*10)
        for n in range(1,10):
            print(m,'x',n,'=',m*m)
elif m == 2:
    m = int(input('단 입력: '))

    while m < 1 or m > 9:
        m = int(input('선택 오류 || 입력: '))
 
    for n in range(1,10):
        print(m,'x',n,'=',m*n)
