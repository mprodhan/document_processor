import PyPDF2

with open ('./documents/dummy.pdf','rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    print(reader.numPages)
    page1 = reader.getPage(0)
    page1.rotateCounterClockwise(90)
    write = PyPDF2.PdfFileWriter()
    write.addPage(page1)
    with open('rotate.pdf', 'wb') as e:
        write.write(e)