# Name: Deepmala Bhomi              Date Assigned: 10/10/2019
#
# Course: 2000-44306                Date Due: 10/17/2019
#
# File name: programmingAssignment4.py
#
# Program Description: The program reads a encoded file and
#                      decodes the file and displays the decoded output.
#                     
#                      


#Creating the header of the program.

print("{0:^61s}".format("=-"*23 + "="))
print()
print("{0:^61s}".format("DECODE MESSAGES HERE!"))
print()
print("{0:^61s}".format("=-"*23 + "="))


#initilizing while loop to continuously start the program if the user wants
#to decode another file.

userResponse="y"

while userResponse=="y":
    print()
    print("="*61)
    print()
    
    
    #asking user for the file which they want to decode.
    fileName=input("Enter encoded file name: ")
    

    #initilizing while loop for input validation.
    #user can only input file name with extension '.txt'.
    
    while not (fileName.endswith(".txt")):
        print("Error!!! Enter valid file name with extension '.txt'")
        print()
        fileName=input("Enter encoded file name: ")

        
    print()
    print()
    design="+"+"-"*17+"+"
    print("{0:^61s}".format(design))
    print("-"*21+"|"+" DECODED MESSAGE "+"|"+"-"*21)
    print("{0:^61s}".format(design))
    print()
    
    
    #opening the user choice file to read only.
    infile=open(fileName,"r")
    

    #declaring variables to use inside the loop.
    eachWord=""
    letter=""
    decodedCharacter=""
    currentASCII=0
    decoded=0


    #initilizing for loop to read each line of the user choice file. 
    for line in infile:
        
        

        #initilizing for loop to read each character in each line of the file.
        for letter in line:
            if letter == " ":           #adds a whitespace after each word.
                decodedCharacter+=" "
                continue               #using continue statement to end current
            #                           loop iteration and return control to the
            #                           loop header if the character is whitespace.
            


            elif ord(letter) < 31:       #special condition to decode whitespace
            #                           which needs to be returned as '!'.
                decodedCharacter += " "


                
            else:
                currentASCII = ord(letter)     #assigining ASCII value of letter to a variable. 
                


                #increasing the ASCII value of each character of the file to decode
                #as the ASCII value was decreased by 2 while encoding.
                
                decoded = currentASCII + 2
                

                #accumulator variable
                decodedCharacter += chr(decoded)


                
        print(decodedCharacter)       #displays the full decoded message.
        
        decodedCharacter = ""         #maintains spacing between each lines.
        
    print()
    print()

    
    design_2="+"+"-"*16+"+"
    print("{0:^61s}".format(design_2))
    print("-"*21+"|"+" END OF MESSAGE "+"|"+"-"*21)
    print("{0:^61s}".format(design_2))
    print()


    #asking user if they want to decode another file?
    #run program again?
    
    userResponse=input("Decode another file? (y/n): ")


    #initilizing while loop for input validation
    while userResponse!="y" and userResponse!="n":

        #displays error message when user inputs character other that 'y' or 'n'.
        print("Error!!! Enter 'y' or 'n' only.")
        
        print()

        userResponse=input("Decode another file? (y/n): ")
        

        
#displaying end note.
print()
print("="*61)
print()
print("{0:^61s}".format("Please come again!"))
print()
print("="*61)
