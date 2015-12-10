import turtle

class Point2D:
    '''
        A 2D point that decide some important localtion of a shape;
    '''
    x=0.0
    y=0.0
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
           
    def drawPoint(self):
        '''
            Draw a point with initial property
        '''
        turtle.speed(0)
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.dot(size,color)
        turtle.penup()    
        
    def drawPoint(self,x,y,size=None,color="black"):
        '''
            Draw a point with given property
        '''
        self.x=x
        self.y=y
        drawPoint()
    
        
class Shape():
    def drawLine(self,start,end,color="black"):
        '''
            Draw a line with given property (the start point and end point )
        '''
        turtle.speed(0)
        turtle.color(color)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(start.x,start.y)
        turtle.pendown()
        turtle.goto(end.x,end.y)
        turtle.penup()

    def drawCircle(self,center,radii,color="black"):
        '''
            Draw a circle with given property (the circle center point and radii )
        '''
        turtle.speed(0)
        turtle.color(color)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(center.x,center.y-radii/2)
        turtle.pendown()
        turtle.circle(radii)
        turtle.penup()
        
    def drawRectangle(self,start,end,color="black"):
        '''
            Draw a rectangle with given property(the left-top point and right-bottom point)
        '''
        turtle.speed(0)
        turtle.color(color)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(start.x,start.y)
        turtle.pendown()
        turtle.goto(end.x,start.y)
        turtle.goto(end.x,end.y)
        turtle.goto(start.x,end.y)
        turtle.goto(start.x,start.y)
        
class Man():  
    '''
        A class that draw a man.
    ''' 

    headCenter=0.0
    bodyStart=0.0
    bodyEnd=0.0
    leftarmStart=0.0
    leftarmEnd=0.0
    rightarmStart=0.0
    rightarmEnd=0.0        
    leftlegStart=0.0
    leftlegEnd=0.0    
    rightlegStart=0.0
    rightlegEnd=0.0   
    size=10.0  
    pre_step=0  
    shapePen=Shape()
        
    def __init__(self,center=Point2D(-200,-50),size=50.0):  
        '''
            Some of the property can be initial with given initial parameter
        '''   
        bodyCenter=Point2D(center.x,center.y)
        
        self.size=size
        self.headcenter=Point2D(bodyCenter.x,bodyCenter.y+1.25*size)
        
        self.bodyEnd=Point2D(bodyCenter.x+0.5*size,bodyCenter.y-size)
        self.bodyStart=Point2D(bodyCenter.x-0.5*size,bodyCenter.y+size)
        
        self.leftarmStart=Point2D(self.bodyStart.x,self.bodyStart.y-size/4)
        self.leftarmEnd=Point2D(self.headcenter.x-size*1.5,self.headcenter.y+0.5*self.size)
        
        self.rightarmStart=Point2D(self.bodyEnd.x,self.bodyStart.y-size/4)
        self.rightarmEnd=Point2D(self.headcenter.x+size*1.5,self.headcenter.y+0.5*self.size)        
    
        self.leftlegStart=Point2D(self.bodyStart.x+size/8,self.bodyEnd.y)
        self.leftlegEnd=Point2D(self.bodyStart.x-size/8,self.bodyEnd.y-size*1.5)
        
        self.rightlegStart=Point2D(self.bodyEnd.x-size/8,self.bodyEnd.y)
        self.rightlegEnd=Point2D(self.bodyEnd.x+size/8,self.bodyEnd.y-size*1.5)
        
    def draw(self,step=6,color="black"):
        '''
            Main function that draw the man with circle,rectangle and line
        '''
        if step>0 and self.pre_step<step : 
            self.shapePen.drawCircle(self.headcenter,self.size*0.5,color)
        if step>1 and self.pre_step<step :
            self.shapePen.drawRectangle(self.bodyStart,self.bodyEnd,color)
        if step>2 and self.pre_step<step :
            self.shapePen.drawLine(self.leftarmStart,self.leftarmEnd,color)
        if step>3 and self.pre_step<step :
            self.shapePen.drawLine(self.rightarmStart,self.rightarmEnd,color)
        if step>4 and self.pre_step<step :
            self.shapePen.drawLine(self.leftlegStart,self.leftlegEnd,color)
        if step>5 and self.pre_step<step :
            self.shapePen.drawLine(self.rightlegStart,self.rightlegEnd,color)
            
