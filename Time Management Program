from datetime import datetime, timedelta # Imports time modules
from os import _exit
import pygame, pickle
width = 800
height = 800

# RGB codes defining colors
red = [233,68,46]
black = [0,0,0]
blue = [1,147,255]
gray = [200,200,200]

dnow = datetime.now() + timedelta(days=0)
title = "Time Management"
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('comicsans',25)
font3 = pygame.font.SysFont('comicsans',20)
prot = 4
fn = "e project info"
# Progress bar
# boxes for each color; a key for each colored line
# displaying: fractions/integers
# reduce lines of code width-25/2 (make a function)
# xsc / 5 smaller lines
# Enter in dates without the 0
# Function for all the inputs
# back function
# re-enter data
# most efficient protocol
# select <-- ideas
# another enter option for x: due in (x) days or 11/20/19
# remove bli
# why does dat != ndat False when I delete a value
# daily
# optional year
 
# cx_freeze convert to executable (at the VERY end) or py2exe
# Type Insturctions (at the end); readme.txt
# Sample
try:
   with open(fn,"rb") as datfile:
      dat = pickle.load(datfile)
except:
   open(fn,"wb")
   dat = []
   print("Insert Instructions\n")
def home():
   global name, x, y, x2, ct, xsc, ysc, a, b, dx2, works, day, pratio, ffiles, adone, now, done, integer, fraction, disyear, dat, ndat#, bli
   fraction = True
   integer = False
   while True:
      print("Your current program files:\n")
      try:
         ffiles = []
         for file in dat:
            ffiles.append(file[0])
         
         # Tests if ffiles is empty
         ffiles[0]

         # Lists every file in memory
         li = []
         bli = []
         dli = []
         nffiles = []
         ndat = []
         tot = 0
         nodis = False
         #for i in dat:
          #  print(i)
         for file in ffiles:
            forgot = False
            displaynum = ffiles.index(file)
            y = dat[displaynum][3]
            x = dat[displaynum][2]
            pratio = dat[displaynum][6]
            x2 = dat[displaynum][1]
            works = dat[displaynum][4]
            now = x2 + timedelta(days=dat[displaynum][5])
            ct = dat[displaynum][7]
            z = y/x * pratio
            a = ((((x-1)/x)*y-y+z))/(((x-1)/x)*x**2-x**2+1) 
            b = (y-x**2*a)/x
            todo = round(funct(len(works)+(now-x2).days)+1e-15)-works[-1]
            if works[-1] >= y:
               isfin = "* Amazing Effort! You have Finished this Assignment! This can be Deleted now."
               bli.append([0,todo*ct,ffiles.index(file)])
            else:
               if (dnow-now).days > len(works)-1:
                  for i in range((dnow-now).days-(len(works)-1)):
                     if round(funct(len(works)+(now-x2).days)+1e-15)-works[-1] <= 0:
                        works.append(works[-1])
                        dump()
                     else:
                        forgot = True
                        break
               if forgot == False:
                  if todo <= 0 or (dnow-now).days < len(works)-1:
                      isfin = "\u2713 Nice Job! You are Finished with this Assignment for Today. Keep it up!"
                      bli.append([1,todo*ct,ffiles.index(file)])
                  else:
                      tot += todo*ct
                      try:
                         b = (works[-1] - works[-2]) / 0.8 < (round(funct(len(works)-1+(now-x2).days)+1e-15)-works[-2])
                      except:
                         b = False
                      if b == True:
                         isfin = "\u26A0 Warning! You are behind scheduele! Complete {} Units of Work Today. ({})".format(todo,con(todo*ct))
                         bli.append([3,todo*ct,ffiles.index(file)])
                      else:
                         isfin = "\u2718 This Assignment is Unfinished for Today! Complete {} Units of Work Today. ({})".format(todo,con(todo*ct))
                         bli.append([2,todo*ct,ffiles.index(file)])
               else:
                  nodis = True
                  isfin = "? Whoops! You have not Entered in your Work completed! Enter it in now."
                  bli.append([4,todo*ct,ffiles.index(file)])
            li.append(str(file).ljust(len(max(ffiles,key=len))+2)+isfin)
         bli = sorted(bli,reverse=True)
         for i in bli:
            nffiles.append(ffiles[i[-1]])
            ndat.append(dat[i[-1]])
            dli.append((str(bli.index(i)+1)+")").ljust(len(str(len(ffiles)))+2)+li[i[-1]])
         ffiles = nffiles[:]
         if dat != ndat:
            dat = ndat[:]
            dump()
         if nodis == True:
            print("{}\n{}\nEstimated Total Completion Time: Not Yet Known! The data is incomplete.\n".format(dnow.strftime('%B %d, %Y (%A):'),"\n".join(dli)))
            nodis = False
         else:
            if tot != 0:
               print("{}\n{}\nEstimated Total Completion Time: {}\n".format(dnow.strftime('%B %d, %Y (%A):'),"\n".join(dli),con(tot)))
            else:
               print("{}\n{}\nCongratulations! You have Finished everything for Today!\n".format(dnow.strftime('%B %d, %Y (%A):'),"\n".join(dli)))
      except:
         print("You have not created a program file yet!\n")
      dec = input("Enter \'new\' to create a new program file\nEnter \'del\' to delete a program file\nSelect a file by entering in its corresponding number: ")
      try:
         if int(dec) == float(dec) and 0 < int(dec) <= len(ffiles):
            name = int(dec)-1
            break
         else:
            print("!!!\nInvalid\n!!!")
      except:   
         if dec == "new":
            fname = input("What would you like to name your program file: ").strip()
            if fname in ffiles:
               print("!!!\nInvalid\n!!!")
               continue
            name = len(ffiles)
            break
         elif dec == "del" and len(ffiles) != 0:
            try:
               numin = input("Enter the corresponding number of the program file you would like to delete: ")
               if float(numin) != int(numin):
                  raise ValueError
               del dat[int(numin)-1]
               del ffiles[int(numin)-1]
               dump()
               print("")
            except:
               print("!!!\nInvalid\n!!!")
         else:
            print("!!!\nInvalid\n!!!")
   try:

      # Tests if values have been filled in the past
      adone = dat[name][4][0]
      
      x = dat[name][2]
      x2 = dat[name][1]
      y = dat[name][3]
      works = dat[name][4]
      pratio = dat[name][6]
      now = x2 + timedelta(days=dat[name][5])
      ct = dat[name][7]
      dx2 = (now-x2).days
      
   except:
       now = datetime.now()
       now = now - timedelta(hours=now.hour,minutes=now.minute,seconds=now.second,microseconds=now.microsecond)
       pratio = 0.925
       skip = False
       while True:
           try:
               x2 = str(input("Assignment date of the assignment (MM/DD/YY or type \"today\"): "))
               if x2.lower() == "today":
                   x2 = datetime.now()
                   x2 = x2 - timedelta(hours=x2.hour,minutes=x2.minute,seconds=x2.second,microseconds=x2.microsecond) 
                   dx2 = 0
                   skip = True
                   adone = 0
                   break
               if len(x2) != 8:
                       raise ValueError
               #for i in range(len(x2)):
                #  if x2[i] == "/":
                 #    first = i   
               x2 = x2[:6] + "20" + x2[6:]
               x2 = datetime.strptime(x2, '%m/%d/%Y')
               dx2 = (now-x2).days
               if dx2 < 0:
                  raise ValueError
               break
           except:
               print("!!!\nInvalid\n!!!")
       while True:
           try:
               x = str(input("Due date of the assignment (MM/DD/YY): "))
               if len(x) != 8:
                   raise ValueError
               x = x[:6] + "20" + x[6:]
               x = (datetime.strptime(x, '%m/%d/%Y')-x2).days
               if int(x) != float(x) or int(x) < 2:
                   raise ValueError
               x = int(x)
               break
           except:
               print('!!!\nInvalid\n!!!')
       while True:
           try:
               y = input("Total amount of units in the entire assignment: ")
               if int(y) < 1 or int(y) != float(y):
                   raise ValueError
               y = int(y)
               break
           except:
               print('!!!\nInvalid\n!!!')
       if skip == False:
          while True:
              try:
                  adone = input("Total amount of units already completed: ")
                  if int(adone) < 0 or int(adone) != float(adone) or int(adone) >= y:
                      raise ValueError
                  adone = int(adone)
                  break
              except:
                  print("!!!\nInvalid\n!!!")
       while True:
          try:
               ct = input("Estimated length of time to complete each unit in minutes: ")
               if int(ct) < 1 or int(ct) != float(ct):
                   raise ValueError
               ct = int(ct)
               break
          except:
               print('!!!\nInvalid\n!!!')
       works = [adone]
       skip = False
       ffiles.append(fname)
       
       # Adds all the inputted information to the main file
       dat.append([fname,x2,x,y,works,(datetime.now()-x2).days,pratio,ct])
       dump()

   # Calculates whether to display the year or not
   disyear = ''
   if datetime.now().year != (datetime.now() + timedelta(days=x)).year:
      disyear = ', %Y'
       
   # Calculates variables for the parabola
   z = y/x * pratio
   a = ((((x-1)/x)*y-y+z))/(((x-1)/x)*x**2-x**2+1) 
   b = (y-x**2*a)/x

   day = len(works) - 1
          
   # Calculates variables for the indexes along the x and y axes
   sxsc = 1
   if x >= 40:
       xsc = 5 * int(x/40)
       sxsc = xsc/5
   elif x > 15:
       xsc = 5 * int(x/(5*int(x/5)))
   else:
       xsc = 1
   if y >= 40:
       ysc = 5 * int(y/40)
   elif y > 15:
       ysc = 5 * int(y/(5*int(y/5)))
   else:
       ysc = 1

