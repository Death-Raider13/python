import tkinter as tk
import random
from PIL import Image, ImageTk

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x550")
root.configure(bg="#1e1e2f")

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

# Load and resize images
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

# Title
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Choose your move!", font=("Arial", 14), bg="#1e1e2f", fg="white")
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text="You: 0   Computer: 0", font=("Arial", 12), bg="#1e1e2f", fg="lightgreen")
score_label.pack(pady=5)

# Game logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(
        text=f"You: {user_choice}   |   Computer: {computer_choice}\n{result}"
    )

    score_label.config(
        text=f"You: {user_score}   Computer: {computer_score}"
    )

# Buttons frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

# Icon buttons
tk.Button(frame, image=rock_img, command=lambda: play("Rock"), bg="#1e1e2f", bd=0).grid(row=0, column=0, padx=15)
tk.Button(frame, image=paper_img, command=lambda: play("Paper"), bg="#1e1e2f", bd=0).grid(row=0, column=1, padx=15)
tk.Button(frame, image=scissors_img, command=lambda: play("Scissors"), bg="#1e1e2f", bd=0).grid(row=0, column=2, padx=15)

# Labels under icons
tk.Label(frame, text="Rock", bg="#1e1e2f", fg="white").grid(row=1, column=0)
tk.Label(frame, text="Paper", bg="#1e1e2f", fg="white").grid(row=1, column=1)
tk.Label(frame, text="Scissors", bg="#1e1e2f", fg="white").grid(row=1, column=2)

# Reset function
def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Choose your move!")
    score_label.config(text="You: 0   Computer: 0")

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset,
                      bg="#f44336", fg="white", font=("Arial", 10, "bold"))
reset_btn.pack(pady=10)

# Run app
root.mainloop()