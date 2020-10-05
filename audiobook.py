import pyttsx3
import PyPDF2

book = open('.pdf', 'rb') # Insert pdf file name here
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
# speaker.say('Hi, I am talking. Is it audible')
for page_number in range(0, pages):
    page = pdfReader.getPage(page_number) 
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
