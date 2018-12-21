#This code calculate the twelve numbers of the fibonacci's series.
#NAME: Carlos Augusto Pérez Méndez.
#Job position: Debug technician at Flextronics.
#Carrer: Mechatronics Engineer.
#Email: mendezd.carlos@gmail.com
#Fibonacci series is calculated as follow way:
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
#   .
#   .
#   .
# 8 + 5 = 13
##########################################################################
#
#Start######################

x = 0
y = 1
z = 0

print (x, y)           #In this line is printed the two numbers by default (0, 1) 
                       #of the Fibonacci's succession.
for i in range (10):   # Calculate of Fibonacci's sucession. 
    z = x + y          # Note: The loop calculate from 0 to 10 numbers of Fibonacci. However, add the two numbers by default, and for this reason in total are 12.
    x = y
    y = z
    print (z)

#End.
