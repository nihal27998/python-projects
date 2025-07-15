import random

# ✅ Dictionary of country: capital pairs
quiz_data = {
    "India": "New Delhi",
    "Germany": "Berlin",
    "France": "Paris",
    "Japan": "Tokyo",
    "USA": "Washington D.C.",
    "Russia": "Moscow",
    "China": "Beijing",
    "Brazil": "Brasilia",
    "Canada": "Ottawa",
    "Australia": "Canberra"
}

print("🌍 Welcome to the Country-Capital Quiz Game! 🎉")
score = 0

# Ask 5 random questions
for i in range(5):
    country = random.choice(list(quiz_data.keys()))
    answer = input(f"{i+1}. What is the capital of {country}? ").strip().lower()
    
    if answer == quiz_data[country].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {quiz_data[country]}.\n")

print(f"🎯 You scored {score} out of 5.")
if score == 5:
    print("🏆 Excellent! You're a geography champ! 🌟")
elif score >= 3:
    print("👍 Good job! Keep practicing!")
else:
    print("📚 Don't worry, try again to improve!")

