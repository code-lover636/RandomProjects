import PyPDF2
import pyttsx3

class PDFUtils:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.pdf_reader = PyPDF2.PdfFileReader(pdf_path)
        self.numPages = self.pdf_reader.numPages
        self.currentPage = 0
        
    def get_page(self, page_number):
        self.currentPage = page_number
        page = self.pdf_reader.getPage(page_number)
        return page.extractText()

    def get_all_content(self):
        return [self.pdf_reader.getPage(page_number).extractText() for page_number in range(self.pdf_reader.numPages)]
  
  
class SoundUtils:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.rate = 100
        self.voices = self.engine.getProperty('voices')
        self.voice = 0
        self.engine.setProperty('rate', self.rate)
        self.engine.setProperty('voice', self.voices[self.voice].id)
        
    def say_sentence(self,sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
        
    
    def save_audio(self, content, name):
        name = f'./audio/{name}.mp3'
        self.engine.save_to_file(content ,name)
        self.engine.runAndWait()
        return name
    
    def chngtone(self, label):
        if self.voice == 0:
            self.voice = 1
            label.config(text="Female Voice")
        else: 
            self.voice = 0
            label.config(text="Male Voice")
        self.engine.setProperty('voice', self.voices[self.voice].id)
        
    def chngrate(self, label):
        rates = (25, 50, 75, 100, 125, 150, 175, 200)
        self.rate = rates[rates.index(self.rate)+1] if self.rate !=200 else 25
        label.config(text=f"{self.rate/100}x")
        self.engine.setProperty('rate', self.rate)
