# IMPORTING pyPDF2 LATEST VERSION :
import pyPDF2

# capturing the required pdf files :
template = pyPDF2.PdfFileReader(open('template.pdf', 'rb'))
watermark = pyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
output = pyPDF2.PdfFileWriter()

# iterating through the pages and making watermarks in each :
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    # storing the final watermarked pdf as output-stream :
    with open("watermarked_pdf.pdf", "wb") as outputStream:
        output.write(outputStream)
