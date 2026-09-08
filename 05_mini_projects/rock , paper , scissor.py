import random

choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]

Mac = random.choice(choices)
jaanvar = input("Choose: 🪨 Rock, 📄 Paper, or ✂️ Scissors: ").lower()

if jaanvar == "rock":
    jaanvar_choice = "🪨 Rock"
elif jaanvar == "paper":
    jaanvar_choice = "📄 Paper"
elif jaanvar == "scissors":
    jaanvar_choice = "✂️ Scissors"
else:
    print("❌ Invalid choice!")
    exit()

print("Jaanvar chose:", jaanvar_choice)
print("Mac choose:", Mac)

if jaanvar_choice == Mac:
    print("🤝 lawde tie ho gya!")

elif (jaanvar_choice == "🪨 Rock" and Mac == "✂️ Scissors") or \
     (jaanvar_choice == "📄 Paper" and Mac == "🪨 Rock") or \
     (jaanvar_choice == "✂️ Scissors" and Mac == "📄 Paper"):
    print("🎉 You win!")

else:
    print("😈 Mac wins!")


age = int(input(" enter your age: "))
name = "rehan"





