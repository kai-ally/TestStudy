'''
10.	递归实现斐波那契数列
'''

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input('请输入需要生成的个数：'))
for i in range(n):
    print(fibo(i))