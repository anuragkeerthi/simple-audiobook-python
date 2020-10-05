import pyttsx3
import PyPDF2

book = open('.pdf', 'rb') # Insert pdf file name here
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
# speaker.say('Hi, I am talking. Is it audible')
page = pdfReader.getPage(7) # Starting Page number
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
