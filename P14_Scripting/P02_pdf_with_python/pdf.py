import PyPDF2

# 'rb' is read binary, for pdf we append 'b' to it
with open('./pdf_file/dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(file)
    print(reader)
    print(reader.numPages)
    print(reader.getPage(0))

    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./modified_pdf/dummy_roated.pdf','wb') as new_file:
        writer.write(new_file)