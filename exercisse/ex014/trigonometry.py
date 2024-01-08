import math
import random


#hypotenuse

#a = float(input('Enter a: '))
#b = float(input('Enter b: '))
#c = math.sqrt((a**2)+(b**2)) # ou c = ((a**2)+(b**2))*0.5
#print('For a right triangle {},{} the hypotenuse is: {:.4f}'.format(a, b, #c))

#another way

#a = float(input('Enter a: '))
#b = float(input('Enter b: '))
#print('For a right triangle {},{} the hypotenuse is: {:.4f}'.format(a, b, #math.hypot(a,b)))

# ========================================================================
# sine = opposite side  / hypotenuse (SOA)
# cosine  = adjacent leg / hypotenuse (CAH)
# tagent =  sine / cosine .: opposite side / adjacent leg (TOA)
# ========================================================================

#For a right-angle triangle, its sides are i cm high and j cm wide. For alpha and beta angles, calculate your sine, cosine, tangent and hypotenuse. 
#  |a\
#  |  \
#i |   \h
#  |___b\ 
#    j

#i = float(input('Enter the height: '))
#j = float(input('Enter the width: '))
#hypo = ((i**2)+(j**2))*0.5
#aSine = (j/hypo)
#aCosine = (i/hypo)
#aTangent = (j/i)
#print('For the right-angle triangle the alpha angle its have sine {}, #cosine {} and tangent {:.2f} . \nFor the beta angle its have sine {}, #cosine {} and tangent {:.2f}'.format(j/hypo, i/hypo, j/i, i/hypo, j/hypo, #i/j))

# a = random.randint(0,360)
# print('For a {} degree angle, its sine is {:.6f}, cosine is {:.6f} and tangent is {:.6f}'.format(a, math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))

#Conditional statement of the existence of a triangle 

a = random.randint(1, 20)
b = random.randint(1, 20)
c = random.randint(1, 20)
print('A: {} \nB: {}\nC: {}'.format(a, b, c))
if (a+b > c) and (a+c > b) and (b+c > a):
    print('Triangle is possible!')
else:
    print("Triangle isn't possible")