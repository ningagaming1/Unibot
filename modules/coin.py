from random import choice

def handle(user_inut,user_data):
    output_set = ("Heads","Tails")
    result = choice(output_set)
    print(f"{result} is the result to the coin toss.")