import glob

def fusion():
    """
    fusionner l'ensemble des lignes des fichiers du document 
    dans un seul fichier.
    """
    total = input("Nom du fichier final : ")
    lista = glob.glob("./dossier_fusion/*")

    with open(total, 'w') as outfile:
        for fname in lista:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    print("fusion faite dans "+total)

def delimitation():
    """
    Creer des delimitations à la place des espaces.
    """
    fichier = input("Nom du fichier à traiter : ")
    total = input("Nom du fichier final : ")
    signe = input("Remplacer les espaces par : ")

    with open(total, 'w') as outfile:
        with open(fichier) as infile:
            for line in infile:
                line_b = line.replace("  ", "|")
                line_c = line_b.replace(" |", "|").replace("| ", "|")
                while "||" in line_c:
                    line_c = line_c.replace("||","|")
                line_d = line_c.replace("|",signe)
                outfile.write(line_d)
    print("modif faite dans "+total)


    
                    