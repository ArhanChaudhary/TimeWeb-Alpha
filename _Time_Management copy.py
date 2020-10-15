try:

   # Pygame module to handle display graphics and receiving mouse inputs
   import pygame
   
except:
   
   # If pygame is not installed, stop the program
   print('Uh Oh! It seems you do not have the Pygame module Installed! This program requires Pygame to Run! Search up how to Install Pygame 1.9.3 on your Operation System.')
   from os import _exit
   _exit(0)

from datetime import datetime as date # Handles Dates as an Object
from datetime import timedelta as time # Handles Adding and Subtracting Dates
from pickle import load, dump, dumps # Stores Data into Memory to be Used Later
from math import ceil, log10 # Function to Round up to the nearest integer and log10 to find a number's magnitude
from os.path import exists # Checks if a file exists
from os import remove # Removes Backups if they are Disabled

# File Directory where the data will be stored
file_directory = 'Time Management'
update_backups = True
debug_mode = True

# Settings Procedure:
# Add/remove it on the boolean settings and Adjust values for other settings
# Change range value
# Change setting "Restore all def setting values" x2
# Change dat[0]
# command F

# QOL todo list:
# replace "unit" to "minute" if u press enter 20 mins
# change warning_flexibility so its displayed value is its actual value in the code 3 (so it works with "Old Value: ") (also rewrite its print code) 15 mins
# dont know the amount of units? ONLy if due date is known ("none" with y) 15 mins
# remove after midnight 15 mins
# fix next_day (make it values 0,1,2,3,etc) (still displays same date), function to set date_now and also take into account "next_day" variable 20 mins

# More Complicated todo list:
# min work time work with the blue line
# daily assignments (x and y will change with the assignment, x will always be (DUE TOMORROW!!!), y will always be the min_work_time)
# maximum work time
# multiple points to hit (piecewise) (combining assignments into one big x axis graph)
# replace "change skew ratio" to "change a property for all assignment" in settings (skew_ratio, nwd, fixed_mode, total mode, min_work_time)
# time table, use (this assignment is complete because there is no time left in today)
   
# Gets today's date
date_now = date.now()

# Checks if it is midnight
after_midnight = date_now.hour < 4
if after_midnight:
   date_now = date(date_now.year,date_now.month,date_now.day,date_now.hour,date_now.minute) - time(1)
else:
   date_now = date(date_now.year,date_now.month,date_now.day,date_now.hour,date_now.minute)

try:

   # Loads Data from Memory if it is found
   with open(file_directory,'rb') as datfile:
      dat = load(datfile)
   if debug_mode:
      print(dat,'\n')
      
   # Loads setting data
   date_last_closed,width,height,animation_frame_count,warning_acceptance,def_min_work_time,def_nwd,display_instructions,display_status_priority,autofill,do_after_midnight,ignore_ends,dark_mode,show_progress_bar,show_past,last_opened_backup,hourly_backup,daily_backup,weekly_backup,monthly_backup = dat[0]
   tomorrow = (date_now.year,date_now.month,date_now.day) != (date_last_closed.year,date_last_closed.month,date_last_closed.day)
   if do_after_midnight and after_midnight:
      print('!!!\n!!!\n!!!\nYOU HAVE RAN THIS PROGRAM AFTER MIDNIGHT!\nTHE DAY IN THE PROGRAM WILL STILL BE SET AS '+date_now.strftime('%B %-d, %Y')+'\nAND WILL ONLY CHANGE TO THE NEXT DAY AFTER 4 A.M\nALL ASSIGNMENTS WILL BE MARKED AS COMPLETED SO YOU CAN SLEEP\nTHIS CAN BE TOGGLED OFF IN THE DEFAULTS\nYOU SHOULD SLEEP AS SOON AS POSSIBLE!\n!!!\n!!!\n!!!')
      
except:

   # If the data is not found, create a new file which will hold all the data
   if after_midnight:
      date_now += time(1)

   # Set after_midnight to ''
   # The reason why I do this is because after_midnight is anyways going to be False
   # An empty string evaluates to False too
   # The fact that it is an empty string instead of a boolean carries the information that the program has just been ran
   # This allows me to save memory by not using an extra variable
   after_midnight = ''

   # Initialize Default settings in a new file
   
   # Each Item in the List of the Settings corresponds to the Variable Name above it
   #       date_last_closed,width,height,animation_frame_count,warning_acceptance,def_min_work_time,def_nwd,display_instructions,display_status_priority,autofill,do_after_midnight,ignore_ends,dark_mode,show_progress_bar,show_past,last_opened_backup,hourly_backup,daily_backup,weekly_backup,monthly_backup
   dat = [[date_now        ,750  ,750   ,35                   ,1                 ,15               ,()     ,True                ,False                  ,True    ,True             ,True       ,True     ,True             ,True     ,True              ,True         ,True        ,False         ,False         ]]

   # Loads setting data
   date_last_closed,width,height,animation_frame_count,warning_acceptance,def_min_work_time,def_nwd,display_instructions,display_status_priority,autofill,do_after_midnight,ignore_ends,dark_mode,show_progress_bar,show_past,last_opened_backup,hourly_backup,daily_backup,weekly_backup,monthly_backup = dat[0]
   print('Welcome to Time Management Beta!\nThis program will help you properly manage time by spliting up work for all of your assignments and ordering them in an organized manner\nIf you have any question on how to use or suggestions for the program, contact me at arhan.ch@gmail.com')
         
# Function that stores the main data
def save_data():
    with open(file_directory,'wb') as datfile:
        dump(dat,datfile,protocol=4)
      
# Creates Backup Files if the program was Ran for the First Time
original_file_directory = file_directory
if after_midnight == '':

   # Create the main File and backup Files
   for open_files in (file_directory + ' Every Run Backup',file_directory + ' Hourly Backup',file_directory + ' Daily Backup',file_directory + ' Daily Backup',file_directory):
      file_directory = open_files
      save_data()
   
# RGB codes defining colors
red = (233,68,46)
blue = (1,147,255)
green = (0,255,0)
dark_green = (0,128,0)
if dark_mode:
   black = (255,255,255)
   border = (200,200,200)
   gray = (55,55,55)
   gray1 = (40,40,40)
   gray2 = (50,50,50)
   gray3 = (105,105,105)
   gray4 = (70,70,70)
   gray5 = (135,135,135)
   white = (0,0,0)
else:
   black = (0,0,0)
   border = (55,55,55)
   gray = (200,200,200)
   gray1 = (215,215,215)
   gray2 = (205,205,205)
   gray3 = (150,150,150)
   gray4 = (185,185,185)
   gray5 = (120,120,120)
   white = (255,255,255)

# Note: ceil([number] - 0.5) is the same as round([number]). I chose to use this way because it is faster, and I am aware it rounds down when the number ends with .5

# Checks if the manual backup exists
manual_backup = exists(file_directory + ' Manual Backup')

# Initialize pygame and define fonts
font_type = 'freesansbold.ttf'
pygame.init()
font3 = pygame.font.SysFont(font_type,25)
if width > 748:
   font_size = 25
else:
   font_size = ceil((width+450)/47-0.5)
font = pygame.font.SysFont(font_type,font_size)
font4 = pygame.font.SysFont(font_type,20)
max_w, max_h = pygame.display.Info().current_w, pygame.display.Info().current_h

def qinput(input_message):
   return_input = input(input_message)
   if 'quit' in return_input.lower():
      quit_program()
   return return_input

