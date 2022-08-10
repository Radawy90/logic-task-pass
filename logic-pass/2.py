
# write a program to find all prime numbers up to a given range of numbers ? 

lower = int(input('Enter number one'))
upper =int(input('Enter number tow'))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)








