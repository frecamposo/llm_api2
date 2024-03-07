import PyPDF2

def text_extractor(path):
    data = []
    with open(path, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        num_pages = reader.getNumPages()
        for i in range(num_pages) : 
            page = reader.getPage(i)
            data.append(page.extractText())
    return data

def convertir_pdf(path):
    #    path = 'Instrucciones.pdf'
    pypdf = text_extractor(path)
    print("OK Convertido el PDF")
    return (pypdf)

'''if __name__ == "__main__":
    path = 'Instrucciones.pdf'
    pypdf = text_extractor(path)
    print(pypdf)
    print('The pdf has {} pages and the data structure is a {} where the index refers to the page number.'.format(len(pypdf), type(pypdf)))'''