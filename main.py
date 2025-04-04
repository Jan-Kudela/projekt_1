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


#users = ["bob", "ann", "mike", "liz"]
#passwords = ["123", "pass123", "password123", "pass123"]
registered = {"bob": "123", "ann": "pass123",
               "mike": "password123", "liz": "pass123"}

username = input("username: ")

if username not in registered:
    print("Wrong user name.") 
    quit()

user_password = input("password: ")
print("-" * 40)


if registered.get(username) == user_password:
    print(f"Welcome to the app, {username}.")

    print("We have 3 texts to be analyzed.")
    print("-" * 40)
    text_numbers = ["1", "2", "3"]
    choosen_number = (input("Enter a number btw. 1 and 3 to select: "))
    print("-" * 40)
    
    if choosen_number not in text_numbers:
        print("You are out of range or you didn´t write a number.")
    else:
        choosen_number = int(choosen_number)

        choosen_text = TEXTS[choosen_number - 1]

        one_line = choosen_text.replace("\n","" )
        one_line = one_line.replace("    "," ")
        one_line_clear = one_line.replace(".","")
        one_line_clear = one_line_clear.replace(",","")
        one_line_clear = one_line_clear.replace("-"," ")
        choosen_text_list = one_line_clear.split(" ")

        print(
            f"There are {len(choosen_text_list)} words in the selected text.")


        first_upper = [] 
        for upper in choosen_text_list:
            if upper[0].isupper() and upper[1].islower():
                first_upper.append(upper)

        print(f"There are {len(first_upper)} titlecase words.")


        all_upper = [] 
        for all in choosen_text_list:
            if all[-1].isupper():
                all_upper.append(all)

        print(f"There are {len(all_upper)} uppercase words.")


        numbers = []
        for num in choosen_text_list:
            if num.isdigit():
                numbers.append(num)

        smaller = len(choosen_text_list) - len(
            first_upper) - len(all_upper) - len(numbers)

        print(f"There are {smaller} lowercase words.")
        print(f"There are {len(numbers)} numeric strings.")

        numbers_int = []
        for nr in range(0,len(numbers)):
            numbers_int.append(int(numbers[nr]))


        suma = sum(numbers_int)
        print(f"The sum of all the numbers is {suma}.")
        print("-" * 40)
        print("LEN|    OCCURENCES    |NR.")
        print("-" * 40)

# úprava¨
        lenght_words = {}
        for word in choosen_text_list:
            lenght = len(word)
            if lenght in lenght_words:
                lenght_words[lenght] += 1
            else:
                lenght_words[lenght] = 1

        #print(lenght_words)

        lenght_sorted = sorted(lenght_words.items())
        #print(lenght_sorted)

        for graf in range(0,len(lenght_sorted)):
            if lenght_sorted[graf][0] < 10:
                print(
                    f"  {lenght_sorted[graf][0]}|{lenght_sorted[graf][1] * '*'}{(18 - lenght_sorted[graf][1]) * ' '}|{lenght_sorted[graf][1]}")
            else:
                print(
                    f" {lenght_sorted[graf][0]}|{lenght_sorted[graf][1] * '*'}{(18 - lenght_sorted[graf][1]) * ' '}|{lenght_sorted[graf][1]}")    


        print("-" * 40)

  
else:
    print("You are not registered.")
 
