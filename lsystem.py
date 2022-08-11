#姓名:
#列表格式：['F-F-F-F',[['F','FF-F+F-F-FF']]]
import sys
def init():#初始化列表
    global lsys
    lsys=[]
    return lsys
def setBase(lsys,base):#为列表添加一个基础字符串
    base=base
    lsys.append(base)
def addRule(lsys,rule):#为列表添加一个rule
    rules=[rule]
    lsys.append(rules)
def getBase(lsys):#获取列表的基础字符串
    return lsys[0]
def getRule(lsys,ruleIdx):#获取列表的rule
    return lsys[1][ruleIdx]

# Test the L-system functions
'''
def main():
    my_lsys = init()
    setBase( my_lsys, 'A' )
    addRule( my_lsys, ['A','AB'] )
    print(my_lsys)
    print("the base is ", getBase( my_lsys ))
    print("the first rule is ", getRule( my_lsys, 0 ))
if __name__ == '__main__':
    main()
'''
def creatLsystemFile(filename):
    # Create an L-system list by reading in the specified file
    # assign to lsys the result of calling the function init()
    # assign to fp the result of opening the file (use open(filename, "r") )
    # assign to lines the result of calling fp.readlines()
    # close the file using the close method of the file object held in fp
    # for each line in lines
    # assign to line the result of calling line.strip()
    # assign to words the result of calling line.split(' ')
    # if the first item in words is equal to 'base'
    # use the setBase function to make the base string be the second item in words
    # else if the first item in words is equal to 'rule'
    # use the addRule function to add the rule given all but the first item in words
    # return the L-system list lsys
    lsys=init()
    with open(filename,'r')as fp:
        lis=fp.readlines()#一行一行的读取文件内容
        base=lis[1][:-1]#base数据
        lis[3]=lis[3].replace('\n','')
        rule=[]#rule数据
        word=''
        index=0
        for i in lis[3]:
            #print(i,index)
            if i ==' ':
                rule.append(word)
                word=''
                continue
            elif index==len(lis[3])-2:
                word+=i
                rule.append(word)
            word+=i
            index+=1
    #print(lsys)
    setBase(lsys,base)#执行setBase函数
    addRule(lsys,[rule])#执行addRule函数
    return lsys
#lsys=creatLsystemFile('base_rule.txt')
#print(lsys)
def buildString(lsys,n):
    nstring=getBase(lsys)#将getBase（lsys）的结果分配给局部变量（例如nstring）
    rule=getRule(lsys,0)#将getRule（lsys，0）的结果分配给局部变量（例如，规则）
    r1=rule[0][0]#将规则的第一个元素分配给局部变量（例如，符号）
    r2=rule[0][1]#将规则的第二个元素分配给局部变量（例如替换）
    #print(rule,r1,r2)
    for i in range(n):#＃循环n次
        #nstring=nstring.replace('F',r1)
        #nstring=nstring.replace('f',r2)
        try:
            nstring=nstring.replace('F',r1)
            nstring=nstring.replace('f',r2)
        except:
            nstring=nstring.replace('f',r2)
            nstring=nstring.replace('F',r1)
    return nstring

def main():
    #if len(argv)<3:
     #   print("用法：python3 lsystem.py <文件名><num_iterations>")
        #print(sys.argv)
    #lsys_filename=argv[1]
    lsys_filename='base_rule.txt'
    lsys=creatLsystemFile(lsys_filename)#'base_rule.txt'
    #num_iter = int(argv[2])
    num_iter=4
    nstring=buildString(lsys,num_iter)
    #print(nstring)
    return nstring

if __name__ == '__main__':
    main()