# Main assignment home function
def home(last_sel=0):
   autofill_override = False
   global date_now, min_work_time, sel, x, y, ad, ctime, dif_assign, works, day, skew_ratio, file_sel, adone, date_file_created, disyear, dat, screen, ndif, xdif, rem_zero, lw, start_lw, assign_day_of_week, wlen, funct_round, nwd, len_nwd, fixed_mode, dynamic_start, stry, slash_x_counter, red_line_start, unit, wCon, hCon, total_mode, set_start, set_skew_ratio, clicked_once, fixed_start, remainder_mode, smart_skew_ratio, due_date, selected_assignment, width,height,animation_frame_count,warning_acceptance,def_min_work_time,def_nwd,display_instructions,autofill,show_past,ignore_ends,ignore_ends_mwt,dark_mode,show_progress_bar,display_status_priority,last_opened_backup,hourly_backup,daily_backup,weekly_backup,monthly_backup,manual_backup,do_after_midnight, file_directory, black, border, gray, gray1, gray2, gray3, gray4, gray5, white, min_work_time_funct_round, left_adjust_cutoff, up_adjust_cutoff, point_text_width, point_text_height, y_fremainder, y_mremainder, original_min_work_time, tomorrow
   next_day = False
   set_tomorrow = True
   while 1:

      # Update the today's time in the date_now variable
      date_now = date.now()  
      date_now = date(date_now.year,date_now.month,date_now.day)
      if not tomorrow and set_tomorrow:
          tomorrow = (date_now.year,date_now.month,date_now.day) != (date_last_closed.year,date_last_closed.month,date_last_closed.day)
      try:
         
         # List of every assignment name
         files = [file[0] for file in dat[1:]]
         amount_of_assignments = len(files)
         
         # Tests if files is empty
         # If it is, raise an error and run the "except" part of the "try"
         # If it is not, continue on
         files[0]
         
         assign, ordli, daysleft = [], [], []
         max_assignment_name_len = len(max(files,key=len))+1
         file_index = 1
         tot = tomorrow_tot = 0
         nodis = False
         set_skew_ratio = False
         for file in dat[1:]:

            # First, loop through each assignment and load each assignment's variables
            file_sel,ad,x,y,works,dif_assign,skew_ratio,ctime,funct_round,nwd,fixed_mode,dynamic_start,unit,total_mode,fixed_start,remainder_mode,min_work_time = file

            # Calculates the start of the red line (used in other functions) and the value of the work input the start is at
            if fixed_mode:
               start_lw = works[fixed_start - dif_assign]
               red_line_start = fixed_start
            else:
               start_lw = works[dynamic_start - dif_assign]
               red_line_start = dynamic_start
               
            # Caps funct_round at y
            if funct_round > y - start_lw:
               funct_round = y - start_lw

            # Caps min_work_time at y
            if min_work_time > y - start_lw:
               min_work_time = y - start_lw

            # If the minimum work time is less than the grouping value, that means
            # The minimum work time is always fulfilled by the grouping value, making
            # It completely irrelevant
            if min_work_time <= funct_round:
               min_work_time = 0

            # Let funct_round be 4 and min_work_time be 5
            # In the code, f(4) = 18 and f(5) = 23
            # However, f(4) gets rounded to 20 and f(5) gets rounded to 24, breaking min_work_time
            # This fixes the problem
            elif 1 < min_work_time / funct_round < 2:
               min_work_time = funct_round * 2

            # Smallest multiple of min_work_time and funct_round that is greater than min_work_time
            # This is the minimum amount of units the user will do in any given working day
            if min_work_time:
               min_work_time_funct_round = ceil(min_work_time/funct_round)*funct_round
            else:
               min_work_time_funct_round = funct_round

            assign_day_of_week = ad.weekday() # Weekday of assign date
            len_nwd = len(nwd) # Length of not working days
            if nwd:
               set_mod_days()
               x1 = (x - red_line_start) - (x - red_line_start)//7 * len_nwd - mods[(x - red_line_start) % 7] - 1
            else:
               x1 = x - red_line_start - 1
            ignore_ends_mwt = ignore_ends and min_work_time and x1 != 1
            if not x1:
               x1 = 1
               
            wlen = len(works) - 1 # Length of work inputs subtracted by 1 to not count the 0th work input
            lw = works[wlen] # Last work input

            y_fremainder = (y - start_lw) % funct_round # Remainder when the total number of units left in the assignment is divided by funct_round, or the grouping value
            y_mremainder = (y - start_lw) % min_work_time_funct_round # Remainder when the total number of units left in the assignment is divided by min_work_time_funct_round, or the minimum a use will work in a day

            # Define a and b for the parabola
            pset()

            todo = funct(wlen+dif_assign+1) - lw # Amount of work to be done
            dayleft = (ad-date_now).days # Days between assign date and today
            strdayleft = '' # Formatting Variable
            
            # Checks if Assign Date is in the Future
            if dayleft > 0:
               status_message = '#　This Assignment has Not been Assigned Yet! Please wait until it is.'
               if dayleft == 1:
                  strdayleft = ' (Assigned Tomorrow!)'
               elif dayleft < 7:
                  strdayleft = ad.strftime(' (Assigned on %A)')
               else:
                  strdayleft = f' (Assigned in {dayleft} Days)'
               status_value = 5
            else:
               
               # Checks if Assignment is completed
               if lw >= y or dayleft + x < 1:
                  if tomorrow:
                     ordli.append((6,))
                     continue
                  status_message = '*　You have Finished this Assignment! This will be Deleted Tommorrow.'
                  status_value = 6
               else:
                  
                  # Distance between today's date and the date assignment was made
                  ndif = -dayleft-dif_assign
                  
                  # Auto fills in zero if work has not been done
                  if autofill and ndif > wlen:
                     has_autofilled = False
                     for i in range(ndif-wlen):

                        # Don't set todo value if it is on its first loop
                        # This is because it checks on the next line of code if it needs to autofill zero
                        # If all the conditions are met for auto filling, then allow todo to be reset on the next loops
                        if has_autofilled:
                           todo = funct(wlen+dif_assign+1) - lw

                        # Stops auto filling if the work to be done from the last work input is greater than 0 or when the end of the assignment is reached
                        if not (autofill_override or todo <= 0 or (assign_day_of_week + wlen + dif_assign) % 7 in nwd) or wlen + dif_assign == x - 1:
                           break
                        
                        has_autofilled = True
                        works.append(lw)
                        wlen += 1

                        # If dynamic mode is enabled (the start is allowed to change), only change the start of the red line if the work inputs are below the red line
                        if not fixed_mode and todo > 0 and (assign_day_of_week + wlen + dif_assign) % 7 not in nwd:
                           dynamic_start = wlen + dif_assign
                           red_line_start = dynamic_start
                           start_lw = works[wlen-dif_assign]
                           if nwd:
                              set_mod_days()
                     if has_autofilled:

                        # Save data if it passed the first loop test
                        y_fremainder = (y - start_lw) % funct_round
                        y_mremainder = (y - start_lw) % min_work_time_funct_round
                        todo = funct(wlen+dif_assign+1) - lw
                        file[11] = dynamic_start
                        save_data()
                  dayleft += x

                  # Checks if all the Work Inputs have been Inputted until Today
                  if not autofill_override and ndif > wlen and wlen + dif_assign < x:
                     nodis = True
                     status_message = '?　Whoops! You have not Entered in your Work Completed from Previous Days!'
                     status_value = 1
                  else:
                     
                     # Checks if Assignment is Completed for Today
                     this_funct = funct(wlen+dif_assign)
                     check_inpro = ndif == wlen - 1 and lw != works[-2] and lw < this_funct
                     if after_midnight and dayleft != 1 or not check_inpro and (todo <= 0 or ndif < wlen) or date_now.weekday() in nwd:
                        status_message = '\u2714　Nice Job! You are Finished with this Assignment for Today. Keep it up!'
                        status_value = 4
                     else:
                        
                        # Checks if Assignment is in Progress
                        status_value = 3
                        if check_inpro:
                              status_message = "@　This Assignment's Daily Work is in Progress!"
                              todo = this_funct - lw
                        else:
                           
                           # Determines whether to display a warning
                           if wlen > 0 and not (ndif == wlen - 1 and fixed_mode) and (lw - works[-2]) / warning_acceptance < funct(wlen+dif_assign) - works[-2]:
                              status_message = '!　Warning! You are behind your Work schedule! '
                           else:
                              status_message = "\u2718　This Assignment's Daily Work is Unfinished! "
                              
                        # Formatting
                        if todo == 1:
                           s = ''
                        else:
                           s = 's'
                        if total_mode:
                           strtotal = 'Total '
                           strtodo = '%g' % (todo + lw)
                           complete_or_reach = 'Reach'
                        else:
                           strtotal = ''
                           strtodo = '%g' % todo
                           complete_or_reach = 'Complete'
                        status_message += f' {complete_or_reach} {strtodo} {strtotal}{unit}{s} Today. ({format_minutes(todo*ctime)})'
                        tot += ceil(todo*ctime)
                  if dayleft == 1:
                     strdayleft = ' (Due TOMORROW!!)'
                     tomorrow_tot += ceil(todo*ctime)
                     status_value = 2
                  elif dayleft < 7:
                     strdayleft = (ad + time(x)).strftime(' (Due on %A)')
                  else:
                     strdayleft = f' (Due in {dayleft} Days)'
                     
            # Assigns each assignment a value based on an algorithm
            # Then, all the assignments are sorted by their value to determine each assignment's priority.
            # The most important assignments are closer to spot #1
            if status_value in (5,6):
               status_priority = -dayleft
            else:
               if skew_ratio < 0.8 or skew_ratio > 1.2:
                  skew_ratio = 1
               red_line_start = dif_assign
               pset()
               todo = funct((date_now-ad).days+1) - lw

               # todo*ctime is the total amount of minutes it will take to complete the work for that day
               # x-dif_assign-wlen is the amount of days until the assignment is due
               if not x-dif_assign-wlen:
                  status_priority = 0
                  
               elif not todo*ctime:
                  
                  # Variation of the Algorithm
                  how_well_follow = 1-sum(works[i]-funct(i) for i in range(1,wlen+1) if (assign_day_of_week + i - 1) % 7 not in nwd)/x1/y*10
                  if how_well_follow == 1:
                     how_well_follow = 0
                  status_priority = how_well_follow/(x-dif_assign-wlen)
                  
               else:
                  
                  # This is the Priority Algorithm
                  # The algorithm is simple, as it only consists of two parts
                  # First, the program finds the ratio of the time it will take to finish work to the amount of days left until the assignment is due
                  # Then, the program loops through each work input and calculates the distance between each work input and where your progress was actually supposed to be on that day
                  # Then, more calculations are done to find a constant to multiply by the first value in the algorithm
                  status_priority = (1-sum(works[i]-funct(i) for i in range(1,wlen+1) if (assign_day_of_week + i - 1) % 7 not in nwd)/x1/y*10) * todo*ctime/(x-dif_assign-wlen)
                  
            # Appends the status value (calculated above), the status priority, and the file index to a list called ordli
            # After each assignment appends to ordli, ordli is then sorted
            
            # In the sorted() method, if the objects to be sorted are collectibles, such as:
            # [(5,7,1),(7,4,2),(5,8,0)]
            # Then, the collectibles are first sorted by their first value
            # If their first values are the same, then it sorts by their second value
            # If their second values are the same, then it sorts by their third value and so on
            
            # First, it sorts by the status_value variable from lowest to greatest because it is the first value
            # Important and more urgent assignments, such as ones due tomorrow, have a low status_value
            # So, they are ordered closer to the top
            # Less urgent assignments have a higher status value
            # So, they are ordered closer to the bottom
            # If two assignments have the same status_value, then they are sorted by their status priority because it is the second value
            # When ordli is sorted, it doesn't actually change the order of assignments, ordli is just a list of numbers
            # Notice the last value appended to ordli is file_index
            # file_index is the original order of each assignment before all of this
            # Since the loop starts from the 1st assignment all the way to the last, file_index will be 0, 1, 2, 3, 4, etc for each loop
            # Then, when ordli is sorted, I can use the file_index to refer to which assignments moved to where after ordli was sorted
            ordli.append((status_value, -status_priority, file_index))

            # These lists are for Formatting
            assign.append(file[0].ljust(max_assignment_name_len)+status_message)
            daysleft.append(strdayleft)

            # Add one to the file_index because the loop starts from the first assignment
            file_index += 1
         autofill_override = False  

         # Sorts ordli with the logic stated above
         ordli = sorted(ordli)
         statuses = tuple(i[0] for i in ordli)
         
         if tomorrow and 6 in statuses:
            tomorrow = False
            dat = dat[:statuses.index(6)+1]
            save_data()
            ordli = ordli[:statuses.index(6)]
            statuses = statuses[:statuses.index(6)]
         # If display status priority is enabled, this gets the assignment with the highest priority and finds the ratio of all the other assignments' status priority by the one with the highest priority

         # First, the maximum status priority is defined as the status value of the first element on ordli
         # This is the comparison that the other assignments will use to determine their status percentage
         maxsp = ordli[0][1]

         # This block of code loops through every assignment finds the ratio of its status priority and the highest status priority
         
         # It also makes sure to have a transition between status values
         # An assignment that is due tomorrow could actually have a low status priority compared to the other assignments and is only put as the most important assignment because it is due tomorrow
         # This messes up calculating the ratio
         # The solution to this is to always make sure: (lowest status priority with a higher status value)/(highest status priority with lower status value) = 2
         # This basically ensures that the percentages will always be decreasing order
         percentage3, percentage4 = None, None
         for j in ordli:
            if j[0] == 2:
               percentage2 = j[1] / maxsp * 100
               daysleft[j[2]-1] += f' SP: {ceil(percentage2)}%'
               
            if j[0] == 3:

               # Only run this on the first time
               if percentage3 == None:

                  # Defines constant to multiply the calculated by in order to make sure percentages will always be decreasing order
                  if 2 in statuses:
                     percentage3_half_constant = percentage2 / (j[1] / maxsp * 100) / 2
                  else:
                     percentage3_half_constant = 1
               percentage3 = j[1] / maxsp * 100 * percentage3_half_constant
               daysleft[j[2]-1] += f' SP: {ceil(percentage3)}%'

            elif j[0] == 4:

               # Only run this on the first time
               if percentage4 == None:

                  # Defines constant to multiply the calculated by in order to make sure percentages will always be decreasing order
                  if 3 in statuses:
                     percentage4_half_constant = percentage3 / (j[1] / maxsp * 100) / 2
                  elif 2 in statuses:
                     percentage4_half_constant = percentage2 / (j[1] / maxsp * 100) / 2
                  else:
                     percentage4_half_constant = 1
               percentage4 = j[1] / maxsp * 100 * percentage4_half_constant
               daysleft[j[2]-1] += f' SP: {ceil(percentage4)}%'

         # Formatting
         massign = len(max(assign,key=len))
         max_assignment_name_len = len(str(amount_of_assignments))+2

         # Once ordli is sorted, this list comprehension resorts the actual list of assignments based on ordli
         # The ljust() method makes sure the assignments are aligned

         #        This part of the list comprehension adjusts the number of the     This part displays the assignment name, the status    This part displays the days
         #        assignment                                                        message, and the estimated time until completion      left and the status priority
         assign = [(str(ordli.index(ordas)+1)+')').ljust(max_assignment_name_len) + assign[ordas[2]-1].ljust(massign)                  +  daysleft[ordas[2]-1]          for ordas in ordli]
         
         # Saves sorted data to memory if it changed after sorting
         if any(ordli[ordindex][2] != ordindex + 1 for ordindex in range(len(ordli))):
            dat = [dat[0]] + [dat[assignment[2]] for assignment in ordli]
            save_data()

         # Formatting
         if next_day:
            istod = ' (Tomorrow)'
         else:
            istod = ' (Today)'
         projects = '\nYour current assignments:\n\n'+date_now.strftime(f'%B %-d, %Y (%A){istod}:\n')+'\n'.join(assign)+'\n'
         if nodis:
            if last_sel:
               project_time = '\nThe Work time is Incomplete! Please enter in your work done from Previous Days to proceed.'
            else:
               project_time = '\nThe Work time is Incomplete! Please enter in your work done from Previous Days to proceed.\nEnter "none" to automatically Enter in no work done for every Incomplete Assignment'
         elif tot:
            project_time = f'\nEstimated Total Completion Time: {format_minutes(tot)} ({format_minutes(tomorrow_tot)} of it is Due Tomorrow)\nCurrent Time: {date.now().strftime("%-I:%M%p")}\nEstimated Time of Completion: {(date.now() + time(minutes=tot)).strftime("%-I:%M%p")}'
         else:
            if last_sel or next_day:
               project_time = '\nAmazing Effort! You have finished everything for Today!'
            else:
               project_time = '\nAmazing Effort! You have finished everything for Today!\nEnter "next" to see Tomorrow\'s Work'
         if next_day and not last_sel:
            project_time += '\nEnter "back" to go Back to the Current Day'
         if last_sel:
            print(projects + project_time)
         else:
            print(projects + project_time + '\n\nEnter "new" to Create an Assignment\nEnter "delete" to Remove an Assignment\nEnter "re" to Re-Enter Data values of an Assignment\nEnter "settings" to Customize the Settings\nEnter "quit" at any time to Exit and Backup\nEnter "fin" if you have Finished the work for the First Assignment\nPress Return to Select the First Assignment')
            input_message = 'Select an Assignment by Entering in its Corresponding Number:'
      except:
         if debug_mode:
            raise Exception

         # If file is empty, print the instructions
         print('\nThis is the assignment page where all of your assignments will be organized, sorted, and listed daily.\nThe assignments with higher priority will be closer to the beginning of the list.\n\nCurrently, You have not created an assignment yet!\n')
         input_message = "Enter 'new' to create your first assignment:"
         nodis = True

      # Last_sel is used to go to the next assignment when pressing key "n"
      reenter_mode = False
      if last_sel:
         sel = last_sel - 1
      else:
         while 1:
            
            # Input which Assignment to Select
            sel = qinput(input_message).strip()

            # You might see the variable "outercon" be used a lot.
            # Outercon is a flag used to either break or continue out of outer loops, which are loops that contain a loop that needs to break out of the outer one
            outercon = False

            # If nothing is entered, select the first assignment
            if not sel:
               if amount_of_assignments:
                  sel = 1
                  break
               continue
            try:
               sel = int(sel,10)

               # If the input is valid, proceed to the next section
               if 0 < sel and sel <= amount_of_assignments:
                  break
               print('!!!\nInput Number is not Valid!\n!!!')
            except:
               sel = sel.lower()

               # Checks if input is one of the special keywords
               
               # If the input is "new", Then purposely select a value that is out of range of the assignments. This is to raise an exception in the next section.
               if sel == 'new':
                  sel = amount_of_assignments + 1
                  break

               # If the input is "re", then toggle reenter_mode to True and proceed to the next section
               elif amount_of_assignments and sel == 're':
                  while 1:
                     try:
                        sel = qinput('Select which Assignment you would Like to Re-enter Data by Entering in its Corresponding Number:')
                        if not sel:
                           outercon = True
                           break
                        sel = int(sel,10)
                        if 0 < sel and sel <= amount_of_assignments:
                           reenter_mode = True
                           break
                        raise Exception
                     except:
                        print('!!!\nInput Number is not Valid!\n!!!')
                  if outercon:
                     continue
                  break
               else:
                  outercon = True

                  # If the input is "delete", then delete the selected assignment
                  if sel == 'delete':
                     if amount_of_assignments:
                        while 1:
                           try:
                              sel = qinput('Enter the corresponding Number of the Assignment you would Like to Delete:')
                              if not sel:
                                 break
                              sel = int(sel,10)
                              if 1 > sel or sel > amount_of_assignments:
                                 raise Exception
                              del dat[sel]
                              save_data()
                              break
                           except:
                              print('!!!\nInvalid Number!\n!!!')
                     else:
                        print('!!!\nThere is Nothing to Delete!\n!!!')

                  # If the input is "none", then add zeros to the incompleted assignment even if the amount to be done for that day is greater than 0
                  elif sel == 'none':
                     autofill_override = True

                  # If the input is "next", go to the next day
                  elif not nodis and not tot and not next_day and sel == 'next':
                     next_day = True
                     date_now += time(1)

                  # If the input is "back", go back to the current day
                  elif next_day and sel == "back":
                     next_day = False
                     date_now = date.now()
                     date_now = date(date_now.year,date_now.month,date_now.day)

                  elif sel == 'fin':
                     file_sel,ad,x,y,works,dif_assign,skew_ratio,ctime,funct_round,nwd,fixed_mode,dynamic_start,unit,total_mode,fixed_start,remainder_mode,min_work_time = dat[1]
                     ndif = (date_now-ad-time(dif_assign)).days
                     wlen = len(works) - 1
                     lw = works[wlen]
                     day = wlen
                     if fixed_mode:
                        start_lw = works[fixed_start - dif_assign]
                        red_line_start = fixed_start
                     else:
                        start_lw = works[dynamic_start - dif_assign]
                        red_line_start = dynamic_start
                     if ndif > -1 and ndif == day - 1 and lw != works[-2] and lw < funct(day + dif_assign):
                        day -= 1
                     if min_work_time:
                        min_work_time_funct_round = ceil(min_work_time/funct_round)*funct_round
                     else:
                        min_work_time_funct_round = funct_round
                     assign_day_of_week = ad.weekday()
                     len_nwd = len(nwd)
                     if nwd:
                        set_mod_days()
                     y_fremainder = (y - start_lw) % funct_round
                     y_mremainder = (y - start_lw) % min_work_time_funct_round
                     pset()
                     if (assign_day_of_week + dif_assign + day) % 7 in nwd:
                       todo = 0          
                     else:
                       todo = funct(day+dif_assign+1) - lw
                     rem_work = ndif == wlen - 1 and lw != works[-2] and lw < funct(wlen+dif_assign)
                     if todo > 0:
                        lw += todo
                     if rem_work:
                        del works[wlen]
                        wlen -= 1
                     works.append(lw)
                     wlen += 1
                     day = wlen
                     save_data()

                  # If the input is "settings", then print the settings
                  elif sel == "settings":

                     # Settings is a pointer to dat[0], which means it refers to dat[0] in memory
                     # That means changing anything in settings will also directly change the same thing in dat[0]
                     settings = dat[0]
                     
                     while 1:
                        outercon = False
                        while 1:
                           
                           change_setting = f'''
1)  Screen Width                       : {width} Pixels
2)  Screen Height                      : {height} Pixels
3)  Graph Animation Frame Count        : {animation_frame_count}
4)  Warning Flexibility                : {100-int(warning_acceptance*100)}% (Select for More Info)
5)  Default Minimum Work Time          : {def_min_work_time} Minutes
6)  Default Not Working Days           : {format_not_working_days()}
7)  Display Instructions               : {display_instructions}
8)  Display Status Priority            : {display_status_priority} (Select for More Info)
9)  Autofill Work*                     : {autofill} (Select for More Info)
10) After Midnight Assignment Pass*    : {do_after_midnight} (Select for More Info)
11) Ignore Min Work Time Ends*         : {ignore_ends} (Select for More Info)
12) Dark Mode for Graph                : {dark_mode}
13) Show Progress Bar in Graph         : {show_progress_bar}
14) Show Past Inputs in Graph Schedule : {show_past}
15) Backup Every time Program is Run*  : {last_opened_backup}
16) Backup Every Hour*                 : {hourly_backup}
17) Backup Every Day                   : {daily_backup}
18) Backup Every Week                  : {weekly_backup}
19) Backup Every Month                 : {monthly_backup}
20) Set Skew Ratio for each Assignment
21) Manual Backup
22) Load Backups
23) Restore all Default Values

A Star next to a Setting means its Default Setting Value is Recommended
Press Return at Any Time to Escape
Select a Setting you would like to Change by Entering its Corresponding Number:
'''
                           
                           # All settings in an input
                           change_setting = qinput(change_setting)
                           
                           # Check if input is valid
                           try:
                              if not change_setting:
                                 outercon = True
                                 break
                              change_setting = int(change_setting,10)
                              if 0 < change_setting and change_setting < 24:
                                 break
                              print('!!!\nInput Number is not Valid!\n!!!')
                           except:
                              print('!!!\nInput is Not an Integer!\n!!!')
                           qinput('Enter Anything to Continue:')
                        if outercon:
                           break

                        # Settings with Numeric Values
                        if change_setting in range(1,6):
                           if change_setting == 4:
                              print('\nWarning flexibility is how much percent of the amount of work for a day does not have to be done in order to trigger a warning\nFor example, suppose you have to read 10 pages of a book one day\nIf your warning flexibility is 0%, then that means you have to read all 10 pages to not trigger a warning\nIf your warning flexibility is 40%, then you can read 6 pages of the 10 pages and still not trigger a warning\nWarning flexibilty does not affect any of the code determining an assignment\'s priority\nEnter the percent of warning flexibility, from 1 - 100\n')
                           while 1:
                              new_value = qinput(f'What would you Like the New value of this Setting to be (Old Value: {settings[change_setting]}):').rstrip('%')
                              try:
                                 if not new_value:
                                    outercon = True
                                    break
                                 new_value = int(new_value,10)

                                 # Width
                                 if change_setting == 1 and new_value > 349 and new_value <= max_w:
                                    width = new_value

                                 # Height
                                 elif change_setting == 2 and new_value > 374 and new_value <= max_h:
                                    height = new_value

                                 # Animation frame count
                                 elif change_setting == 3 and new_value > 0:
                                    animation_frame_count = new_value

                                 # Warning Acceptance
                                 elif change_setting == 4 and -1 < new_value and new_value < 101:
                                    new_value = ceil(100-new_value)/100
                                    warning_acceptance = new_value

                                 # Default minimum work time
                                 elif change_setting == 5 and -1 < new_value:
                                    def_min_work_time = new_value
                                    
                                 else:
                                    print('!!!\nInput Number is not Valid! (Too Big or Too Small)\n!!!')
                                    continue

                                 settings[change_setting] = new_value
                                 save_data()
                                 break
                              except:
                                 print('!!!\nInput is Not an Integer!\n!!!')
                        if outercon:
                           continue

                        # Change default not working days
                        if change_setting == 6:
                           new_value = qinput(f'\nEnter the Default Days of the Week you will Not Work on any assignment separated by a Space as your Default Setting\nPress Return to set as None\nExample: mon tue wed thu fri sat sun\n').strip().lower().replace(',',' ').replace('.',' ')
                           if new_value:
                              new_value = new_value.split(' ')
                              valid_days = {'mon':0,'mond':0,'tue':1,'tues':1,'wed':2,'wedn':2,'thu':3,'thur':3,'thurs':3,'fri':4,'frid':4,'sat':5,'satu':5,'sun':6,'sund':6}
                              for index, not_working_day in enumerate(new_value):
                                 if not_working_day in valid_days:
                                    new_value[index] = valid_days[not_working_day]
                                 else:
                                    new_value[index] = None
                              new_value = set(new_value)
                              if None in new_value:
                                 new_value.remove(None)
                              new_value = tuple(new_value)
                           else:
                              new_value = ()
                           settings[6] = new_value
                           def_nwd = new_value
                           save_data()

                        # Toggles boolean settings
                        elif change_setting in range(7,20):

                           # Toggles True to False and False to True
                           new_value = not settings[change_setting]

                           # Modifies the actual settings
                           settings[change_setting] = new_value

                           # Redefines changed variables
                           display_instructions,display_status_priority,autofill,do_after_midnight,ignore_ends,dark_mode,show_progress_bar,show_past,last_opened_backup,hourly_backup,daily_backup,weekly_backup,monthly_backup = settings[7:]

                           # Saves data
                           save_data()
                           
                           # Prints settings that have instructions on how to use
                           if 7 < change_setting and change_setting < 12:
                              print(('\nDisplays the Percentage of an Assignment\'s Priority on the home Assignment Page\nAbbreviated as "SP"',
                                     "\nIf you do not have to Work for a day in an Assignment, and you Forget to input work for that Day, it is assumed you did Nothing\nThe program will auto fill in No work Done on that day because you anyways did Not have to Work\nApplies to periods of a time Longer than a Day",
                                     '\nThe after Midnight assignment Pass is a pass that sets all your current Assignments to Completed, regardless even if they are not.\nThis is to Encourage you to Sleep, as sleep is Extremely important.\nThis can be set to False if you do not want this to Happen, but is not Recommended',
                                     "\nIgnore Ends is only relevant when Minimum Work Time is also Enabled for an Assignment\nIgnores the Minimum Work Time on the first and last Working Day to make the Work Distribution smoother\nThis also fixes an Issue that causes you to Work a Lot More on the First and Last days of an Assignment"
                                     )[change_setting-8]+f"\nThis Setting\'s new value is {new_value} (Old Value: {not new_value})\n")
                              qinput('Enter Anything to Continue:')
                              
                           # Changes colors
                           elif change_setting == 12:
                              if dark_mode:
                                 black = (255,255,255)
                                 border = (200,200,200)
                                 gray = (55,55,55)
                                 gray1 = (40,40,40)
                                 gray2 = (50,50,50)
                                 gray3 = (105,105,105)
                                 gray4 = (70,70,70)
                                 gray5 = (135,135,135)
                                 white = (0,0,0)
                              else:
                                 black = (0,0,0)
                                 border = (55,55,55)
                                 gray = (200,200,200)
                                 gray1 = (215,215,215)
                                 gray2 = (205,205,205)
                                 gray3 = (150,150,150)
                                 gray4 = (185,185,185)
                                 gray5 = (120,120,120)
                                 white = (255,255,255)
                  
                           elif change_setting > 14:
                              # This code handles removing and creating backups
                              
                              backups = {15:' Every Run Backup',16:' Hourly Backup',17:' Daily Backup',18:' Weekly Backup',19:' Monthly Backup'}
                              if new_value:

                                 # If the backup is toggled to True, use the backups dictionary to figure out the name of the backup file to create so it can be referred to later
                                 # This part creates a new file 
                                 file_directory += backups[change_setting]
                                 save_data()
                                 file_directory = original_file_directory

                              # If the backup is toggled to False, then ask for confirmation and then delete the backup
                              elif 'YES' in qinput(f'The{backups[change_setting]} will be Deleted Forever because you have Disabled it.\nEnter "YES" in capital letters to confirm (Enter anything other than "YES" to cancel)\n'):
                                 remove(file_directory + backups[change_setting])
                              else:
                                 continue
                                 
                        # Sets skew ratio for every assignment
                        elif change_setting == 20:
                           while 1:
                              try:
                                 selected_skew_ratio = qinput('Enter the Skew Ratio for Each Assignment (Will be Capped at each assignment\'s Skew Ratio Limit) (Note: 0 is linear):')
                                 if not selected_skew_ratio:
                                    break
                                 selected_skew_ratio = int(selected_skew_ratio,10) + 1
                                 file_index = 1

                                 # Gets the necessary variables from each assignment to calculate the maximum and minimum skew ratio
                                 for file in dat[1:]:
                                    if file[10]:
                                       red_line_start = file[14]
                                    else:
                                       red_line_start = file[11]
                                    x = file[2]
                                    nwd = file[9]
                                    if nwd:
                                       ad = file[1]
                                       assign_day_of_week = ad.weekday()
                                       set_mod_days()
                                    calc_skew_ratio_lim()

                                    # Compares the selected skew_ratio to the skew_ratio limit and caps the skew_ratio at its min/max
                                    if selected_skew_ratio > skew_ratio_lim:
                                       dat[file_index][6] = skew_ratio_lim
                                    elif selected_skew_ratio < 2 - skew_ratio_lim:
                                       dat[file_index][6] = 2 - skew_ratio_lim
                                    else:
                                       dat[file_index][6] = selected_skew_ratio
                                    file_index += 1

                                 # Saves data
                                 if amount_of_assignments:
                                    save_data()
                                 break
                              except:
                                 print('!!!\nInput is Not an Integer!\n!!!')
                                 
                        # Updates the Manual Backup
                        elif change_setting == 21:
                           if manual_backup:
                              selected_backup = qinput('Updating the Manual Backup will Override and Permanently delete the Last manual backup.\nEnter "YES" in capital letters to Confirm\nEnter "DELETE" in capital letters to Permanently Delete the Last Manual Backup\n(Enter anything other than "YES" or "DELETE" to cancel)\n')
                           else:
                              print('Successfully Backed up')
                           if not manual_backup or 'YES' in selected_backup:

                              # If the manual backup is updated, update (or create) the new file storing the data from the manual backup
                              manual_backup = True
                              file_directory += ' Manual Backup'
                              save_data()
                              file_directory = original_file_directory
                              
                           elif 'DELETE' in selected_backup:

                              # Delete the manual backup using os.remove
                              manual_backup = False
                              remove(file_directory + ' Manual Backup')
                              
                        # Loads Backups
                        elif change_setting == 22:
                           backups = []

                           # Loops through all enabled backups and appends the date the backup was last opened (as a datetime object), the date the backup was last opened and the size of the backup, and the name of the backup
                           dict_backups = {' Every Run Backup':last_opened_backup,' Hourly Backup   ':hourly_backup,' Daily Backup    ':daily_backup,' Weekly Backup   ':weekly_backup,' Monthly Backup  ':monthly_backup,' Manual Backup   ':manual_backup}
                           for i in dict_backups:
                              if dict_backups[i]:
                                 with open(file_directory + i.rstrip(),'rb') as datfile:
                                    backup_dat = load(datfile)

                                    # The first item appended is the date the backup was last opened
                                    # However, it is not called anywhere in the code
                                    
                                    # In the sorted() method the collections are first sorted by their first value
                                    # If their first values are the same, then it sorts by their second value
                                    # If their second values are the same, then it sorts by their third value and so on

                                    # Since I am appending tuples (which are collectables) to a list, the sorted() method will sort by the logic stated above
                                    # My goal is to sort the backups by the date the backup was last opened
                                    # Since the first item in the list is the date the backup was last opened, it is will be the first value considered in the sorting algorithm
                                    # Therefore, the backups are sorted from newest to oldest by their date last opened
                                    backups.append((backup_dat[0][0], backup_dat[0][0].strftime(f'%-m/%-d/%Y %-I:%M%p) Size: {len(dumps(backup_dat[1:],protocol=4))-14} Bytes'), i))
                                    
                           if backups:
                              backups = sorted(backups,reverse=True)
                              while 1:
                                 try:

                                    # Asks which backup will be loaded and asks for confirmation
                                    selected_backup = qinput(f'\nAll Available Backups (Sorted from Newest to Oldest):\nCurrent Version Size: {len(dumps(dat[1:],protocol=4))-14} Bytes\n'+'\n'.join(f'{i + 1}){backups[i][2]} (Last Backed Up on {backups[i][1]}' for i in range(len(backups)))+ '\n\nPress Return at Any Time to Escape\nChanging anything after you have loaded a backup does not affect the backup itself\nSelect which Backup you would Like to Load by Entering its Corresponding Number:')
                                    if not selected_backup or 'YES' not in qinput('\nAre you Sure you Want to load this Backup? This will transfer All Backup Data from this Backup to the Current Version\nThis Will Override the current version and Replace it with the Backup Version\nEnter "YES" in capital letters to Confirm (Enter anything other than "YES" to cancel)\n'):
                                       break
                                    selected_backup = int(selected_backup,10) - 1
                                    if -1 < selected_backup and selected_backup < len(backups):

                                        # Transfers backup data to the file directory
                                        with open(file_directory + backups[selected_backup][2].rstrip(),'rb') as datfile:
                                            dat = load(datfile)
                                        set_tomorrow = False
                                        settings = dat[0]
                                        settings[0] = date_last_closed
                                        save_data()
                                        outercon = True
                                        break
                                    print('!!!\nInput Number is not Valid!\n!!!')
                                 except:
                                    print('!!!\nInput is Not an Integer!\n!!!')
                              if outercon:
                                 break
                              continue
                           print('!!!\nThere are no Available Backups to Load!\n!!!')
                        elif change_setting == 23:
                           if 'YES' in qinput('Are you Sure you Want to Restore all Default Setting Values? (This will NOT affect the backup settings)\nEnter "YES" in capital letters to Confirm (Enter anything other than "YES" to cancel)\n'):
                              
                              # Resets Setting Data
                              settings[1:15] = [750,750,35,1,30,(),True,False,True,True,True,True,True,True]
                              width,height,animation_frame_count,warning_acceptance,def_min_work_time,def_nwd,display_instructions,display_status_priority,autofill,do_after_midnight,ignore_ends,dark_mode,show_progress_bar,show_past = settings[1:15]
                              black = (255,255,255)
                              border = (200,200,200)
                              gray = (55,55,55)
                              gray1 = (40,40,40)
                              gray2 = (50,50,50)
                              gray3 = (105,105,105)
                              gray4 = (70,70,70)
                              gray5 = (135,135,135)
                              white = (0,0,0)
                              save_data()
                  else:
                     print('!!!\nInvalid Command!\n!!!')
                     outercon = False
               if outercon:
                  break
         if outercon:
            continue

      # This next section handles assignment input and graph initialization
         
      try:
         
         # If the selected file has already been initialized, load the variables from the saved data
         # selected_assignment is not actually a new list
         # selected_assignment is a pointer to dat[sel], which means changing anything in selected_assignment will also directly change dat[sel]
         selected_assignment = dat[sel]
         file_sel,ad,x,y,works,dif_assign,skew_ratio,ctime,funct_round,nwd,fixed_mode,dynamic_start,unit,total_mode,fixed_start,remainder_mode,min_work_time = selected_assignment
         adone = works[0] # Original starting work value

         # Reinitialize inputs if re-enter mode is enabled
         if reenter_mode:
            raise Exception
      except:

         # If the selected file has not yet been initialized, then initialize it with these inputs
         if reenter_mode:
            old_values = (file_sel,ad,ad+time(x),y,works[0],funct_round,nwd,ctime,min_work_time)
         else:
            dif_assign = 0 # Distance between assign date and start date (redefined later)
            skew_ratio = 1 # Skew Ratio

            # Default variables in an assignment
            fixed_mode = True
            remainder_mode = False
            total_mode = False
         
         # Name of the assignment
         print()
         while 1:
            if reenter_mode:
               reenter_input = qinput(f'Press Return at any Time to Skip Re-Entering the Input and Keep its Old Value\nEnter in "cancel" at Any Time to stop Re-Entering Data and keep the Original Version\nTry not to enter Inputs faster than 0.2 seconds\n\nWhat would you Like to Rename this Assignment (Old Value: {old_values[0]})\n').strip()
               if not reenter_input:
                  break
               file_sel = reenter_input
            else:
               file_sel = qinput('Enter in "cancel" at Any Time to stop Entering in Data\nTry not to enter Inputs faster than 0.2 seconds\n\nWhat would you Like to Name this Assignment\n').strip()
               if not file_sel:
                  outercon = True
                  break
            if file_sel.lower() == 'cancel':
               outercon = True
               break
            if file_sel in files and (not reenter_mode or file_sel != files[sel-1]):
               print('!!!\nName has Already been Taken!\n!!!')
               continue
            break
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         # Assignment date of the assignment
         while 1:
            try:
               if reenter_mode:
                  reenter_input = qinput(f'Re-enter the Assignment Date of this assignment or Enter "today" (Old Value: {old_values[1].strftime("%-m/%-d/%Y")})\nFormat: Month/Day/Year\nExample: 3/2 or mar/2/{str(date_now.year)[-2:]} or mar/2\nYou can Assign in the Future\n').replace(' ','')
                  if not reenter_input:
                     break
                  ad = reenter_input
               else:
                  ad = qinput(f'Enter the Assignment Date of this assignment or Enter "today"\nFormat: Month/Day/Year\nExample: 3/2 or mar/2/{str(date_now.year)[-2:]} or mar/2\nYou can Assign in the Future\n').replace(' ','')
                  if not ad:
                      outercon = True
                      break
               if ad.lower() == 'cancel':
                     outercon = True
                     break
               date_now = date.now()
               date_now = date(date_now.year,date_now.month,date_now.day)
               if ad.lower() == 'today':
                   ad = date_now
                   date_file_created = date_now
                   break
               ad = slashed_date_convert(ad.strip('/'),False)
               if date_now >= ad:
                  dif_assign = (date_now-ad).days
                  dynamic_start = fixed_start = dif_assign   
               break
            except:
               print('!!!\nInvalid Date!\n!!!')
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         # Due date of the assignment
         while 1:
              try:
                  if reenter_mode:
                     reenter_input = qinput(f'Re-enter the Due Date of this assignment (Old Value: {old_values[2].strftime("%-m/%-d/%Y")})\nFormat: Month/Day/Year\nExample: 3/2, mar/2/{str(date_now.year)[-2:]}, mar/2, or 10\nOr, enter the Amount of Days in which this Assignment is Due from the Re-entered Assign Date (As a Whole Number)\n(Don\'t Have a Due Date? Enter in "none" to proceed)\n').replace(' ','').lower()
                     if not reenter_input:
                        x -= (ad - old_values[1]).days
                        if x < 1 or x > (date(9999,12,30)-ad).days:
                           raise Exception
                        break
                     x = reenter_input
                  else:
                     x = qinput(f'Enter the Due Date of this assignment\nFormat: Month/Day/Year\nExample: 3/2, mar/2/{str(date_now.year)[-2:]}, mar/2, or 10\nOr, enter the Amount of Days in which this Assignment is Due from the Assign Date (As a Whole Number)\n(Don\'t Have a Due Date? Enter in "none" to proceed)\n').replace(' ','').lower()
                     if not x:
                        outercon = True
                        break
                  if x == 'cancel':
                     outercon = True
                     break
                  if x == 'none':
                     while 1:
                        try:
                           mx = qinput(f'Enter the Latest date this Assignment can be Due\nOr, enter the Amount of Days until the Latest date this Assignment can be Due\n(Don\'t Care when this Assignment will be Due? Enter "none" to skip)\n')
                           if 'none' in mx.lower():
                              mx = float('inf')
                              break
                           try:
                              mx = int(mx,10)
                           except:
                              date_now = date.now()
                              mx = (slashed_date_convert(mx.strip('/'))-ad).days
                           if mx < 1 or mx > (date(9999,12,30)-ad).days:
                              raise Exception
                           break
                        except:
                           print('!!!\nInvalid Date!\n!!!')
                     x = None
                     break
                  try:
                     x = int(x,10)
                  except:
                     date_now = date.now()
                     x = (slashed_date_convert(x.strip('/'))-ad).days
                  if x < 1 or x > (date(9999,12,30)-ad).days:
                     raise Exception
                  break
              except:
                 print('!!!\nInvalid Date!\n!!!')
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         # Name of each unit of the assignment
         if reenter_mode:
            reenter_input = qinput(f'Re-enter what you would Like to Rename each Unit of Work in this Assignment (Old Value: {unit})\nExample: If this assignment is a book, enter "page"\nIf you are not sure what to name each Unit of Work, Press Return to set it as "Unit"\n').strip().lower()
            if reenter_input:
               unit = reenter_input.rstrip('s').capitalize()
         else:
            unit = qinput('Enter what you would Like to Name each Unit of Work in this Assignment\nExample: If this assignment is a book, enter "page"\nIf you are not sure what to name each Unit of Work, Press Return to set it as "Unit"\n').strip().lower()
            if unit:
               unit = unit.rstrip('s').capitalize()
            else:
               unit = 'Unit'
         if unit == 'Cancel':
            print('Successfully Escaped from Inputs')
            continue

         # Total amount of units in the assignment
         while 1:
              try:
                  if reenter_mode:
                     reenter_input = qinput(f'Re-enter the Total amount of {unit}s in this Assignment (Allows Decimal Inputs) (Old Value: {old_values[3]})\n')
                     if not reenter_input:
                        break
                     y = reenter_input
                  else:
                     y = qinput(f'Enter the Total amount of {unit}s in this Assignment (Allows Decimal Inputs)\n')
                     if not y:
                        outercon = True
                        break
                  if 'cancel' in y.lower():
                     outercon = True
                     break

                  # Note: this equation is a more efficient way of rounding to the nearest millionth place
                  y = ceil(float(y)*1000000-0.5)/1000000
                  
                  if y < 1:
                     raise Exception
                  elif not y % 1:
                     y = ceil(y)
                  break
              except:
                  print('!!!\nInvalid Number!\n!!!')
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         # Total amount of units already completed in the assignment
         ##if reenter_mode and len(works) != 1 and (ad - old_values[1]).days - dif_assign < len(works):
          ##  adone = None
            ##print(f'Re-enter the Total amount of {unit}s Already completed at the Beginning of this Assignment (Allows Decimal Inputs) (Old Value: {old_values[4]}) (SKIPPED)\nThis input has been Skipped because you have changed the Assign Date')
         ##else:
         while 1:
            try:
               if reenter_mode:
                  reenter_input = qinput(f'Re-enter the Total amount of {unit}s Already completed at the Beginning of this Assignment (Allows Decimal Inputs) (Old Value: {old_values[4]})\nThe very First Point on the Blue Line will be set to this Value\n')
                  if not reenter_input:
                     break
                  adone = reenter_input
               else:
                  adone = qinput(f'Enter the Total amount of {unit}s Already completed in this Assignment (Allows Decimal Inputs)\n')
                  if not adone:
                     outercon = True
                     break
               if 'cancel' in adone.lower():
                  outercon = True
                  break
               adone = ceil(float(adone)*1000000-0.5)/1000000
               if adone < 0 or adone >= y:
                  raise Exception
               elif not adone % 1:
                  adone = ceil(adone)
               break
            except:
               print('!!!\nInvalid Number!\n!!!')
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         # Estimated completion time of each unit in the assignment
         while 1:
             try:
                  if reenter_mode:
                     reenter_input = qinput(f'Re-enter the Estimated amount of time to Complete each {unit} in Minutes (Allows Decimal Inputs) (Old Value: {old_values[7]})\n')
                     if not reenter_input:
                        break
                     ctime = reenter_input
                  else:
                     ctime = qinput(f'Enter the Estimated amount of Minutes to Complete each {unit} (Allows Decimal Inputs)\n')
                     if not ctime:
                        outercon = True
                        break
                  if 'cancel' in ctime.lower():
                     outercon = True
                     break
                  ctime = ceil(float(ctime)*1000000-0.5)/1000000
                  if not ctime % 1:
                     ctime = ceil(ctime)
                  if ctime <= 0:
                     raise Exception
                  break
             except:
                print('!!!\nInvalid Number!\n!!!')
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         # Grouping value of the assignment
         while 1:
             try:
                  if reenter_mode:
                     reenter_input = qinput(f'Re-enter what you would Like the Grouping Value of each {unit} to be (Allows Decimal Input) (Enter "1" to group to the nearest whole number) (Old Value: {old_values[5]})\nFor example, if you Enter in 3 as the Grouping Value, you will always work in multiples of 3 (such as 3, 6, 12, etc)\n')
                     if not reenter_input:
                        break
                     funct_round = reenter_input
                  else:
                     funct_round = qinput(f'Enter what would you Like the Grouping Value of each {unit} to be (Allows Decimal Input) (Press Return to group to the nearest whole number)\nFor example, if you Enter in 3 as the Grouping Value, you will always work in multiples of 3 (such as 3, 6, 12...)\n')
                     if not funct_round:
                        funct_round = 1
                        break
                  if 'cancel' in funct_round.lower():
                     outercon = True
                     break
                  funct_round = ceil(float(funct_round)*1000000-0.5)/1000000
                  if not funct_round % 1:
                     funct_round = ceil(funct_round)
                  if funct_round <= 0:
                     raise Exception
                  break
             except:
                print('!!!\nInvalid Number!\n!!!')
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         # Minimum work time
         while 1:
             try:
                  if reenter_mode:
                     min_work_time = ceil(old_values[8]*old_values[7]*1000000-0.5)/1000000
                     if not min_work_time % 1:
                        min_work_time = ceil(min_work_time)
                     if not min_work_time:
                        min_work_time = None
                     min_work_time = qinput(f'Re-enter the Minimum Work Time for each Day you will Work in Minutes (Allows Decimal Inputs) (Enter "none" to disable) (Old Value: {min_work_time})\n').strip().lower()
                     if not min_work_time:
                        min_work_time = str(old_values[8]*old_values[7])
                  else:
                     if def_min_work_time:
                        return_message = f'(Press Return to set as Default: {def_min_work_time} Minutes) (Enter "none" to skip)'
                     else:
                        return_message = '(Press Return to Skip)'
                     min_work_time = qinput(f'Enter the Minimum Work Time for each Day you will Work in Minutes (Allows Decimal Inputs) {return_message}:\n').strip().lower()
                  if min_work_time == 'cancel':
                     outercon = True
                     break
                  if (reenter_mode or def_min_work_time) and min_work_time == 'none':
                     min_work_time = 0
                  else:
                     if min_work_time:
                        min_work_time = ceil(float(min_work_time)*1000000-0.5)/1000000/ctime
                     else:
                        min_work_time = ceil(float(def_min_work_time)*1000000-0.5)/1000000/ctime
                     if min_work_time < 0:
                        raise Exception
                     if not min_work_time % 1:
                        min_work_time = ceil(min_work_time)
                  break
             except:
                print('!!!\nInvalid Number!\n!!!')
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         # Not working days of the assignment
         while 1:
            if reenter_mode:
               nwd = old_values[6]
               reenter_input = qinput(f'Re-enter the Days of the Week you will Not Work on this assignment separated by a Space (Enter "none" to disable) (Old Value: {format_not_working_days(False)})\nExample: mon tue wed thu fri sat sun\nAnything Other than the Days of the Week will be Ignored\n').strip().lower().replace(',',' ').replace('.',' ')
               if not reenter_input:
                  len_nwd = len(nwd)
                  break
               nwd = reenter_input
            else:
               if def_nwd:
                  return_message = f'(Press Return to Set as Default: {format_not_working_days()}) (Enter "none" to skip)'
               else:
                  return_message = '(Press Return to Skip)'
               nwd = qinput(f'Enter the Days of the Week you will Not Work on this assignment separated by a Space {return_message}\nExample: mon tue wed thu fri sat sun\nAnything Other than the Days of the Week will be Ignored\n').strip().lower().replace(',',' ').replace('.',' ')
            if nwd == 'cancel':
               outercon = True
               break
            if (reenter_mode or def_nwd) and nwd == 'none':
               nwd = ()
            else:
               if nwd:
                  nwd = nwd.split(' ')

                  # Uses a dictionary to convert weekdays into numbers
                  valid_days = {'mon':0,'mond':0,'tue':1,'tues':1,'wed':2,'wedn':2,'thu':3,'thur':3,'thurs':3,'fri':4,'frid':4,'sat':5,'satu':5,'sun':6,'sund':6}
                  
                  for index, not_working_day in enumerate(nwd):
                     if not_working_day in valid_days:
                        nwd[index] = valid_days[not_working_day]
                     else:
                        nwd[index] = None
                  nwd = set(nwd)
                  if None in nwd:
                     nwd.remove(None)
                  nwd = tuple(nwd)
               else:
                  nwd = def_nwd
            len_nwd = len(nwd)
            break
         if outercon:
            print('Successfully Escaped from Inputs')
            continue

         if reenter_mode:

            # If the reentered assign date cuts off some of the work inputs, adjust the work inputs accordingly
            removed_works_start = (ad - old_values[1]).days - dif_assign
            if removed_works_start < 0:
               removed_works_start = 0
            removed_works_end = len(works) - 1
            if removed_works_end + dif_assign >= x:
               removed_works_end = x - dif_assign
               if works[removed_works_end] != y:
                  removed_works_end -= 1
            works = [works[n] - works[0] + adone for n in range(removed_works_start,removed_works_end+1)]
            if not works:
               works = [adone]
               if dif_assign:
                  dif_assign -= 1
            adone = works[0]
            if dynamic_start > x - 1:
               dynamic_start = x - 1
            if fixed_start > x - 1:
               fixed_start = x - 1
            
         else:

            # Defines the work inputs
            # Since the assignment was just created there are not any work inputs
            # The reason why the variable "works" has adone as the first value is to
            # serve as the 0th or the starting day of the assignment
            # This is the reason why wlen, which represents the length of works,
            # Is subtracted by 1 as it doesn't count the 0th day, which is not needed
            # For all the calculations involving it
            works = [adone]

         # If the user doesn't have a due date, set the due date to the x value of when the line with the slope of min_work_time intersects y
         if x == None:
            if min_work_time:
               x = (y - works[-1])/ceil(ceil(min_work_time/funct_round)*funct_round)
            else:
               x = (y - works[-1])/funct_round
            if nwd:
               if len_nwd == 7:
                  x = 1
               else:
                  # This tiny equation has a bit of thinking

                  # My goal here is to find a value where removing all not working days results in x (without not working days)
                  # For referance, look at this:
                  # x    0 1 2 3 4 5 6 7 | 8 9 10 11 12 13 14 | 15 16 17 18 19 20 21
                  # f(x) 0 0 0 0 0 0 3 6 | 6 6 6  6  6  9  12 | 12 12 15
                  # The goal is to find the week before the value and guess and check each day of the next week for the first value that results in x (without not working days)
                  # The equation for doing this backwards is 7*x/(7-len_nwd)
                  # To explain this, pretend x = 5 from the above example, which represents the number of days the user will work or x (without not working days)
                  # For every week in this example, the user works 2 days
                  # So, find how many 2 days fit into x = 5 and multiply that number by 7 
                  # If you aren't me, don't worry if you don't get this

                  # Since we want to find the week before the value, round x down to the nearest (7 - len_nwd), or 2 in this example
                  # that would simplify it to be 7*int(x/(7-len_nwd))*(7-len_nwd)/(7-len_nwd)
                  # or 7*int(x/(7-len_nwd))
                  
                  # I subtract one at the end of the assignment for the for loop
                  # And I subtract one in the middle of the equation to fix a wrong week bug
                  guess_x = 7*int(x/(7-len_nwd) - 1) - 1

                  # Guesses for the rest of the week
                  assign_day_of_week = ad.weekday()
                  red_line_start = dif_assign
                  set_mod_days()
                  while 1:
                     guess_x += 1
                     if guess_x - guess_x // 7 * len_nwd - mods[guess_x % 7] == ceil(x):
                        x = guess_x
                        break
            elif x:
               x = ceil(x)
            else:
               x = 1
            if x > mx:
               x = mx
               
         if reenter_mode:
            dynamic_start -= (ad - old_values[1]).days
            fixed_start -= (ad - old_values[1]).days
            if dynamic_start < 0:
               dynamic_start = 0
            if fixed_start < 0:
               fixed_start = 0
         else:
            dynamic_start = fixed_start = dif_assign # X value of the start of the red line in dynamic and fixed mode

         # Appends all the inputted information to the main file
         #                         0     1  2 3   4       5          6        7        8       9      10          11        12      13         14            15            16
         selected_assignment = [file_sel,ad,x,y,works,dif_assign,skew_ratio,ctime,funct_round,nwd,fixed_mode,dynamic_start,unit,total_mode,fixed_start,remainder_mode,min_work_time]

         if reenter_mode:

            # If reenter_mode is enabled, replace the old data with the reentered data
            dat[sel] = selected_assignment

            # Saves the data
            save_data()
            continue
            
         else:

            # If reenter_mode is disabled, append new data
            dat.append(selected_assignment)

            # Saves the file to Memory
            save_data()

      # Calculates the start of the red line (used in other functions) and the value of the work input the start is at
      if fixed_mode:
         start_lw = works[fixed_start - dif_assign]
         red_line_start = fixed_start
      else:
         start_lw = works[dynamic_start - dif_assign]
         red_line_start = dynamic_start
         
      # Caps funct_round at y
      if funct_round > y - start_lw:
         funct_round = y - start_lw

      # Caps min_work_time at y
      if min_work_time > y - start_lw:
         min_work_time = y - start_lw

      # If the minimum work time is less than the grouping value, that means
      # The minimum work time is always fulfilled by the grouping value, making
      # It completely irrelevant
      if min_work_time <= funct_round:
         min_work_time = 0
         
      # Fixes a rounding bug with min_work_time

      # Let funct_round be 4 and min_work_time be 5
      # In the code, f(4) = 18 and f(5) = 23
      # However, f(4) gets rounded to 20 and f(5) gets rounded to 24, breaking min_work_time
      # This fixes the problem
      elif 1 < min_work_time / funct_round < 2:
         min_work_time = funct_round * 2
         
      # Smallest multiple of min_work_time and funct_round that is greater than min_work_time
      # This is the minimum amount of units the user will do in any given working day
      if min_work_time:
         min_work_time_funct_round = ceil(min_work_time/funct_round)*funct_round
      else:
         min_work_time_funct_round = funct_round
         
      assign_day_of_week = ad.weekday() # Weekday of assign date
      len_nwd = len(nwd) # Length of not working days
      if nwd:
         set_mod_days()
         ignore_ends_mwt = ignore_ends and min_work_time and (x - red_line_start) - (x - red_line_start)//7 * len_nwd - mods[(x - red_line_start) % 7] != 2
      else:
         ignore_ends_mwt = ignore_ends and min_work_time and x != 2

      # Defining variables
      date_file_created = ad + time(dif_assign) # Date file is created
      set_start = False # Manual set start
      set_skew_ratio = False # Manual set skew_ratio
      clicked_once = False # Flag if "n" is pressed once
      due_date = ad + time(x) # Due date
      
      # Calculates weather to display the year or not
      if ad.year != due_date.year:
         disyear = ', %Y'
      else:
         disyear = ''

      # Defining more variables
      date_now = date.now()
      date_now = date(date_now.year,date_now.month,date_now.day)
      ndif = (date_now-date_file_created).days # Amount of days between today and the date when the assignment was created
      xdif = (date_now-ad).days # Amount days between today and assign date
      rem_zero = x - dif_assign > 15 # Determines if to overlook zero values in the schedule        
      wlen = len(works) - 1 # Length of inputs minus one because most calculations involving it don't use the intial work value
      day = wlen # Day of the assignment you will be at
      smart_skew_ratio = x < 50 # Cutoff for using smart skew ratio (explained later)
      lw = works[wlen] # Last work input
      stry = '%g' % y # Formatted Total Units of Work
      wCon = (width-55)/x # Important Scaling Constant for Width
      hCon = (height-55)/y # Important Scaling Constant for Height

      # Formatting variables for the graph
      point_text_width = gw(font3,f'(Day:{x},{unit}:{y})')
      point_text_height = font3.render(f'(Day:{x},{unit}:{y})',1,black).get_height()
      left_adjust_cutoff = (width - 50 - point_text_width)/wCon
      up_adjust_cutoff = point_text_height/hCon
      
      y_fremainder = (y - start_lw) % funct_round # Remainder when the total number of units left in the assignment is divided by funct_round, or the grouping value
      y_mremainder = (y - start_lw) % min_work_time_funct_round # Remainder when the total number of units left in the assignment is divided by min_work_time_funct_round, or the minimum a use will work in a day

      # Initializing assignment
      calc_skew_ratio_lim()
      pset()

      # Subtracts 1 day if the assignment is in progress
      # This is because if the an assignment is in progress, that means there is an input less than the amount needed to be done for a day
      # Normally each input increases the day by 1
      # However, if the assignment is in progress, then it do not increase the day by 1 because the work has not been done
      if ndif > -1 and ndif == day - 1 and lw != works[-2] and lw < funct(day + dif_assign):
         day -= 1

      # Limits animation_frame_count if x or y is too small
      min_xy = min(x,y)
      if (min_xy - 1)/animation_frame_count < 0.5:
         animation_frame_count = ceil((min_xy - 1)/0.5)
         if not animation_frame_count:
            animation_frame_count = 1
         
      # Precalculated increase x and y amount in order to make sure there are an animation_frame_count amount of frames
      increase_x = (x - 1)/animation_frame_count
      increase_y = (y - 1)/animation_frame_count 

      # x and y are set to 1 at the beginning of the animation
      x = 1
      y = 1
         
      # Initializes Screen
      pygame.display.set_caption('Time Management')
      screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)

      original_min_work_time = min_work_time
         
      # Used for positioning the slashes in the progress bar during the animation
      slash_x_counter = width-145
      (event.type for event in pygame.event.get())
      for i in range(animation_frame_count - 1):
         
         if any(event.type not in (1,4) for event in pygame.event.get()):
            break

         # increase_x and increase_y are added a precalculated amount such that x and y will reach their original value after the animation
         x += increase_x
         y += increase_y

         # redefines remainder variables
         y_fremainder = (y - start_lw) % funct_round
         y_mremainder = (y - start_lw) % min_work_time_funct_round
         if selected_assignment[8] > y - start_lw:
            funct_round = y - start_lw
            if original_min_work_time > y - start_lw:
               min_work_time = y - start_lw
            if original_min_work_time <= funct_round:
               min_work_time = 0
            elif 1 < original_min_work_time / funct_round < 2:
               min_work_time = funct_round * 2
            if min_work_time:
               min_work_time_funct_round = ceil(min_work_time/funct_round)*funct_round
            else:
               min_work_time_funct_round = funct_round
         else:
            funct_round = selected_assignment[8]
            min_work_time = original_min_work_time
            if min_work_time:
               min_work_time_funct_round = ceil(min_work_time/funct_round)*funct_round
            else:
               min_work_time_funct_round = funct_round

         # draws each frame
         draw(1,0)
         pygame.event.pump()

         # Moves the slash in the progress bar because it looks cool
         if lw: 
            slash_x_counter -= lw/y*4
         else:
            slash_x_counter -= 4/y

      # Even though the x and y values are precalculated to reach their original value, there still may be a floating point error of a few quadrillionth decimal places, messing up flooring and ceiling calculations
      # To make sure this does not happen, I set x and y back to their inputted value
      x = selected_assignment[2]
      y = selected_assignment[3]
      funct_round = selected_assignment[8]
      min_work_time = original_min_work_time
      if min_work_time:
         min_work_time_funct_round = ceil(min_work_time/funct_round)*funct_round
      else:
         min_work_time_funct_round = funct_round
      y_fremainder = (y - start_lw) % funct_round
      y_mremainder = (y - start_lw) % min_work_time_funct_round
      draw(0,0)
      pygame.event.pump()

      # This is the end of the home() function. This entire thing handles the assignment page, the settings, the commands for assignments, the inputs of an assignment, and the initialization of an assignment
      print()
      return
   
