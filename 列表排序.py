##输入一系列元素，对列表内元素进行排序
#将获得三行两列列表
students=[['zhang',84],['wang',98],['li',76]]
#首先定义一个函数，即使其得到列表某列元素，方便后续进行排序
def f(a):
    return a[1]
#在sort函数里，reverse表示排序顺序，True即由大到小，默认为从小到大
#key即选取其中元素
students.sort(key= f,reverse=True)
print (students)
##另一种方法，匿名函数
#students.sort(key=lambda x:x[1],reverse=True)