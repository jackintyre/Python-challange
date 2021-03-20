import os
import csv
num_votes=0
canidates=[]
x=0
invotes=[]
i=0
poll_csv = os.path.join("..", "Resources", "election_data.csv")
with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    num_votes = len(list(csvreader)) #counts the total votes cast

with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        if row[2] not in canidates:
            canidates.append(row[2])
            x+=1
#for i in range(x):
    #invotes.append([0]) 
    #invotes[i]=invotes[i]+1
    #print(invotes[i])
    
i=0   
j=0     
for i in range(x):
    with open(poll_csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
    
        j=0
        for row in csvreader:
            if row[2] == canidates[i]:
               j+=1
        invotes.append(int(j))
        
        
        
            


j=0
pervote=[]

for j in range(x):
    percent=0.0
    #invotes =[int(y) for y in invotes]
    #tempvote = int(invotes[j])
    percent=(int(invotes[j])/num_votes)*100
    pervote.append(percent)

y=0    
print("Total votes:", num_votes, "Votes")
for y in range(x):
    print(str(canidates[y]),":", round(pervote[y],3),"(", invotes[y], ")")


y=0

with open("vote.txt",'w',encoding = 'utf-8') as f:
    f.write("Total votes:"+ str(num_votes)+"Votes"+"\n")   
    for y in range(x):
        f.write(str(canidates[y])+":"+ str(round(pervote[y],3))+"("+ str(invotes[y])+ ")"+"\n") 