'''
7.	有一堆字符串，“welcome to super&Test”，打印出emoclew ot seT&repus……全部单词原位置反转
'''

str01 = 'welcome to super&Test'

list01 = str01.split(' ')
print(list01)
list02 = []
for i in list01:
    str02 = ''
    list03 = list(i)
    print(list03)
    n = len(list03)
    j = 0
    while j < n//2 :
        list03[j],list03[n-1-j] = list03[n-1-j],list03[j]
        j += 1
    for s in list03:
        str02 += s
    list02.append(str02)
print(' '.join(list02))