"""This program is basically an madlibs game, nothing more and nothing less."""

# Here you actually have to replace %s with {} because we are using Python 3
STORY = ("This morning I woke up and felt {} because {} was going"
         " to finally {} over the big {} {}. On the other side of the {}"
         " were many {}s protesting to keep {} in stores. The crowd bega"
         "n to {} to the rhythm of the {}, which made all of the {}s ver"
         "y {}. {} tried to {} into the sewers and found {} rats. Needi"
         "ng help, {} quickly called {}. {} appeared and saved {} by fly"
         "ing to {} and dropping {} into a puddle of {}. {} then fell "
         "asleep and woke up in the year {}, in a world where {}s ruled "
         "the world.")



def welcome():
    """ Define our welcome stuff and add anymore welcomes you would have"""
    print("Welcome to the Mad Libs game!")
    print("I'm your host, killer keemstar, and let's get riiiiiiiiii" +
          "iiiiiiiiiiiight into the libs!")



def input_variables():
    """ This function is for our input variables, and having it in a function
    can be a bit more aesthetically pleasing"""
    # Surprise! It's arrays again, lol
    libs = []
    name = input("Enter a name here!")
    print("Enter three adjectives, separated by the enter key.")
    adj1 = input("Adjective 1: ")
    adj2 = input("Adjective 2: ")
    adj3 = input("Adjective 3: ")
    print("Enter three verbs, also separated by the enter key.")
    verb1 = input("Verb 1: ")
    verb2 = input("Verb 2: ")
    verb3 = input("Verb 3: ")
    print("Please enter four nouns now.")
    noun1 = input("Noun 1: ")
    noun2 = input("Noun 2: ")
    noun3 = input("Noun 3: ")
    noun4 = input("Noun 4: ")
    print("Please enter the following items when prompted.")
    animal = input("Animal: ")
    food = input("Food: ")
    fruit = input("Fruit: ")
    number = input("Number: ")
    superhero = input("Superhero: ")
    country = input("Country: ")
    dessert = input("Dessert: ")
    year = input("Year: ")
    # I am currently inserting the values into the array here
    libs.insert(0, adj1)
    libs.insert(1, name)
    libs.insert(2, verb1)
    libs.insert(3, adj2)
    libs.insert(4, noun1)
    libs.insert(5, noun2)
    libs.insert(6, animal)
    libs.insert(7, food)
    libs.insert(8, verb2)
    libs.insert(9, noun3)
    libs.insert(10, fruit)
    libs.insert(11, adj3)
    libs.insert(12, name)
    libs.insert(13, verb3)
    libs.insert(14, number)
    libs.insert(15, name)
    libs.insert(16, superhero)
    libs.insert(17, superhero.capitalize())
    libs.insert(18, name)
    libs.insert(19, country)
    libs.insert(20, name)
    libs.insert(21, dessert)
    libs.insert(22, name)
    libs.insert(23, year)
    libs.insert(24, noun4)
    return libs


# Run the welcome function here
welcome()

""" Set the value of a new variable known as "libs" equal to the value that is
    returned from the input_variables function"""
libs = input_variables()

""" Notice how it looks better if I instead just use the index of whatever thing
    I need"""
# Switch the percent for a simple .format and it works beautifully!
print(STORY.format(libs[0], libs[1], libs[2], libs[3], libs[4], libs[5],
                   libs[6], libs[7], libs[8], libs[9], libs[10], libs[11],
                   libs[12], libs[13], libs[14], libs[15], libs[16], libs[17],
                   libs[18], libs[19], libs[20], libs[21], libs[22], libs[23],
                   libs[24]))
