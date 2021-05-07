# This function will ask you the number for which they want to print the table of their entered number

table = int(input('Enter the number of Table you want to Print : '))
quotation = (" x ")

print("Table of " + str(table))
twosequence = 1
twomulti = table

ab = (10 * twomulti)

while twosequence<=10 or twomulti<=ab:
    print(str(table) + str(quotation) + str(twosequence) + " = " + str(twomulti))
    twosequence = twosequence + 1
    twomulti = twomulti + table