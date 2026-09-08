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

# SCORE BOARD
if jaanvar_choice == Mac:
    jaanvar_score = 0
    mac_score = 0

elif (jaanvar_choice == "🪨 Rock" and Mac == "✂️ Scissors") or \
     (jaanvar_choice == "📄 Paper" and Mac == "🪨 Rock") or \
     (jaanvar_choice == "✂️ Scissors" and Mac == "📄 Paper"):
    jaanvar_score = 1
    mac_score = 0

else:
    jaanvar_score = 0
    mac_score = 1

print("\n🏆 ===== SCORE BOARD =====")
print("👤 Jaanvar:", jaanvar_score)
print("💻 Mac:", mac_score)



