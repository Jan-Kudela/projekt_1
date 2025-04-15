"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgenr@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


registered = {
    "bob": "123", 
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

separator = "-" * 40
username = input("username: ")

if username not in registered:
    print("Wrong user name, terminating the program.") 
    quit()

user_password = input("password: ")
print(separator)


if registered.get(username) == user_password:
    print(f"Welcome to the app, {username.title()}.")

    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(separator)
    text_numbers = range(1,len(TEXTS)+1)
    choosen_number = (
        input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
    )
    print(separator)

    if choosen_number.isdigit() is False:
        print("You do not enter a number.\nTerminating Program.")
        quit()
    else:
        choosen_number = int(choosen_number)
        if choosen_number not in text_numbers:
            print(
                f"You are out of range 1 to {len(TEXTS)}. "
                f"Terminating the program."
            )
            quit()
        else:
            choosen_text = TEXTS[choosen_number - 1]

            one_line = choosen_text.replace(
                "\n","" ).replace("    "," ").replace(".","").replace(
                ",","").replace("-"," "
            )

            choosen_text_list = one_line.split(" ")
         
            print(
                f"There are {len(choosen_text_list)} "
                f"words in the selected text."
            )


        title = []
        upper = []
        lower = []
        numbers = []
        
        for word in choosen_text_list:
            if word.istitle():
                title.append(word)
            elif word.isupper():  
                upper.append(word)  
            elif word.islower():  
                lower.append(word)   
            else:   
                numbers.append(word)
                
        print(f"There are {len(title)} titlecase words.")
        print(f"There are {len(upper)} titlecase words.")
        print(f"There are {len(lower)} lowercase words.")
        print(f"There are {len(numbers)} numeric strings.")

        
        numbers_int = []
        for nr in range(0,len(numbers)):
            numbers_int.append(int(numbers[nr]))

        suma = sum(numbers_int)
        print(f"The sum of all the numbers is {suma}.")
        
        print(separator)
        print("LEN|    OCCURENCES    |NR.")
        print(separator)


        lenght_words = {}
        for word in choosen_text_list:
            lenght = len(word)
            if lenght in lenght_words:
                lenght_words[lenght] += 1
            else:
                lenght_words[lenght] = 1

        
        lenght_sorted = sorted(lenght_words.items())
        for graf in range(0,len(lenght_sorted)):
            if lenght_sorted[graf][0] < 10:
                print(
                    f"  {lenght_sorted[graf][0]}|"
                    f"{lenght_sorted[graf][1] * '*'}"
                    f"{(18 - lenght_sorted[graf][1]) * ' '}|"
                    f"{lenght_sorted[graf][1]}"
                )
            else:
                print(
                    f" {lenght_sorted[graf][0]}|"
                    f"{lenght_sorted[graf][1] * '*'}"
                    f"{(18 - lenght_sorted[graf][1]) * ' '}|"
                    f"{lenght_sorted[graf][1]}"
                )    
        
        print(separator)

else:
    print("You are not registered, terminating the program.")
 
