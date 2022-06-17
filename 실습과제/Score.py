#과제 2
'''
class Score :
    point = 0
    id = " "

    def __init__(self,id,p=0):
        self.point = p
        self.id = id

    def set(self,p):
        self.point = p

    def get(self):

        return self.point
'''
#과제 3
'''
class Score :
    point = 0
    id = None

    def __init__(self,id,p=0):
        self.point = p
        self.id = id

    def set(self,id):
        self.id = id

    def get(self):
        return self.point

    def getId( self ):
        return self.id
'''
#과제 4

class car :
    color = None
    property = None
    highspeed = 0
    caroption = None
    
    def __init__(self):
        self.caroption = []
        
    def inputcar(self,c,p,h):
        self.color = c
        self.property = p
        self.highspeed = h
        
        self.caroption.append(c)
        self.caroption.append(p)
        self.caroption.append(h)

    def getcolor(self):
        return self.color

    def getproperty(self):
        return self.property
        
    def gethighspeed(self):
        return self.highspeed

    def printcar(self,cou=0):
        print('-' * 20)
        for obj in self.caroption :
            print(obj)
            cou += 1
            if cou % 3 == 0 :
                print('-' * 20)
    

#과제 5
'''
class Score :
    point = 0 # property
    id = None
    
    def __init__(self, i, p=-99 ):
        self.point = p
        self.id = i

    def getId( self ):
        return self.id

    def get( self ) :
        return self.point

    def set( self, p ) :
        self.point = p

class ScoreMgr:
    scores = None

    def __init__(self):
        self.scores = []

    def inputScore(self, i, p ):
        #id = input('학번을 넣어라 : ')
        #p = int(input('점수를 넣어라 : ') )

        s = Score(i, p)

        self.scores.append( s )

        
    def getTotal(self):
        total = 0

        for obj in self.scores :
            total= total + obj.get()

        return total

    def findId(self, i ):
        # i = input('찾을 학번을 입력 : ' )

        for obj in self.scores :
            if obj.getId() == i :
                return obj.get()

        return None
'''    
