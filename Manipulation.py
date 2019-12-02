# Compulsory Task 3
strManip = input("Please enter a sentence:")#Declaring the variable
StrLength = len(strManip)#Storing the length of the sentence as a variable
print(StrLength)# Printing the length of the sentence
LastLetter = strManip[StrLength-1:StrLength] #Storing the last letter of the lentence as a variable
print(strManip.replace(LastLetter,"@"))#Replacing all of the letters that are the same as last letter with the @ symbol
print(strManip[StrLength:StrLength-4:-1])#Printing the last 3 letter using the length of the string as the letters positions
print(strManip[0:3]+ strManip[StrLength-2:StrLength]) #Slicing the string and concatenating the sliced pieces together
print(strManip.replace(" ","\n"))#Replacing all of the spaces with the backslash (there is no backslash on my keyboard so I had to copy it - please help)n to put in new lines


