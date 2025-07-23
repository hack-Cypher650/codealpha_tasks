import random
count=6
dash=7
words=('eardrums','fabulous','macaroni','leveling','vacation')
word=random.choice(words)
letter1=random.choice(word)
i=word.index(letter1)
game=''
for j in range(len(word)):
    if j == i:
        game += letter1
    else:
        game += '_'
while True:
    print(f"Number of incorrect attempts left:{count}")
    print(game)
    l=input("Enter letter\n")
    I=int(input("Enter Index(0-7)\n"))
    if word[I]==l:
        print("Correct!")
        game=game[:I] + l + game[I+1:]
        dash -=1
    else:
        print("Sorry!")
        count -=1
    if dash==0:
        print("CONGRATULATIONS!")
        break
    elif count==0:
        print("GAME OVER:(")
        break