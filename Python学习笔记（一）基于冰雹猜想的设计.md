## 冰雹猜想
考拉兹猜想（Collatz Conjeccture），又称奇偶归一猜想，3n+1猜想，冰雹猜想等
概念：即对于每一个正整数，若为偶数，则除以2，若为奇数，对它乘3加1，最终都能得到1
## 由此进行设计代码验证
验证思路：直接取1-n的数进行循环验证，每个数成功后将会返回一个“true”，不成功即进入死循环
n = int(input('int='))
for i in range(1, n+1):
    while i != 1:
        if i% 2 ==0:
            i=i/2
        else:
            i=i*3+1
    print("true")
##以上成功验证
##一些问题与结论
在pycharm中之前尝试以下，程序运行正确但是没有输出
n = int(input('int='))
for i in range(1, n+1):
    while i != 1:
        if i% 2 ==0:
            i=i/2
            if i==0
            print("true")
        else:
            i=i*3+1
            if i==0
            print("true")
##原因猜测：在while循环中只要i得到1的值即跳出循环，因此while内后续if不进行判断，所以没有输出
n = int(input('int='))
for i in range(1, n+1):
    if i==1
    print("true")
    while i != 1:
        if i% 2 ==0:
            i=i/2
        else:
            i=i*3+1
##原因猜测：同上，当i验证完后直接在for循环进行下一个i+1验证，此时if判断为n+1

总结：其实不需要输出true也可以判断，因为若1-n中存在数不符合该规律程序将会直接报错，while会进入死循环



