#Project Euler Problem #1

#Variables
sum = 0
multiples = []

#Check whether multiple of 3 or 5
for i in range(1,1000):
    if i%3 == 0:
        multiples.append(i)
    elif i%5 == 0:
        multiples.append(i)

print(multiples)

#Create sum of list of multiples
for i in multiples:
    sum += i

print(sum)