# Calculates variables for the parabola
def pset():
         global a, b, skew_ratio, cutoff_transition_value, cutoff_to_use_round, return_y_cutoff, return_0_cutoff, add
         add = 0

         # This entire thing ignores the function outputs before the start and after the end of the assignment
         try:

            # x coordinate of third first point
            x1 = int(x - red_line_start)

            # y coordinate of third first point
            if ignore_ends_mwt:
               
               # If ignore_ends is enabled, which ignores the minimum work time for the first and last working days, set the parabola to end at exactly y
               y1 = y - start_lw
               
            else:
               
               # If ignore_ends is disabled, which ignores the minimum work time for the first and last working days, set the parabola to end at the first value that is rounded to y
               y1 = y - start_lw - y_mremainder

            # Subtracts not working days (explained later)
            if nwd:
               x1 -= x1//7 * len_nwd + mods[x1 % 7]

            # Checks if the parabola is being manually set
            if set_skew_ratio:

               # x2 and y2 are the mouse coordinates, meaning the parabola will pass through the mouse
               x2, y2 = pygame.mouse.get_pos()
               x2 = (x2 - 49.5) / wCon - red_line_start
               y2 = (height - y2 - 50.5) / hCon - start_lw
               
               # Checks if the mouse is outside the graph
               if x2 < 0:

                  # If it is, make a line
                  a = 0
                  b = y1
                  skew_ratio = skew_ratio_lim
                  return_y_cutoff = 0
                  return
               
               # More handling of not working days (still explained later)
               intx2 = int(x2)
               if nwd:
                  if (assign_day_of_week + intx2 + red_line_start) % 7 in nwd:
                     x2 = intx2
                  x2 -= x2//7 * len_nwd + mods[intx2 % 7]

               # Checks if the mouse is outside the graph
               if x2 >= x1:
                  
                  # Heavy simplification here
                  # Set y2 to be zero and x2 to be x - 1 and simplify the a and b equations
                  a = y1/x1
                  b = a - a*x1
                  skew_ratio = 2 - skew_ratio_lim

               else:
                  
                     # Offsets mouse y pos if remainder_mode is enabled
                     if remainder_mode:
                        y2 -= y_fremainder

                     # If parabola is being manually set, Connects the points (0,0) (x2,y2)[mouse coordinates] and (x,y)
                     # CREDIT OF THIS ALGORITHM GOES TO https://stackoverflow.com/questions/717762/how-to-calculate-the-vertex-of-a-parabola-given-three-points
                     a = (x2 * y1 - x1 * y2) / ((x1-x2) * x1 * x2)
                     b = (y1 - x1 * x1 * a) / x1
                     
                     # Sets skew ratio on the graph depending on the mouse coordinates
                     # This is to "save" the curve of the parabola as a skew ratio value
                     skew_ratio = (a + b) * x1 / y1
                     if skew_ratio > skew_ratio_lim:
                        skew_ratio = skew_ratio_lim
                     elif skew_ratio < 2 - skew_ratio_lim:
                        skew_ratio = 2 - skew_ratio_lim

                     # Locks to linear if the skew ratio is +-0.025 away from linear
                     elif 0.975 < skew_ratio and skew_ratio < 1.025:
                        skew_ratio = 1
                        a = 0
                        b = y1/x1
            else:

               # If parabola is not being manually set, connect the points (0,0) (1,y/x * skew ratio) (x,y)
               # Notice how the parabola passes through the origin, meaning it does not use a c variable
               # If the start of the line is moved, requiring the red line to start not at the origin, translate the parabola onto the start instead of using a variable
               # This increases efficiency and optimizations
               # CREDIT OF THIS ALGORITHM GOES TO https://stackoverflow.com/questions/717762/how-to-calculate-the-vertex-of-a-parabola-given-three-points

               a = y1 * (1 - skew_ratio) / ((x1-1) * x1)
               b = (y1 - x1 * x1 * a) / x1
               
         except:
            
            # A function by definition cannot have two separate y values for the same
            # If any two x's of the points the function must connect to are accidentally the same, then run this
            # For example, this cannot pass through (1,1) and (1,2) at the same time as it is impossible for input 1 to output 1 and 2 at the same time

            # This makes a line instead of a parabola
            a = 0
            b = y1
            return_y_cutoff = 0
            return_0_cutoff = 1
            cutoff_transition_value = 0
            return

         # Calculating at which x value the parabola first becomes positive
         # In other words, I am looking for its zero
         
         # a * b > 0 makes sure both a and b are positive (they cannot both be negative)
         # This is because some values of a and b have a skew ratio less than 1, resulting in -b/a being negative number
         # Since this is only paying attention to the values in the assignment and not outside of the assignment, set it back to zero if this happens
         if skew_ratio > 1 or not a or a * b > 0:

            # If the parabola opens downward, its zero is at 0, because f(0) = a*0+b*0 which simplifies f(0) = 0
            # I am ignoring the values of the parabola after the end of the assignment, which includes its second zero
            funct_zero = 0
            
         else:

            # If the parabola opens upwards, its first zero is at 0 by the logic stated above and its second at -b/a by the logic stated below
            # I want to know the zeros of f(x) = ax^2+bx
            # I can rewrite this as 0 = ax^2+bx, which simplifies to 0 = x(ax+b)
            # If a product is equal to zero, then either of the terms must be zero
            # So, either x = 0, which is a zero we already know, or ax+b = 0, which simplifies to x = -b/a
            # In this case, I want the rightmost zero because the values between 0 and -b/a are all negative because the parabola opens upwards
            # Since I am looking for when the parabola first becomes positive, I am focusing on the second zero, -b/a
            funct_zero = -b/a
         
         # FIRST READ THE COMMENTS IN FUNCT() BEFORE READING THE COMMENTS HERE
         # The goal of this entire section is to calculate the cutoff, the cutoff transition value, and the return y cutoff

         if funct_round < min_work_time:
            cutoff_transition_value = 0
            if a:
               while 1:

                  # The equation (s-b)/a/2 calculates the rate of change "s" on a parabola with the values of a and b. Here is the reasoning:
                  # The derivative of an equation is the slope of a line that lies tangent to a curve at a specific point
                  # I want to find when the derivative of the parabola is min_work_time, which I will refer to as "s" for this demonstration
                  # The function of the parabola is in the form: f(x) = ax^2+bx
                  # The derivative of the parabola is f'(x) = 2ax+b, which can be calculated using the power rule
                  # I want to find when 2ax+b is equal to s, so I can make the equation s = 2ax+b
                  # If I solve for x in this equation, I get x = (s-b)/(2*a), or x = (s-b)/a/2

                  # I set s to min_work_time_funct_round, which is the least amount of units of work a user will do in any given day
                  cutoff_to_use_round = int(ceil((min_work_time_funct_round-b)/a/2*1000000)/1000000)

                  # This part calculates the cutoff transition value
                  # The reason why I need this variable is fix the transition in the cutoff
                  # This is better explained with an example
                  # pretend the minimum work time is 10 and the cutoff to stop using round is at 9.5
                  # Let's say the raw unrounded of the function outputs are f(8) = 46, f(9) = 56, f(10) = 66
                  # Since f(8) and f(9) are before the cutoff, they will both be rounded to the nearest 10, because that is the minimum work time.
                  # So, the final values of the function outputs are f(8) = 50 and f(9) = 60
                  # Since f(10) is after the cutoff, it will not be rounded. So, f(10) = 66
                  # Notice how f(9) = 60 and f(10) = 66
                  # You will only have to work 6 units even though the minimum work time is 10 units
                  # To fix this issue, I decided to add a cutoff transition value to all the function outputs after the cutoff
                  # In this case, after calculating the cutoff transition value, 4 will be added to f(10) and all outputs after it.
                  # So, f(10) will be 70 instead of 66
                  # This entire bottom section's purpose is to calculate the cutoff transition value

                  # Once I have calculated the zero, it checks whether the cutoff is between the zero and the end of the assignment
                  # If it is not, the cutoff is outside of the graph, which makes the cutoff_transition_value irrelevant
                  # If it is, then calculate the cutoff transition value
                  if funct_zero < cutoff_to_use_round and cutoff_to_use_round < x1:

                     # Uses a modified version of the function to find the difference between the output before the after the cutoff
                     # Then, it calculates the cutoff transition value by finding out how much to add or subtract
                     first_loop=True
                     for n in range(cutoff_to_use_round,cutoff_to_use_round + 2):
                        if (skew_ratio < 1) == (n == cutoff_to_use_round):
                           output = min_work_time_funct_round * ceil(n*(a*n+b)/min_work_time_funct_round-0.5+1e-10)
                        else:
                           output = funct_round * ceil(n*(a*n+b)/funct_round-0.5+1e-10)
                        if debug_mode and output < 0:
                           print('output less than 0')
                        if remainder_mode and output:
                           output += y_fremainder
                        if first_loop:
                           difference = output
                        first_loop = False

                     # Around this block of code under this comment, there was an if statement that surrounded this:
                     # If output - difference: (run the block)
                     # else: cutoff_transition_value = 0
                     # I do not remember why I put this code nor how it is useful
                     # If there is ever an error, consider putting that if statement back

                     # Calculates cutoff transition_value to adjust the transition in min work time

                     cutoff_transition_value = min_work_time_funct_round - output + difference

                     # This part only runs if ignore_ends is enabled
                     
                     # Pretend cutoff_transition_value is 0 for now
                     # In the code, the parabola connects directly to y instead of connecting to the point where it first rounds to y
                     # For example, pretend y is 50 and it rounds to the nearest 10
                     # If ignore_ends were disabled, then the last value of the parabola would be at 45, which would round to 50
                     # Pretend the parabola values are 15,25,35, and 45
                     # However, since the 45 is rounded to 50, the real values are 5,15,25,35, and 50
                     # This causes you to work 15 units at the end while on all the other days you work 10, which is weird and unneccessary
                     # The reason why not connect the parabola directly to y is because it sometimes breaks minimum work time on the very last day of the assignment
                     # Similarly, if the first working day on the parabola is less than the minimum work time, it adds that value to the next working day value, which can sometimes cause excess work to be done on the first day
                     # This is what ignore_ends does; when it is enabled it notifies the user that the minimum work time will be ignored on the first and last working days
                     # On the first day, it runs a check to not combine it with the next day if the value is less than minimum work time
                     # On the last day, it connects directly to y

                     # Now pretend the cutoff_transition_value is more than 0
                     # For this example, pretend it is 5
                     # This would mean all values of the parabola will be added to 5
                     # Pretend y is 100 and the minimum work time is 10 units
                     # The parabola values for this example are ...70, 80, 90, 100
                     # In this situation, since the cutoff transition value is 5, all values will be added to 5
                     # Since 100 is the end of the assignment, 100 stays at 100
                     # The new values of the parabola are now ...75, 85, 95, 100
                     # Since ignore_ends is on in this situation, it is ok that the last working day is less than the minimum work time
                     # So far, there is nothing wrong with this

                     # Now pretend the cutoff_transition_valus is less than 0
                     # For this example, pretend it is -5
                     # This would mean all values of the parabola will be added to 5
                     # Pretend y is 100 and the minimum work time is 10 units
                     # The parabola values for this example are ...70, 80, 90, 100
                     # In this situation, since the cutoff transition value is -5, all values will be subtracted 5
                     # Since 100 is the end of the assignment, 100 stays at 100
                     # The new values of the parabola are now ...65, 75, 85, 100
                     # This time, the user will have to work an excess amount on the last working day
                     # On all the other days, the user will work 10 units but on the last day, the user works 15 units
                     # The whole point of ignore_ends was the fix this issue and it is still happening
                     # Instead of trying to fix the parabola values when it negative, I thought the best way to fix this issue was to make sure it never happened
                     # The below line of code keeps adding 1 to y1 until the cutoff_transition_value is positive again, making it so that the above situation never happens
                     # The 2nd to last statement in the line puts a limit to how much can be added to y1
                     # The last statement is a while loop failsafe if it loops for more than 1000 times                     
                     if ignore_ends_mwt and cutoff_transition_value < y_mremainder - min_work_time_funct_round and y1 + cutoff_transition_value <= y - start_lw and y - start_lw - y1 - cutoff_transition_value < 1000:
                        y1 += 1
                        a = y1 * (1 - skew_ratio) / ((x1-1) * x1)
                        b = (y1 - x1 * x1 * a) / x1
                        continue
                  else:
                     cutoff_transition_value = 0
                  break
               else: cutoff_to_use_round = None
         # For the rest of the function, I will refer to the total amount of units in the assignment as y
         # The rest of the function calculates the return_y_cutoff, or when the parabola exceeds y
         # I found it the most efficient to use a cutoff, because I can run a check at the beginning of the funct to return y if the inputted value is after the cutoff, increasing efficiency

         # If the user chooses to apply the min_work_time for the first and last days of the assignment, set the cutoff to when the red line hits y
         
         # First, I need to calculate the x value when the function first returns y
         # This was actually a lot more complicated than I originally thought
         # This equation determines whether the function output rounds to the minimum work time or not at the return_y_cutoff
         return_y_cutoff = 1e-10
         if funct_round < min_work_time and (not a and b < min_work_time_funct_round or skew_ratio < 1 and x1 <= cutoff_to_use_round or skew_ratio > 1 and cutoff_to_use_round < ceil(((b*b+4*a*y1)**0.5-b)/a/2-1)):

               if ignore_ends_mwt:

                     # Sets the y_value_to_cutoff if ignore_ends is enabled
                     y_value_to_cutoff = y - start_lw - y_mremainder - min_work_time_funct_round / 2
                     if cutoff_transition_value < y_mremainder and (x1-1) * ((x1-1) * a + b) > y_value_to_cutoff:

                        # suppose min_work_time_funct_round is 10 and y is 148
                        # Suppose f(x-2) = 130, f(x-1) = 140, and f(x) = 150
                        # Normally, return_y_cutoff would be set at 140 and then f(x-1) would output 150 instead of 140 in order to obey the minimum work time
                        # The new outputs would be f(x-2) = 130, f(x-1) = 148, f(x) = 148
                        # But since ignore_ends is enabled, the minimum work time is ignored
                        # This means f(x-1) no longer has to obey the minimum work time
                        # So, one would be added to return_y_cutoff in order to make the outputs stop at 148
                     
                        # (x1-1) * ((x1-1) * a + b) > y_value_to_cutoff makes sure the line doesn't accidentally go over y because of return_y_cutoff if the first condition is true
                        
                        return_y_cutoff += 1
                  
               else:
               
                  # If ignore_ends is disabled, run this code
               
                  # To understand this part, first know that the parabola doesn't always reach y
                  # For example, let's say an assignment groups to multiples of 5 and the y is 93
                  # It would be impossible for the parabola to reach y because y is not divisible by 5
                  # So, the parabola instead reaches 90, which I will now refer to as y1
                  # The 3 remainder units is referred to as y_mremainder in the code
                  # In the function, there will be a check with the return_y_cutoff where if the output is y1 or higher, then return y
                  # That might have sounded confusing, know the parabola hits y1 but the function actually returns y
                  
                  # If the function rounds to the minimum work time, set the y_value_to_cutoff to y1 - min_work_time / 2
                  # The reason why I subtracted min_work_time / 2 from the end of y1 is because I know y1 is divisible by min_work_time, which is the grouping value, by the logic above
                  # I also know the function is rounded to the nearest min_work_time
                  # So, that means y1 - min_work_time / 2 is the first value that rounds to y1
                  y_value_to_cutoff = y1 - min_work_time_funct_round / 2
                  
                  # Pretend y is 144 and the minimum work time is 6
                  # This will mean y1 is 144 because it is the biggest number divisible by six that is less than or equal to y
                  # Pretend f(8) = 132 and f(9) = 138 and f(10) = 144
                  # Know that f(9) - f(8) = 6 and f(10) - f(9) = 6
                  # Now, let's say the cutoff_transition_value from above is 2, which means add 2 to these values
                  # So, f(8) = 134 and f(9) = 140 and f(10) = 144
                  # f(10) doesn't increase to 146 because 144 is the y or maximum value
                  # Now, when you compare the difference, f(9) - f(8) = 6 and f(10) - f(9) = 4
                  # This breaks the minimum work time, since even though I inputted 6 there is a difference of 4 units at the end
                  # This line of code below checks for that error and adjusts the y_value_to_cutoff appropriately
                  if y_mremainder < cutoff_transition_value:

                     # Decreases y_value_to_cutoff accordingly to solve the above problem
                     y_value_to_cutoff -= min_work_time_funct_round

                  # Pretend y is 148 and the minimum work time is 6
                  # This will mean y1 is 144 because it is the biggest number divisible by six that is less than or equal to y
                  # Pretend in this case f(8) = 132 and f(9) = 138 and f(10) = 144
                  # f(10) goes through a check and since it realizes that it reached 144, f(10) actually returns 148
                  # So, f(8) = 132 and f(9) = 138 and f(10) = 148
                  # Know that f(9) - f(8) = 6 and f(10) - f(9) = 10
                  # Now, let's say the cutoff_transition_value from above is -2, which means subtract 2 from these values
                  # So, f(8) = 130 and f(9) = 136 and f(10) is still 148 because of the check
                  # Now, when you compare the difference, f(9) - f(8) = 6 and f(10) - f(9) = 12
                  # It doesn't make sense from a user perspective to have a difference of 12 when it can just be split up into 2 sixes
                  # This code checks for that error and adjusts the y_value_to_cutoff appropriately
                  elif y_mremainder - cutoff_transition_value >= min_work_time_funct_round:

                     # Makes sure the parabola reaches y before the end of the assignment in order for the above problem to be valid
                     ##print((skew_ratio > 1) == (-b/a/2 < x1))
                     if skew_ratio > 1 and -b/a/2 < x1:

                        # Increases y_value_to_cutoff accordingly to solve the above problem
                        y_value_to_cutoff += min_work_time_funct_round
                        if b*b < -4*a*y_value_to_cutoff:

                           # If parabola doesn't reach the readjusted value, set it back to y1
                           y_value_to_cutoff = y1
                     else:

                        # If the graph reaches y only at the end of the assignment and not anywhere before,
                        # Set the return_y_cutoff to be at the end
                        return_y_cutoff = x1 - 1

                  # Offsets the y_value_to_cutoff if remainder_mode is enabled
                  if remainder_mode:
                     y_value_to_cutoff -= y_fremainder
         else:
            
               if ignore_ends_mwt:

                  # Sets the y_value_to_cutoff if ignore_ends is enabled
                  y_value_to_cutoff = y - start_lw - y_fremainder - funct_round / 2

               else:

                  # If the function does not round to the minimum work time, set the y_value_to_cutoff to this
                  y_value_to_cutoff = y - start_lw - y_fremainder - min_work_time_funct_round + funct_round / 2

                  # Subtracts the cutoff_transition_value if the function uses it at the return_y_cutoff
                  if funct_round < min_work_time and skew_ratio < 1:
                     y_value_to_cutoff -= cutoff_transition_value

                     # Makes sure the cutoff doesn't accidentally exceed the maximum of the parabola
                     if y_value_to_cutoff >= y1:
                        return_y_cutoff = x1 - 1
                     
         # Once the y_value_to_cutoff has been calculated, use the quadratic formula to find when the parabola is equal to that value to find the return_y_cutoff
         if return_y_cutoff != x1 - 1:
            if y_value_to_cutoff > 0 and y > start_lw and (a or b):
               if a:
                  return_y_cutoff += ((b*b+4*a*y_value_to_cutoff)**0.5-b)/a/2
               else:
                  return_y_cutoff += y_value_to_cutoff/b
            else:
               return_y_cutoff = 0

            # Fixes a glitch when the cutoff_transition_value causes the output value right before the return_y_cutoff to exceed y
            # It does this by running a modified version of funct() and checking whether it exceeds y
            # If it does, subtract 1 from the return_y_cutoff
            first_loop = True
            for n in range(ceil(return_y_cutoff - 2),ceil(return_y_cutoff)):
               if funct_round < min_work_time and (not a and b < min_work_time_funct_round or a and (skew_ratio < 1) == (n <= cutoff_to_use_round)):
                  original_output = output = min_work_time_funct_round * ceil(n*(a*n+b)/min_work_time_funct_round-0.5+1e-10)
                  if skew_ratio > 1:
                     output += cutoff_transition_value
                  else:
                     output -= cutoff_transition_value
               else:
                  original_output = output = funct_round * ceil(n*(a*n+b)/funct_round-0.5+1e-10)
               if remainder_mode:
                  output += y_fremainder
                  original_output += y_fremainder
               if first_loop:
                  difference = output
               first_loop = False
            if output > original_output and output + start_lw > y:
               return_y_cutoff -= 1

         # The same data collected from the modified version of funct() from above is also used to set the variable add
         # This variable adds the min_work_time_funct_round on the very last day of the assignment in order to make linear graphs more smooth
         if ignore_ends_mwt and y - output - start_lw > min_work_time_funct_round and not output - difference and not ((y - start_lw) / funct_round) % 1:
            add = min_work_time_funct_round

         # Sets the return_0_cutoff
         if a:
            if ignore_ends_mwt and skew_ratio < 1 and funct_round < min_work_time and cutoff_to_use_round < funct_zero:

               # This is supposed to solve the issue where it still obeyed the min_work_time when ignore_ends was enabled and when cutoff_to_use_round < funct_zero and skew_ratio < 1
               # This basically sets the y_value_to_cutoff to be at 0 instead of min_work_time_funct_round - funct_round / 2
               return_0_cutoff = funct_zero
               return
            
            if funct_round < min_work_time and (not a and b < min_work_time_funct_round or a and (skew_ratio < 1) == (funct_zero <= cutoff_to_use_round)):

               # If the function rounds to min_work_time_funct_round at its zero, set the y_value_to_cutoff to this
               y_value_to_cutoff = min_work_time_funct_round / 2
               
            else:

               # If the function rounds to funct_round at its zero, set the y_value_to_cutoff to this
               y_value_to_cutoff = min_work_time_funct_round - funct_round / 2

            # Uses the quadratic equation to find the x value when the y value is y_value_to_cutoff
            return_0_cutoff = (-b + (b*b + 4*a*y_value_to_cutoff)**0.5)/a/2

            if funct_round < min_work_time:
               if ignore_ends_mwt:
                  if cutoff_transition_value < 0 and return_0_cutoff > 1:

                     # If ignore_ends is enabled, subtract 1 from the return_0_cutoff
                     # Copy of the below problem from earlier but except at the beginning of the graph instead of at the end
                     
                     # suppose min_work_time_funct_round is 10 and y is 148
                     # Suppose f(x-2) = 130, f(x-1) = 140, and f(x) = 150
                     # Normally, return_y_cutoff would be set at 140 and then f(x-1) would output 148 instead of 140 in order to obey the minimum work time
                     # The new outputs would be f(x-2) = 130, f(x-1) = 148, f(x) = 148
                     # But since ignore_ends is enabled, the minimum work time is ignored
                     # This means f(x-1) no longer has to obey the minimum work time
                     # So the real outputs would be f(x-2) = 130, f(x-1) = 140, f(x) = 148
                     # So, one would be added to return_y_cutoff in order to make the outputs stop at 148
                     
                     return_0_cutoff -= 1
               else:

                  # If ignore_ends is not enabled, the predicted value of return_0_cutoff is sometimes too low
                  # meaning it sometimes allowed values after its zero to be less than the minimum work time
                  # To fix this, I use another modified version of funct() to keep increasing the cutoff until it finally satisfies the minimum work time

                  # Currently, I'm not satisfied with how this code is implimented, and I plan to figure out a better way to do this in the future
                  for n in range(ceil(return_0_cutoff),ceil(x)+1):
                     if funct_round < min_work_time and (not a and b < min_work_time_funct_round or a and (skew_ratio < 1) == (n <= cutoff_to_use_round)):
                        output = min_work_time_funct_round * ceil(n*(a*n+b)/min_work_time_funct_round-0.5+1e-10)
                        if skew_ratio > 1:
                           output += cutoff_transition_value
                        else:
                           output -= cutoff_transition_value
                     else:
                        output = funct_round * ceil(n*(a*n+b)/funct_round-0.5+1e-10)
                     if remainder_mode and output:
                        output += y_fremainder
                     if output >= min_work_time_funct_round:
                        break
                     return_0_cutoff += 1
               
         else:

            # If the graph is linear, then that means it only intersects zero at the origin
            # So, set the return_0_cutoff to 1
            return_0_cutoff = 1
         
