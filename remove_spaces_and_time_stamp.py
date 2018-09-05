import pyperclip
import re


def getClipboard():
    clipboard_content = str(pyperclip.paste())  # gets content of clipboard.
    paste = ' '.join(clipboard_content.split())  # removes extra spaces.
    # new = re.sub(r'\b\d+(?:\:\d+)?\s+', '', paste)  # removes numbers around : (timestamp)
    # new = re.sub((r'\d{2}:\d{2}'), '', paste) # Regex for MM:SS format
    new = re.sub((r'\d{1,2}:\d{2}:\d{2}'), '', paste)  # regex for H:MM:SS format
    pyperclip.copy(new)
    #print (new)


getClipboard()
