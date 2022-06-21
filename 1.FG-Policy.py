import os
nl=0
p=0
FGPolicy=open ('Policy.txt',"w")
if os.path.exists('FG.txt'):
	with open('FG.txt',"r") as FGConfig:
		for line in FGConfig.readlines():
			nl+=1			
			if 'config firewall policy' in line:
				p+=1
			if p==1:
				FGPolicy.write(line)	
			if p==1:
				if 'end\n' in line:
					break
else:
	print("file not exists")
FGPolicy.close()

