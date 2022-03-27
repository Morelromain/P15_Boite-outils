import glob
import shutil


class Fichier:

    def __init__(self):
        self.liste = glob.glob("./dossier_initial/*")
        
    def fusion(self, total):
        """
        fusionner l'ensemble des lignes des fichiers du document
        dans un seul fichier.
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            with open(f'dossier_final/FUSION_{total}', 'w') as outfile:
                for fname in self.liste:
                    with open(fname) as infile:
                        for line in infile:
                            outfile.write(line)
        except :
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"Fichier FUSION_{total} généré dans dossier_final"

    def delimitation(self, signe):
        """
        Creer des delimitations à la place des espaces.
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                with open(f'dossier_final/DELIMIT_{name_file}', 'w') as outfile:
                    with open(filea) as infile:
                        for line in infile:
                            line_b = line.replace(" ", "|")
                            line_c = line_b.replace(" |", "|").replace("| ", "|")
                            while "||" in line_c:
                                line_c = line_c.replace("||", "|")
                            line_d = line_c.replace("|", signe)
                            outfile.write(line_d)
        except UnicodeDecodeError:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"fichier(s) généré(s) dans dossier_final avec {signe} en délimitation"

    def suppression_blanc(self):
        """
        Suppression des zones blanches dans les csv.
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                with open(f'dossier_final/BLANC_{name_file}', 'w') as outfile:
                    with open(filea) as infile:
                        for line in infile:
                            line = line.replace('\n', '')
                            line = f';{line};'
                            while " ;" in line:
                                line = line.replace(" ;", ";")
                            while "; " in line:
                                line = line.replace("; ", ";")
                            line = line[1:-1]
                            outfile.write(line+"\n")
        except UnicodeDecodeError:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return "fichier(s) généré(s) dans dossier_final"

    def renommage_fichier(self, old_part, new_part):
        """
        Renomme une partie dans un groupe de fichiers
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        for fichier in self.liste:
            extention = (fichier.rfind("."))
            new_file = fichier[len("./dossier_initial/"):extention].replace(old_part, new_part)
            shutil.copy2(fichier, f'./dossier_final/{new_file}{fichier[extention:]}')
        return f"fichier(s) généré(s) dans dossier_final avec {old_part} modifié en {new_part}"
