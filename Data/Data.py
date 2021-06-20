import csv
listname=[]
listloc=[]
listword=[]
listtype=[]
listlink=[]
with open('./Data/Data.csv','r')as f:
    f_csv=csv.reader(f)
    for row in f_csv:
        listname.append("<b>"+row[0]+"</b>")
        listloc.append(list(map(float,row[1].split(","))))
        listword.append(row[2])
        listtype.append(eval(row[3]))
for i in listname:
    print('"',i,'"',',')
print('\n')
for i in listloc:
    print(i,',')
print(listtype)