import pypandoc

def convertir_word(path):
    # Example file:
    docxFilename = 'Instrucciones de la actividad con encargo_S6.docx'
    #######output = pypandoc.convert_file(docxFilename, 'plain', outputfile="somefile.txt")
    output = pypandoc.convert_file(path, 'plain')
    print("OK convertido el Word")
    return (output)
