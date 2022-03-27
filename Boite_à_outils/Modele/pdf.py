import glob
import pdfplumber
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


class PDF:

    def __init__(self):
        self.liste = glob.glob("./dossier_initial/*")

    def split_pdf(self, mid):
        """
        Division d'un pdf en deux.
        Necessite modules pdfplumber + PyPDF2.
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        if mid.isdigit() == False:
            return "Erreur : Chiffre demandé"
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                pdfWriter1 = PdfFileWriter()
                pdfWriter2 = PdfFileWriter()
                pdfReader = PdfFileReader(filea)
                with pdfplumber.open(filea) as pdf:
                    nb_pages = pdf.pages
                    for j, pg in enumerate(nb_pages):
                        if j < int(mid):
                            pdfWriter1.addPage(pdfReader.getPage(j))
                        if j > (int(mid))-1:
                            pdfWriter2.addPage(pdfReader.getPage(j))
                with open(f'dossier_final/SPLIT_1_{name_file}', 'wb') as f:
                    pdfWriter1.write(f)
                with open(f'dossier_final/SPLIT_2_{name_file}', 'wb') as f:
                    pdfWriter2.write(f)
        except:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"fichiers coupés à {mid} généré(s) dans dossier_final"

    def fusion_pdf(self, total):
        """
        Fusionne les pdf entre eux.
        Necessite module PyPDF2.
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            merger = PdfFileMerger()
            for filename in self.liste:
                merger.append(PdfFileReader(open(filename, "rb")))
            merger.write(f'dossier_final/FUSION_{total}.pdf')
        except :
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"fichier FUSION_{total} généré dans dossier_final"

    def cherche_donnee_pdf(self, before):
        """
        Trouve des données dans un pdf.
        Necessite module pdfplumber.
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                with pdfplumber.open(filea) as pdf:
                    nb_pages = pdf.pages
                    with open(f'dossier_final/FOUND_{name_file}.txt', 'w') as f:
                        for j, pg in enumerate(nb_pages):
                            first_page = pdf.pages[j]
                            texte = first_page.extract_text()
                            position = texte.find(before)
                            texte2 = texte[position+len(before):]
                            position2 = texte2.find('\n')
                            NUM_DOSSIER = texte2[:position2]
                            f.write(f"'{NUM_DOSSIER}',\n")
        except:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"fichier(s) ayant {before} généré(s) dans dossier_final"

    def page_exclusion_pdf(self, p1, p2, p3, p4, p5):
        """
        Exclu des pages d'un pdf
        Necessite module pdfplumber.
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        liste_page = []
        if p1.isdigit() == False and p1 != "":
            return "Erreur : Chiffre demandé"
        if p2.isdigit() == False and p2 != "":
            return "Erreur : Chiffre demandé"
        if p3.isdigit() == False and p3 != "":
            return "Erreur : Chiffre demandé"
        if p4.isdigit() == False and p4 != "":
            return "Erreur : Chiffre demandé"
        if p5.isdigit() == False and p5 != "":
            return "Erreur : Chiffre demandé"
        if p1 == p2 == p3 == p4 == p5 == "":
            return "Erreur : Veuillez rentrer un chiffre"
        if p1 != "":
            liste_page.append(int(p1)-1)
        if p2 != "":
            liste_page.append(int(p2)-1)
        if p3 != "":
            liste_page.append(int(p3)-1)
        if p4 != "":
            liste_page.append(int(p4)-1)
        if p5 != "":
            liste_page.append(int(p5)-1)
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                pdfWriter1 = PdfFileWriter()
                pdfReader = PdfFileReader(filea)
                with pdfplumber.open(filea) as pdf:
                    nb_pages = pdf.pages
                    for j, pg in enumerate(nb_pages):
                        if j not in liste_page:
                            pdfWriter1.addPage(pdfReader.getPage(j))
                with open(f'dossier_final/EXCLU_{name_file}', 'wb') as f:
                    pdfWriter1.write(f)
        except:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"fichiers généré(s) dans dossier_final, exclusion de la page {p1} {p2} {p3} {p4} {p5}"

    def page_selection_pdf(self, p1, p2, p3, p4, p5):
        """
        Selectionne des pages d'un pdf
        Necessite module pdfplumber.
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        liste_page = []
        if p1.isdigit() == False and p1 != "":
            return "Erreur : Chiffre demandé"
        if p2.isdigit() == False and p2 != "":
            return "Erreur : Chiffre demandé"
        if p3.isdigit() == False and p3 != "":
            return "Erreur : Chiffre demandé"
        if p4.isdigit() == False and p4 != "":
            return "Erreur : Chiffre demandé"
        if p5.isdigit() == False and p5 != "":
            return "Erreur : Chiffre demandé"
        if p1 == p2 == p3 == p4 == p5 == "":
            return "Erreur : Veuillez rentrer un chiffre"
        if p1 != "":
            liste_page.append(int(p1)-1)
        if p2 != "":
            liste_page.append(int(p2)-1)
        if p3 != "":
            liste_page.append(int(p3)-1)
        if p4 != "":
            liste_page.append(int(p4)-1)
        if p5 != "":
            liste_page.append(int(p5)-1)
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                pdfWriter1 = PdfFileWriter()
                pdfReader = PdfFileReader(filea)
                with pdfplumber.open(filea) as pdf:
                    nb_pages = pdf.pages
                    for j, pg in enumerate(nb_pages):
                        if j in liste_page:
                            pdfWriter1.addPage(pdfReader.getPage(j))
                with open(f'dossier_final/EXCLU_{name_file}', 'wb') as f:
                    pdfWriter1.write(f)
        except:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"fichiers généré(s) dans dossier_final, exclusion de la page {p1} {p2} {p3} {p4} {p5}"
