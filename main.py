class Box:
    def __init__(self,name,roll,score):
        self.name=name
        self.roll=roll
        self.score=score
def namesort(p):
    return p.name
def rollsort(p):
    return p.roll
def scoresort(p):
    return p.score
s=[]
s.append(Box(None, 0, 0))
i=1
while True:
    s.append(Box(None, 0, 0))
    s[i].name = str(input('enter name / 0 to exit: '))
    if s[i].name!='0':
        s[i].roll = int(input('enter roll: '))
        s[i].score = int(input('enter score: '))
        s[i] = Box(s[i].name,s[i].roll, s[i].score)
    else:
        break
    i+=1
s=s[1:-1]
sort=input('to be sorted by name or roll or score: ')
list=[]
if sort == 'name':
    list=sorted(s,key=namesort)
elif sort == 'roll':
    list=sorted(s,key=rollsort)
elif sort == 'score':
    list=sorted(s,key=scoresort,reverse=True)
for i in list:
    print("{: <15} {: <15} {: <10}".format(i.name, i.roll, i.score))