def dump():
   
   with open(fn,"wb") as datfile:
      pickle.dump(dat,datfile,protocol=prot)
      
def funct(i):

    # Main function for receiving an output
    return a*i**2+b*i

def con(n):
    n = datetime(1,1,1) + timedelta(minutes=n)
    hour = n.hour
    for i in range(n.day-1):
       hour += 24
    hs = 's'
    ms = 's'
    if n.minute == 1:
       ms = ''
    if hour == 1:
       hs = ''
    if hour == 0:
       sttodo = '{} Minute{}'.format(n.minute,ms)
    elif n.minute == 0:
       sttodo = '{} Hour{}'.format(hour,hs)
    else:
       sttodo = '{} Hour{} and {} Minute{}'.format(hour,hs,n.minute,ms)
    return sttodo
home()
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption(title)

# Pygame draw function
def draw():

       # Font fitting variables
       xfit = 0
       yfit = 4

       # Defining constants
       hCon = (height-55)/y
       wCon = (width-55)/x
       screen.fill([255,255,255])

       # Creates the indexes along the y axis
       for i in range(y,0,-1):
           if i % ysc == 0:
               font2 = pygame.font.SysFont('comicsans',25)
               if len(str(i)) > 2:
                   font2 = pygame.font.SysFont('comicsans',25-(len(str(i))-2)*5)
               screen.blit(font2.render(str(i), True, black),(39-font2.render("0", True, black).get_width()-(len(str(i))-1)*(font2.render("0", True, black).get_width()),height-(i*hCon+50)-yfit))
               yfit = font2.render("0", True, black).get_height()/2
               pygame.draw.rect(screen,[220,220,220],(50,height-52.5-i*hCon,width-50,5))

       # Creates the indexes and the lines for the x axis
       #xma = 0
       for i in range(1,x+1):
            #if i % (xsc + xma) == 0:
             #  
              # pygame.draw.rect(screen,[235,235,235],(i*wCon+48.75,0,2.5,height-50))
            if i % xsc == 0:
               if font.render(str(i), True, black).get_width()+i*wCon+45 >= width:
                   xfit = font.render(str(i), True, black).get_width()+i*wCon+45-(len(str(i))-1)*4.5-(width-1)
               pygame.draw.rect(screen,[220,220,220],(i*wCon+47.5,0,5,height-50))
               screen.blit(font.render(str(i), True, black),(i*wCon+45-xfit-(len(str(i))-1)*4.5,height-40))
               xfit = 0
      
       # Main loop for plotting reccommended amounts of work as points on the graph
       #mis = 
       for i in range(1,x+1):
           if i == 1:
                  pygame.draw.circle(screen,red,(50,height-50),5)
           #if x > (width-55)/10:
            #   if i % 2 == 0:
             #     print(i)
              #    continue
           if fraction == True:
               pygame.draw.circle(screen,red,(round(i*wCon+50),round(height-(funct(i)*hCon+50))),5)
               pygame.draw.line(screen,red,(round((i-1)*wCon+50),round(height-(funct(i-1)*hCon+50))), (round(i*wCon+50),round(height-(funct(i)*hCon+50))),5)
           else:
               pygame.draw.circle(screen,red,(round(i*wCon+50),round(height-(round(funct(i)+1e-15)*hCon+50))),5)
               pygame.draw.line(screen,red,(round((i-1)*wCon+50),round(height-(round(funct(i-1)+1e-15)*hCon+50))), (round(i*wCon+50),round(height-(round(funct(i)+1e-15)*hCon+50))),5)

       # Main function for plotting input points
       for i in range(len(works)):
           if i != 0:
               pygame.draw.line(screen,blue,(((i+dx2)*wCon+50,height-(works[i]*hCon+50))),(((i-1+dx2)*wCon+50,height-(works[i-1]*hCon+50))),5)
           pygame.draw.circle(screen,blue,(round((i+dx2)*wCon+50),round(height-(works[i]*hCon+50))),5)
       pygame.draw.rect(screen,gray,(40,0,10,height))
       pygame.draw.rect(screen,gray,(0,height-50,width,10))
       #pygame.draw.rect(screen,[230,230,230],(0,height-50,width,10))
       screen.blit(font.render("0", True, black),(51,height-39))
       screen.blit(font.render("0", True, black),(30,height-66))
       screen.blit(font.render("Days", True, black),(width/2+25-19,height-19))
       screen.blit(pygame.transform.rotate(font.render("Units of work", True, black),270),(-2,height/2-25-55))
       try:
          b = (works[-1] - works[-2]) / 0.8 < (round(funct(len(works)-1+(now-x2).days)+1e-15)-works[-2])
       except:
          b = False
       if b == True:
          screen.blit(font.render("!!! ALERT !!!", True, black),(width/2+25-50,height/3-25-19)) ###<< -- simplify
          screen.blit(font.render("You Are BEHIND Scheduele!", True, black),(width/2+25-115,height/3-25))

       # Calculates work to be done today
       todo = round(funct(day+dx2+1)+1e-15)-works[-1]
       if todo <= 0:
           todo = 0
           sttodo = "Already Completed!"
       else:
          sttodo = con(todo*ct)
          
       # Formatting
       screen.blit(font.render("Name: "+ffiles[name], True, black),(width/2+25-font.render("Name: "+ffiles[name], True, black).get_width()/2,0))
       if width/2+25-max(font.render("Today's deadline: "+str(works[-1]+todo)+" units of work", True, black).get_width(),font.render("Name: "+ffiles[name], True, black).get_width())/2 >= 208:
          screen.blit(font3.render("'i' to switch between", True, black),(51,0))
          screen.blit(font3.render("fractions and integers", True, black),(51,12))
          screen.blit(font3.render("'d' to list each day's work", True, black),(51,24))
          screen.blit(font3.render("'h' to select another file", True, black),(51,36))
          screen.blit(font3.render("'Return' to input work done", True, black),(51,48))
          screen.blit(font3.render("'Delete' to undo inputs", True, black),(51,60))
          screen.blit(font3.render("Up/Down arrow to change", True, black),(51,72))
          screen.blit(font3.render("the Z ratio of the distribution", True, black),(51,84))
       if works[-1] < y:
          screen.blit(font.render(str((now+timedelta(days=day)).strftime('%B %d, %Y (%A):')), True, black),((width+50-font.render(str((now+timedelta(days=day)).strftime('%B %d, %Y (%A):')), True, black).get_width())/2,38))
          screen.blit(font.render("Units to complete today: "+str(todo), True, black),((width-155-font.render(str(todo), True, black).get_width())/2,57))
          screen.blit(font.render("Units already completed: "+str(works[-1]), True, black),((width-159-font.render(str(works[-1]), True, black).get_width())/2,76))
          screen.blit(font.render("Unit deadline for this day: "+str(works[-1]+todo), True, black),((width-166-font.render(str(works[-1]+todo), True, black).get_width())/2,95))
          screen.blit(font.render("Estimated completion time: "+sttodo, True, black),((width-181-font.render(sttodo, True, black).get_width())/2,114)) # (width/2+25-font.render("Estimated completion time: "+sttodo, True, black).get_width()/2,114)
       if (now+timedelta(days=day)) > dnow:
          screen.blit(font.render("Finished for Today!", True, black),(width/2-53,154))
       pygame.display.update()
