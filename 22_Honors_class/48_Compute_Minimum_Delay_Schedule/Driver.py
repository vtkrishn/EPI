#set of tasks T = [t0, t1,t2,.....tn-1]
#task ti is having duration of Tr

#P is another tasks which needs to be completed before Ti is started

import random
class Task:
    name=''
    child=[]

tasks=[]
for i in range(1,6):
    t = Task()
    t.name = 'Tasks ' + str(i)
    tasks.append(t)

for i in tasks:
    for j in range(random.choice([1,2,3,4,5])):
        if tasks[j].name != i.name:
            if (tasks[j] not in i.child):
                i.child.append(tasks[j])

stack = []
for i in tasks:
    print i.name
    if len(t.child) > 0:
        for k in t.child:
            print '------> ' + k.name
