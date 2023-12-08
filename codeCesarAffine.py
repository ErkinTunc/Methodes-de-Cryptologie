# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:13:05 2023

@author: acer
"""

# Les Fonctions

def pgcd(a,b):  
    if(b == 0):
        return a
    else:
        return pgcd(b,a % b)
  

def creationDic(li_biblio):
    ### Il cree un dictionnaire qui contient toutes les lettres de cette li_biblio et ses index.  ###
    
    dic_Alpha = {}
    location = 0
    for i in li_biblio: # par exemple : li_biblio = "abcdefghijklmnopqrstuvwxyz"
        dic_Alpha[i] = location
        location += 1
    
    return dic_Alpha



def Cryptage_CesarAffine(message,cle_a,cle_b): #cle_a et cle_b doivent etre entier
    
    # Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
             #| si le lettre n'est pas dans le li_biblio on laissez-le inchangé
    
    # message.miniscule()
    message = message.lower()  # car dans notre alphabet il y a seulement les miniscule
    
    # Taille de alphabet
    n = len(alphabet)
    
    # dictionnaire d'alphabet
    dic_Alpha = creationDic(alphabet) 
    
    # Verification de "a" et "n"  sont  premier entre eux
    if (pgcd(cle_a,n) != 1):
        print("cle_a et le taille d'alphabet ne sont pas premier entre eux!!! \n")
        print("Arret de codage \n")
        return
    
    # Chiffrement
    message_crypte = ""
    for char in message:
        if char  in alphabet:
            # index_letrreCrypte = ((a * lettre) + (b % n)) % n   <==> n : y = ax +b[n]
            index_letrreCrypte = ((cle_a * dic_Alpha[char]) + (cle_b % n)) % n
            lettre_crypte = alphabet[index_letrreCrypte] # il trouve le nouveau lettre
            message_crypte += lettre_crypte        # Ajout de lettre modifie
        
        else:
            # Si le caractère n'est pas dans l'alphabet, laissez-le inchangé
            message_crypte += char
    return message_crypte


def Decrtyptage_CesarAffine(message_crypte,cle_a,cle_b):
    
    
    # Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
             #| si le lettre n'est pas dans le li_biblio on laissez-le inchangé
    
    # message.miniscule()
    message_crypte = message_crypte.lower() # car dans notre alphabet il y a seulement les miniscule
    
    # Taille de alphabet
    n = len(alphabet)
    
    # dictionnaire d'alphabet
    dic_Alpha = creationDic(alphabet) 
    
    # Verification de "a" et "n"  sont  premier entre eux
    if (pgcd(cle_a,n) != 1):
        print("cle_a et le taille d'alphabet ne sont pas premier entre eux!!! \n")
        print("Arret de codage \n")
        return
    
    # Chiffrement
    message = ""
    for char in message_crypte:
        if char  in alphabet:
            # cryptage : n : y = ax +b[n]     # decryptage  n : ax = b[n] - y
            # index_letrreDecrypte =  (((cle_b % n) - dic_Alpha[char]) // a ) % n    <==> n : ax = b[n] - y
            index_letrreDecrypte = (((cle_b % n) - dic_Alpha[char]) // cle_a ) % n  # on utilise //(division entier)
            lettre_Decrypte = alphabet[index_letrreDecrypte] # il trouve le nouveau lettre
            message += lettre_Decrypte        # Ajout de lettre modifie
        
        else:
            # Si le caractère n'est pas dans l'alphabet, laissez-le inchangé
            message += char
    
    return message

# Programme
def main():
    
    # === Exemple 1 ===
    print("Exemple 1 ","\n")
    
    # Initialization de message et clé
    message = "Si deux hommes ont la même opinion. L’un d’eux est de trop"
    cle_a = 1 
    cle_b = 2
    
    # Chiffrement de message 
    message_crypte = Cryptage_CesarAffine(message,cle_a,cle_b)
    
    # Affichage de message_crypte
    print("Chiffrement :",message_crypte,"\n")

    # Décryptage de message
    message1 = Decrtyptage_CesarAffine(message_crypte,cle_a,cle_b)
    
    # Affichage de message1
    print("Décryptage :",message1,"\n")
    
    
    
    # === Exemple 2 ===
    print("Exemple 2 ","\n")
    
    # Initialization de message et clé
    message = """ "Chez moi, le secret est enfermé dans une maison aux solides cadenas dont la clé est perdue et la porte scellée."-Les milles et une nuits """
    cle_a = 1 
    cle_b = 2
    
    # Chiffrement de message 
    message_crypte = Cryptage_CesarAffine(message,cle_a,cle_b)
    
    # Affichage de message_crypte
    print("Chiffrement :",message_crypte,"\n")

    # Décryptage de message
    message1 = Decrtyptage_CesarAffine(message_crypte,cle_a,cle_b)
    
    # Affichage de message1
    print("Décryptage :",message1,"\n")
    
    
main()