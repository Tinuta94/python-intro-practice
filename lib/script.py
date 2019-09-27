from capitals import states
import random
​
print ("Welcome, ready to test your knowledge of state capitals?")
​
random.shuffle(states)
​
for state in states:
    state["Correct"] = 0
    state["Incorrect"] = 0
​
def play():
    for state in states:
        print ("What is the capital of {}?".format(state['name']))
        if input() == state["capital"]:
            print('Correct!')
            state["Correct"] += 1
        else:
            print("Wrong!")
            state["Incorrect"] += 1
        print("Correct: {}".format(state["Correct"]))
        print("Incorrect: {}".format(state["Incorrect"]))
    print ("Would you like to play again? y/n")
    if input() == "y":
        play()
    else:
        None
​
play()