draw()
while True:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
         pygame.quit()
         _exit(0)
     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_i:
             integer = not integer
             fraction = not fraction
             draw()
         if event.key == pygame.K_h:
            print("")
            home()
            draw()
         if event.key == pygame.K_BACKSPACE:
             if len(works) > 1:
                 del works[-1]
                 day -= 1
                 dump()
                 draw()
         if event.key == pygame.K_d:
            li, hli, qli = [], [], []
            total = works[0]
            for i in range(dx2,x):
               date = now + timedelta(days=i-dx2)
               fdate = date.strftime('%B %d'+disyear+' (%A):')
               try:
                  dif = works[i-dx2+1]-works[i-dx2]
               except:
                  if i == len(works) - 1 + dx2 or works[-1] > funct(i):
                        dif = round(funct(i+1)+1e-15)-works[-1]
                  else:
                        dif = round(funct(i+1)+1e-15)-round(funct(i)+1e-15)
               if dif <= 0:
                  if x - dx2 <= 15:
                     dif = 0
                  else:
                     continue
               s = 's'
               if dif == 1:
                  s = ''
               total += dif
               li.append('{}P {}\t unit{} of work ({} total)'.format(fdate,dif,s,total))
               hli.append(fdate)
               qli.append(str(dif))
            if max(qli,key=len) != min(qli,key=len):
               for i in range(len(li)):
                  li[i] = li[i].replace('P',' '*(len(max(hli,key=len))-len(hli[i]))).replace('\t',' '*(len(max(qli, key=len))-len(qli[i])))
            else:
               for i in range(len(li)):
                  li[i] = li[i].replace('P',' '*(len(max(hli,key=len))-len(hli[i]))).expandtabs(0)
            print("\n".join(li)+"\n")
         if (event.key == pygame.K_DOWN and round(pratio - 0.075,3) >= 0.5) or (event.key == pygame.K_UP and round(pratio + 0.075,3) <= 1):
             if event.key == pygame.K_DOWN and round(pratio - 0.075,3) >= 0.5:
                pratio = round(pratio - 0.075,3)
                dat[name][6] = round(dat[name][6] - 0.075,3)
             elif event.key == pygame.K_UP and round(pratio + 0.075,3) <= 1:
                pratio = round(pratio + 0.075,3)
                dat[name][6] = round(dat[name][6] + 0.075,3)
             dump()
             z = y/x * pratio
             a = ((((x-1)/x)*y-y+z))/(((x-1)/x)*x**2-x**2+1)
             b = (y-x**2*a)/x
             draw()
         if event.key == pygame.K_RETURN:
             while True:
                 try:
                     date = now + timedelta(days=day)
                     fdate = date.strftime('%B %d'+disyear+' (%A)')
                     if (dnow-date).days == 0:
                        fdate += ' (Today)'
                     done = int(input('(Your progress: {}/{} units are completed so far) Amount of work done on {}: '.format(works[-1],y,fdate)))
                     if done < 0 or type(done) != int or (day + dx2 + 1 == x and done+works[-1] < y):
                         raise ValueError
                     day += 1
                     break
                 except:
                     print("!!!\nInvalid\n!!!")
             works.append(done+works[-1])
             dump()
             if works[-1] >= y:
                print("\nFinish! You have completed your assignment. Good job!\n")
             draw()
     if event.type == pygame.VIDEORESIZE:
         width = event.w
         height = event.h
         surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
         draw()
