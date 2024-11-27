import random
diceses= {
    "1": ("┌─────────┐",
          "│         │",
          "│    ●    │",
          "│         │",
          "└─────────┘"),
    "2":("┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘"),
    "3":("┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘"),
    "4":("┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘"),
    "5":("┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘"),
    "6":("┌─────────┐",
         "│ ●     ● │",
         "│ ●     ● │",
         "│ ●     ● │",
         "└─────────┘")
}
userInput = int(input("Enter a number between 1 and 6: "))
dices = []
total = 0
for dice in range(userInput):
    dices.append(random.randint(1,6))
    total += dices[dice]
for i in dices:
    die = diceses[str(i)]
    for di in die:
        the_dice="".join(di)
        print(the_dice)
print(f"Total : {total}")