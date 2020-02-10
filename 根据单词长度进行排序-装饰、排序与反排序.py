#DSU模式
##设计函数，对列表内元素跟句单词长度进行排序
def sort_by_length(words):
    #decorate,加入排序元素，长度len
    t=[]
    for word in words:
        t.append(len(word),word)
    #Sort，根据len进行排序
    t.sort(reverse=True)
    #undecorate，去掉len
    res=[]
    for len,word in t:
        res.append(word)
    return res
#匿名函数
#words.sort(key=lambda x:len(x),reverse=True)