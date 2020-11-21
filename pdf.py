import PyPDF2

with open ('./documents/dummy.pdf','rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    # The class method, starts off to read the file. Must be in that class at the beginning.
    # To access a file, since the file is on binary mode, the reader must read binary. So 'rb'
    # is implimented.
    # The reader variable object, represent the class object code that reads the file.
    print(reader.numPages)
    
    page1 = reader.getPage(0)
    # page1 is the page object that retrieves the page after reading the file via reader.
    page1.rotateCounterClockwise(90)
    # Before writing a file of the page1, page1 must be set to an orientation. 
    # This part is only neccessary if the file needs the rotate orientation. 
    # Other method can be used before writing to a new file.
    write = PyPDF2.PdfFileWriter()
    # This is the write object that accesses a method.
    write.addPage(page1)
    with open('rotate.pdf', 'wb') as e:
        write.write(e)
    # The process code with which the file is created and written.
    # Displays the rotation of the page as specified by rotateCounterClockwise.