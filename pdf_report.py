from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.lib.pagesizes import A4
data = [
    ["Header 1", "Header 2", "Header 3"],
    ["Row 1 Col 1", "Row 1 Col 2", "Row 1 Col 3"],
    ["Row 2 Col 1", "Row 2 Col 2", "Row 2 Col 3"],

]



def pdf(pdf_file="test.pdf"):
     doc = SimpleDocTemplate(pdf_file,pagesize=A4)
     table = Table(data)
     table.setStyle(TableStyle([
         # ("BACKGROUND",(0,0), (-1,0)),
         ("GRID",(0,0),(-1,-1), 1, colors.black)
     ]))
     elements = [table]
     doc.build(elements)

pdf()