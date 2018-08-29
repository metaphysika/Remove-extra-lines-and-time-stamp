import pyperclip
import re


def getClipboard():
    clipboard_content = str(pyperclip.paste())  # gets content of clipboard.
    paste = ' '.join(clipboard_content.split())  # removes extra spaces.
    new = re.sub(r'\b\d+(?:\:\d+)?\s+', '', paste)  # removes numbers around : (timestamp)
    pyperclip.copy(new)
    # print (new)


getClipboard()
