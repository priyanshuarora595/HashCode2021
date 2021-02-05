def out_write(lst):
    for k in range(len(lst)):
        if len(lst[k])>0:
            out.write("\n")
            out.write(str(k+2)+' ')
            for i in lst[k]:
                for j in i:
                    out.write(str(j)+' ')

inp=input("please enter name of the file(the file must be in the same directory) = ")
f=open(inp,'r')
open("output.txt","w").close()
out=open("output.txt",'a')

l=[]
base=[]
ingredients=set()
pizza_list_distinct={}
for i in f.readlines():
    t=i[:len(i)]
    pizza=t.split()
    if len(l)==0:
        base=pizza.copy()
    l.append(pizza)
length=len(l)
del l[0]

for i in range (len(l)):
    pizza_list_distinct[i]=set(l[i][1:])


for j in range(len(base)):
    base[j]=int(base[j])
total_pizzas=base[0]
total_participants=(base[1]*2)+(base[2]*3)+(base[3]*4)
diff=total_participants-total_pizzas
if diff<0:
    diff=total_participants

t2=[]
t3=[]
t4=[]


counter=diff
if total_participants>total_pizzas:
    while diff>0:
        if diff>=4 and base[3]>0:
            base[3]-=1
            diff-=4
        elif diff>=3 and base[2]>0:
            base[2]-=1
            diff-=3
        elif diff>=1 and base[1]>0:
            base[1]-=1
            diff-=2

counter=base[1]*2+base[2]*3+base[3]*4

count=0
counter1=counter

all_pizzas=[]
for j in l:
    t=set(j[1:])
    all_pizzas.append(t)


while counter>0:
    if base[3]>0:
        temp=set()
        i=1
        val=[]
        while len(val)!=4:
            for key,value in pizza_list_distinct.items() :
                if len(val)==0:
                    if all_pizzas[0]==value:
                        temp=temp.union(pizza_list_distinct[key])
                        val.append(key)
                        del pizza_list_distinct[key]
                        del all_pizzas[0]
                        counter-=1
                        break
                else:
                    if len(temp.union(value)) >= (len(temp) + len(value) -1):
                        temp=temp.union(pizza_list_distinct[key])
                        val.append(key)
                        del pizza_list_distinct[key]
                        all_pizzas.remove(value)
                        counter-=1
                        break
        base[3]-=1
        t4.append(val)
        val=[]

    if base[2]>0:
        temp=set()
        i=1
        val=[]
        while len(val)!=3:
            for key,value in pizza_list_distinct.items() :
                if len(val)==0:
                    if all_pizzas[0]==value:
                        temp=temp.union(pizza_list_distinct[key])
                        val.append(key)
                        del pizza_list_distinct[key]
                        del all_pizzas[0]
                        counter-=1
                        break
                else:
                    if len(temp.union(value)) >= (len(temp) + len(value) -1):
                        temp=temp.union(pizza_list_distinct[key])
                        val.append(key)
                        del pizza_list_distinct[key]
                        all_pizzas.remove(value)
                        counter-=1
                        break
        base[2]-=1
        t3.append(val)
        val=[]

    if base[1]>0:
        temp=set()
        i=1
        val=[]
        while len(val)!=2:
            for key,value in pizza_list_distinct.items() :
                if len(val)==0:
                    if all_pizzas[0]==value:
                        temp=temp.union(pizza_list_distinct[key])
                        val.append(key)
                        del pizza_list_distinct[key]
                        del all_pizzas[0]
                        counter-=1
                        break
                else:
                    if len(temp.union(value)) >= (len(temp) + len(value) -1):
                        temp=temp.union(pizza_list_distinct[key])
                        val.append(key)
                        del pizza_list_distinct[key]
                        all_pizzas.remove(value)
                        counter-=1
                        break
        base[1]-=1
        t2.append(val)
        val=[]
    
    else:
        continue

count=(len(t2)+len(t3)+len(t4))

output=[t2,t3,t4]
out.write(str(count))
out_write(output)