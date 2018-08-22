space='   '
character=' * '
import sys

n = int(input())
if n%2==0:
    print('ERROR::')
    print('Entered Number is Even. Only Odd numbers allowed')
    sys.exit()
    
if n == 1:
    print(character)
    
else:
    
    initialspaces = int((n-1)/2)
    starCharacter = 1
    totalLines = int(n/2) +1

    lines = [0]*totalLines
    line = ['']*n
    
    for lineNumber in range(0,totalLines):
            pointer=0
            for spaceCharacter in range(0,initialspaces):
                line[pointer]=space
                pointer+=1

            for star in range(0,starCharacter):
                line[pointer]=character
                pointer+=1

            for spaceCharacter in range(0,initialspaces):
                line[pointer]=space
                pointer+=1
            lines[lineNumber] = list(line)
            initialspaces-=1
            starCharacter+=2
    for x in lines:
        for y in x:
            print(y,end='')
        print()
                        
    
