#主要存在问题是，互换过程中，可能存在多键同值情况，因此在互换前需要进行判断
d1={'zhang':123,'wang':456,'li':123,'zhao':456}
d2={}
#赋予两个值，分别对应名与数两列元素
for name,room in d1.items():
    #若值相同，在值后添加键
    if room in d2:
        d2[room].append(name)
    #若值不同，直接添加键
    else:
        d2[room]=[name]
print (d2)