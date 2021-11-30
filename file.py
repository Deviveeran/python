#File creation

import os
import datetime
import re
#print(os.mkdir("Resumefolder"))
print(os.chdir('/home/durgadevi/Documents/Resumefolder'))
'''
f=open("durga.txt",'w')
f.write("hello duga 08778298677")
f1=open("lakshmi.txt",'w')
f1.write("916789123467 this is lakshmi sister number")
f2=open("raja.txt",'w')
f2.write("this 916789089876 is raja brother number")
f3=open("vignesh.txt",'w')
f3.write("this is vignesh brother number 07907899089")
f.close()
f1.close()
f2.close()
f3.close()
#reading files and getting phone number 
'''
files=os.listdir()
a=[]
for resume in files:
    fi=open(resume,'r')
    fil=fi.read()
    mobileno=re.compile('(0|91)[6-9][0-9]{9}')
    value=mobileno.search(fil)
    val=value.group()
    a.append(val)
for i in a:
    newfile=open("numers.txt",'a')
    newfile.write(i)
    newfile.close()

        
        
