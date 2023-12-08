# Decembre 2023

# Méthodes de Cryptologie


def crypt(message): 
    ### Code Inverse : Il inverse le message ###
    resultat = ''
    i = len(message) - 1
    while i > -1:
        resultat = resultat + message[i]
        i = i - 1
    return resultat


def decryptage_crypt(message):
    ### Decrtyptage de Code Inverse ###
    return crypt(crypt(message))


def decalage_mot(mot, b):
    ### Code César Simple : y ≡ x + b[n] ###
    
    # Alphabet
    lettres = 'abcdefghijklmnopqrstuvwxyz'
    
    # Chiffrement
    resultat = ''
    
    for char in mot:
        if char.isalpha(): # isalpha() : True <= Si tous les caractères de la chaîne sont des alphabets (peuvent être en minuscules ou majuscules).
            maj = char.isupper()# maj = charactère majuscule
            char = char.lower() #char = charactère minuscule
            
            if char in lettres:
                i = (lettres.index(char) + b) % 26   # i = index de message crypte
                c_decale = lettres[i] 
            if maj:
                c_decale = c_decale.upper()
            resultat += c_decale
        else:
            # si le lettre n'est pas dans les lettres on laissez-le inchangé
            resultat += char
            
    return resultat


def decryptage_decalage_mot(mot, k):
    ### Decryptage de Code César Simple ###
    a = -k
    return decalage_mot(mot, a)




def pgcd(a, b):
    ### Plus grand diviseur Commun ###
    if (b == 0):
        return a
    else:
        return pgcd(b, a % b)


def creationDic(li_biblio): # li_biblio = liste de bibliotheque(l'alphabet)
    ### Il cree un dictionnaire qui contient toutes les lettres de cette li_biblio et ses index.  ###
    dic_Alpha = {}
    location = 0
    for i in li_biblio:  # par exemple : li_biblio = "abcdefghijklmnopqrstuvwxyz"
        dic_Alpha[i] = location
        location += 1
    return dic_Alpha


def liste_decalage(message, cle, bibliotheque):
    ### Il créer une liste qui contient l'index de chaque lettre de cle(cle va avoir le meme taille avec message) ###

    # creation de l'alphabet
    dic_Alphabet = creationDic(bibliotheque)

    # creation du liste cle qui a le meme taille avec message
    li_cle = []
    i = 0  # i := index
    for x in range(0, len(message)):
        if i == len(cle):
            i = 0
        li_cle.append(cle[i])

        # initialization de liste de decalage
    li_decalage = []

    # affectation sur le liste de decalage
    for i in range(0, len(li_cle)):
        num = li_cle[i]  # mettre le lettre de clé
        num = dic_Alphabet[num]  # mettre le location dans l'alphabet (a=0)
        li_decalage.append(num)  # ajout de location de chaque lettre

    return li_decalage  # liste d'entier


def Cryptage_Vigenere(message, cle):
    ### Il chiffrer le message avec décalage de chaqu lettre grace aux index de chaque lettre de cle. ###

    # Bibliotheque
    li_biblio = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{é}£"""
    # ou "abcdefghijklmnopqrstuvwxyz" | si le lettre n'est pas dans le li_biblio on laissez-le inchangé

    # liste de décalage
    li_decalage = liste_decalage(message, cle, li_biblio)

    # Le taille de message
    lenthM = len(message)

    # Chiffrement
    message_crypte = ""

    for i in range(lenthM):
        char = message[i]  # une lettre de message

        if char in li_biblio:
            # Trouver l'index de character de l'alphabet
            index_en_alphabet = li_biblio.index(char)

            # Décalez le caractère de la valeur correspondante dans li_decalage
            index_decale = (index_en_alphabet + li_decalage[i]) % len(
                li_biblio)  # il trouve nouveau index # on utilise le modulo(%) pour retourner au debut de alphabet
            encrypted_char = li_biblio[index_decale]  # on trouve nouveua lettre de message_crypte
            message_crypte += encrypted_char  # Ajout de lettre

        else:
            # Si le caractère n'est pas dans l'alphabet, laissez-le inchangé
            message_crypte += char

    return message_crypte


def Decrtyptage_Vigenere(message_crypte, cle):
    ### Décrypte le message_crypte ###

    # Bibliotheque
    li_biblio = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{é}£"""
    # ou "abcdefghijklmnopqrstuvwxyz" | si le lettre n'est pas dans le li_biblio on laissez-le inchangé

    # liste de décalage
    li_decalage = liste_decalage(message_crypte, cle, li_biblio)

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
            index_decale = (index_en_alphabet - li_decalage[i]) % len(li_biblio)  # il trouve nouveau index
            if index_decale < 0:
                index_decale += len(li_biblio)  # si index est -5 est le taille de alphabet est 26 , index = 21

            encrypted_char = li_biblio[index_decale]  # on trouve nouveua lettre de message_crypte
            message += encrypted_char  # Ajout de lettre

        else:
            # Si le caractère n'est pas dans l'alphabet, laissez-le inchangé
            message += char

    return message