class Alphabet: 
    '''
        A class that draw all the letter or sentence in the plot.
    ''' 

    alphabet={'A':[0,Point2D(0,0),[20,"green"]],\
              'B':[1,Point2D(0,0),[20,"green"]],\
              'C':[2,Point2D(0,0),[20,"green"]],\
              'D':[3,Point2D(0,0),[20,"green"]],\
              'E':[4,Point2D(0,0),[20,"green"]],\
              'F':[5,Point2D(0,0),[20,"green"]],\
              'G':[6,Point2D(0,0),[20,"green"]],\
              'H':[7,Point2D(0,0),[20,"green"]],\
              'I':[8,Point2D(0,0),[20,"green"]],\
              'J':[9,Point2D(0,0),[20,"green"]],\
              'K':[10,Point2D(0,0),[20,"green"]],\
              'L':[11,Point2D(0,0),[20,"green"]],\
              'M':[12,Point2D(0,0),[20,"green"]],\
              'N':[13,Point2D(0,0),[20,"green"]],\
              'O':[14,Point2D(0,0),[20,"green"]],\
              'P':[15,Point2D(0,0),[20,"green"]],\
              'Q':[16,Point2D(0,0),[20,"green"]],\
              'R':[17,Point2D(0,0),[20,"green"]],\
              'S':[18,Point2D(0,0),[20,"green"]],\
              'T':[19,Point2D(0,0),[20,"green"]],\
              'U':[20,Point2D(0,0),[20,"green"]],\
              'V':[21,Point2D(0,0),[20,"green"]],\
              'W':[22,Point2D(0,0),[20,"green"]],\
              'X':[23,Point2D(0,0),[20,"green"]],\
              'Y':[24,Point2D(0,0),[20,"green"]],\
              'Z':[25,Point2D(0,0),[20,"green"]],\
              ' ':[52,Point2D(0,0),[20,"green"]],\
              '!':[53,Point2D(0,0),[20,"green"]]}
              
    
    size=20
    titleCenter=Point2D(0,0)
    interval=0.0
    
    def __init__(self,center=Point2D(60,-240),interval=10.0,size=10.0,penclr="green"):
        '''
           Init the alphabet to align it to be a line.
        '''
        self.size=size 
        self.interval=interval
        
        self.titleCenter.x=center.x+(-14)*(size+interval) 
        self.titleCenter.y=center.y
       
        
        for letter in self.alphabet:
            self.alphabet[letter][1].y=center.y
            self.alphabet[letter][1].x=center.x+(self.alphabet[letter][0]-12+0.5)*(size+interval)  
            self.alphabet[letter][2][0]=size 
            self.alphabet[letter][2][1]=penclr
                
    def draw(self,letter,unline=False,size=None,center=None,interval=None,color=None):
        '''
            Draw a letter or special symbol in the alphabet 
        '''
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        if center==None:
            center=self.alphabet[letter][1]
        if color==None:
            color=self.alphabet[letter][2][1]
        if size==None:
            size=self.alphabet[letter][2][0]   
        if interval==None:
            interval=self.interval    
        turtle.color(color) 
        turtle.goto(center.x,center.y) 
        turtle.pendown() 
        turtle.write(letter,align="center",font=("Trebuchet MS", size, "normal"))  #write this letter
        if unline :
            turtle.penup()
            turtle.goto(center.x-self.size*0.5,center.y-interval)
            turtle.pendown()
            turtle.goto(center.x+self.size*0.5,center.y-interval)
    
    def drawTitle(self,title,center=None, color="black"):
        '''
            Draw a given title,for example : Congratulation!
        '''
        if center==None:
            center=self.titleCenter
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        turtle.color(color)
        turtle.goto(center.x,center.y)
        turtle.pendown()
        turtle.write(title,align="center",font=("Trebuchet MS",self.size,"normal")) 

    def drawName(self,str,unline=False,size=None,center=Point2D(0,0),color=None):
        '''
            Draw a scientists name,
            if unline=True,then 
                there will be a line below every letter,exclude the space between the first name and family name
        '''
        strlen=len(str)
        for i in range(strlen):
            letterCenter=Point2D(center.x+(i-strlen/2+0.5)*(self.size+self.interval),center.y)
            self.draw(str[i],unline=unline,size=size,center=letterCenter,color=color)        
         
                     

