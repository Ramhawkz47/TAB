import PyPDF2
import gtts
import os
from googletrans import Translator

gTTS=gtts.gTTS

def translateto(text,to):
    print("translating...")
    translator = Translator(service_urls=['translate.google.com', 'translate.google.lv'])
    translation = translator.translate(text, dest=to)
    print("translation completed!")

def pdftomp3(inputfilename, language, speed):
    data=[]
    pdfFileObject = open(inputfilename+".pdf", 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    print(" No. Of Pages :", pdfReader.numPages)
    for i in range(pdfReader.numPages):
        pageObject = pdfReader.getPage(i)
        if(len(pageObject.extractText())>2):
            data.append(pageObject.extractText())
        
        #print(pageObject.extractText())
    if(language=="en"):
        myobj = gTTS(text="\n\n".join(data), lang=language, slow=speed)
    else:
        myobj = gTTS(text=translateto("\n\n".join(data),language), lang=language, slow=speed)
    print("Text to Speech Completed!")
    pdfFileObject.close()
    myobj.save(inputfilename+".mp3")
    print("Audio file is saved as "+inputfilename+".mp3")

def initials():
    filename=input("Filename:")
    lisoflang=gtts.lang.tts_langs()
    lang=input("\n".join([x+" : "+lisoflang[x] for x in lisoflang])+"\n\n enter your choice: ")
    pdftomp3(filename,lang,False)

initials()
