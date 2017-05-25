import math,random
import pygame,time
import Tkinter as tk
from Tkinter import *
import os


class points(object):
      def __init__(self,x,y,size,color,theta,feq,velo,curveType):
          self.x = x
          self.y = y
          self.size = size # size of the particles
          self.color = color # color of particles
          self.theta = theta# initial phase
          self.feq = feq # frequencey
          self.t = 1/feq # time period
          self.velo = velo # wave velocity
          self.lamda = velo/feq# wavelength
          self.wn = 1/self.lamda # wave number
          self.omega = 2*math.pi*feq # angular frequency 
          self.k = 2*math.pi*self.wn # 'k' is the spatial frequency analogue of angular temporal frequency and is measured in radians per meter
          self.curveType = curveType # Osilation curve
          self.radius = 50 # amplitude of the particle
          self.time = 0.0 # time 
          self.dt = 0.015 # diffrential time
          self.phase = 0.0 # instantaneous phase of the particle
          self.x1,self.y1 = x,y # temporary cords
      def update(self):
          
          self.time += self.dt
          self.curve()
      def get(self):
          return self.x1,self.y1,self.omega
      def setDt(self,dt):
          self.dt = dt
      def setFeq(self,f):
          self.feq += f
          # recalculating factors
          self.t = 1/self.feq
          self.omega = 2*math.pi*self.feq
          self.lamda = self.velo/self.feq
          self.wn = 1/self.lamda
          self.k = 2*math.pi*self.wn
      def curve(self):
          
          self.phase = ((self.theta*math.pi)/180) +((self.omega*self.dt)/180)-(self.time)
          
          if self.curveType == 'sin':
             self.y1 = self.y + math.sin(-self.phase)*self.radius
          if self.curveType == 'cos':
             self.y1 = self.y + math.sin(-self.phase)*self.radius
          if self.curveType == 'log':
             self.y1 = self.y + math.log(-self.phase)*self.radius
def display():
  global Points
  for p in Points:
    pygame.draw.circle(screen,p.color,(int(p.x1),int(p.y1)),int(p.size))
    #pass
def textShow(_str_,qty,pos):
    
    font = pygame.font.SysFont("calibri",20)
    pop = font.render(_str_+" : "+str(qty),True,BLACK)
    screen.blit(pop,pos)
def timeline():
  global Points
  for p in Points:
    p.update()
def genratePoints(num):
    global Points
    j = 0
    for i in range(0,num):
      #          x    y  size color     theta  feq     velo   curve
      p = points(30+j,200,2,(200,100,50),0.0,200.0+i*30,100.0,'sin')
      Points.append(p)
      j+=1

def phaseTransfer():
      for i  in range(0,len(Points)-1):
            Points[i+1].phase = Points[i].phase
def show():
  for p in Points:
      #print p.get()
      textShow('Phi',p.get(),(10,10))
def draw():
    pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    pygame.display.update()
    
def ampAdd():
    for p in Points:
      p.radius += 10
def ampSub():
    for p in Points:
      p.radius -= 10
def feqAdd():
    i = 1
    for p in Points:
      p.setFeq(2*i)
      i+=1
      
def feqSub():
    i = 1  
    for p in Points:
      p.setFeq(-2*i)
      i+=1
      
def buttons():
    button1 = Button(buttonwin,text = 'Draw',  command=draw)
    button1.pack(side=LEFT)
    amp = Label(root,text="Amplitude:")
    amp.pack(side=LEFT)
    button2 = Button(buttonwin,text = '+',  command = ampAdd)
    button2.pack(side=LEFT)
    button2 = Button(buttonwin,text = '-',  command = ampSub)
    button2.pack(side=LEFT)
    amp = Label(root,text="Frequency:")
    amp.pack(side=LEFT)
    button3 = Button(buttonwin,text = '+',  command = feqAdd)
    button3.pack(side=LEFT)
    button4 = Button(buttonwin,text = '-',  command = feqSub)
    button4.pack(side=LEFT)
    root.update()
    
#--------------------------------#
      
# ======================
# initilising the pygame
# ======================

# colors 
WHITE = (254,254,254)
RED = (254,0,0)
BLACK = (0,0,0)
BLUE = (0,0,254)
YELLOW = (254,254,0)


Points = list()


root = tk.Tk()
embed = tk.Frame(root, width = 900, height = 400) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 50, height = 100)
buttonwin.pack(side = TOP)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

# init the pygame 
window = (900,400)
pygame.init()
screen = pygame.display.set_mode(window)
clock = pygame.time.Clock()
screen.fill(pygame.Color(255,255,255))
pygame.display.init()
pygame.display.update()


buttons()
##while True:
##    pygame.display.update()
##    root.update()      

def main():
   genratePoints(800)
   timeline()
   i = 0
   while True:
       # setting the smallest time variation
       clock.tick(60)
       # Fill the background color to screen as black
       screen.fill(WHITE)
       #phaseTransfer()
       display()
       # loop through the events
       for event in pygame.event.get():
        #check if the event is the x button
        if event.type==pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
       #show()
       
       timeline()
       pygame.display.update()
       root.update()  
       #break
   show()

   
if __name__== '__main__':
   main()
