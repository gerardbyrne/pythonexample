MenuChoice = 0
Firstname = ""
Surname = ""
    
while MenuChoice != "x":
    print()
    print("Type 1 to calculate a Lucky Number")
    print()
    print("Type x to EXIT")
    print()

    MenuChoice =input("Choice please --> ")
    print()

    if MenuChoice == "1":  #calculate a Lucky Number

        #Firstname = input ("Firstname  ---> ") 
        #Surname = input ("Surname   ---> ")

        #Firstname = "Eleanor"  #used as test data to save input a name every time the program runs
        #Surname = "Wiseman"

        Firstname = "iiiiiiiiiiiiiiiiiiiiii"   #used as test to generate more than one digit
        Surname = "rrrrrrrrrrrrrrrrrrrrr"

        Firstname = Firstname.upper() # convert to uppercase
        Surname = Surname.upper()

        FirstnameTotal = 0
        
        for letter in Firstname:  # look at each letter in Firstname
            if letter  in ["A","J","S"]:    #check if letter is A J or S
                FirstnameTotal = FirstnameTotal + 1
            if letter  in ["B","K","T"]:    #check if letter is B K or T
                FirstnameTotal = FirstnameTotal + 2
            if letter  in ["C","L","U"]:    #check if letter is C L or U
                FirstnameTotal = FirstnameTotal + 3
            if letter  in ["D","M","V"]:
                FirstnameTotal = FirstnameTotal + 4
            if letter  in ["E","N","W"]:
                FirstnameTotal = FirstnameTotal + 5              
            if letter  in ["F","O","X"]:
                FirstnameTotal = FirstnameTotal + 6
            if letter  in ["G","P","Y"]:
                FirstnameTotal = FirstnameTotal + 7
            if letter  in ["H","Q","Z"]:
                FirstnameTotal = FirstnameTotal + 8 
            if letter  in ["I","R"]:
                FirstnameTotal = FirstnameTotal + 9 

        print("Firstname Total is", FirstnameTotal)

        SurnameTotal = 0
        
        for letter in Surname:  # look at each letter in Firstname
            if letter  in ["A","J","S"]:  #check if letter is A J or S
                SurnameTotal = SurnameTotal + 1
            if letter  in ["B","K","T"]:
                SurnameTotal = SurnameTotal + 2
            if letter  in ["C","L","U"]:
                SurnameTotal = SurnameTotal + 3
            if letter  in ["D","M","V"]:
                SurnameTotal = SurnameTotal + 4
            if letter  in ["E","N","W"]:
                SurnameTotal = SurnameTotal + 5              
            if letter  in ["F","O","X"]:
                SurnameTotal = SurnameTotal + 6
            if letter  in ["G","P","Y"]:
                SurnameTotal = SurnameTotal + 7
            if letter  in ["H","Q","Z"]:
                SurnameTotal = SurnameTotal + 8 
            if letter  in ["I","R"]:
                SurnameTotal = SurnameTotal + 9 

        print("Surname Total is", SurnameTotal)

        FirstnameDigits = str(FirstnameTotal)  # convert Total to a string so we can deal with each individual digit
        SurnameDigits =str(SurnameTotal)
       
        print("FirstnameDigits is", FirstnameDigits)
        FirstnameTotal = 0
        for digit in FirstnameDigits:   #add up all digits in Firstname
            FirstnameTotal = FirstnameTotal + int(digit)
        print("Firstname Total is", FirstnameTotal)

        FirstnameDigits = str(FirstnameTotal)  # convert to a string so we can deal with each individual digit

        print("SurnameDigits is", SurnameDigits)
        SurnameTotal = 0
        for digit in SurnameDigits: #add up all digits in Surname
            SurnameTotal = SurnameTotal + int(digit)

        print("SurnameTotal is", SurnameTotal)
        SurnameDigits = str(SurnameTotal) # convert to a string so we can deal with each individual digit

        Total = FirstnameTotal + SurnameTotal           
        print("Total for Firstnmae and Surnmae is", Total)
        
        AllDigits = str(Total) # convert to a string so we can deal with each individual digit
        print("AllDigits is", AllDigits)

        while len(AllDigits) > 1:   # if it is not a sigle digit then keep adding
                                    # them together until it is a single digit
            Total = 0
            for digit in AllDigits: # look at each digit in AllDigits
                Total = Total + int(digit)  # add each digit to Total
                print("Total is", Total)
                
            AllDigits = str(Total)
            print("AllDigits is", AllDigits)

        LuckyNumber = Total
        #print(Firstname, Surname+"\'s","lucky number is", LuckyNumber)

        # check LuckyNumber and assign Meaning
        if LuckyNumber == 1:
            Meaning = "Natural leader"
        if LuckyNumber == 2:
            Meaning = "Natural peacemaker"
        if LuckyNumber == 3:
            Meaning = "Creative and optimistic"
        if LuckyNumber == 4:
            Meaning = "Hard worker"
        if LuckyNumber == 5:
            Meaning = "Value freedom"
        if LuckyNumber == 6:
            Meaning = "Carers and providers"
        if LuckyNumber == 7:
            Meaning = "Thinker"
        if LuckyNumber == 8:
            Meaning = "Have diplomatic skills"
        if LuckyNumber == 9:
            Meaning = "Selfless and generous"

        print(Firstname, Surname+"\'s","lucky number is", LuckyNumber, "which means", Meaning)
  