def drawMan(man,step=6):
    '''
    Draws the hangman figure on the screen. You may find it useful to have a global
    variable that keeps track of the number of guesses. This variable will determine which body
    parts to draw.
    '''
    man.draw(step)

def drawAlphabet(alphabet): 
    '''
        Draws all 26 letters of the alphabet on screen, with unused letters in green and guessed 
        letters in red.
    '''
    alphabet.drawTitle("Letters:")  
    for letter in alphabet.alphabet :
        if alphabet.alphabet[letter][0]<26:
            alphabet.draw(letter)
        
def drawGuessSurface(alphabet,guessList,center=Point2D(50,-50),size=10.0,interval=12.0,color="black"):
    '''
        An interface that draw the letter that had been guess in the plot
    '''
    for i,part in enumerate(guessList):
        partCenter=Point2D(center.x+(i-len(guessList)/2+0.5)*(len(part)*size+len(part)*interval),center.y)
        alphabet.drawName(part,unline=True,center=partCenter,color=color)


def drawGuess(alphabet,guess):
    '''
        guess: a string that contain the letter,'_' represent that the letter had not been guessed;
            for example: A_AN T___NG
    '''
    nameList=guess.split(' ')
    for i,namepart in enumerate(nameList):
        nameList[i]=namepart.replace('_',' ')
    drawGuessSurface(alphabet, nameList)   



import random 

allNameList=['ALAN TURING',\
      'DONALD KNUTH',\
      'ADA LOVELACE',\
      'GRACE HOPPER',\
      'GORDON MOORE']     
 
def randomName(nameList):
    '''
        Random to select a name from the name list.
    '''
    return nameList[random.randint(0, len(nameList)-1)]  

def initGuess(name):
    '''
        Init the guess list ;
        that is : init all the letter in the list with _ exclucde the space
    '''
    guessList=[]
    for i in range(len(name)):
        if not name[i].isspace() :
            guessList.append('_') 
        else:
            guessList.append(' ')
            
    return guessList


def updateGuess(name,letter,preGuessList):
    '''
        Updates the data structure that store thet user's guessed at the correct answer.
    '''
    for i in range(len(name)):
        if name[i]==letter:
            preGuessList[i]=letter
    return preGuessList

def hangMinGame():
    '''
        The algorithm of the Game.
    '''
  
    alphabetList=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
                  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    correctLetterList=[]
    incorrectLetterList=[]

    turtle.screensize(640,480) 
  
    turtle.title('HangMan Game')

    man=Man() 
  
    alphabet=Alphabet(size=15,interval=4) 
    drawAlphabet(alphabet)

    name=randomName(allNameList)
    nameList=list(name.replace(' ',''))

    guessList=initGuess(name)
    drawGuess(alphabet,''.join(guessList))

    errorTime=0
    while errorTime<6 and len(correctLetterList)<len(set(nameList)):

        inputLetter=turtle.textinput("Guess a letter","Guess a letter")
        if inputLetter in alphabetList:
   
            inputLetter=inputLetter.upper()[0]

            alphabet.draw(inputLetter, color="red")

            if (inputLetter not in nameList):
                if (inputLetter not in incorrectLetterList):
                    errorTime=errorTime+1

                    man.draw(errorTime)

                    incorrectLetterList.append(inputLetter)
            else:
  
                if inputLetter not in correctLetterList:

                    guessList=updateGuess(name,inputLetter,guessList)
                    drawGuess(alphabet,''.join(guessList))
                    correctLetterList.append(inputLetter)

    if errorTime<6:
       
        alphabet.drawTitle("Congratulations!", center=Point2D(0,150), color="green")
    else:
      
        alphabet.drawTitle("You lost! The answer was:", center=Point2D(0,150), color="red")
        alphabet.drawTitle(name, center=Point2D(0,120), color="red")
 
    turtle.delay(5000)
    turtle.up()
    turtle.bye() 
    
import sys
def pyVersionEval():
    '''
        Check tht python version to be upper that 3.3 for the reason that lower version(ie. 2.7.6) does not support turtle.textinput function
    '''
    if sys.version_info < (3, 3):
        raise RuntimeError('At least Python 3.3 is required')
 
def main():
    '''
        main function.
    '''
    pyVersionEval()
    hangMinGame()
if __name__=="__main__":
    main()
    
    
