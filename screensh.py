#!/usr/bin/env python3
import pyautogui as pygrab

def main():
	image = pygrab.screenshot()
	image.save(r'/root/name.png')
main()
