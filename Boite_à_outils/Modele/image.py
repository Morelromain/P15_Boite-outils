import pytesseract
from removebg import RemoveBg

import os
import configparser
import glob
import shutil
from PIL import Image as Img


class Image:

    def __init__(self):
        self.liste = glob.glob("./dossier_initial/*")

    def transforme_image_en_texte(self):
        """
        Trouve les textes dans un png ou jpg.
        Necessite module pytesseract + install tesseract windows
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                config = configparser.RawConfigParser()
                config.read('config.config')
                adresse = config.get('PYTESSERACT','path')
                if adresse == "default":
                    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                else:
                    pytesseract.pytesseract.tesseract_cmd = adresse
                texte = pytesseract.image_to_string(filea)
                with open(f'dossier_final/TRANSFORME_{name_file}.txt', 'w') as f:
                    f.write(texte)
        except:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return "fichier(s) généré(s) dans dossier_final"

    def trouve_texte_dans_images(self, selection):
        """
        Trouve un textes précis dans des png ou jpg.
        Necessite module pytesseract + install tesseract windows
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            for path_file in self.liste:
                name_file = path_file.replace("./dossier_initial\\", "")
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                texte = pytesseract.image_to_string(path_file)
                if selection in texte:
                    shutil.copy2(path_file, f'./dossier_final/{name_file}')
        except:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"fichiers contenant {selection} généré(s) dans dossier_final"
    
    def modifie_format_image(self, conversion1, conversion2, conversion3):
        """
        Modifie le format des images et leurs resolutions
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                name_file2 = name_file[:name_file.rfind(".")]
                img = Img.open(filea)
                if conversion2 != "" and conversion3 != "":
                    if conversion2.isdigit() == False or conversion3.isdigit() == False:
                        return "Erreur : Chiffre demandé"
                    img = img.resize((int(conversion2),int(conversion3)), Img.ANTIALIAS)
                if conversion1 != "":
                    img.save(f'./dossier_final/{name_file2}.{conversion1}')
                else :
                    img.save(f'./dossier_final/{name_file}')
        except:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return f"fichier(s) généré(s) dans dossier_final convertie en {conversion1} {conversion2} {conversion3}"

    def enleve_fond(self):
        """
        Enlève le fond d'une photo
        Necessite module removebg + apikey removebg valide
        """
        if self.liste == []:
            return "Erreur : Dossier initial vide"
        try:
            for filea in self.liste:
                name_file = filea.replace("./dossier_initial\\", "")
                shutil.copy2(filea, f'./dossier_final/FOND_{name_file}')
                config = configparser.RawConfigParser()
                config.read('config.config')
                apikey = config.get('REMOVEBG','apikey')
                rmbg = RemoveBg(apikey, "error.log")
                rmbg.remove_background_from_img_file(f'./dossier_final/FOND_{name_file}')
                os.remove(f'./dossier_final/FOND_{name_file}')
        except:
            return "Erreur : Le dossier initial contient des fichiers inadaptés ou non modifiable"
        return "fichiers généré(s) dans dossier_final"
    