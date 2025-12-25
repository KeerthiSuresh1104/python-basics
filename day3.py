#1 .Add two numbers using function
def add(a, b):
     return a+b
print(add(3,5))

#2 .Find maximum of two numbers 
def maximum(a,b):
     if a>b:
       return a
     else:
       return b  
 print(maximum(10,20))

#3. check even or odd
def even_odd(n)
  if n%2==0:
    return "even"
else :
    return "odd"
  print (even_odd(8))


#LOGIC PRACTICE
#4.Find factorial using function 
def factorial(n)
  fact=1
  for i in range(1,n+1)
  fact *= i
return fact
print(factorial(4))

#5.count vowels using function 
def count_vowel(s)
   count = 0
  for ch in s:
    if ch.lower() in "aeiou":
          count += 1
      return count
print (count_vowel("keerthi"))
