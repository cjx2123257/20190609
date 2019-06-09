# print('hello,bast')
#
# def jjcfb():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('%s x %s = %s'%( i , j ,i*j),end=('   '))
#         print(' ')
# def maopao():
#     alist = [1,23,12,44,56,78,23,45,57,122,345,345,123,678,1314,535,123,19]
#     for i in range(len(alist)-1):
#         for j in range(len(alist)-i-1):
#             if alist[j] > alist[j+1]:
#                 bkj = alist[j]
#                 alist[j] = alist[j+1]
#                 alist[j+1] = bkj
#     print(alist)

def test1():
    print('test1')
def test2():
    print('test2')
def test3():
    print('test3')
def list1():
    list111 = ['作业',333,'果芽',444,'软件']
    print (list111[3])
    print (list111[0:4])
    list111.pop(0)
    print(list111)
    list111.append(555)
    list111.append('星期日')
    print(list111)
    list111[0] = '777 '
    print(list111)
    print(len(list111))

def jishuhe():
    sum = 0
    for i in range(1,51):
        if i%2 == 1 :
            sum = sum + i
    print(sum)
def jjcfb():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s x %s = %s'%( i , j ,i*j ),end=('   '))
        print('  ')
def lsosh():
    x = 3
    y = 10
    sum = 0
    if x <= y :
        for i in range(x,y+1):
            if i%2 == 0:
                sum = sum + i
    else:
        for i in range(y,x+1):
            if i%2 == 0:
                sum = sum + i
    print(sum)


if __name__ == '__main__':
    test3()
    test1()
    test2()
    list1()
    jishuhe()
    jjcfb()
    lsosh()