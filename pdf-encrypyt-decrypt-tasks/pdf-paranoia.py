import os
from pathlib import Path
import PyPDF2


def encryptPDFs(root, password):
    """
     Encrypts all pdfs.
     Saves them inside ecrypted folder in the respective directories.
    """
    for folder, subfolder, fileList in os.walk(root):
        for file in fileList:
            if file.endswith('.pdf'):
                #filepath = os.path.join(os.path.abspath(folder), file)
                basePath = Path(folder).absolute()
                filePath = str(basePath/file)
                pdfFileObj = open(filePath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                if not pdfReader.isEncrypted:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))

                    pdfWriter.encrypt(password)                    
                    Path(basePath/'encrypted').mkdir(parents=True, exist_ok=True)          
                    newPath = Path(basePath/'encrypted')/file                            
                    resultPdf = open(str(newPath), 'wb')
                    pdfWriter.write(resultPdf)
                    resultPdf.close()

def decryptPDFs(root, password):
    """
     Decrypts all pdfs.
     Saves them inside decrypted folder in the respective directories.
    """
    for folder, subfolder, fileList in os.walk(root):
        for file in fileList:
            if file.endswith('.pdf'):               
                basePath = Path(folder).absolute()                
                filePath = str(basePath/file)
                pdfFileObj = open(filePath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                if  pdfReader.isEncrypted:
                    isDone = pdfReader.decrypt(password)
                    if isDone :
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(pageNum))
                        
                        baseParentPath = basePath.parent          
                        Path(baseParentPath/'decrypted').mkdir(parents=True, exist_ok=True)          
                        newFilePath = Path(baseParentPath/'decrypted')/file                            
                        resultPdf = open(str(newFilePath), 'wb')
                        pdfWriter.write(resultPdf)
                        resultPdf.close()

                    else :
                        print(f'{filePath} decryption failed..Moving onto next pdf file')        


pw = input("Please enter the password that you wish to set as encryption password: ")
encryptPDFs('.',pw)
decryptPDFs('.',pw)