#request库爬虫性能分析
#尝试使用request爬取www.hao123.com一百次，并给出爬取时间
#由于需要计时，因此需要用到time函数
import requests
import time
url='https://www.hao123.com/'
global time

a=1
start_time=time.time()
while a<=100:
    try :
        r=requests.get(url)
        r.raise_for_status()#防止网络异常
        a+=1
    except :
        print( "something is error")
end_time=time.time()
time=-(start_time-end_time)
print ('the whole time is',time,'s')

