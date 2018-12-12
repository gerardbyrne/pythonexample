# Prompt the user to input the window measurements in cm 
# Add a bit for the hems 
# Work out how many widths of cloth will be needed 
# and figure out the total length of material for each curtain (in cm still) 
# Actually there are two curtains, so we must double the amount of material 
# and then divide by 10 to get the number of meters 
# Finally, work out how much it will cost 
# And print out the result  


# To start with, all the measurements will be in cm 
# Assume that the roll of material is going to be 140cm wide 
# and that the price per meter will be 5 units of currency 

rollwidth = 140 
pricepermetre = 5  

# Prompt the user to input the window measurements in cm 

windowheight = input('Enter the height of the window (cm): ') 
windowwidth = input('Enter the width of the window (cm): ') 
 
# Add a bit for the hems 
# First we must convert the string into a number 
# otherwise we will get an error if we try to perform arithmetic on a text string 

curtainwidth = float(windowwidth) * 0.75 + 20 
curtainlength = float(windowheight) + 15  

# Work out how many widths of cloth will be needed 
# and figure out the total length of material for each curtain (in cm still) 

widths = curtainwidth / rollwidth 
totallength = curtainlength * widths  

# Actually there are two curtains, so we must double the amount of material 
# and then divide by 10 to get the number of meters  

totallength = (totallength * 2) / 10  

# Finally, work out how much it will cost 

price = totallength * pricepermetre  

# And print out the result 

print("You need", totallength, "meters of cloth for ", price) 

raw_input('Press Enter to Continue');
