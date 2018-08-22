#As per the question, the program is solved only for ODD Numbers
#For any even numbers entered, the program throws an error


def main():
	N = int(input())
	character1=' * '
	character2='   '
	printPattern_freeMemory(character1,character2,N)

#This function will not store the pattern in memory
def printPattern_freeMemory(character1,character2,n):
	import sys

	if n%2==0:
		print('ERROR::')
		print('Entered Number is Even. Only Odd numbers allowed')
		sys.exit()
		
	if n == 1:
		print(character1)
		
	else:		
		initialspaces = int((n-1)/2)
		starCharacterCount = 1
		totalLines = int(n/2) +1 	#total lines in the pattern. Example: for 5 it will be 3, 7 it will be 4 etc

		for lineNumber in range(0,totalLines):

			for c in range(0,initialspaces):
				print(character2,end='')

			for star in range(0,starCharacterCount):
				print(character1,end='')
				
			for c in range(0,initialspaces):
				print(character2,end='')
			print()
			initialspaces -= 1
			starCharacterCount += 2

#This function returns the full pattern as a list, with each line as an individual list

def printPattern_memory(character1,character2,n):
	import sys

	if n%2==0:
		print('ERROR::')
		print('Entered Number is Even. Only Odd numbers allowed')
		sys.exit()
		
	if n == 1:
		print(character1)
		
	else:		
		initialspaces = int((n-1)/2)
		starCharacterCount = 1
		totalLines = int(n/2) +1 	#total lines in the pattern. Example: for 5 it will be 3, 7 it will be 4 etc

		lines = [0]*totalLines		#Storing entire pattern in a list for further manipulation if required
		line = ['']*n
		
		for lineNumber in range(0,totalLines):
				pointer=0
				for c in range(0,initialspaces):
					line[pointer]=character2
					pointer+=1

				for star in range(0,starCharacterCount):
					line[pointer]=character1
					pointer+=1

				for c in range(0,initialspaces):
					line[pointer]=character2
					pointer+=1
				lines[lineNumber] = list(line)
				initialspaces -= 1
				starCharacterCount += 2
		
		for x in lines:
			for y in x:
				print(y,end='')
			print()
		return lines
                        	
main()	
