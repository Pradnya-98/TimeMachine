'''Name of module: Prime number
Date:18 feb 2021
Author: Pradnya Jadhav
Synopsis: Finding prime number within the series without using for loop'''

#prime number

#script start here

number=1
while (number <= 50):
    count = 0
    i = 2
    while (i <= number // 2):
        if(number % i ==0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and number !=1):
        print(number,end=' ')
    number = number +1

#End of script


