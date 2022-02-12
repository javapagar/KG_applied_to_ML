from PyPDF2 import PdfFileReader
import os
import pikepdf


current_path = os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_path,'uva_transformacion.pdf')
output = os.path.join(current_path,'output.pdf')

if not os.path.isfile(output):
    pdf = pikepdf.open(filename)
    pdf.save(output)

doc = PdfFileReader(output)
page = doc.getPage(66)
print(page.extractText())