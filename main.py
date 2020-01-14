from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS

Tk().withdraw()
fileLocation = askopenfilename()

with open(fileLocation, "rb") as f:
    pdf = pdftotext.PDF(f)

stringOfText = ''
for text in pdf:
    stringOfText += text

finalFile = gTTS(text=stringOfText, lang='en')
finalFile.save("GeneratedSpeech.mp3")
