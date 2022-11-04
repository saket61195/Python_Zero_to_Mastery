import PyPDF2

template = PyPDF2.PdfFileReader(open('./modified_pdf/merged_super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('./pdf_file/wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range (template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('./modified_pdf/watermarked.pdf','wb') as file:
        output.write(file)