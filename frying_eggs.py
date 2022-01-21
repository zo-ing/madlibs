#==============================
#This is a simple chatbot project created by Zoraida Ingles

#This iteration uses a function with parameters to replace adjectives, nouns, etc.
#It's not a true Madlib in that it takes user-input for some outputs.
#I wanted to play with a different format for gathering user-input and automation
#Instead of a story, this is a tutorial on frying a sunny side egg

#Created on: 20/01/2022
#Last updated on: 21/01/2022
#==============================

#Madlibs will begin
def intro():
    greeting = "Welcome to the Madlibs chatbot! \nThis version provides instructions on frying a sunny side egg.\n"
    title = "How to Fry A Sunny Side Egg\n"

    print(greeting)
    print(title)

def step_one():
    number = input("Add a number: ")
    adjective = input("Add an adjective: ")

    step_one = "Step one: Gather you need\n You will need a frying pan, " + number + " eggs, oil or butter, and a " + adjective + " stove.\n"

    print(step_one)

def step_two(heat, number):
    step_two = "Turn on your stove and set to " + heat + " heat. Add " + number + " tablespoons of your oil or butter. Then wait until the oil or butter is heated.\n"

    print(step_two)

def step_three():
    adjective = input("Add an adjective: ")
    sound = input("Add a sound: ")
    kitchen_utensil = input("Name a kitchen utensil: ")
    verb = input("Name a verb: ")

    step_three = "Once your oil is hot enough, add your eggs. You will hear a " + adjective + " " + sound + " as your egg(s) cook. During this time, take a " + kitchen_utensil + " and with a scooping motion, pick up the hot oil and " + verb + " it over the egg(s).\n"

    print(step_three)

def step_four(emotion, measure_of_time):
    step_four = "Watch with " + emotion + " as the sides of your egg(s) crisp. Continue the scooping motion with the hot oil until the yolk appears cooked.\n"
    option = "For runnier egg(s): Turn off heat and let sit on the stove for 30 " + measure_of_time

    print(step_four)
    print(option)

def final_step():
    kitchen_utensil = input("Name a kitchen utensil: ")
    condiment1 = input("Name a condiment: ")
    condiment2 = input("Name another condiment: ")
    food = input("What's your favorite food? ")

    final_step = "Finally, with a " + kitchen_utensil + " remove your egg(s) from the pan and plate.\n"
    garnish = "Serve with a dash of " + condiment1 + " and " + condiment2 + ". You may even eat your egg(s) with a slice of " + food + " for a tastier meal."

    print(final_step)
    print(garnish)
    print("Bon appetit!")

intro()
step_one()
step_two("scorching hot", "20")
step_three()
step_four("festering enthusiasm", "lightyears")
final_step()