# Main function for receiving an output
def funct(n):
      
   # If the start is not at the origin, then translate the graph back to the origin
   n -= red_line_start

   # This part handles not working days
   
   # For demonstration, I will choose the starting date to be the Monday 1st of January and
   # the ending date to be Wednesday 31st of January, and the chosen weekday to be Tuesday
   # The first way I thought of to find the number of any chosen weekday between two dates is to
   # loop through every single day between the start and then end and add one to a 
   # counter variable if that day is one of the chosen weekdays
   # This clearly did not work out because it is extremely inefficient over long periods of time
   
   # I eventually found an efficient method to solve this problem
   # To make explaining this simpler, instead of thinking as the ending date to be Janruary 31,
   # think of it to be the amount of days between the end date and the start date
   # In this case, there are 30 days between Janruary 1 and Janruary 31
   # I know in each 7 consecutive days, or week, of the 30 days, there will always be exactly on tuesday
   # I can take advantage of this property by splitting the 30 days into 7 days at a time like this:
   # 30 days --> 7 days + 7 days + 7 days + 7 days + 2 days
   # I know in each of those 7 days there will be one tuesday
   # And since there are four 7 days, I know there are at least 4 tuesdays between Janruary 1 and Janruary 31
   # Finally, what about the remaining 2 days? What if those days contain a 5th tuesday? That problem is solved
   # with the tuple mods
   # Mods simply goes through the remanding days and determines if there is a tuesday and adds to the counter if there is
   
   # What if I have multiple chosen weekdays, for example tuesday and wednesday?
   # The same logic still works. I know two of 7 consecutive days will always be either tuesday or wednesday
   # If I break the 30 days down again:
   # 30 days --> 7 days + 7 days + 7 days + 7 days + 2 days
   # Instead of one for every 7 days, I know there are two tuesday or wednesdays for every 7 days
   # So, I know there are at least 8 tuesdays or wednesdays between January 1 and January 31
   # This is the purpose of the variable len_nwd, which is basically the amount of chosen weekdays

   # So, why do I need to know the amount of any chosen weekdays between two dates?
   # I needed to develop this algorithm because of how the not working days work
   # The method I chose to implement not working days is as follows
   # First, to make things simpler, let's use the above example
   # The starting date is January 1 and the due date is in 30 days
   # I know there are 10 tuesdays and wednesdays between January 1 and January 31 by using the above algorithm
   # The next step is to remove all the not working days from the 30 days
   # So, instead of 30 days, subtract 10 and get 20 days
   # The reason why this is done is because you are not supposed to do work on the not working days
   # Then, the pset() function defines a and b variables for the parabola that pass through 20 days instead of 30
   # Lastly, the not working days are "added back in"
   # In this example, days 8 and 9 are tuesdays and wednesdays
   # f(6) is the 6th value on the parabola
   # f(7) is the 7th value on the parabola
   # Since day 8 is a tuesday, meaning you won't do any work,
   # f(8) will also be the 7th value on the parabola
   # Since day 9 is a wednesday, meaning you still won't do any work,
   # f(9) will also be the 7th value on the parabola
   # Then f(10) is the 8th value on the parabola and f(11) is the 9th value on the parabola and so on
   # For any f(n), it first subtracts the amount of not working days between
   #the starting date and the starting date plus n days
   # This in a way "adds back in" in the not working days

   # This equation subtracts the amount of not working days between the starting date and the starting date plus n days
   if nwd:
      n -= n//7 * len_nwd + mods[n % 7]

   # If the input is greater than the return_y_cutoff, defined in the pset() function, then return y
   if n > return_y_cutoff:
      return y
   elif n < return_0_cutoff:
      return start_lw

   # This section handles minimum work time
   # The goal of minimum work time is to make sure you never work less than the minimum work time
   # However, if that day is not a working day, then you can work 0 and do nothing
   # The main challenge with this is that you need to know the previous function output in order to make sure you work
   # at least minimum work time units each working day
   # Originally, I tried to make a list of every single function output from the start to the end of the assignment
   # Then, I would loop through the list and modify each function output such that they are either at least minimum
   # work time distance away or at zero (which means that day isn't a working day)
   # This obviously made some problems because not only was it extremely inefficient but it took so much memory that
   # longer assignments could overflow and corrupt the memory
   # As a note, I cannot do something like this: f(x)[defined earlier in the function] - f(x - 1) < minimum work time
   # This is because f(x - 1) would create an infinitely recurring loop calling the same line back again
   
   # On my second attempt, I thought of utilizing rounding
   # Rounding doesn't require knowing the previous function output, which solves the recursion problem
   # Rounding works when the slope of the graph is low, meaning you would work once every couple days
   # However, rounding does not work when there is a higher slope.
   # For example, if I were rounding to the nearest 10, It might accidentally round to 20, which makes no sense to a
   # user considering the only thing inputted was the minimum work time to be 10
   # I then thought of finding a cutoff to begin to use rounding on a parabola
   # The logic with the cutoff is to only use rounding when there is a low slope and then run the function normally
   # once the rate of change is greater than the minimum work time
   # When the rate of change of a parabola is greater than the minimum work time, by definition you will work at least2
   # the minimum work time amount of units
   # If I make a tangent line with a certain slope to the parabola, I can find the point on the parabola where the rate
   # of change is that certain slope
   # If I set that slope to be the minimum work time, I can find this cutoff
   # So I used some basic calculus to calculate the cutoff and applied it to implement to minimum work time
   if funct_round < min_work_time and (not a and b < min_work_time_funct_round or a and (skew_ratio < 1) == (n <= cutoff_to_use_round)):
      
      # If the input number is before the cutoff, round it to the minimum work time
                                                   
      # n*(a*n+b) simplifies to an^2 + bn, which is a quadratic function for returning the output
      # Then, it is rounded to the nearest multiple of funct_round that is greater than the minimum work time

      output = min_work_time_funct_round * ceil(n*(a*n+b)/min_work_time_funct_round-0.5+1e-10)
      if skew_ratio > 1:
         output += cutoff_transition_value
      else:
         output -= cutoff_transition_value
            
   else:
      
      # If input number is after the cutoff, the slope is high enough to satisfy the minimum work time
      # So, round it to the grouping value
      output = funct_round * ceil(n*(a*n+b)/funct_round-0.5+1e-10)
            
   if add and n == ceil(return_y_cutoff - 1):
      output += add
                                                      
   # This part handles the remainder
   # Pretend the amount of units in the assignment is 23, or y, and the grouping value is 5
   # This looks impossible to do with the grouping value because 23 is not divisible by 5
   # How this is solved is by adding the remainder that isn't divisible by 5, which is 3, to the last working day
   # For example, this would look like: f(0) = 0, f(1) = 5, f(2) = 10, f(3) = 15, and f(4) = 23
   # If we look at the differences between the function outputs, we see f(4)-f(3) = 8, f(3)-f(2) = 5, f(2)-f(1) = 5,
   # and f(1)-f(0) = 5
   # There is a difference of 8 even though the grouping value is 5
   # This is unavoidable because 23 is not divisible by 5
   # With remainder mode, you get to choose whether you want the difference of 8 to be at the first or the last working day
   # I implemented this by adding the remainder to all the function outputs
   # If I add 3 to all outputs, it would look like: f(0) = 0, f(1) = 8, f(2) = 13, f(3) = 18, and f(4) = 23
   # Note: don't add 3 to f(0), because the remainder is added to the next working day. Since f(0) is not a working day don't add 3 to it
   if remainder_mode and output:
      output += y_fremainder
            
   # Returns the final output
   return output + start_lw

