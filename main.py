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


users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

username = input("username: ")

if username in users:
    user_password = input("password: ")
    print("-" * 40)
    if user_password not in passwords:
        print("Wrong password.")
    
    elif users.index(username) == passwords.index(
        user_password) or username == "liz" and user_password == "pass123":
        print(f"Welcome to the app, {username}")

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

            print(f"There are {len(choosen_text_list)} words in the selected text.")


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

            smaller = len(choosen_text_list) - len(first_upper) - len(all_upper) - len(numbers)

            print(f"There are {smaller} lowercase words.")
            print(f"There are {len(numbers)} numeric strings.")

            numbers_int = []
            for nr in range(0,len(numbers)):
                numbers_int.append(int(numbers[nr]))


            suma = sum(numbers_int)
            print(f"The sum of all the numbers is {suma}.")
            print("-" * 40)
            print("LEN|    OCCURENCES    |NR.")


            lenght_1 = []
            for x1 in choosen_text_list:
                if len(x1) == 1:
                    lenght_1.append(x1)

            lenght_2 = []
            for x2 in choosen_text_list:
                if len(x2) == 2:
                    lenght_2.append(x2)
            
            lenght_3 = []
            for x3 in choosen_text_list:
                if len(x3) == 3:
                    lenght_3.append(x3)
            
            lenght_4 = []
            for x4 in choosen_text_list:
                if len(x4) == 4:
                    lenght_4.append(x4)
            
            lenght_5 = []
            for x5 in choosen_text_list:
                if len(x5) == 5:
                    lenght_5.append(x5)
            
            lenght_6 = []
            for x6 in choosen_text_list:
                if len(x6) == 6:
                    lenght_6.append(x6)

            lenght_7 = []
            for x7 in choosen_text_list:
                if len(x7) == 7:
                    lenght_7.append(x7)

            lenght_8 = []
            for x8 in choosen_text_list:
                if len(x8) == 8:
                    lenght_8.append(x8)

            lenght_9 = []
            for x9 in choosen_text_list:
                if len(x9) == 9:
                    lenght_9.append(x9)
        
            lenght_10 = []
            for x10 in choosen_text_list:
                if len(x10) == 10:
                    lenght_10.append(x10)
                
            lenght_11 = []
            for x11 in choosen_text_list:
                if len(x11) == 11:
                    lenght_11.append(x11)
            
            lenght_12 = []
            for x12 in choosen_text_list:
                if len(x12) == 12:
                    lenght_12.append(x12)

            print("-" * 40)
            if len(lenght_1) != 0:
                print(f" 1| {len(lenght_1) * '*'} {(17 - len(lenght_1)) * " "}|{len(lenght_1)}")
            if len(lenght_2) != 0:
                print(f" 2| {len(lenght_2) * '*'} {(17 - len(lenght_2)) * " "}|{len(lenght_2)}")
            if len(lenght_3) != 0:
                print(f" 3| {len(lenght_3) * '*'} {(17 - len(lenght_3)) * " "}|{len(lenght_3)}")
            if len(lenght_4) != 0:
                print(f" 4| {len(lenght_4) * '*'} {(17 - len(lenght_4)) * " "}|{len(lenght_4)}")
            if len(lenght_5) != 0:
                print(f" 5| {len(lenght_5) * '*'} {(17 - len(lenght_5)) * " "}|{len(lenght_5)}")
            if len(lenght_6) != 0:
                print(f" 6| {len(lenght_6) * '*'} {(17 - len(lenght_6)) * " "}|{len(lenght_6)}")
            if len(lenght_7) != 0:
                print(f" 7| {len(lenght_7) * '*'} {(17 - len(lenght_7)) * " "}|{len(lenght_7)}")
            if len(lenght_8) != 0:
                print(f" 8| {len(lenght_8) * '*'} {(17 - len(lenght_8)) * " "}|{len(lenght_8)}")
            if len(lenght_9) != 0:
                print(f" 9| {len(lenght_9) * '*'} {(17 - len(lenght_9)) * " "}|{len(lenght_9)}")
            if len(lenght_10) != 0:
                print(f"10| {len(lenght_10) * '*'} {(17 - len(lenght_10)) * " "}|{len(lenght_10)}")
            if len(lenght_11) != 0:
                print(f"11| {len(lenght_11) * '*'} {(17 - len(lenght_11)) * " "}|{len(lenght_11)}")
            if len(lenght_12) != 0:
                print(f"12| {len(lenght_12) * '*'} {(17 - len(lenght_12)) * " "}|{len(lenght_12)}")
    else:
        print("Wrong password.")
else:
    print("You are not registered.")
 
