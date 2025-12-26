#STRING PRACTICE
name = "Keerthi S"

print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("S","student"))
print(name[0:4])
print(name[::-1])


#LIST PRACTICE
marks=[78,85,90,66,88]
print(marks)
print(len(marks))
marks.append(94)
print(marks)
marks.remove(66)
print(marks)
print(marks[1:4]
print(marks[::-1])

#LOGIC PRACTICE

#count vowels in the string
text="python programing"
count=0

for ch in text.lower():
      if ch in "aeiou":
        count +=1
print("vowel count:",count)


#Find largest number in a list 

nums=[23,56,78,90]
largest=num[0]

for n in nums:
  if n>largest:
    largest=n
print("largest number:",largest)