def Cryptage_CesarAffine(message, cle_a, cle_b):  # cle_a et cle_b doivent etre entier

    # Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # | si le lettre n'est pas dans le li_biblio on laissez-le inchangé

    # message.miniscule()
    message = message.lower()  # car dans notre alphabet il y a seulement les miniscule

    # Taille de alphabet
    n = len(alphabet)

    # dictionnaire d'alphabet
    dic_Alpha = creationDic(alphabet)

    # Verification de "a" et "n"  sont  premier entre eux
    if (pgcd(cle_a, n) != 1):
        print("cle_a et le taille d'alphabet ne sont pas premier entre eux!!! \n")
        print("Arret de codage \n")
        return

    # Chiffrement
    message_crypte = ""
    for char in message:
        if char in alphabet:
            # index_letrreCrypte = ((a * lettre) + (b % n)) % n   <==> n : y = ax +b[n]
            index_letrreCrypte = ((cle_a * dic_Alpha[char]) + (cle_b % n)) % n
            lettre_crypte = alphabet[index_letrreCrypte]  # il trouve le nouveau lettre
            message_crypte += lettre_crypte  # Ajout de lettre modifie

        else:
            # Si le caractère n'est pas dans l'alphabet, laissez-le inchangé
            message_crypte += char
    return message_crypte


