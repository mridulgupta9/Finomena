import csv
import math
data = []
with open("test.csv","rb") as file:
	data = file.read()
data = data.split("\n")[:-1]

c = csv.writer(open("testdatag.csv", "wb"))
row=data[0].split(",")

for i in range(1,len(data)):
	row=data[i].split(",")
	for j in range(1,len(row)):
	 	if row[j]=="":
	 		row[j]='0'


	 	
		elif(len(row[j])==1 and row[j]>='A' and row[j]<='Z'):
			row[j]=str(ord(row[j])-64)
		elif(len(row[j])!=1 and row[j][0]>='A' and row[j][0]<='Z'):
			leng=len(row[j])
			sum=0
			for k in range(0,leng):
				sum=sum+ord(row[j][k])
			row[j]=str(sum)
		
	c.writerow(row[1:])
