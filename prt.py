5


#used for aleatoric quasi-intelligible poetry
import numpy
class Permute:
    def __init__(self, x):
        self.elem=[]
        self.d=0
        for y in x:
            self.elem.append(y)
            if isinstance(y, Permute):
                a=y.d
            else:
                a=-1
            self.d=max(self.d,1+a)
    def copy(self):
        e=[]
        if self.d==0:
            return Permute(self.elem)
        for x in self.elem:
            e.append(x.copy())
        return Permute(e)
    def merge(self):
        if self.d<1:
            return none
        else:
            self.d=self.d-1
            e=[]
            for x in self.elem:
                e.extend(x.elem)
            self.elem=e
    def perm(self):
        self.elem=numpy.random.permutation(self.elem)
    def permute(self,y):
        if self.d>0 and len(y)>0:          
            if y[0]==0:
                self.merge()
                self.permute(y[1:])
            else:
                if y[0]==1:
                    self.perm()
                for x in self.elem:
                   x.permute(y[1:])
    def str(self):
        if self.d==0:
            return self.elem
        else:
            e=[]
            for x in self.elem:
                e.append(x.str())
            return e
def permify(a, dt):
    if dt==0:
        arr=a
    else:
        e=[]
        arr=[]
        for x in a:
            arr.append(permify(x,dt-1))
    re=Permute(arr)
    return re
def sonnet(line):
    p=permify(line,3)
    #randord=[[0,1],[1,1],[1,2],[2,1],[2,2]]
    randord=[[0,0,1],[0,1,1],[2,0,1],[2,2,1],[1,1,1],[1,0,1],[2,1,1],[1,1,2],[1,2,2],[1,2,1],[0,1,2],[2,1,2]]
    s=[]
    for x in randord:
        print(x)
        l=p.copy()
        l.permute(x)
        f=l.str()
        print(f)
        s.extend(f)
    return s
j=[[0]]
#k=[[[['u']],[['r'],['d'],['z']]],[[['ah'],['r']]],[[['f'],['l'],['uh']],[['u']],[['in'],['g']]],[[['a']],[['u'],['t']]],[[['l'],['uh']],[['ee'],['k']]],[[['eh'],['n'],['d']],[['l'],['eh'],['s']]],[[['r'],['eh']],[['ee'],['n']],[['j'],['r'],['ah'],['p'],['s']]],[[['f'],['r'],['uh'],['m']]],[[['uh']]],[[['p'],['eh']],[['ee']],[['p'],['r']]],[[['c'],['uh'],['p']]]]
#k=[[[['th'],['r']],[['t'],['ee']],[['n']]],[[['oo']],[['eh']],[['ee',],['z']]],[[[['uh'],['v']]]],[[['l']],[['ou'],['k']],[['i']],[['n'],['g']]   ]]
#k=[[['s'],['e']],[['l']],[['r']],[['d'],['o']],[['r']]]
k=[[[['u']],[['r'],['d'],['z']]],[[['ah'],['r']]],[[['f'],['l']],[['uh']],[['u']],[['i']],[['n'],['g']]],[[['a']],[['u'],['t']]],[[['l']],[['uh']],[['ee'],['k']]],[[['eh']],[['n'],['d']],[['l']],[['eh'],['s']]],[[['r']],[['eh']],[['ee']],[['n']],[['d'],['r']],[['ah'],['p'],['s']]],[[['f'],['r']],[['uh']],[['m']]],[[['uh']]],[[['p'],['eh']],[['ee']],[['p'],['r']]],[[['c'],['uh'],['p']]]]

po=sonnet(k);