if debug_mode:
   def rfunct(n):
      n -= red_line_start
      if nwd:
         n -= n//7 * len_nwd + mods[n % 7]
      if ignore_ends_mwt:
         y1 = y - start_lw     
      else:
         y1 = y - start_lw - y_mremainder
      if a and n > (-b + (b*b + 4*a*y1)**0.5)/a/2 or not a and b and n > y/b:
         return y
      if skew_ratio > 1 or not a or a * b > 0:
         funct_zero = 0
      else:
         funct_zero = -b/a
      if a and n < funct_zero:
         return start_lw
      return n*(a*n+b) + start_lw
# Function to get the modulo days when using not working days (explained above)
def set_mod_days():
   global mods
   xday = assign_day_of_week + red_line_start
   mods = [0]
   mod_counter = 0
   for mod_day in range(6):

      # Adds one to the counter if the day is a not working day
      if (xday + mod_day) % 7 in nwd:
            mod_counter += 1
      mods.append(mod_counter)
   mods = tuple(mods)

# Calculates the skew_ratio limit
# The skew ratio limit is the skew ratio when the first function output reaches y
def calc_skew_ratio_lim():
   global skew_ratio_lim
   skew_ratio_lim = x - red_line_start
   if nwd:
      skew_ratio_lim -= skew_ratio_lim//7 * len_nwd + mods[skew_ratio_lim % 7]
   if y - start_lw == y_mremainder:
      skew_ratio_lim = ceil(skew_ratio_lim*10)/10
   else:
      skew_ratio_lim = ceil((y-start_lw)*skew_ratio_lim/(y - start_lw - y_mremainder)*10)/10
     
