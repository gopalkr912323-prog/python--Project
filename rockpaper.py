import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "🤝 It's a Draw!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        user_score += 1
    else:
        result = "💻 Computer Wins!"
        computer_score += 1

    user_label.config(text=f"You: {user_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=result)

    score_label.config(
        text=f"Score  You: {user_score}   Computer: {computer_score}"
    )

# Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x400")
root.configure(bg="#222222")

title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 22, "bold"),
    bg="#222222",
    fg="white"
)
title.pack(pady=15)

user_label = tk.Label(
    root,
    text="You: -",
    font=("Arial", 16),
    bg="#222222",
    fg="cyan"
)
user_label.pack()

computer_label = tk.Label(
    root,
    text="Computer: -",
    font=("Arial", 16),
    bg="#222222",
    fg="orange"
)
computer_label.pack()

result_label = tk.Label(
    root,
    text="Choose an option",
    font=("Arial", 18, "bold"),
    bg="#222222",
    fg="yellow"
)
result_label.pack(pady=20)

frame = tk.Frame(root, bg="#222222")
frame.pack()

tk.Button(
    frame,
    text="🪨 Rock",
    width=12,
    font=("Arial", 14),
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=8)

tk.Button(
    frame,
    text="📄 Paper",
    width=12,
    font=("Arial", 14),
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=8)

tk.Button(
    frame,
    text="✂️ Scissors",
    width=12,
    font=("Arial", 14),
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=8)

score_label = tk.Label(
    root,
    text="Score  You: 0   Computer: 0",
    font=("Arial", 16),
    bg="#222222",
    fg="lightgreen"
)
score_label.pack(pady=25)

root.mainloop()