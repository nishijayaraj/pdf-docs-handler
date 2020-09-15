import os


import PyPDF2


def breakPassword(filename):
    """
    Breaks password of a PDF
    
    """
    encryptedFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(encryptedFile)
    dict_file = open('dictionary.txt')
       
    key_word = ''
    for word in dict_file.readlines():
        word = word.strip()
        word_sm = word.lower()
        word_up = word.capitalize()

        if pdfReader.decrypt(word):
            key_word = word
            break
        elif pdfReader.decrypt(word_up):
            key_word = word_up
            break
        elif pdfReader.decrypt(word_sm):
            key_word=word_sm
            break
    dict_file.close()        
    encryptedFile.close()
    print("Password :",key_word)
    return key_word
        

def generate_PDF():
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.encrypt('ABAFT')
    encryptedPdf = open('pdf_encrypted.pdf', 'wb')
    pdfWriter.write(encryptedPdf)
    encryptedPdf.close()

generate_PDF()
breakPassword('pdf_encrypted.pdf')
