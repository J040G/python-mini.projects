import random
import string


def gerador(min_lenght, number = True, special_characters = True):
    letter = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letter
    if number:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ""
    meets_criteria = False 
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            
        meets_criteria = True
        if number:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
            
    return pwd
        
min_lenght = int(input("Coloque a quantidade mínima de caractéres: "))
has_number = input("Você quer que tenha números (s/n)? ").lower() == "s"
has_special = input("Quer que tenha caractéres especiais (s/n)? ").lower() == "s" 
pwd = gerador(min_lenght, has_number,has_special)
print("A senha gerada é: ", pwd)