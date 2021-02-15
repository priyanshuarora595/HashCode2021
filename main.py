from datetime import datetime

def out_write(lst):
    for k in range(len(lst)):
        if len(lst[k])>0:
            # out.write("\n")
            for i in lst[k]:
                out.write(str(k+2)+' ')
                for j in i:
                    out.write(str(j)+' ')
                out.write("\n")

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)

inf=['a_example.in','b_little_bit_of_everything.in','c_many_ingredients.in','d_many_pizzas.in','e_many_teams.in']
ouf=['a_example.out','b_little_bit_of_everything.out','c_many_ingredients.out','d_many_pizzas.out','e_many_teams.out']
for x in range(5):
    f=open(inf[x],'r')
    open(ouf[x],"w").close()
    out=open(ouf[x],'a')

    l=[]
    base=[]

    ingredients=set()
    pizza_list_distinct_unsorted={}
    pizza_list_distinct=[]
    for i in f.readlines():
        t=i[:len(i)]
        pizza=t.split()
        if len(l)==0:
            base=pizza.copy()
        l.append(pizza)
    length=len(l)
    del l[0]

    for i in range (len(l)):
        pizza_list_distinct_unsorted[i]=set(l[i][1:])
    for k in sorted(pizza_list_distinct_unsorted, key=lambda k: len(pizza_list_distinct_unsorted[k]), reverse=True):
            pizza_list_distinct.append(k)


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
    output=[t2,t3,t4]
    allot=output.copy()
    while counter>0:
        for j in [3,2,1]:
            if base[j]>0:
                temp=set()
                val=[]
                c=0
                while len(val)!=j+1:
                    prev=len(val)
                    m=max(pizza_list_distinct_unsorted.keys())
                    for key in pizza_list_distinct :
                        if prev==0:
                            temp=temp.union(pizza_list_distinct_unsorted[key])
                            val.append(key)
                            del pizza_list_distinct_unsorted[key]
                            pizza_list_distinct.remove(key)
                            counter-=1
                            break
                        else:
                            if len(temp.union(pizza_list_distinct_unsorted[key])) >= (len(temp) + len(pizza_list_distinct_unsorted[key]) -c):
                                
                                temp=temp.union(pizza_list_distinct_unsorted[key])
                                val.append(key)
                                
                                del pizza_list_distinct_unsorted[key]
                                pizza_list_distinct.remove(key)
                                counter-=1
                                break
                        if key==m:
                            c+=1
                    
                base[j]-=1
                allot[j-1].append(val)
                val=[]


    count=(len(t2)+len(t3)+len(t4))

    output=[t2,t3,t4]
    out.write(str(count))
    out.write("\n")
    out_write(output)
    print(x+1,' done')

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("End Time =", current_time)
