import random
from art import logo
from game_data import data

print(logo)

#formate the acount data into printable formate
def format_data(account):
  account_name = account["name"]
  account_discription = account["description"]
  account_country = account["country"]
  return(f" {account_name}, is a {account_discription}, from {account_country}.")


##use if statement if user is correct
def check_answer(user_guess, a_followers, b_followers):
  if a_followers > b_followers:
    return user_guess == "a"
  else :
    return user_guess == "b"  


score = 0 # keep the  track of socre 
play_game = True #make the game repeatable

#convert account A into account B when user guess is correct.
account_b = random.choice(data)#generate a random account from game data

while play_game:

  #generate a random account from game data
  #convert account A into account B when user guess is correct.
  account_a = account_b 
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A : {format_data(account_a)}. ")

  logo_2 = r"""
      
  \ \   / /__   
  \ \ / / __|  
    \ V /\__ \_ 
    \_/ |___(_)

  """

  print(logo_2)

  print(f"Against B : {format_data(account_b)}. ")

  #ask user for a guess

  guess = input("Who has more follower A 0r B? ").lower()
  

  #check if user is correct
  ##get follower count of each acoount
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  #give user feedback on their guess

  if is_correct:
    score += 1 # keep the  track of socre 
    print(f"You are right! and current score is {score} ")
  else:
    print(f"Sorry! You are worng. And final score is {score} ")  
    play_game = False #make the game repeatable
