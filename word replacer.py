def replace_word():
    
    str = "eai mano, eu criei essa parada, será que funciona?"
    word_to_replace = input("Coloque a palavra que será substituida: ")
    word_to_replacement = input("Coloque a palavra para substituir: ")
    print(str.replace(word_to_replace, word_to_replacement))
    
replace_word()