MenuChoice = 0
BagCount = 0
TotalValueCoinsAdded = 0
TotalValueCoinsRemoved = 0
    
while MenuChoice != "x":
    print()
    print("Type 1 for a bag of 1p coins")
    print("Type 2 for a bag of 2p coins")
    #print("Type 5 for a bag of 5p coins")
    #print("Type 10 for a bag of 10p coins")
    #add other denominations here
    print()
    print("Type x to EXIT")
    print()

    MenuChoice =input("Choice please --> ")
    print()
   
    if MenuChoice == "1":
        CoinType = "1p"
        BagCount = BagCount + 1

        #BagWeight = float(input ("Weight in grams  ---> "))

        #BagWeight = 359.56 # test data gives one extra 1p
        BagWeight = 352.44 # test data gives one less 1p
        
        if BagWeight > 356:  # 100 1p coins weigh 356 grams
            Difference = BagWeight - 356
            NumCoinsDifference = int(Difference / 3.56)
            TotalValueCoinsAdded = TotalValueCoinsAdded + (NumCoinsDifference * 1)

        if BagWeight < 356:
            Difference = 356 - BagWeight
            NumCoinsDifference = int(Difference / 3.56)
            TotalValueCoinsRemoved = TotalValueCoinsRemoved + (NumCoinsDifference * 1)

        if BagWeight == 356:
            Difference = 0
            NumExtraCoins = 0

    if MenuChoice == "2":
        print("2p")
        CoinType = "2p"
        BagCount = BagCount + 1

       #BagWeight = 704.88 # test data gives one less 2p
        #BagWeight = 356 # test data gives no coins
       # BagWeight = 356 + 7.12 #  test data gives one extra 2p
        #BagWeight = 356 + 2*(7.12) # test data gives two extra 2p
        BagWeight = 356 - 7.12 #  test data gives one less 2p
        
        if BagWeight > 356:  # 100 2p coins weigh 712 grams BUT 50 weigh 356 grams
            print("2p is greater than 712")
            Difference = BagWeight - 356
            NumCoinsDifference = int(Difference / 7.12)
            TotalValueCoinsAdded = TotalValueCoinsAdded + (NumCoinsDifference * 2)

        if BagWeight < 356:  
            print("2p is less than 712")
            Difference = 356 - BagWeight
            NumCoinsDifference = int(Difference / 7.12)
            TotalValueCoinsRemoved = TotalValueCoinsRemoved + (NumCoinsDifference * 2)

        if BagWeight == 356:
            print("2p is 712")
            NumCoinsDifference = 0
            Difference = 0
            NumExtraCoins = 0

    print("Difference for the ",CoinType, "coin bag is", Difference)
    print("Number of coins added or removed for the ",CoinType, "coin bag is", NumCoinsDifference)
    print()


##    if MenuChoice == "5":
##        CoinType = "5p"
##        BagCount = BagCount + 1
##  REST OF CODE FOR 5p COIN HERE
##
##    if MenuChoice == "10":
##        CoinType = "10p"
##        BagCount = BagCount + 1
##  REST OF CODE FOR 10p COIN HERE
        
print()
print("BagCount is ", BagCount) 
print("TotalValueCoinsAdded is ", TotalValueCoinsAdded)    
print("TotalValueCoinsRemoved is ", TotalValueCoinsRemoved)
# Next line formats the output to 2 deciml places but 5 places in total
print ("TotalValueCoinsRemoved formatted is £","{:5.2f}".format(TotalValueCoinsRemoved/100))
      
