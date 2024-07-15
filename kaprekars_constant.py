
#Takes the input from the user
userin = int(input("Enter a four-digit integer: "))

ascend = 0
descend = 0
difference = 0
tempint = userin
count = 0
#print(reversed(sorted(userin)))

#Loop keeps running intil 6174 or 0 reaches
while tempint != 6174 and tempint != 0:
   
    if tempint != 6174 or tempint != 0:      
        tempint = f"{tempint:0>4}"
        #ascending the input
        ascend = "".join(sorted(tempint))
        #Finding the input in descending order
        descend = "".join(reversed(ascend))
        #Difference btwn descend and ascend
        difference = int(descend) - int(ascend)
        print(int(tempint),"> ", end='')
        tempint = difference
        count += 1
        
        #Checking to see if the temp variable reaches 0 or the constant
    if tempint == 6174 or tempint == 0:
        
        #if true, then outputs the following and loop will end
        print(tempint)
        print(f"{userin} reaches {tempint} via Kaprekar's routine in {count} iterations")
        
    


