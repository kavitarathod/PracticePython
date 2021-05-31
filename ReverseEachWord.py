str = "Hello World"

word = str.split(" ")
print(word)
rev = ""
for i in word:
    rev = rev + i[::-1]+" "

print(rev)