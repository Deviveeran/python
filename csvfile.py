#writting
import csv
'''
print(dir(csv))
with open('staff.csv','w',newline='')as files:
    new_file=csv.writer(files)
    new_file.writerow(["ID","NAME","CITY"])
    count=int(input("Enter no of student: "))
    for no in range(count):
        ID=int(input("enter ID: "))
        NAME=input("enter NAME: ")
        CITY=input("enter CITY: ")
        new_file.writerow([ID,NAME,CITY])
'''
#reading
import csv
with open('staff.csv','r')as file:
    re=csv.reader(file)
    l=list(re)
    for i in l:
        for line in i:
            print(line,end=' ')
        print()
