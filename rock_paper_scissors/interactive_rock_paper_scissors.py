import tkinter as tk
from tkinter import messagebox
import random
from rich import print as rprint

def play(user_choice):
    global bot_point, human_point, no_of_chance

    bot_choice = random.choice(choices)

    if user_choice not in choices:
        rprint("[red]Wrong input!![/red] \n")
    elif user_choice == bot_choice:
        rprint("Tie!! 0 points achieved \n")
        messagebox.showinfo("Result", "It's a Tie!")
    else:
        if user_choice == "r":
            if bot_choice == "p":
                bot_point += 1
                winner = "bot"
            elif bot_choice == "s":
                human_point += 1
                winner = "you"
        elif user_choice == "p":
            if bot_choice == "r":
                human_point += 1
                winner = "you"
            elif bot_choice == "s":
                bot_point += 1
                winner = "bot"
        elif user_choice == "s":
            if bot_choice == "r":
                bot_point += 1
                winner = "bot"
            elif bot_choice == "p":
                human_point += 1
                winner = "you"

        result_text = f"You chose {user_choice.upper()} and the bot chose {bot_choice.upper()}. {winner.capitalize()} wins this round!"
        rprint(result_text)
        messagebox.showinfo("Result", result_text)

    no_of_chance += 1
    if no_of_chance >= chance:
        game_over()

    update_status()

def update_status():
    status_text.set(f"Chances left: {chance - no_of_chance}\nYour points: {human_point}\nBot points: {bot_point}")

def game_over():
    if bot_point == human_point:
        rprint("[yellow]Tie![/yellow]")
        messagebox.showinfo("Game Over", "It's a Tie!")
    elif bot_point > human_point:
        rprint("[red]Bot won and you lost.[/red]")
        messagebox.showinfo("Game Over", "Bot won and you lost.")
    else:
        rprint("[green]You won and bot lost.[/green]")
        messagebox.showinfo("Game Over", "You won and bot lost.")

    reset_game()

def reset_game():
    global bot_point, human_point, no_of_chance
    bot_point = 0
    human_point = 0
    no_of_chance = 0
    update_status()

if __name__ == "__main__":
    choices = ["r", "p", "s"]
    chance = 3
    no_of_chance = 0
    bot_point = 0
    human_point = 0

    # Initialize the GUI application
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")

    status_text = tk.StringVar()
    status_text.set(f"Chances left: {chance - no_of_chance}\nYour points: {human_point}\nBot points: {bot_point}")

    # GUI Elements
    instructions = tk.Label(root, text="Choose: r for Rock, p for Paper, s for Scissors")
    instructions.pack()

    rock_button = tk.Button(root, text="Rock (r)", command=lambda: play("r"))
    rock_button.pack()

    paper_button = tk.Button(root, text="Paper (p)", command=lambda: play("p"))
    paper_button.pack()

    scissors_button = tk.Button(root, text="Scissors (s)", command=lambda: play("s"))
    scissors_button.pack()

    status_label = tk.Label(root, textvariable=status_text)
    status_label.pack()

    reset_button = tk.Button(root, text="Reset Game", command=reset_game)
    reset_button.pack()

    # Start the GUI event loop
    root.mainloop()
