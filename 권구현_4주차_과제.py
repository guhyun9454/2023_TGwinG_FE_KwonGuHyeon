# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    a = {i/2 for i in lst if i%2 == 0}
    return len(a.intersection(lst))

# 2번
def pascal(n):
    lst = []
    for i in range(n):
        U,L =  1,1
        for j in range(i):
            U *= (n-1-j)
        for k in range(i):
            L *= (k+1)
        lst.append(int(U/L))
    return lst

# 3번
def beerRefrigerator(n):
    min_surface = -1
    min_a_b_c = 0
    lst_a = [i for i in range(1,n+1) if n%i == 0]
    b = []
    for a in lst_a:
        lst_ab = int(n/a)
        for b in [j for j in range(1,lst_ab+1) if lst_ab%j == 0]:
            if n % (a*b) == 0:
                c = int(n/(a*b))
                if min_surface == -1 or min_surface > (a*b+b*c+c*a):
                    min_surface = (a*b+b*c+c*a)
                    min_a_b_c = sorted([a,b,c])[::-1]
    return f'{min_a_b_c[0]} X {min_a_b_c[1]} X {min_a_b_c[2]}'

# 4번
def matrixMul(mat1, mat2):
    ans = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                ans[i][j] += mat1[i][k] * mat2[k][j]
    return ans

