from time import sleep
import sys
from rich.console import Console
from rich.table import Table
from tqdm import tqdm
import os
import progressbar
import random
from alive_progress import alive_bar
from time import process_time

def  createTable(resultList):
    table = Table(title="Danh sách các file đáng ngờ", show_lines=True, expand=True)
    rows = []
    for record in resultList:
        # record.pop(-2)
        if record[7] != '':
            record.pop(3)
            record.pop(5)
            record = map(str, record)
            rows.append(record)
    columns = ["STT", "File path", "Tình trạng", "Dung lượng file (KB)", "Chênh lệch so với file cũ (B)", "Chi tiết", "Đuôi file", "Định dạng"]

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)

def processing_animation1():
    for x in range(1,11):
        for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
            sleep(0.1)
            if x == 10:
                print('(Done ;)' , end='')
                break
            else:
                print('Loading ' +i, end = '\r')

def processing_animation2():
    loop = tqdm(total = 50000, position = 0, leave=False)
    for k in range(50000):
        loop.set_description("Loading...".format(k))
        loop.update(1)
    loop.close()

# Function for implementing the loading animation
def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "[*] Starting tool..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 20):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46 and x != 91 and  x != 93 and x != 42 and x != 83:
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1

    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear lines 

    print('''
 __  __                    _____     __   __
 \ \/ /__  __ _____  ___ _/ ___/__  / /__/ /
  \  / _ \/ // / _ \/ _ `/ (_ / _ \/ / _  / 
  /_/\___/\_,_/_//_/\_, /\___/\___/_/\_,_/  
                   /___/                    
                   
    ''')

def processing_animation3():
    bar = progressbar.ProgressBar(maxval=20, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for i in range(20):
        bar.update(i+1)
        sleep(0.1)
    bar.finish()

def logic(stage, hasFolder):
    t1_start = process_time()
    getFileTime = int(round(random.uniform(3,4) * 1000,0))
    compareTime = int(round(random.uniform(1,1.3) * 1000,0))
    print(hasFolder)
    if hasFolder:
        getFileTime = int(round(random.uniform(5,7) * 1000,0))
        compareTime = int(round(random.uniform(5,6) * 1000,0))
    outputTime = int(round(random.uniform(0.2,0.4) * 1000,0))
    sleepTime = 0.5
    if stage == 'get files':
        print('Getting files...')
        percent42 = int(round(getFileTime*42/100,0))
        percent65 = int(round(getFileTime*23/100,0))
        percent87 = int(round(getFileTime*22/100,0))
        percent96 = int(round(getFileTime*9/100,0))
        percent100 = getFileTime - (percent42 + percent65 + percent87 + percent96)
        with alive_bar(getFileTime, bar = 'filling') as bar:
            for i in range(percent42):
                sleep(0.000005)
                sleepTime += 0.000005
                bar()
            for i in range(percent65):
                sleep(0.001)
                sleepTime += 0.001
                bar()
            for i in range(percent87):
                sleep(0.005)
                sleepTime += 0.005
                bar()
            for i in range(percent96):
                sleep(0.003)
                sleepTime += 0.003
                bar()
            for i in range(percent100):
                sleep(0.02)
                sleepTime += 0.02
                bar()
        print('Get files finished! ✅', end = '\n')

    if stage == 'output': 
        print('Writing ressult to excel files...')
        percent65 = int(round(outputTime*65/100,0))
        percent87 = int(round(outputTime*22/100,0))
        percent96 = int(round(outputTime*9/100,0))
        percent100 = outputTime - (percent65 + percent87 + percent96)
        with alive_bar(outputTime, bar = 'filling') as bar:
            for i in range(percent65):
                sleep(0.001)
                sleepTime += 0.001
                bar()
            for i in range(percent87):
                sleep(0.005)
                sleepTime += 0.005
                bar()
            for i in range(percent96):
                sleep(0.003)
                sleepTime += 0.003
                bar()
            for i in range(percent100):
                sleep(0.02)
                sleepTime += 0.02
                bar()
        print('Done! ✅', end = '\n')


    if stage == 'compare':
        print('Comparing...')
        with alive_bar(compareTime, bar = 'filling') as bar:
            percent65 = int(round(compareTime*65/100,0))
            percent87 = int(round(compareTime*22/100,0))
            percent98 = int(round(compareTime*2/100,0))
            percent100 = compareTime - (percent65 + percent87 + percent98)
            for i in range(percent65):
                sleep(0.001)
                sleepTime += 0.001
                bar()
            for i in range(percent87):
                sleep(0.005)
                sleepTime += 0.005
                bar()
            for i in range(percent98):
                sleep(0.003)
                sleepTime += 0.003
                bar()
            for i in range(percent100):
                sleep(0.02)
                sleepTime += 0.02
                bar()
        # sys.stdout.write("\033[F\033[F") #back to previous 2 lines 
        # sys.stdout.write("\033[K") #clear lines 
        print('Comparing files finished! ✅')
    
# if __name__ == "__main__":
#     logic('get files')
#     logic('compare')
#     logic('output')



