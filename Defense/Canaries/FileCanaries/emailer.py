from smtplib import SMTP_SSL
from ssl import create_default_context

class Emailer():
    def __init__(self, smtp_server, smtp_port):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def __enter__(self):
        context = create_default_context()
        self.server = SMTP_SSL(self.smtp_server, self.smtp_port, context=context)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.server.quit()
        return False

    def authenticate(self, sender_email, password):
        self.sender_email = sender_email
        try:
            self.server.login(self.sender_email, password)
        except:
            return False
        return True

    def send(self, recipient_email, subject, msg):
        # Using RFC822 email string
        msg = f"Subject:{subject}\n\n{msg}"
        try:
            self.server.sendmail(self.sender_email, recipient_email, msg)
        except:
            return False
        return True

