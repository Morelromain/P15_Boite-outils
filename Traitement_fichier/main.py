from .fonction1  import fusion, delimitation


sortir = False
while not sortir:
    print("Sommaire : \n\
1 : Fusion fichier \n\
2 : Ajout délimitation fichier")
    choix = input("que voulez vous faire? : ")
    if choix == "1":
        fusion()
    if choix == "2":
        delimitation()