def Decrtyptage_CesarAffine(message_crypte, cle_a, cle_b):
    
    # Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # | si le lettre n'est pas dans le li_biblio on laissez-le inchangé

    # message.miniscule()
    message_crypte = message_crypte.lower()  # car dans notre alphabet il y a seulement les miniscule

    # Taille de alphabet
    n = len(alphabet)

    # dictionnaire d'alphabet
    dic_Alpha = creationDic(alphabet)

    # Verification de "a" et "n"  sont  premier entre eux
    if (pgcd(cle_a, n) != 1):
        print("cle_a et le taille d'alphabet ne sont pas premier entre eux!!! \n")
        print("Arret de codage \n")
        return

    # Chiffrement
    message = ""
    for char in message_crypte:
        if char in alphabet:
            # cryptage : n : y = ax +b[n]     # decryptage  n : ax = b[n] - y
            # index_letrreDecrypte =  (((cle_b % n) - dic_Alpha[char]) // a ) % n    <==> n : ax = b[n] - y
            index_letrreDecrypte = (((cle_b % n) - dic_Alpha[char]) // cle_a) % n  # on utilise //(division entier)
            lettre_Decrypte = alphabet[index_letrreDecrypte]  # il trouve le nouveau lettre
            message += lettre_Decrypte  # Ajout de lettre modifie

        else:
            # Si le caractère n'est pas dans l'alphabet, laissez-le inchangé
            message += char

    return message



# Programme
def main():
    # === Exemple 1 ===
    print("Exemple 1 ", "\n")

    # Initialization de message et clé
    k = 3
    message = "Si deux hommes ont la même opinion. L’un d’eux est de trop"
    cle_a = 1
    cle_b = 2
    cle = "hope"


    # Chiffrement de message
    mot1 = crypt(message)
    mot2 = decalage_mot(message, k)
    message_crypte = Cryptage_CesarAffine(message, cle_a, cle_b)
    message_crypte2 = Cryptage_Vigenere(message, cle)

    # Affichage de message_crypte
    print("Chiffrement Crypt :", mot1, "\n")
    print("Chiffrement decalage :", mot2, "\n")
    print("Chiffrement CesarAffine :", message_crypte, "\n")
    print("Chiffrement Vigenere :", message_crypte2, "\n")


    # Décryptage de message
    motD1 = decryptage_crypt(message)
    motD2 = decryptage_decalage_mot(mot2, k)
    message1 = Decrtyptage_CesarAffine(message_crypte, cle_a, cle_b)
    message2 = Decrtyptage_Vigenere(message_crypte, cle)


    # Affichage de message1
    print("Décryptage Crypt :", motD1, "\n")
    print("Décryptage decalage :", motD2, "\n")
    print("Décryptage CesarAffine :", message1, "\n")
    print("Décryptage Vigenere :", message2, "\n")


    # === Exemple 2 ===
    print("Exemple 2 ", "\n")

    # Initialization de message et clé
    k = 2
    message = """ "Chez moi, le secret est enfermé dans une maison aux solides cadenas dont la clé est perdue et la porte scellée."-Les milles et une nuits" """
    cle_a = 1
    cle_b = 2
    cle = "2023"

    # Chiffrement de message
    mot1 = crypt(message)
    mot2 = decalage_mot(message, k)
    message_crypte = Cryptage_CesarAffine(message, cle_a, cle_b)
    message_crypte2 = Cryptage_Vigenere(message, cle)

    # Affichage de message_crypte
    print("Chiffrement Crypt :", mot1, "\n")
    print("Chiffrement decalage :", mot2, "\n")
    print("Chiffrement CesarAffine :", message_crypte, "\n")
    print("Chiffrement Vigenere :", message_crypte2, "\n")

    # Décryptage de message
    motD1 = decryptage_crypt(message)
    motD2 = decryptage_decalage_mot(mot2, k)
    message1 = Decrtyptage_CesarAffine(message_crypte, cle_a, cle_b)
    message2 = Decrtyptage_Vigenere(message_crypte, cle)

    # Affichage de message1
    print("Décryptage Crypt :", motD1, "\n")
    print("Décryptage decalage :", motD2, "\n")
    print("Décryptage CesarAffine :", message1, "\n")
    print("Décryptage Vigenere :", message2, "\n")

    # === Exemple 3 ===
    print("Exemple 3 ", "\n")

    k = 4
    message = """ 'snoçel sed ennod em no uq sruojuot sap emia n ej euq neib erdnerppa a terp sruojuot sius ej' """
    cle_a = 1
    cle_b = 2
    cle = "BYE"

    # Chiffrement de message
    mot1 = crypt(message)
    mot2 = decalage_mot(message, k)
    message_crypte = Cryptage_CesarAffine(message, cle_a, cle_b)
    message_crypte2 = Cryptage_Vigenere(message, cle)

    # Affichage de message_crypte
    print("Chiffrement Crypt :", mot1, "\n")
    print("Chiffrement decalage :", mot2, "\n")
    print("Chiffrement CesarAffine :", message_crypte, "\n")
    print("Chiffrement Vigenere :", message_crypte2, "\n")

    # Décryptage de message
    motD1 = decryptage_crypt(message)
    motD2 = decryptage_decalage_mot(mot2, k)
    message1 = Decrtyptage_CesarAffine(message_crypte, cle_a, cle_b)
    message2 = Decrtyptage_Vigenere(message_crypte, cle)

    # Affichage de message1
    print("Décryptage Crypt :", motD1, "\n")
    print("Décryptage decalage :", motD2, "\n")
    print("Décryptage CesarAffine :", message1, "\n")
    print("Décryptage Vigenere :", message2, "\n")

main()