# Formats Seconds into time
def format_minutes(total_minutes):
   hour = str(int(total_minutes / 60))
   minute = ceil(total_minutes % 60)
   if hour == '0':
      form = f'{minute}m'
      if total_minutes and total_minutes < 1:
         return '<1m'
   elif not minute:
      form = hour + 'h'
   else:
      form = f'{hour}h {minute}m'
   return form

# Formats not working days
def format_not_working_days(format_default=True):
   if format_default:
      nwd2 = def_nwd
   else:
      nwd2 = nwd
   len_nwd = len(nwd2)
   if not len_nwd:
      return 'None'
   elif len_nwd == 1:
      return (date(1,1,1) + time(nwd2[0])).strftime('%A')
   elif len_nwd == 2:
      return (date(1,1,1) + time(nwd2[0])).strftime('%A') + ' and ' + (date(1,1,1) + time(nwd2[1])).strftime('%A')
   elif len_nwd > 2:
      return ', '.join((date(1,1,1) + time(nwd_day)).strftime('%A') for nwd_day in nwd2[:len_nwd - 1]) + ', and ' + (date(1,1,1) + time(nwd2[len_nwd - 1])).strftime('%A')

# Converts dates like "4/30/20" to datetime objects
def slashed_date_convert(slashed_date,next_year=True,spos=-1):
   slashes = []
   while 1:
      try:
         spos = slashed_date.index('/',spos + 1)
         slashes.append(spos)
      except:
         try:
            month = slashed_date[:slashes[0]]
            month = int(month,10)
         except:
            month = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'june':6,'jul':7,'july':7,'aug':8,'sep':9,'sept':9,'oct':10,'nov':11,'dec':12}[month.lower()]
         try:
            day = int(slashed_date[slashes[0]+1:slashes[1]],10)
            if len(slashed_date[slashes[1]+1:]) in (1, 2):
               year = int(str(date_now.year)[:4-len(slashed_date[slashes[1]+1:])]+str(slashed_date[slashes[1]+1:]),10)
            else:
               year = int(slashed_date[slashes[1]+1:],10)
         except:
            day = int(slashed_date[slashes[0]+1:],10)
            year = date_now.year
            if next_year and date(date_now.year,month,day) <= date_now:
               year += 1
         if next_year and date(year,month,day) <= date_now:
            raise Exception
         return date(year,month,day)

# Gets width of text for formating
def gw(font,text):
   return font.render(text,1,black).get_width()

# Centers text on the graph
def center(text,y_pos):
   screen.blit(font.render(text,1,black),((width+45-gw(font,text))/2,y_pos))

# Function that draws graph
def draw(doing_animation=0,do_return=1):

      # Important Scaling Variables
      # When given a coordinate point, for example (6,8), multiply the x value by wCon and the y value by hCon
      # This puts the coordinate in "graph terms," where it can be plotted to its respective coordinates on the actual graph window
      # Similarly, dividing the "graph terms" coordinates by wCon and hCon yield the original "coordinate terms" of (6,8)
      global hCon, wCon
      wCon = (width-55)/x
      hCon = (height-55)/y
   
      # Used to manually set the start of the red line and the skew ratio of the graph
      if set_start or draw_point:
         global red_line_start, start_lw, last_mouse_x2, y_fremainder, y_mremainder

         # Gets the position of the mouse
         mouse_x, mouse_y = pygame.mouse.get_pos()

         # Unconverts the x mouse position from graph terms into coordinate terms
         mouse_x = (mouse_x-49.5)/wCon
         if set_start:

            # If the start of the red line is being set, then run this code

            # Rounds the coordinate terms to the nearest whole number
            mouse_x_set_start = ceil(mouse_x-0.5)

            # Caps the start at its lower and upper limits
            if mouse_x_set_start < dif_assign:
               mouse_x_set_start = dif_assign
            elif mouse_x_set_start > wlen + dif_assign:
               mouse_x_set_start = wlen + dif_assign
            mouse_x2 = mouse_x_set_start

            # If the new just calculate mouse_x_set_start is the same as it was last calculation, return out of the function
            # This is because there is no point using excess CPU if the graph is exactly the same as last calculation
            if do_return and mouse_x_set_start == red_line_start:## and mouse_x2 < dif_assign + 1 and mouse_x2 > wlen + dif_assign - 1:
               return

            # Sets the start
            red_line_start = mouse_x_set_start
            start_lw = works[mouse_x_set_start - dif_assign]
            y_fremainder = (y - start_lw) % funct_round
            y_mremainder = (y - start_lw) % min_work_time_funct_round
            if nwd:
               set_mod_days()
            calc_skew_ratio_lim()
         elif draw_point:

            # If the skew ratio of the graph is being manually set, then run this code

            # Unconverts the y mouse position from graph terms into coordinate terms
            mouse_y = (height-mouse_y-50.5)/hCon - start_lw
            mouse_x -= red_line_start
                     
            # Sets the displayed point to the rounded value of the x position
            mouse_x2 = ceil(mouse_x-0.5)

            # Caps point X at its lower and upper limits
            if mouse_x2 < 0:
               mouse_x2 = 0
            elif mouse_x2 > x - red_line_start:
               mouse_x2 = x - red_line_start

            # If the new displayed point is the same as it was last calculation, return out of the function
            # This is because there is no point using excess CPU if the graph doesn't change
            if do_return and not (set_skew_ratio or set_start) and last_mouse_x2 == mouse_x2:
               if nwd:
                  pset()
               return
            last_mouse_x2 = mouse_x2
            mouse_x2 += red_line_start

      # Initializes the parabola
      old_parabola_values = (a,b)
      pset()
      # Returns if the parabola values are the same
      if do_return and set_skew_ratio and not draw_point and (a,b) == old_parabola_values:
         return
      
      # Determines circle radius
      circle_r = ceil(2*wCon - 0.5)
      if circle_r > 5:
         circle_r = 5
      elif circle_r < 3:
         circle_r = 3
      if circle_r == 3:
         blwidth = circle_r - 1
      else:
         blwidth = circle_r - 2
      
      # Resets the screen
      screen.fill(white)

      # Sets up graph
      pygame.draw.line(screen,gray4,(44,0),(44,height),10)
      pygame.draw.line(screen,gray4,(0,height-46),(width,height-46),10)
      screen.blit(font3.render('0',1,black),(51,height-39))
      screen.blit(font3.render('0',1,black),(30,height-66))
      screen.blit(font3.render('Days',1,black),((width+11)/2,height-19))
      screen.blit(pygame.transform.rotate(font3.render(f'{unit}s ({format_minutes(ctime)} per {unit})',1,black),270),(-2,(height-50-gw(font3,f'{unit}s ({format_minutes(ctime)} per {unit})'))/2))
         
      # Loops through and makes smaller indexes

      # This entire section finds the index steps for the x and y axes and plots them
      # The below line is the most important one
      # This determines the index step for the bigger x axis
      # Let's break it down

      # 10**int(log10(x)) is the magnitude of x
      # For example, if x was 45387, 10**int(log10(x)) would be 10000
      # I made it so that it always steps in powers of 10
      
      # ceil(int(str(x)[0])/ceil((width-100)/100)) makes the step obey the max number of x indexes
      # For example, if x was 99999, then the steps would be: 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, and 90000
      # This may be too many steps for a user
      # ceil((width-100)/100) is a simple formula that determines an approximate maximum number of x indexes
      # the expression basically compares the total number of steps with the maximum and adjusts the step value
      # In the above case, say that the maximum number of index steps is 7
      # If x was 99999, the equation would realize there are too many indexes and instead multiply the step by 2, so the new step value is 20000
      # then the steps would be: 20000, 40000, 60000, and 80000, obeying the maximum number of indexes
      x_axis_scale = 10**int(log10(x)) * ceil(int(str(x)[0],10)/ceil((width-100)/100))

      # Calculates smaller steps
      if x >= 10:
         small_x_axis_scale = x_axis_scale / 5

         # Draws smaller x indexes
         for smaller_index in range(1,int(x/small_x_axis_scale + 1)):

            # Doesn't plot the smaller index line if it will be covered up by the bigger index line
            if smaller_index % 5:
               displayed_number = smaller_index*small_x_axis_scale
               if not displayed_number % 1:
                  displayed_number = ceil(displayed_number)

               # Draws smaller index line
               pygame.draw.line(screen,gray1,(displayed_number*wCon+49.5,0),(displayed_number*wCon+49.5,height-49.5),2)

               # If there is enough space to label the smaller indexes, then label it on the graph
               if gw(font4,str(int(x))) * 1.75 < small_x_axis_scale*wCon:
                  numberwidth = gw(font4,str(displayed_number))

                  # Subtracts half the width of the number
                  number_x_pos = displayed_number*wCon+50-numberwidth/2

                  # If the number goes off the screen, adjust it to fit on the screen
                  if number_x_pos + numberwidth > width-1:
                     number_x_pos = width-numberwidth-1

                  # Draws the number
                  screen.blit(font4.render(str(displayed_number),1,black),(number_x_pos,height-40))

      # This part is exactly the same as the above code, but except in the y axis instead of the x axis       
      y_axis_scale = 10**int(log10(y)) * ceil(int(str(y)[0],10)/ceil((height-100)/100))
      if y >= 10:
         small_y_axis_scale = y_axis_scale / 5
         font_size = ceil(27.5-(len(str(ceil(y - y % y_axis_scale))))*2.5)
         if font_size < 19:
            font_size = 19
         font5 = pygame.font.SysFont(font_type,font_size-4)
         for smaller_index in range(1,int(y/small_y_axis_scale + 1)):
            if smaller_index % 5:
               displayed_number = smaller_index*small_y_axis_scale
               if not displayed_number % 1:
                  displayed_number = ceil(displayed_number)
               pygame.draw.line(screen,gray1,(50,height-50.5-smaller_index*hCon*small_y_axis_scale),(width,height-50.5-smaller_index*hCon*small_y_axis_scale),2)
               if font5.render('0',1,black).get_height()*1.4 < small_y_axis_scale*hCon:
                  number_y_pos = height-displayed_number*hCon-49-gw(font5,'0')
                  if number_y_pos < 1:
                     number_y_pos = 1
                  number_x_pos = 39-gw(font5,str(displayed_number))
                  if number_x_pos < 1:
                     number_x_pos = 1
                  screen.blit(font5.render(str(displayed_number),1,black),(number_x_pos,number_y_pos))

      # Loops through and makes bigger indexes along the x axis
      for bigger_index in range(ceil(x - x % x_axis_scale),0,-x_axis_scale):

            # Uses the gw(), or get width function, that was defined earlier
            numberwidth = gw(font3,str(bigger_index))

            # Subtracts half the width of the number from 
            number_x_pos = bigger_index*wCon+50-numberwidth/2

            # If the number goes off the screen, adjust it to fit on the screen
            if number_x_pos + numberwidth > width-1:
               number_x_pos = width-numberwidth-1

            # Draws the line
            pygame.draw.line(screen,gray2,(bigger_index*wCon+50.5,0),(bigger_index*wCon+50.5,height-49.5),5)

            # Draws the number
            screen.blit(font3.render(str(bigger_index),1,black),(number_x_pos,height-40))

      # Loops through and makes bigger indexes along the y axis
      for bigger_index in range(ceil(y - y % y_axis_scale),0,-y_axis_scale):

            # Bugchecks for rounding error
            # The *2 makes sure it doesn't accidentally break out of the loop on a valid y index
            # Dont worry about it for now
            if bigger_index * 2 < y_axis_scale:
               break

            # Determines the font
            font_size = ceil(28.5-(len(str(bigger_index)))*2.5)
            if font_size < 15:
               font_size = 15
            font2 = pygame.font.SysFont(font_type,font_size)
            number_y_pos = height-bigger_index*hCon-49-gw(font2,'0')

            # Adjusts the number_y_pos if the number goes off screen
            if number_y_pos < 1:
               number_y_pos = 1

            number_x_pos = 39-gw(font2,str(bigger_index))
            if number_x_pos < 1:
               number_x_pos = 1

            # Draws the vertical line
            pygame.draw.line(screen,gray2,(50,height-49.5-bigger_index*hCon),(width,height-49.5-bigger_index*hCon),5)

            # Draws the index
            screen.blit(font2.render(str(bigger_index),1,black),(number_x_pos,number_y_pos))

      # Displays today's line
      today_x = xdif*wCon+47.5
      if xdif > -1:
         pygame.draw.line(screen,gray3,(today_x+2.5,0),(today_x+2.5,height-50),5)
         screen.blit(pygame.transform.rotate(font3.render('Today Line',1,black),270),(today_x-6,(height-50-gw(font3,'Today Line'))/2))
      if debug_mode:
         pygame.draw.line(screen,gray3,((return_0_cutoff+red_line_start)*wCon+47.5+2.5,0),((return_0_cutoff+red_line_start)*wCon+47.5+2.5,height-50),5)
         screen.blit(pygame.transform.rotate(font3.render('Return 0 Cutoff',1,black),270),((return_0_cutoff+red_line_start)*wCon+47.5-6,(height-50-gw(font3,'Today Line'))/2))
         try:
            pygame.draw.line(screen,gray3,((cutoff_to_use_round+red_line_start)*wCon+47.5+2.5,0),((cutoff_to_use_round+red_line_start)*wCon+47.5+2.5,height-50),5)
            screen.blit(pygame.transform.rotate(font3.render('Cutoff to Use Round',1,black),270),((cutoff_to_use_round+red_line_start)*wCon+47.5-6,(height-50-gw(font3,'Cutoff to Use Round'))/2))
         except:pass
         pygame.draw.line(screen,gray3,((return_y_cutoff+red_line_start)*wCon+47.5+2.5,0),((return_y_cutoff+red_line_start)*wCon+47.5+2.5,height-50),5)
         screen.blit(pygame.transform.rotate(font3.render('Return Y Cutoff',1,black),270),((return_y_cutoff+red_line_start)*wCon+47.5-6,(height-50-gw(font3,'Return Y Cutoff'))/2))

      # Displays the start if manual set start is enabled
      if set_start:
         mouse_x_set_start = mouse_x_set_start*wCon + 50
         pygame.draw.line(screen,gray5,(mouse_x_set_start,0),(mouse_x_set_start,height-50),5)
         screen.blit(pygame.transform.rotate(font3.render('Click to Set',1,black),270),(mouse_x_set_start-8,(height-50-gw(font3,'Click to Set'))/2))
      
      # Red line
      # Loops through all the days and plots its corresponding function output
      # At first, I would loop through every value and plot each function output
      # However, I noticed some inefficiencies
      # Going through the days, the loop will connect a line between f(0) and f(1)
      # Then, it will connect f(1) and f(2)
      # But wait, f(1) was calculated twice, which is an inefficiency
      # To solve this, I store f(1) into a variable while the code is connecting a line between f(0) and f(1)
      # That way, each function output is only calculated once
      circle_x, circle_y = ceil(red_line_start*wCon+49.5), ceil(height-start_lw*hCon-50.5)
      rcircle_y = circle_y
      pygame.draw.circle(screen,red,(circle_x,circle_y),circle_r)
      line_end = int(x+ceil(1/wCon))
      if debug_mode:
         end = False
         for i in range(red_line_start+1,line_end,ceil(1/wCon)):
            
            prev_circle_x = circle_x
            prev_circle_y = circle_y
            prev_rcircle_y = rcircle_y
            circle_x = ceil(i*wCon+49.5)
            if circle_x >= width-5:
               pygame.draw.line(screen,green,(prev_circle_x,prev_rcircle_y),(width-5,ceil(height-rfunct(i)*hCon-50.5)),circle_r-2)
               pygame.draw.circle(screen,green,(width-5,ceil(height-rfunct(i)*hCon-50.5)),circle_r)
               pygame.draw.line(screen,red,(prev_circle_x,prev_circle_y),(width-5,5),circle_r)
               pygame.draw.circle(screen,red,(width-5,5),circle_r)
               break
            circle_y = ceil(height-funct(i)*hCon-50.5)
            rcircle_y = ceil(height-rfunct(i)*hCon-50.5)

            # Doesn't draw green line if it is covered by the red line (same position)
            if circle_y < rcircle_y - 3 or circle_y > rcircle_y + 3:
               pygame.draw.line(screen,green,(prev_circle_x,prev_rcircle_y),(circle_x,rcircle_y),circle_r-2)
               pygame.draw.circle(screen,green,(circle_x,rcircle_y),circle_r)
               end = True
            elif end:
               end = False
               pygame.draw.line(screen,green,(prev_circle_x,prev_rcircle_y),(circle_x,rcircle_y),circle_r-2)

            pygame.draw.line(screen,red,(prev_circle_x,prev_circle_y),(circle_x,circle_y),circle_r)
            pygame.draw.circle(screen,red,(circle_x,circle_y),circle_r)
      else:
         for i in range(red_line_start+1,line_end,ceil(1/wCon)):
            prev_circle_x = circle_x
            prev_circle_y = circle_y
            circle_x = ceil(i*wCon+49.5)
            circle_y = ceil(height-funct(i)*hCon-50.5)
            
            pygame.draw.line(screen,red,(prev_circle_x,prev_circle_y),(circle_x,circle_y),circle_r)
            pygame.draw.circle(screen,red,(circle_x,circle_y),circle_r)
            if circle_x >= width-5:
               break
   
      # Blue line
      # This plots the user inputs
      # This uses the same logic as the red line
      circle_x, circle_y = ceil(dif_assign*wCon+49.5), ceil(height-adone*hCon-50.5)
      pygame.draw.circle(screen,blue,(circle_x,circle_y),circle_r-1)
      if wlen + 1 < line_end:
         line_end = wlen + 1
      for i in range(1,line_end,ceil(1/wCon)):
   
         prev_circle_x = circle_x
         prev_circle_y = circle_y
         circle_x = ceil((i+dif_assign)*wCon+49.5)
         circle_y = ceil(height-works[i]*hCon-50.5)
         pygame.draw.line(screen,blue,(prev_circle_x,prev_circle_y),((circle_x,circle_y)),blwidth)
         pygame.draw.circle(screen,blue,(circle_x,circle_y),circle_r-1)
         if circle_x >= width-5:
            break

      # Draws the point closest to the parabola from the mouse
      if draw_point and not doing_animation:
         pygame.draw.circle(screen,green,(ceil(wCon*mouse_x2 + 49.5),ceil(height-funct(mouse_x2)*hCon-50.5)),circle_r)
         funct_mouse_x2 = round(funct(mouse_x2),str(float(funct_round))[::-1].find("."))
         if mouse_x2 > left_adjust_cutoff:
            left_adjust = gw(font3,f'(Day:{mouse_x2},{unit}:{funct_mouse_x2})')
         else:
            left_adjust = 0
         if funct_mouse_x2 < up_adjust_cutoff:
            up_adjust = font3.render(f'(Day:{mouse_x2},{unit}:{funct_mouse_x2})',1,black).get_height()
         else:
            up_adjust = 0
         screen.blit(font3.render(f'(Day:{mouse_x2},{unit}:{funct_mouse_x2})',1,black),(wCon*mouse_x2 + 50 - left_adjust,height-funct_mouse_x2*hCon-50 - up_adjust))
            
      # Handles moving the progress bar left if the Goal Line does not fit inside the screen
      if show_progress_bar:
         move_text_down = 0
         should_be_done_x = width-153+funct(xdif+1)/y*145
         bar_move_left = should_be_done_x - width + 17
         if bar_move_left < 0 or x <= xdif or (not doing_animation and lw >= selected_assignment[3]):
            bar_move_left = 0
         elif should_be_done_x > width - 8:
            bar_move_left = 8
         pygame.draw.line(screen,border,(width-155-bar_move_left,height-96),(width-7-bar_move_left,height-96),50)
         pygame.draw.line(screen,green,(width-153-bar_move_left,height-96),(width-9-bar_move_left,height-96),46)
         slash_x = width - 145 - bar_move_left + slash_x_counter % 35
         pygame.draw.line(screen,dark_green,(slash_x,height-118),(slash_x+45,height-73),15)
         pygame.draw.line(screen,dark_green,(slash_x+35,height-118),(slash_x+80,height-73),15)
         if slash_x + 132 + bar_move_left <= width:
            pygame.draw.line(screen,dark_green,(slash_x+70,height-118),(slash_x+115,height-73),15)
         if x > xdif and (doing_animation or lw < selected_assignment[3]):
            screen.blit(font3.render(f'Your Progress: {int(lw/y*100)}%', 1, black),(width-gw(font3,f'Your Progress: {int(lw/y*100)}%')-5,height-68))
            done_x = width-153+lw/y*145-bar_move_left
            if done_x < width - 8:
               pygame.draw.line(screen,white,(done_x,height-96),(width-9-bar_move_left,height-96),46)
            if should_be_done_x > width - 17:
               should_be_done_x = width - 17
            pygame.draw.line(screen,border,(should_be_done_x,height-119),(should_be_done_x,height-73),2)
            screen.blit(pygame.transform.rotate(font3.render('Goal',1,black),270),(should_be_done_x,height-113.5))
         else:
            screen.blit(font3.render('Completed!', 1, black),(width-80-gw(font3,'Completed!')/2 - bar_move_left,height-68))
      else:
         move_text_down = 70

      # Formats the graph
      rounded_skew_ratio = ceil(skew_ratio*1000-1000.5)/1000
      if not rounded_skew_ratio % 1:
         rounded_skew_ratio = ceil(rounded_skew_ratio)
      if rounded_skew_ratio:
         disttype = 'Parabolic'
      else:
         disttype = 'Linear'
      if fixed_mode:
         mode = 'Fixed Mode'
      else:
         mode = 'Dynamic Mode'
      if ((selected_assignment[3] - start_lw) / funct_round) % 1:
         if remainder_mode:
            strremainder = 'First'
         else:
            strremainder = 'Last'
         screen.blit(font3.render(f'Remainder: {strremainder}',1,black),(width-gw(font3,f'Remainder: {strremainder}')-1,height-155+move_text_down))
         screen.blit(font3.render(mode,1,black),(width-gw(font3,mode)-1,height-172+move_text_down))
         if total_mode:
            screen.blit(font3.render('Total Mode',1,black),(width-gw(font3,'Total Mode')-1,height-189+move_text_down))
      else:
         screen.blit(font3.render(mode,1,black),(width-gw(font3,mode)-1,height-155+move_text_down))
         if total_mode:
            screen.blit(font3.render('Total Mode',1,black),(width-gw(font3,'Total Mode')-1,height-172+move_text_down))
      screen.blit(font3.render(f'Skew Ratio: {rounded_skew_ratio} ({disttype})', 1, black),(width-gw(font3,f'Skew Ratio: {rounded_skew_ratio} ({disttype})')-1,height-138+move_text_down))
      center('Assignment name: '+file_sel,0)
         
      # Skips formatting text if in animation
      if doing_animation:
         pygame.display.update()
         return

      # Formats and sets up the Central text on the graph that displays the daily information
      row_height = gw(font,'0')*2+1
      dayleft = x - xdif
      if dayleft in (-1,0,1):
         if dayleft == -1:
            strdayleft = 'Yesterday'
         elif not dayleft:
            strdayleft = 'TODAY!!!'
         elif dayleft == 1:
            strdayleft = 'TOMORROW!!!'
      elif dayleft < -1:
         strdayleft = f'Was Due {-dayleft} Days Ago'
      else:
         strdayleft = f'Due in {dayleft} Days'
      center('Due Date: '+str(due_date.strftime(f'%B %-d, %Y (%A) ({strdayleft})')),row_height)
      if lw < y and dayleft > 0:
         nowork = (date_file_created.weekday() + day) % 7 in nwd
         todo = funct(day+dif_assign+1) - lw
         if todo <= 0 or nowork:
            todo = 0
            reach_deadline = ' (Deadline Reached!)'
         else:
            center('Estimated completion time: '+format_minutes(todo*ctime),row_height*7)
            reach_deadline = ''
         current_day = date_file_created+time(day)
         dist_from_today = ndif - day
         display_date = current_day.strftime('%B %-d, %Y (%A)')
         if not dist_from_today:
            display_date += ' (Today)'
         elif dist_from_today == -1:
            display_date += ' (Tomorrow)'
         elif dist_from_today == 1:
            display_date += ' (Yesterday)'
         display_date += ':'
         center(display_date,row_height*3)
         center(f'{unit}s already completed: {lw}/{stry}',row_height*5)
         center(f'{unit}s to complete: %g' % todo,row_height*4)
         center('Total %s deadline for this day: %g' % (unit, todo+lw) + reach_deadline,row_height*6)
         if after_midnight:
            center('It is currently past Midnight! You need to get sleep!',row_height*14)
         elif after_midnight == '':
            center('Welcome to the Graph!',row_height*12)
            center('Please read the Instructions displayed on the Idle',row_height*13)
            center('Click on the Graph and Press the Return Key to enter your first Work Input',row_height*14)
         if xdif < 0:
            center('This Assignment has Not Yet been Assigned!',row_height*11)
         elif dist_from_today > 0:
            center('You have not Entered in your Work from Previous Days!',row_height*11)
            center('Please Enter in your Progress to Continue',row_height*12)
         else:
            date_now = date.now() 
            if nowork or current_day > date(date_now.year,date_now.month,date_now.day):
               center('You have Completed your Work for Today!',row_height*9)
            else:
               try:
                  llw = works[-2]
                  if not (ndif == wlen - 1 and fixed_mode) and (lw - llw) / warning_acceptance < funct(wlen+dif_assign) - llw:
                     center('!!! ALERT !!!',row_height*11)
                     center('You Are BEHIND Schedule!',row_height*12)
               except:
                  pass
      else:
         center('Amazing Effort! You have Finished this Assignment!',row_height*10)

      # Updates the screen
      pygame.display.update()

