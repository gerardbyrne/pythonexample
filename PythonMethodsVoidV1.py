# Program Description:     Python Data Arithmetic
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015 

print('');
# Create a two dimensional string array with 6 rows and 5 columns
listOrders =( 
                        [
                        ["000001","Allstate NI","100","20","120"],
                        ["000002","May Jones","200","40","240"],
                        ["000003","Alison Smyth","300","60","360"],
                        ["000004","Albert Jones","400","80","480"],
                        ["000005","Andrew White","500","100","600"],
                        ["000006","Peter Brown","600","120","720"]
                       ]
                    );

columnCounter =0;
for row in listOrders:
    # Loop over columns.
    for column in row:
        print(column, end="");
    print(end="\n");

