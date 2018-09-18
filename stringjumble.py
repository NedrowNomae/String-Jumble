"""
stringjumble.py
Author: Eamon
Credit: stack overflow

Assignment:string jumble

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
def tnirp(b):
    print(b[::-1])
a = 0
#reverse the text
string = input("Please enter a string of text (the bigger the better): ")
unedit = list(string)
words = list(string)
revcor = list(string)
spaces = list(string)
idk = list(string)
n = (len(string))
a = n
b = 0
m = 0
print(a)
for j in range(1, n + 1):
    if words[j-1] != " ":
        spaces[j-1] = m
        m = m + 1
    else:
        m = 0
for p in range(1, n + 1):
    if spaces[p-1] == " ":
        idk[b] = p-1
        b = b+1
    else:
        revcor[p-1]
for q in range(1,n):
    if idk[q-1] == range(0, 1000000):
        for z in range(q,n-q):
            revcor[z] = unedit[n-z]
print(spaces)
print(revcor)
print(idk)



print("You entered " + str(string) +". Now jumble it:")
tnirp(string)


