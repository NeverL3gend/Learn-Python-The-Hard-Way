################################################################################
#Prompting and Passing
################################################################################
from sys import argv
script, user_name = argv
prompt = '> ' #this is our variable prompt

print(f"Hi {user_name}, I'm the {script} script.")
# once we type in powershell the literals will be filled in with a new value
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# this will fill in our name once we type it in powershell
likes = input(prompt)
# we will provide a answer to the question

print(f"Where do you live {user_name}?")
# once that question is asked we will ask another one
lives = input(prompt)
#enter our location here, then move to the next question

print("what kind of computer do you have?")
# ask another question after the previous question was asked
computer = input(prompt)
# enter our response here of what type of computer we have

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
 """)
 # all the answers that we applied to the question before will be filled in here
 
