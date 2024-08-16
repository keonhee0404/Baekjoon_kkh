word=input()
alphabet='abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    index=word.find(letter)
    print(index,end=' ')