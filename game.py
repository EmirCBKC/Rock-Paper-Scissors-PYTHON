import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game_images=[rock,paper,scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")
choose=int(input("Your turn?\n"))
if (choose<=-1 or choose>=3):
    print("You typed an invalid number, you lose!")
else:
    print(f"Your choose: {game_images[choose]}")
    ai=random.randint(0,2)
    print(f"Ai choose: {game_images[ai]}")

if choose==0 and ai==2:
    print(f"You: {choose}, Ai: {ai} You Win!")
elif (choose<=-1 or choose>=3):
    print("You typed an invalid number, you lose!")
elif ai>choose:
    print(f"You: {choose}, Ai: {ai} You Lose...")
elif ai==0 and choose==2:
    print(f"You: {choose}, Ai: {ai} You Lose...")
elif choose>ai:
    print(f"You: {choose}, Ai: {ai} You Win!")
elif choose==ai:
    print(f"You: {choose}, Ai: {ai} DRAW!")