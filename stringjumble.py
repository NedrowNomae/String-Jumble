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
string = " " + input("Please enter a string of text (the bigger the better): ")
unedit = list(string)
revcor = list(string)
print(unedit)

n = (len(unedit))
u = 0
for b in range(0,n-1):
    if unedit[b] == ' ':
        u = u + 1

e = 0
list = [s for s in range(0,u)]
for q in range(0,n-1):
    if unedit[q] == ' ':
        list[e] = q
        e = e + 1
spaces = list[:]
w = len(spaces)

spaces.append(n)
for t in range(1,w+1):
    revcor[[n-spaces[t-1]:n-spaces[t]] = unedit[spaces[t-1]:spaces[t]]
print("revcor: " + str(revcor))
#for t in range(0,w):
    #list[n-spaces[t]] = unedit[0:spaces[t]]
    #print(unedit[0:spaces[t]])
    
#print(n)
#print(u)
print("spaces: " + str(spaces))
#print("revcor: " + str(revcor))
#print(idk)
print("unedit: " + str(unedit))


#print("You entered " + str(string) +". Now jumble it:")
#tnirp(string)


