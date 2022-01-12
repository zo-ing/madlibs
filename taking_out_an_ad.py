#==============================
#This is a simple chatbot project created by Zoraida Ingles

#This iteration uses a function definition to print out the story
#The story is in regards to taking out an ad in a newspaper or similar widely distributed artifact, for a small creature

#Created on: 11/01/2022
#Last updated on: 11/01/2022
#==============================

#Information for the user

greeting = "Welcome to the Madlibs chatbot! \nThe Madlibs chatbot will take your input and craft a story."

print(greeting)

#Madlibs will begin
noun1 = input("Add a noun: ")
adjective1 = input("Add an adjective: ")
adjective2 = input("Add another adjective: ")
celebrity = input("Name a celebrity: ")
adjective3 = input("Add an adjective: ")
body_part_of_animal = input("Add a body part of an animal: ")
clothing = input("Add a piece of clothing: ")
verb1 = input("Add a verb: ")
place = input("Add a place/location: ")
adjective4 = input("Add an adjective: ")
plural_noun = input("Add a plural noun: ")
noun3 = input("Add a noun: ")
number = input("What's your favorite number? ")

#Storytime
def madlibs():
    title = "Taking Out An Ad"
    story = "Must love " + noun1 + " — " + adjective1 + ", " + adjective2 + ", mother of twelve (of no relation to " + celebrity + "). Some describe me as mousey, I prefer petite and " + adjective3 + " with a pointy " + body_part_of_animal + ". Don your own fur " + clothing + ", and let's take a long " + verb1 + ", through " + place + ". Must be an " + adjective4 + " climber, and have a strong dislike for " + plural_noun + ". Send a recent " + noun3 + " and a note. " + number

    print(title)
    print(story)

madlibs()
