import random
from capitals import states

def play_game():
    random.shuffle(states)
    correct_answers = 0
    total_answers = 0
    
    print("Welcome to the State Capitals Game!")
    print("You will be given the name of a state, and you must guess its capital.")
    print("Type 'exit' at any time to end the game.\n")
    
    for state in states:
        capital = state["capital"]
        answer = input(f"What is the capital of {state['name']}? ").strip().title()
        
        if answer.lower() == 'exit':
            break
        
        total_answers += 1
        if answer == capital:
            correct_answers += 1
            print("Correct!")
        else:
            print(f"Sorry, the capital of {state['name']} is {capital}.")
        
        print(f"Score: {correct_answers}/{total_answers}\n")
    
    print("Game Over!")
    print(f"Your final score is: {correct_answers}/{total_answers}")
    play_again = input("Would you like to play again? (yes/no) ").strip().lower()
    
    if play_again == 'yes':
        play_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
