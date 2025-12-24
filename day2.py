#program 1 :if-else loop
num=int(input("enter a number : "))
if num%2==0:
   print("even")
else:
  print("odd")


#program 2: for loop
num=int(input("enter the number:"))
total = 0
for i in range (1,n+1): 
  total +=i
  print("sum = " total)

#program 3:while loop
num= int(input("enter a number:"))
fact=1
i=1
while i <= num:
    fact *= i
    i += 1
  print("factorial =", fact)
