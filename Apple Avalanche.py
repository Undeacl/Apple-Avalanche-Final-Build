import turtle as trtl
from Apple import Apple
import random as rand
import string

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
alphabet = list(string.ascii_uppercase)

#list to store all apple generated
generated_apple = []
clear_apple = []

total = 5

#apple dictionary
apple = {}

#-----functions-----#

#create the apple
def create_apple():

    global total
    apples = 0

    cordinate = [rand.randint(150, 200), rand.randint(20, 50), rand.randint(-200, -100), rand.randint(10, 30), 
                rand.randint(-90, -50), rand.randint(0, 120), rand.randint(50, 70), rand.randint(40, 100), 
                rand.randint(-20, 10), rand.randint(30, 150)]

    while apples < total:

        #generates a random number to identify the apple
        number = rand.randint(0, 25)
        
        if number in generated_apple:
            number = rand.randint(0, 25)

        #number has not been generated, create the apple
        else:

            index = 0

            #adding the apple into the dictionary with its definition

            apple["apple" + alphabet[number]] = Apple(cordinate[index], cordinate[index+1], alphabet[number]) 
                    
            #use the dictionary to display the apple and letter
            apple["apple" + alphabet[number]].draw_apple_and_letter()

            generated_apple.append(number)
            clear_apple.append(number)

            apples += 1

            to_remove = [cordinate[0], cordinate[1]]

            # Removing elements
            for item in to_remove:
                if item in cordinate:
                    cordinate.remove(item)
    
    key_pressed()

#call on the specific apple to make it fall
def make_apple_fall(letter):
    apple["apple" + letter].fall()
    generated_apple.remove(alphabet.index(letter))

    #if list is empty, reset the apple
    if not generated_apple:
        wn.ontimer(reset, 1000)

#reset everything
def reset():
    for number in clear_apple:
        apple["apple" + alphabet[number]].reset_all()
    apple.clear()
    generated_apple.clear()
    clear_apple.clear()
    create_apple()

#binding key presses to make apples fall
def key_pressed():
    for number in generated_apple:
        #check both lower and upper case letter
        wn.onkeypress(lambda l=alphabet[number]: make_apple_fall(l), alphabet[number].lower()) 
        wn.onkeypress(lambda l=alphabet[number]: make_apple_fall(l), alphabet[number].upper())
        wn.listen()

#-----function calls-----
create_apple()

wn.mainloop()