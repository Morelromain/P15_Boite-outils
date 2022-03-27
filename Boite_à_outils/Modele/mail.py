import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser


class Mail:

    def envoi_mail(self, p1, p2, p3, p4, p5):
        """
        Envoi d'un mail
        """
        config = configparser.RawConfigParser()
        config.read('config.config')
        session = config.get('MAIL','session')
        session_port = config.get('MAIL','session_port')

        try:
            emeteur = p1
            mdp_emeteur = p2
            recepteur = p3
            titre = p4
            mail_content = p5
            message = MIMEMultipart()
            message['From'] = emeteur
            message['To'] = recepteur
            message['Subject'] = titre
            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP(session, int(session_port))
            session.starttls()
            session.login(emeteur, mdp_emeteur)
            text = message.as_string()
            toaddrs = [recepteur]
            session.sendmail(emeteur, toaddrs, text)
            session.quit()
        except:
            return "Erreur : configuration mauvaise, mail non envoyé"
        return f"Mail {p4} envoyé à {p3}"

