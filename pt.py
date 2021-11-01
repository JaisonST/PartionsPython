#-------------------Intro Note----------------------------------#
#Function: Backend Functiond for Partions Program 
#Made by: Jaision Thomas 
#---------------------------------------------------------------#

#---------------Create Partion Function-------------------------#
def getPartitions(n):
	retval = []
	p = [0] * n	 
	k = 0		 
	p[k] = n	
				
	cTotal = 0 
	
	while True:

			a = [] 
			for i in range(0,k+1):
				a.append(p[i])
			retval.append(a)		

			rem_val = 0
			while k >= 0 and p[k] == 1:
				rem_val += p[k]
				k -= 1
			
			if k < 0:
				return retval

			p[k] -= 1
			rem_val += 1

			while rem_val > p[k]:
				p[k + 1] = p[k]
				rem_val = rem_val - p[k]
				k += 1

			p[k + 1] = rem_val
			k += 1  

# this function was written 	
# by JoshuaWorthington
#modified by Jaison Thomas 
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

#no number lesser than a number 
def ltn(li, n): 
	for i in li: 
		if i>=n:
			return False 
	return True  

#no number greater than a number 
def gtn(li, n): 
	for i in li: 
		if i<=n:
			return False 
	return True  

#check array is 1,2,4, % 7 
def m7(li):
	rep_check = []	
	for i in li: 
		if i % 7 == 1 or i % 7 == 2 or i % 7 == 4:
			if i in rep_check: 
				return False
			rep_check.append(i)
		else:
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

def lessThanN(ans, n):
	return [i for i in ans if ltn(i, n)]

def greaterThanN(ans, n):
	return [i for i in ans if gtn(i, n)]

def mod7(ans):
	return [i for i in ans if m7(i)]
#--------------------------------------------------------------#

#------------------------Main program--------------------------# 
#a = int(input("Enter the number to partiiton:- "))
#ans = getPartitions(5) 



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

#1,2,4 mod 7 
#a = [i for i in ans if  m7(i)]

#print final 
#for i in a: 
#	print(i) 
#---------------------------------------------------------------#