def quit_program(internal_error=False):
   if not debug_mode:
      pygame.quit()
   global file_directory, date_last_closed
   # Prints error info
   from traceback import format_exc # Prints the Exception if an Error Occurs
   error_info = format_exc().replace('\n\n','\n')
   if internal_error and error_info.split('\n')[-2] != 'KeyboardInterrupt':
      #print(f'\n\n\n\nCOPY ALL INFORMATION STARTING FROM HERE\n\n\n{dat}\n\n{error_info}\n\nAND ENDING AT HERE\n\n\nIt seems like there was an Internal Error somewhere in the code... :/\nPlease copy all of the Data Above and send it to me on G-mail at arhan.ch@gmail.com so I can fix the Error\nThank you')
      print(f'\n\n\n\nCOPY ALL INFORMATION STARTING FROM HERE\n\n\n{dat}\n\n{error_info}\n\nAND ENDING AT HERE\n\n\nSo uhhmmmmmmm... :/\nThere was a bug somewhere in code sorry lol\nshow this message and the info above to me on insta and i promise to buy you mcdonalds')
   else:
      # If the files have already been created, then update the backups by comparing the last opened date to today
      if update_backups:
         date_now = date.now()
         date_now = date(date_now.year,date_now.month,date_now.day,date_now.hour,date_now.minute)
         dat[0][0] = date_now
         save_data()
         if last_opened_backup or hourly_backup or daily_backup or weekly_backup or monthly_backup:
            print('\nUpdating Backups... Go to the Settings to Enable/Disable Different types of Backups\n')
            if last_opened_backup:
               file_directory += ' Every Run Backup'
               save_data()
               print('EVERY RUN BACKUP UPDATED')
            if hourly_backup and (date_last_closed.year,date_last_closed.month,date_last_closed.day,date_last_closed.hour) != (date_now.year,date_now.month,date_now.day,date_now.hour):
               file_directory = original_file_directory + ' Hourly Backup'
               save_data()
               print('HOURLY BACKUP UPDATED')
            if daily_backup and (date_last_closed.year,date_last_closed.month,date_last_closed.day) != (date_now.year,date_now.month,date_now.day):
               file_directory = original_file_directory + ' Daily Backup'
               save_data()
               print('DAILY BACKUP UPDATED')
            if weekly_backup and date(date_last_closed.year,date_last_closed.month,date_last_closed.day) - time(date_last_closed.weekday()) != date(date_now.year,date_now.month,date_now.day) - time(date_now.weekday()):
               file_directory = original_file_directory + ' Weekly Backup'
               save_data()
               print('WEEKLY BACKUP UPDATED')
            if monthly_backup and (date_last_closed.month,date_last_closed.year) != (date_now.month,date_now.year):
               file_directory = original_file_directory + ' Monthly Backup'
               save_data()
               print('MONTHLY BACKUP UPDATED')
            if debug_mode:
               file_directory = original_file_directory
      print('Quitting... Thanks for using!')
   if debug_mode:
      raise Exception
   else:
      from os import _exit
      _exit(0)
      
