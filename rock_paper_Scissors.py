#This Program is about Playing Rock Paper Scissors
#Rock beats Scissors
#Scissors beats paper
#Paper beats Rock
'''
"Note: Rich is python library for rich text and beautiful formatting in the terminal.


'''
import random 
from rich import print as rprint

if __name__ == "__main__":
    choices = ["r", "p", "s"]
    
    chance = 3
    no_of_chance = 0
    bot_point = 0
    human_point = 0
    
    print("Welcome to the rock, paper & scissors Game")
    rprint("[grey]r[/grey] for Rock, [white]p[/white] for paper, [green]s[/green] for scissor\n"
    )
    
    #making the game in while
    while no_of_chance < chance:
        user_choice = input("Enter your choice >> ")
        bot_choice = random.choice(choices)
        
        if user_choice.lower() not in choices:
            rprint("[red]wrong input!![/red] \n")
        elif user_choice == bot_choice:
            rprint("Tie!! 0 point achieved \n ")
        else:
            if user_choice.lower() == "r":
                if bot_choice == "p":
                    bot_point += 1
                    Winner = "bot"
                elif bot_choice == "s":
                    human_point += 1
                    Winner = "you win!!!!"
            elif user_choice.lower() == "p":
                if bot_choice == "r":
                    human_point += 1
                    Winner = "you win!!!!"
                elif bot_choice == "s":
                    bot_point += 1
                    Winner = "bot"
            elif user_choice.lower() == "s":
                if bot_choice == "r":
                    bot_point += 1
                    Winner = "bot"
                elif bot_choice == "p":
                    human_point += 1
                    Winner = "you win!!!!"
            rprint(
                f"You guessed [grey]{user_choice.lower()}[/grey] and bot guessed [cyan]{bot_choice}.[/cyan]\n"
            )
            rprint(
                f"[{'green' if Winner == 'Human' else 'red'}]{Winner} wins 1 point[/{'green' if Winner == 'Human' else 'red'}] \n"
            )

        no_of_chance += 1
        rprint(f"{chance - no_of_chance} chance(s) are left out of {chance} chances.\n")

    print("Game over!")

    if bot_point == human_point:
        rprint("[yellow]Tie![/yellow]")

    elif bot_point > human_point:
        rprint("[red]bot won and you lost.[/red]")

    else:
        rprint("[green]You won and bot lost.[/green]")

    rprint(
        f"[green]Your points: {human_point}\tComputer points: {bot_point}[/green]"
    )