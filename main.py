from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS
from os.path import splitext

Tk().withdraw()
fileLocation = askopenfilename()

with open(fileLocation, "rb") as f:
    pdf = pdftotext.PDF(f)

stringOfText = ''
for text in pdf:
    stringOfText += text

outname = splitext(fileLocation)[0]+".mp3"

finalFile = gTTS(text=stringOfText, lang='en')
finalFile.save(outname)
