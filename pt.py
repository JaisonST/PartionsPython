#-------------------Intro Note----------------------------------#
#Function: Backend Functiond for Partions Program 
#Made by: Jaision Thomas 
#---------------------------------------------------------------#



#---------------Create Partion Function-------------------------#
def getPartitions(n):
	q = [] 
	l = []
	a = [] 
	for i in range(n): 
		a.append(1) 
	q.append(a) 
	
	while len(q) > 0 : 
		a = q.pop(0)
		l.append(a[:])  
		if len(a) > 2:
			for i in range(len(a)-1): 
				
				#go through n sums
				m = a[:]
				m[i] =  m[i]+ m[i+1] 
				m.pop(i+1)

				#sort reverse = true
				m.sort(reverse = True)

				#check if it exists in l and q 
				if (m not in l) and (m not in q):	
					#if it doesnt exist append to q  
					q.append(m[:])		
     
	a=[]
	a.append(n) 
	l.append(a[:]) 
	return l  	
#---------------------------------------------------------------#




#---------------Select Sort Partions Functions-------------------#
#no even numbers  
def oddPart(li):
	for i in li: 
		if i%2==0: 
			return False 
	return True
 
#no odd numbers  
def evenPart(li):
	for i in li: 
		if i%2!=0: 
			return False 
	return True

#no given number 
def rm(li, n): 
	for i in li: 
		if i == n: 
			return False 
	return True  

#no number divisible by a number 
def rmDiv(li, n): 
	for i in li: 
		if i%n == 0:
			return False 
	return True  
#--------------------------------------------------------------#

#-----------------------Sort Functions-------------------------# 
def oddParts(ans): 
	return [i for i in ans if oddPart(i)]

def evenParts(ans): 
	return [i for i in ans if evenPart(i)]

def smallerThan(ans, n): 
	return [i for i in ans if len(i) < n]

def biggerThan(ans, n): 
	return [i for i in ans if len(i) > n]

def removeN(ans, n): 
	return [i for i in ans if rm(i, n)]

def removeDiv(ans, n):
	return [i for i in ans if rmDiv(i, n)]

#--------------------------------------------------------------#

#------------------------Main program--------------------------# 
#a = int(input("Enter the number to partiiton:- "))
#ans = getPartitions(a) 

#partions lesser than a number 
#short = [i for i in ans if len(i) < 3]

#partions more than a number 
#moreThan = [i for i in ans if len(i) > 3]

#partions wihtout even  
#odd = [i for i in ans if oddPart(i)]

#partions without odd 
#even = [i for i in ans if evenPart(i)]
 
#partions removing specific number 
#removedN = [i for i in ans if rm(i, 3)]

#partions removing containing a number divisible by given number   
#removedDiv = [i for i in ans if rmDiv(i, 3)]

#print final 
#for i in removedDiv: 
#	print(i) 
#---------------------------------------------------------------#

