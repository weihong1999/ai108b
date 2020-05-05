import random as r

'''
S = NP VP
NP = DET N
VP = V NP
N = dog | cat
V = chase | eat
DET = a | the
'''
SS=['我', '你', '他' , '他們']
VV=['喜歡', '不喜歡', '非常不喜歡', '非常喜歡']
OO=['上課', '吃飯', '睡覺', '打Game']

def S():
    return N() + V() + DET()

def N():
    return r.choice(SS)

def V():
    return r.choice(VV)

def DET():
    return r.choice(OO)

for a in range(5):
    print(S())