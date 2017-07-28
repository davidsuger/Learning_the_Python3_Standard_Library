# Random Module
import random

# Random Numbers
print(random.random())
decider = random.randrange(2)
print(decider)
if decider == 0:
    print("Heads")
else:
    print("Tails")
    
print("You rolled a", random.randrange(1,7))

# Random Choices
lotteryWinners = random.sample(range(100),5)
print(lotteryWinners)

print(random.sample((1,2,3,45,5),3))
print(random.sample([1,2,3,45,5],3))

possiblePets = ["cat","dog","fish"]
print(random.choice(possiblePets))
print(random.sample(possiblePets,1))

cards = ["Jark","Queen","King","Ace"]
random.shuffle(cards)
print(cards)