try:
    
    # Runs the Assignment Page
    draw_point = False
    home()
    last_mouse_x2 = -1
    first_loop = True
    if display_instructions:
       print('''

Welcome to the Graph!
You are about to read how to use this tool
(Don\'t worry it won\'t take that long to read)

Please note that the graph is not perfect, and you may have to adjust the Skew Ratio of the graph when it is linear to fit your desired schedule
----------------------------------
This graph provides a visualization of how your assignment schedule will look like in days over units of work
The Red Line is the schedule you will be guided to follow during the duration of the assignment
The Blue Line will be the work you actually finish that you will have to input every day
This line is not visible yet because you have not entered any work inputs so far
To do so, press return and enter in how much work you have finished for the day
Entering nothing will always break out of an input anywhere in the program

IMPORTANT NOTE:
You will be unable to interact with the graph if you are entering in an input due to how Pygame works
Make sure you enter in the inputs before trying to use the graph

If you complete less work than the amount you are supposed to complete for a day,
The assignment will be marked as in progress and you will have to make up the remainder of the work later in that day
Exception: entering in 0 will change the day to the next day regardless whether or not you have completed your work for that day

FIXED MODE (enabled by default)
-------------------------------
THIS MODE CAN BE TOGGLED BY CLICKING THE GRAPH AND PRESSING KEY "F" ON YOUR KEYBOARD
In this mode, if you fail to complete the specified amount of work for one day, you will have to make it up on the next day
This mode is recommended for self-discipline and if the assignment is extremely important

DYNAMIC MODE (disabled by default)
----------------------------------
THIS MODE CAN BE TOGGLED BY CLICKING THE GRAPH AND PRESSING KEY "F" ON YOUR KEYBOARD
If you fail to complete the specified amount of work for one day, the graph will change itself to start at your last work input, adapting to your work schedule
The graph will only change is you complete less than the amount of work specified
The graph does not change if you complete more than or equal to the amount of work specified
Use this if you cannot keep up with an assignment's work schedule
It is easy to fall behind with dynamic mode, so be careful while using this mode

TOTAL MODE (disabled by default)
--------------------------------
With this mode, you must enter the total units of work done instead of much done since the last input
This is useful for assignments with a total number count of how much you have done, such as a book with page numbers

REMAINDER FIRST/LAST
--------------------
This only applies if the total units of work is not divisible by the grouping value
If you don\'t see a "Remainder: Last" on your graph, there is no remainder, and it is irrelevant for this assignment

If you do see a "Remainder: Last" on your graph, then the total units of work is not divisible by the grouping value that you entered
Switching between "Remainder: First" and "Remainder: Last" allows you to choose whether you would like to do the remainder of work
on the first working day or the last working day of the assignment

KEYBINDS
--------
IMPORTANT NOTE: You HAVE to click on before pressing the desired key in order for it to be registered
Click on the graph a second time to enable/disable displaying the value of the closest point to the mouse (not 100% accurate)
"f" to toggle dynamic mode/fixed mode
"d" to get the entire schedule of an assignment
"s" to manually set the skew ratio of the red line using the graph
"c" to manually set the start of the red line using the graph
"m" to manually set the skew ratio and the start of the red line by typing in its value
"t" to toggle total mode
"r" to toggle "remainder: first/last"
"a" to return to the assignment page
"n" to automatically go to the next assignment
Press Return to enter a work input
Backspace to delete a work input
Up/down arrow keys to control the skew ratio

KEYBINDS WHEN ENTERING WORK INPUTS
----------------------------------
"fin" to enter the exact amount required to do
"none" to enter no work done. Using "none" works with while total mode is both enabled and disabled, while instead typing in "0" does not work with total mode


IMPORTANT NOTE: The setting "Ignore Min Work Time Ends" is enabled by default in the settings
If you entered in an assignment with a minimum work time, this will cause the first and last working days of the assignment to not follow the minimum work time
This is explained more in the settings, which can be accessed at the assignment page

Once you have finished reading this and using the graph, press "a" to return to the home assignment page
Type in "settings" to customize your settings


That's all, and have a nice day

(Go to the top ^)
Make sure you read the instructions, as some things are important''')
   
    while 1:

        # Waits for you to do an event, such as a mouse movement or a key press
        # This is more efficient than checking for an event 100 times per second
        event = pygame.event.wait()
        etype = event.type
        
        # Handles manually setting the start of the red line and the skew ratio of the graph
        # These make the mouse interactive
        if set_start or set_skew_ratio or draw_point:

           # Draws every time mouse is moved
           # 4 is detecting mouse movements
           if etype == 4:
              draw()

           # When mouse is pressed, the interactive mouse stops
           # 5 is detecting a mouse click
           elif etype == 5:

              # If the mouse point is enabled, disable it
              if draw_point and not (set_start or set_skew_ratio):
                 draw_point = False
                 last_mouse_x2 = -1
                 draw(0,0)
                 continue

              # If the manual set start is enabled set the skew ratio and disable it
              if set_start:
                 set_start = False
                 if fixed_mode:
                    fixed_start = red_line_start
                    selected_assignment[14] = fixed_start
                 else:
                    dynamic_start = red_line_start
                    selected_assignment[11] = dynamic_start

              # If the manual set skew ratio is enabled set the skew ratio and disable it
              else:
                 set_skew_ratio = False
                 selected_assignment[6] = skew_ratio

              # Change day to +-1 if the assignment is in progress after manually setting the skew ratio
              if change_day_mouse:
                 pset()
                 if change_day_upper:
                     day -= lw < funct(wlen+dif_assign)
                 else:
                     day += lw >= funct(wlen+dif_assign)

              # Saves Data
              save_data()
              draw(0,0)
              continue

        # If mouse draw point is disabled, enable it if the user clicks
        # 5 is detecting a mouse click
        if not draw_point and etype == 5:
              draw_point = True
              draw()

        # 2 is detecting a key press
        elif etype == 2:
            key = event.key

            # Goes back to assignment page
            # 97 is the 'a' key
            if key == 97:
               pygame.display.set_mode((1,1))
               home()

            # Initializes manually setting the start of the red line
            # 115 is the 's' key
            elif not set_start and key == 115:
               change_day_mouse = ndif > -1 and ndif == wlen - 1 and lw != works[-2]
               if change_day_mouse:
                  change_day_upper = lw >= funct(wlen+dif_assign)
               set_skew_ratio = True
               draw()
               print('\nManual Set Skew Ratio Enabled\nHover Over the Graph and Click to set the Skew Ratio of the Red Line')

            # Initializes manually setting the skew ratio
            # 99 is the 'c' key
            elif not set_skew_ratio and key == 99:
               change_day_mouse = ndif > -1 and ndif == wlen - 1 and lw != works[-2]
               if change_day_mouse:
                  change_day_upper = lw >= funct(wlen+dif_assign)
               set_start = True
               draw(0,0)
               pygame.event.pump()
               print('\nManual Set Start Enabled\nHover Over the Graph and Click to set the Start of the Red Line')

            # Allows user to manually type in the skew ratio or the start of the red line
            # 109 is the 'm' key
            elif key == 109:

               # Gets input
               while 1:
                  choice = qinput('Enter in "1" to Type in the Desired Value of the Skew Ratio\nEnter in "2" to Type in the Desired Start of the Red Line\n').strip()
                  if choice in ('1','2'):
                     break
                  print('!!!\nInvalid Number!\n!!!')

               # Changes day to +-1 if the assignment is in progress after manually setting the skew ratio (copied from set start and set skew ratio)
               change_day_mouse = ndif > -1 and ndif == wlen - 1 and lw != works[-2]
               if change_day_mouse:
                  change_day_upper = lw >= funct(wlen+dif_assign)
               if choice == '1':

                  # If the user selects to type in the skew ratio, get the input
                  while 1:
                     try:
                        choice = qinput('Enter in the desired skew ratio value:')
                        if choice:
                           skew_ratio = ceil(float(choice)*1000000 + 999999.5)/1000000
                           if skew_ratio < 2 - skew_ratio_lim:
                              skew_ratio = 2 - skew_ratio_lim
                           elif skew_ratio > skew_ratio_lim:
                              skew_ratio = skew_ratio_lim
                           if not skew_ratio % 1:
                              skew_ratio = ceil(skew_ratio)
                           selected_assignment[6] = skew_ratio
                        break
                     except:
                        print('!!!\nInvalid Number!\n!!!')
               else:
                  while 1:
                     try:
                        choice = qinput(f'Enter the Date at which the Red Line will Start\nFormat: Month/Day/Year\nExample: 2/16/{date_now.year}, nov/5, or 10\nOr, enter the Amount of Days since the Assignment Date the Red Line will Start at (As a Whole Number)\n').replace(' ','')
                        if choice:
                           try:
                              choice = int(choice,10)
                           except:
                              choice = (slashed_date_convert(choice.strip('/'),False)-ad).days
                           if choice < dif_assign or choice > (date(9999,12,30)-ad).days or choice > dif_assign+wlen:
                              raise Exception
                           red_line_start = choice
                           if fixed_mode:
                              fixed_start = red_line_start
                              selected_assignment[14] = fixed_start
                           else:
                              dynamic_start = red_line_start
                              selected_assignment[11] = dynamic_start
                        break
                     except:
                        print('!!!\nInvalid Date!\n!!!')                                    

               # Changes day to +-1 if the assignment is in progress after manually setting the skew ratio (copied from set start and set skew ratio)
               if change_day_mouse:
                  pset()
                  if change_day_upper:
                     day -= lw < funct(wlen+dif_assign)
                  else:
                     day += lw >= funct(wlen+dif_assign)

               # Saves data and draws
               save_data()
               draw(0,0)
               continue

            # Deletes the last work
            # 8 is the backspace key
            elif key == 8:
                if wlen > 0:

                     # Changes day if the assignment is not in progress
                     if not (lw != works[-2] and ndif == wlen - 1 and lw < funct(wlen+dif_assign)):
                        day -= 1

                     # Deletes work and sets the start
                     deleted = works[wlen]
                     del works[wlen]
                     if red_line_start >= wlen + dif_assign:
                        red_line_start -= 1
                        start_lw = works[red_line_start - dif_assign]
                        y_fremainder = (y - start_lw) % funct_round
                        y_mremainder = (y - start_lw) % min_work_time_funct_round
                        if nwd:
                           set_mod_days()
                        calc_skew_ratio_lim()
                     if fixed_start >= wlen + dif_assign:
                        fixed_start -= 1
                        selected_assignment[14] = fixed_start
                     if dynamic_start >= wlen + dif_assign:
                        dynamic_start -= 1
                        selected_assignment[11] = dynamic_start
                     save_data()
                     wlen -= 1
                     lw = works[wlen]
                     draw(0,0)
                     print(f'Deleted Work Input (Used to be at {deleted} Total {unit}s at {(date_file_created + time(day+1)).strftime("%B %-d"+disyear)})')

            # Displays the entire schedule of the assignment
            # 100 is the 'd' key
            elif key == 100:
                 info, fdates, difs, totals = [], [], [], []
                 add_last_work_input = day and lw < y and ndif not in (day, day - 1) and (show_past or not show_past and ndif < day)
                 next_work = adone

                 # If the assignment is in progress, temporarily remove the last work because it is irrelevant for now
                 if (fixed_mode or day + dif_assign == x - 1) and ndif > -1 and ndif == wlen - 1 and lw != works[-2] and lw < funct(wlen+dif_assign):
                    remlw = works[wlen]
                    del works[wlen]
                    lw = works[-1]
                 else:
                    remlw = 0

                 # dstart is the start of the loop that loops through each day of the assignment
                 if show_past or xdif < 1:
                    dstart = dif_assign - 1
                 else:
                    dstart = xdif - 1
                 total = 0
                 dskp = 1
                 end_of_works = False
                 first_loop = True

                 # Zero except are the days that are displayed in the schedule even if the user doesn't have to work for that day
                 if add_last_work_input:
                    zero_except = (0, xdif, dif_assign, day + dif_assign - 1)
                 else:
                    zero_except = (0, xdif, dif_assign)
                 do_format = return_y_cutoff - return_0_cutoff < 10000
                 if not do_format and 'YES' not in qinput('!!!\nWarning!\n!!!\nThere are a lot of Days in this Assignment, and printing the Schedule may take a Long time\nWould you Like to Print it Anways? Enter "YES" in capital letters to Confirm (Enter anything other than "YES" to cancel)\n'):
                         continue
                 for i in range(dstart,x):

                    # If the total has been reached, break
                    if total == y:
                        i -= 1
                        break
                     
                    if i == dstart:
                        if not dif_assign:
                           continue
                        i = 0.0
                    elif i == dstart + 1:
                       if show_past:
                          total = adone
                       else:
                          if xdif < 1:
                             next_work = works[i - dif_assign]
                          else:
                             next_work = lw
                          total = next_work

                    # Stores the start of the assignment when the loop ever reaches the start of the assignment
                    if dif_assign and i == dif_assign:
                        d_start = len(info)
                        
                    s = 's'
                    formatted_date = (date_file_created + time(i-dif_assign)).strftime('%B %-d'+disyear+' (%A):')
                    if end_of_works:

                       # the variable end_of_works if first set to False, so first read the comments below
                       # This also uses the same logic the red line start uses
                       if lw > next_funct:
                          this_funct = lw
                       else:
                          this_funct = next_funct
                       next_funct = funct(i+1)

                       # dif is the difference, or the amount of work to be done, between two days
                       dif = next_funct - this_funct
                    else:

                        # First, the loop runs through all of the inputs
                        try:

                          # Makes sure i isn't negative
                          # An exception must be raised here becuse negative indexing a list is valid and will not raise an exception
                          if i < dif_assign:
                             raise Exception

                          # This uses the same logic the red line start uses
                          # Once i becomes too high and out of range of works, then this raises an exception
                          this_work = next_work
                          next_work = works[i-dif_assign+1]

                          # dif is the difference, or the amount of work to be done, between two days
                          dif = next_work - this_work
                        except:

                          # In this exception, sets end_of_works to True
                          # This makes it so that the loop will start following the red line instead of the 
                          if (i or show_past or xdif < 1) and (i or (not i and not dif_assign)) and (assign_day_of_week + i) % 7 not in nwd:
                             end_of_works = True
                             next_funct = funct(i+1)
                             dif = next_funct - lw
                          else:
                             dif = 0
                             
                    if dif < 0 and end_of_works:
                        dif = 0
                    if dif == 1:
                        s = ' '

                    # Skip that day in the schedule if dif is zero and that day is not in the zero except
                    elif rem_zero and not dif and i not in zero_except:
                        dskp += 1
                        continue

                    # Formats the day information for the schedule
                    total += dif
                    dif = '%g' % dif
                    strtotal = '%g' % total
                    if first_loop and str(i) == '0.0':
                        this_day = formatted_date
                        first_loop = False
                    elif do_format:
                        this_day = f'{formatted_date}ZL {dif}XL {unit}{s} (QL{strtotal} / {stry})'
                    else:
                        this_day = f'{formatted_date}\t{dif} {unit}{s} ({strtotal} / {stry})'.expandtabs(32)
                    if dskp > 1:
                       this_day += f' ({dskp} Days Later)'
                       dskp = 1

                    # Stores today as a variable if the loop ever reaches today
                    if not ndif - i + dif_assign:
                       d_today = len(info)

                    # Stores the last work input as a variable if the loop ever reaches today
                    if add_last_work_input and i == day + dif_assign - 1:
                       d_end = len(info)

                    # Appends to the lists containing all the formatted information
                    info.append(this_day)
                    if do_format:
                        fdates.append(formatted_date)
                        difs.append(dif)
                        totals.append(strtotal)
                    
                 if info:

                    if do_format:
                        # Formatting variables
                        mfdate = len(max(fdates,key=len))
                        mdif = len(max(difs,key=len))
                        mtotal = len(max(totals,key=len))

                    # Adds to the info using the stored variables in the loop
                    if dif_assign:
                       if xdif == 1:
                          info[d_start] += ' (Start)'
                       else:
                          info[d_start] += f' ({xdif} Days Later) (Start)'
                    info[0] += ' (Assign Date)'
                    info[-1] += ' (Finish)'
                    try:
                       info[d_today] += ' (Today)'
                       del d_today
                    except:
                       pass
                    if add_last_work_input:
                       info[d_end] += ' (Last Work Input)'

                    # Formats the info
                    # The phrases "XL", "QL", and "ZL" are all placeholders for whitespace
                    if do_format:
                        info2 = map(lambda i: info[i].replace('ZL',' '*(mfdate-len(fdates[i]))).replace('XL',' '*(mdif-len(difs[i]))).replace('QL', ' '*(mtotal-len(totals[i]))),range(len(info)))
                    else:
                        info2 = info
                    dskp = (due_date-date_file_created).days-i+dif_assign

                    # Prints the info
                    if dskp == 1:
                       assignment_info = f' (Due Date)\nSkew Ratio: {round(skew_ratio-1,3)}\n'
                    else:
                       assignment_info = f' ({dskp} Days Later) (Due Date)\nSkew Ratio: {round(skew_ratio-1,3)}\n'
                    if funct_round != 1:
                       assignment_info += f'Grouping Value: {selected_assignment[8]} {unit}s\n'
                    if len_nwd:
                       assignment_info += f'Not Working Days: {format_not_working_days(False)}\n'
                    if original_min_work_time:
                       rounded_original_min_work_time = ceil(original_min_work_time*ctime*1000000-0.5)/1000000
                       if not rounded_original_min_work_time % 1:
                          rounded_original_min_work_time = ceil(rounded_original_min_work_time)
                       if funct_round % 1:
                          assignment_info += f'Minimum Work Time: {rounded_original_min_work_time} Minutes ({ceil(original_min_work_time*str(float(funct_round))[::-1].find("."))/str(float(funct_round))[::-1].find(".")} {unit}s)'
                       else:
                          assignment_info += f'Minimum Work Time: {rounded_original_min_work_time} Minutes ({ceil(original_min_work_time)} {unit}s)'
                    print('\n'+'\n'.join(info2)+due_date.strftime(f'\n%B %-d{disyear} (%A):') + assignment_info)

                    # Prints warnings and errors
                    if not show_past and ndif > day: 
                        print('!!!\n!!!\nWarning! This Schedule may not be Accurate!\nThis is because the Show Past Inputs in Schedule setting is\ndisabled and the Progress is Incomplete!\nThe schedule has assumed that you have not\nCompleted any work since your Last Input!\nOnce you Input your work, the Schedule\nwill become more Accurate\n!!!\n!!!')
                    if total < y:
                       print('!!!\nCould not Complete Assignment!\nThis is because there are\nNo More Working days Remaining!\n!!!')
                 else:
                    print('\n!!!\nNothing to Display!\n!!!')
                    if not show_past:
                       print('(If this is not your expected outcome, consider toggling the show_past variable in the settings)')

                 # Adds back the in progress work if it was removed
                 if remlw:
                    works.append(remlw)
                    lw = remlw

                 # Deletes the lists to save memory
                 del info, info2, fdates, difs, totals

            # 274 is the down arrow key
            elif not set_skew_ratio and key == 274:
               
                 # If the assignment is in progress, then define a variable on whether to change the day or not
                 change_day = ndif > -1 and ndif == wlen - 1 and lw != works[-2] and lw < funct(wlen+dif_assign)

                 # The smart skew ratio first creates a list of all the function outputs before the skew ratio is changed
                 # Then, it increases or decrease the skew ratio by 0.1 depending on if you inputted the up or down key
                 # Finally, it creates another list of all the function outputs with the new skew ratio
                 # If the two lists are identical, meaning the graph did not change, then repeat this progress until the lists are not identical
                 # This way obviously is slow and takes up a lot of memory, so I made this only run if the amount of days in the assignment is less than 200
                 if smart_skew_ratio:
                    outercon = True
                    while 1:

                        # Old List
                        oldfuncts = tuple(funct(i) for i in range(red_line_start+1,x) if (assign_day_of_week + i) % 7 not in nwd)

                        # Setting Skew Ratio
                        skew_ratio = ceil(skew_ratio*10 - 1.5)/10
                        if skew_ratio < 2 - skew_ratio_lim:
                           skew_ratio = skew_ratio_lim
                        elif skew_ratio != 1:

                           # Compares the new values with the old values and keeps adjusting the skew ratio until they are different
                           pset()
                           oldfuncts_iter = 0
                           for i in range(1,x - red_line_start):
                              if (assign_day_of_week + i + red_line_start) % 7 not in nwd:
                                 if funct(i + red_line_start) != oldfuncts[oldfuncts_iter]:
                                    outercon = False
                                    break
                                 oldfuncts_iter += 1
                           if outercon:
                              continue
                        break

                    # Delete list Variable to save memory
                    del oldfuncts
                 else:

                    # If the smart skew ratio is disabled, increases or decreases the skew ratio by 0.1 depending on if you inputted the up or down key without
                    skew_ratio = ceil(skew_ratio*10-1.5)/10
                    if skew_ratio < 2 - skew_ratio_lim:
                       skew_ratio = skew_ratio_lim
                       
                 if not skew_ratio % 1:
                    skew_ratio = ceil(skew_ratio)
                 selected_assignment[6] = skew_ratio
                 save_data()

                 # Checks if day needs to be changed
                 if change_day:
                    pset()
                    if lw >= funct(wlen+dif_assign):
                       day += 1
                       
                 draw(0,0)
                 
            # Exact same concepts as the down key above
            # 273 is the up arrow key
            elif not set_skew_ratio and key == 273:
                 change_day = ndif > -1 and ndif == wlen - 1 and lw != works[-2] and lw >= funct(wlen+dif_assign)
                 if smart_skew_ratio:
                    outercon = True
                    while 1:
                        oldfuncts = tuple(funct(i) for i in range(red_line_start+1,x) if (assign_day_of_week + i) % 7 not in nwd)
                        skew_ratio = ceil(skew_ratio*10 + 0.5)/10
                        if skew_ratio > skew_ratio_lim:
                           skew_ratio = 2 - skew_ratio_lim
                        elif skew_ratio != 1:
                           pset()
                           oldfuncts_iter = 0
                           for i in range(1,x - red_line_start):
                              if (assign_day_of_week + i + red_line_start) % 7 not in nwd:
                                 if funct(i + red_line_start) != oldfuncts[oldfuncts_iter]:
                                    outercon = False
                                    break
                                 oldfuncts_iter += 1
                           if outercon:
                              continue
                        break
                    del oldfuncts
                 else:
                    skew_ratio = ceil(skew_ratio*10 + 0.5)/10
                    if skew_ratio > skew_ratio_lim:
                       skew_ratio = 2 - skew_ratio_lim
                 if not skew_ratio % 1:
                    skew_ratio = ceil(skew_ratio)
                 selected_assignment[6] = skew_ratio
                 save_data()
                 if change_day:
                    pset()
                    if lw < funct(wlen+dif_assign):
                       day -= 1
                 draw(0,0)

            # Toggles remainder_mode
            # 114 is the 'r' key
            elif ((y - start_lw) / funct_round) % 1 and key == 114:
                 remainder_mode = not remainder_mode
                 selected_assignment[15] = remainder_mode
                 save_data()
                 draw(0,0)

            # Toggles total_mode
            # 116 is the 't' key
            elif key == 116:
                 total_mode = not total_mode
                 selected_assignment[13] = total_mode
                 save_data()
                 draw(0,0)

            # Goes to the next assignment on the list of assignments
            # 110 is the 'n' key
            elif key == 110:

               # Alerts you if the work hasn't been completed
               if not clicked_once and wlen <= xdif and date.now().weekday() not in nwd and lw < funct(xdif+1):
                  print('\n!!!\nEnter your Work Done for Today before going to the Next Assignment\n!!!\nPress "n" again to Ignore this Warning and go to the Next Assignment Anyways')
                  clicked_once = True

               # If you anyways click "n" again, go to the next assignment
               else:
                  clicked_once = False
                  pygame.display.set_mode((1,1))
                  if sel == len(dat) - 1:
                     home(2)
                  elif lw < y:
                     home(sel + 2)
                  else:
                     home(sel + 1)

            # Toggles fixed mode to dynamic mode
            #f  102 is the 'f' key
            elif key == 102:
               fixed_mode = not fixed_mode
               selected_assignment[10] = fixed_mode
               save_data()

               # Sets the start of the red line
               if fixed_mode:
                  red_line_start = fixed_start
                  start_lw = works[fixed_start - dif_assign]

                  # If the assignment is in progress, subtract the day by 1
                  if ndif > -1 and ndif == wlen - 1 and lw != works[-2] and lw < funct(wlen+dif_assign) and day + dif_assign != x - 1:
                     day -= 1
               else:
                  red_line_start = dynamic_start
                  start_lw = works[dynamic_start - dif_assign]
                  day = wlen
                  if day + dif_assign == x:
                     day -= 1
               y_fremainder = (y - start_lw) % funct_round
               y_mremainder = (y - start_lw) % min_work_time_funct_round
                  
               if nwd:
                  set_mod_days()
               draw(0,0)

            # Interprets user inputs
            # 13 is the return key
            elif key == 13:
                 if lw >= y:
                    print('\n!!!\nYou have Reached the End of this Assignment!\n!!!')
                 elif xdif > -1:
                    while 1:
                         try:
                             if (assign_day_of_week + dif_assign + day) % 7 in nwd:

                                # Set the amount done to be zero if the input day is not a working day
                                todo = 0
                                
                             else:
                                todo = funct(day+dif_assign+1) - lw

                             # Checks if the assignment is in progress
                             rem_work = ndif == wlen - 1 and lw != works[-2] and lw < funct(wlen+dif_assign)
                             if rem_work:
                                input_message = f'Amount of {unit}s completed since your Last Input on '
                             else:
                                input_message = f'Amount of {unit}s completed on '
                             if total_mode:
                                input_message = 'Total '+input_message

                             # Formatting for the input
                             formatted_date = (date_file_created + time(day)).strftime('%B %-d'+disyear+' (%A)')
                             if not ndif - day:
                                formatted_date += ' (Today)'
                             elif ndif - day == 1:
                                formatted_date += ' (Yesterday)'
                             if first_loop:
                                print('Press at Any Time Return to Escape')
                                if ndif - day > 1:
                                   formatted_date += ' (Don\'t Remember? Enter "remember" to Proceed)'

                             # Asks for the input
                             input_done = qinput(input_message+formatted_date+':').strip().lower()
                             if not input_done:
                                break
                             elif ndif - day > 1 and input_done == 'remember':

                                 print()
                                 outercon = False
                                 
                                 # If the user doesn't remember, enter the amount they are already at and autofill zero for all the day they can't remember
                                 if total_mode:
                                    input_message = f'Enter the Total Amount of {unit}s you are Currently at Now:'
                                 elif not wlen:
                                    input_message = f'Enter the Amount of {unit}s you have Completed Since you Inputted in this Assignment on this Program:'
                                 else:
                                    input_message = f'Enter the Amount of {unit}s you have Completed Since your last Work Input:'
                                 while 1:
                                    try:
                                       input_done = qinput('Since you do not Remember the Work you have Completed since your last Input,\nThis program will Assume you have not done any work until today and will Autofill Zero work\n'+input_message).strip()
                                       if not input_done:
                                          outercon = True
                                          break
                                       input_done = ceil(float(input_done)*1000000-0.5)/1000000 - lw * total_mode
                                       break
                                    except:
                                       print('!!!\nInvalid Number!\n!!!')
                                 if outercon:
                                    break

                                 # Autofills in work
                                 works.extend((lw,)*(ndif - day - 1))
                                 wlen += ndif - day - 1

                             # "fin" keyword if the user completed the exact amount of work needed
                             elif input_done == 'fin':
                                 if todo > 0:
                                    lw += todo
                                 if rem_work:
                                    del works[wlen]
                                    wlen -= 1
                                 works.append(lw)
                                 wlen += 1
                                 day = wlen
                                 save_data()
                                 if ndif == wlen - 1:
                                    pygame.display.set_mode((1,1))
                                    try:
                                       home()
                                    except:
                                       quit_program(True)
                                 else:
                                    draw(0,0)
                                    pygame.event.pump()
                                 if ndif == wlen or lw >= y:
                                    break
                                 continue

                             # "none" keyword that also works with total_mode
                             elif input_done == 'none':
                                input_done = 0
                             else:
                                input_done = ceil(float(input_done)*1000000-0.5)/1000000 - lw * total_mode

                             # If the user is at the end of the assignment, check to make sure their input is valid
                             # The below equation will be broken down


                             # "wlen+dif_assign == x-1"
                             # Simply checks if the user is entering in the last input
                             
                             # "not input_done and fixed_mode"
                             # The user can't enter 0 for the last input in the assignment
                             # This is because 0 changes the day to the next day no matter what
                             # This will mean the user will reach the end of the assignment
                             # But since the input was 0, the user still hasn't completed the assignment
                             # And since the user must complete the assignment by the due date, entering 0 is not valid

                             # "(not fixed_mode or x-1 != xdif and not rem_work) and input_done + lw < y"
                             # If dynamic mode is enabled and the last input does not complete the assignment, the input is not valid
                             # If fixed mode is enabled and if the user is entering the last input ahead of their current date and the last input does not complete the assignment, the input is not valid
                             # One last condition to the above comment is the 2nd to last input cannot be in progress
                             # This is because without this condition, the code will think the user is entering the last input and make the input invalid, even though the user isn't actually entering the last input
                             if wlen+dif_assign == x-1 and (not input_done and fixed_mode or (not fixed_mode or x-1 != xdif and not rem_work) and input_done + lw < y):
                                raise Exception
                              
                             total_done = input_done + lw
                             if total_done < 0:
                                total_done = 0

                             # If the assignment is in progress, replace the work that was in progress with the newly inputted work
                             if rem_work:
                                del works[wlen]
                                wlen -= 1

                             # Adds the input value to works
                             if not total_done % 1:
                                total_done = ceil(total_done)
                             works.append(total_done)
                             lw = total_done
                             wlen += 1
                             
                             # Change the red line start if the input done is less than the amount to be done
                             if input_done < todo:
                                 if wlen + dif_assign == x:
                                    dynamic_start = wlen + dif_assign - 1
                                 else:
                                    dynamic_start = wlen + dif_assign
                                 selected_assignment[11] = dynamic_start
                                 if not fixed_mode:
                                    red_line_start = dynamic_start
                                    start_lw = works[dynamic_start - dif_assign]
                                    y_fremainder = (y - start_lw) % funct_round
                                    y_mremainder = (y - start_lw) % min_work_time_funct_round
                                    if nwd:
                                       set_mod_days()
                                    calc_skew_ratio_lim()
                             save_data()
                             day = wlen

                             # If the assignment is in progress, subtract the current dya by one
                             if ndif == wlen - 1 and lw != works[-2] and lw < funct(wlen+dif_assign):
                                day -= 1
                             draw(0,0)
                             pygame.event.pump()

                             # Check if the assignment is finished
                             if lw >= y:
                                 print('\nFinish! You have completed your assignment. Good job!')
                                 break
                             if ndif in (wlen-1,wlen):
                                 break
                             first_loop = False
                         except:
                            print('!!!\nInvalid Number!\n!!!')
                 else:
                    print('\n!!!\nPlease Wait until this is Assigned!\n!!!')
      
        # 16 is the video resize event
        elif etype == 16:

            # Get new width and height
            width, height = event.size

            # Cap the width and height at their lower limits
            if height < 375:
                height = 375
            if width < 350:
                width = 350
            if width > max_w:
                width = max_w
            if height > max_h:
                height = max_h
            dat[0][1],dat[0][2] = width,height
            save_data()
            wCon = (width-55)/x
            hCon = (height-55)/y

            # Set a new surface with the width and height
            surface = pygame.display.set_mode((width,height),pygame.RESIZABLE)

            # Define the font size and values involving wCon and hCon
            if width > 748:
               font_size = 25
            else:
               font_size = ceil((width+450)/47-0.5)
            font = pygame.font.SysFont(font_type,font_size)
            left_adjust_cutoff = (width - 50 - point_text_width)/wCon
            up_adjust_cutoff = point_text_height/hCon
            draw(0,0)

        # 12 is the quit event
        elif etype == 12:
           quit_program()
         
except:
   quit_program(True)
