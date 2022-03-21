## Author:RavelloH
## 计算1-1/2+1/3-1/4.....+(-)1/n
def pressn():
    n = int(input('n的值为')) + 1 ## 自动补充1
    s = 0
    f = 1   #f为分子
    print("ProgramResulrList:")
    for i in range(1,n):
        s += f / i 
        f = -f
        print("进度:",i,"/",n-1,"\n","分子",f,"\n","结果:",s,"\n")
    print("最终s的值（保留3位）为{:.3f}".format(s))    
    
pressn()
