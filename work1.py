from tkinter import *
'''member=[1,2,3,4,5]
member1=member[:]
member[0]=0
print(member,member1)
该方法直接复制'''
'''列表，并且使当改变新列表中的元素时不改变原来列表的值
若直接member1=member则是将两个列表的地址连到一起，使改变member1的值时也会改变
member的值


member.append(1)
print(member)
start=input('输入开始端')
terminal=input('输入终止端')
del member[int(start):int(terminal)]
print(member)
for i in member:
    if i==2:
        print('find it')
        print('the delete number is %d'%i,)
        member.remove(i)
        print(member)
'''
'''judge=False
root = Tk()
root.geometry('200x200')
root.title('the first attempt')
var=StringVar()
var1=StringVar()
e=Entry(root,show='*')
e.pack()

def calculate():
    global judge
    if judge==False:
        judge=True
        var.set('you hit me')
    else:
        judge=False
        var.set('')
def log_in():
    inp=e.get()
    global var1
    if inp=='1249360629':
        var1.set('pass')
    else:
        var1.set('username error!')



m=Label(root,textvariable=var,bg='green',width=15,height=2,font=('Arial',12))
p=Label(root,textvariable=var1)
a=Button(root,text='quit',width=15,height=2,command=quit)
b=Button(root,text='calculate',width=10,height=2,command=calculate)
pas=Button(root,text='log in',width=8,height=1,command=log_in)




p.pack()
b.pack()
a.pack()
m.pack()
pas.pack()
root.mainloop()
'''
#简单计算器编写
'''window=Tk()
window.title('简单计算器')
window.geometry('400x300')

def evaluate(event):
    data=e.get()
    ans.configure(text='Answer:'+str(eval(data)))


e=Entry(window)
e.bind("<Return>",evaluate)
e.pack()

ans=Label(window)
ans.pack()

window.mainloop()
'''
#制作简单计算器
root=Tk()
root.title('简单计算器')
root.geometry('800x400')

result=StringVar()
result.set('')
result_label=Label(root,textvariable=result,font=('Helvetica',20),width=34,anchor='e')
result_label.grid(column=0,row=1,columnspan=4)


expr=StringVar()
expr.set('')
expr_label=Label(root,textvariable=expr,font=('Helvetica',10),width=64,fg=('#666666'),anchor='e')
expr_label.grid(column=0,row=0,columnspan=4)


judge=True
buttons=(('CE','C','<-','/'),
         ('7','8','9','*'),
         ('4','5','6','-'),
         ('1','2','3','+'),
         ('±','0','.','=')
         )#用元组循坏设置按钮位置
def click(key):
    global judge
    if key=='=':
        resultExpr=expr.get()+result.get()
        resultnum=eval(resultExpr)
        result.set(resultnum)
        expr.set('')
        judge=True
    elif key in'+-*/':
        tempExpr=expr.get()
        if len(tempExpr)>1 and tempExpr[len(tempExpr)-1] in '+-*/':#这里发现如果连续输入两次符号会出现错误，所以进行纠正，保证两个数间仅有一种符号
            expr.set(tempExpr[:-1])
            resultExpr=expr.get()+key
        else:
            resultExpr=result.get()+expr.get()+key
        expr.set(resultExpr)
        judge=True
    elif key=='C':
        result.set('')
        expr.set('')
    elif key=='CE':
        result.set('')
    elif key=='<-':
        oldnum=result.get()
        if len(oldnum)==1:
            newnumber=0
        else :
            newnumber=oldnum[:-1]
        result.set(newnumber)
    elif key=='±':
        tempResult=result.get()
        if tempResult[0]=='-':
            newnumber=tempResult[1:]
        else:
            newnumber='-'+tempResult
        result.set(tempResult)
    else:
        if judge==True:
            result.set(0)
            judge=False
        oldnum=result.get()
        if oldnum=='0':
            result.set(key)
        else:
            newnum=oldnum+key
            result.set(newnum)
for r in range(5):
    for i in range(4):
        def cmd(key=buttons[r][i]):
            click(key)
        b=Button(root,text=buttons[r][i],width=16,command=cmd)
        b.grid(row=r+2,column=i)
root.mainloop()







