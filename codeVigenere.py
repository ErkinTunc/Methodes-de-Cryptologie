# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:09:26 2023

@author: etboya
"""


# Les Fonctions

def creationDic(li_biblio):
    ### Il cree un dictionnaire qui contient toutes les lettres de cette li_biblio et ses index.  ###
    
    dic_Alpha = {}
    location = 0
    for i in li_biblio: # par exemple : li_biblio = "abcdefghijklmnopqrstuvwxyz"
        dic_Alpha[i] = location
        location += 1
    
    return dic_Alpha

    
def liste_decalage(message,cle,bibliotheque):
   ### Il créer une liste qui contient l'index de chaque lettre de cle(cle va avoir le meme taille avec message) ###
    
    #creation de l'alphabet
    dic_Alphabet = creationDic(bibliotheque)
    
    # creation du liste cle qui a le meme taille avec message
    li_cle = []
    i = 0 # i := index
    for x in range(0,len(message)) :   
        if i == len(cle):
            i=0
        li_cle.append(cle[i])   
    
    #initialization de liste de decalage
    li_decalage = []
    
    #affectation sur le liste de decalage
    for i in range(0,len(li_cle)):
        num =  li_cle[i]    #mettre le lettre de clé
        num = dic_Alphabet[num] #mettre le location dans l'alphabet (a=0)
        li_decalage.append(num) #ajout de location de chaque lettre
    
    return li_decalage #liste d'entier
     


def Cryptage_Vigenere(message,cle):
    ### Il chiffrer le message avec décalage de chaqu lettre grace aux index de chaque lettre de cle. ###
    
    # Bibliotheque
    li_biblio = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{é}£"""
              # ou "abcdefghijklmnopqrstuvwxyz" | si le lettre n'est pas dans le li_biblio on laissez-le inchangé
    
    # liste de décalage
    li_decalage = liste_decalage(message,cle,li_biblio)
    
    # Le taille de message
    lenthM = len(message) 
    
    # Chiffrement
    message_crypte = ""
    
    for i in range(lenthM):
        char = message[i]   # une lettre de message 
        
        if char in li_biblio:
            # Trouver l'index de character de l'alphabet
            index_en_alphabet = li_biblio.index(char)
            
            # Décalez le caractère de la valeur correspondante dans li_decalage
            index_decale = (index_en_alphabet + li_decalage[i]) % len(li_biblio) # il trouve nouveau index # on utilise le modulo(%) pour retourner au debut de alphabet
            encrypted_char = li_biblio[index_decale]  # on trouve nouveua lettre de message_crypte
            message_crypte += encrypted_char    # Ajout de lettre
            
        else:
            # Si le caractère n'est pas dans l'alphabet, laissez-le inchangé
            message_crypte += char
    
    
    return message_crypte


def Decrtyptage_Vigenere(message_crypte,cle):
    ### Décrypte le message_crypte ###
    
    # Bibliotheque
    li_biblio = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{é}£"""
              # ou "abcdefghijklmnopqrstuvwxyz" | si le lettre n'est pas dans le li_biblio on laissez-le inchangé
    
    # liste de décalage
    li_decalage = liste_decalage(message_crypte,cle,li_biblio)
    
    # Le taille de message
    lenthMC = len(message_crypte)  # lenth Message Crypte
    
    # Décryptage
    message = ""
    
    for i in range(lenthMC):
        char = message_crypte[i]
        
        if char in li_biblio:
            # Trouver l'index de character de l'alphabet
            index_en_alphabet = li_biblio.index(char)
            
            # Décalez le caractère de la valeur correspondante dans li_decalage
            index_decale = (index_en_alphabet - li_decalage[i]) % len(li_biblio) # il trouve nouveau index 
            if index_decale < 0 :
                index_decale += len(li_biblio) # si index est -5 est le taille de alphabet est 26 , index = 21
            
            encrypted_char = li_biblio[index_decale]  # on trouve nouveua lettre de message_crypte
            message += encrypted_char    # Ajout de lettre
            
        else:
            # Si le caractère n'est pas dans l'alphabet, laissez-le inchangé
            message += char
            
    return message



# Programme:
def main():

    # === Exemple 1 ===
    print("Exemple 1 ","\n")
    
    # Initialization de message et clé
    message = "Si deux hommes ont la même opinion. L’un d’eux est de trop"
    cle = "hope"
    
    # Chiffrement de message 
    message_crypte = Cryptage_Vigenere(message,cle)
    
    # Affichage de message_crypte
    print("Chiffrement :",message_crypte,"\n")

    # Décryptage de message
    message1 = Decrtyptage_Vigenere(message_crypte,cle)
    
    # Affichage de message1
    print("Décryptage :",message1,"\n")
    
    
    
    # === Exemple 2 ===
    print("Exemple 2 ","\n")
    
    # Initialization de message et clé
    message = """ "Chez moi, le secret est enfermé dans une maison aux solides cadenas dont la clé est perdue et la porte scellée."-Les milles et une nuits """
    cle = "2023"
    
    # Chiffrement de message 
    message_crypte = Cryptage_Vigenere(message,cle)
    
    # Affichage de message_crypte
    print("Chiffrement :",message_crypte,"\n")

    # Décryptage de message
    message1 = Decrtyptage_Vigenere(message_crypte,cle)
    
    # Affichage de message1
    print("Décryptage :",message1,"\n")
    

main()








    
