#changing list of image names in particular folder

import os
print(os.chdir("/home/durgadevi/Documents/durga"))
lists=os.listdir()
for i in range(len(lists)):
    a=os.rename(lists[i],'kodai'+str(i))
    print(a)
    

#Getting .txt files
'''
import os
print(os.chdir("/home/durgadevi/Documents/files txt"))
files=os.listdir()
for i in files:
    if i.endswith(".txt"):
        print(i)
''' 
#Getting list of files modified time
'''
import os
from datetime import *
print(os.chdir("/home/durgadevi/Documents/files txt"))
lists=os.listdir()
for i in range(len(lists)):
    #print(os.stat(lists[i]))
    acctime=os.stat(lists[i]).st_mtime
    print(datetime.fromtimestamp(acctime))
'''

