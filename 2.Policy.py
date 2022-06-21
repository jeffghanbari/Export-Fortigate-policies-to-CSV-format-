import os
import csv
c=0
t=0
p6='not define'
outputcsv =open('output.csv','w')
spamwriter = csv.writer(outputcsv)
spamwriter.writerow(["policyID","Source interface","destination interface","source address","destination address","action","schedule","service"])
with open('Policy.txt',"r") as FGPolicy:
	for line in FGPolicy.readlines():
		if ' edit ' in line:
			p1=line[9:-1]
			c+=1
		if ' srcintf ' in line:
			p2=line[21:-1]
			c+=1
		if ' dstintf ' in line:
			p3=line[21:-1]
			c+=1
		if ' srcaddr ' in line:
			p4=line[21:-1]
			c+=1
		elif ' internet-service-src-id ' in line:
			p4='interne Service='+line[21:-1]
			c+=1
		if ' dstaddr ' in line:
			p5=line[21:-1]
			c+=1
		if ' action ' in line:
			p6=line[19:-1]
			t=1
			c+=1
		if ' schedule ' in line:
			p7=line[22:-1]
			c+=1
		if ' service ' in line:
			p8=line[21:-1]
			c+=1
		if c==7 and t==0:
			p6='deny'
			spamwriter.writerow([p1,p2,p3,p4,p5,p6,p7,p8])
			c=0
		if c==8:
			spamwriter.writerow([p1,p2,p3,p4,p5,p6,p7,p8])
			t=0
			c=0
