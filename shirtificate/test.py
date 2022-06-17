from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font(family="Courier", size=30)
pdf.cell(txt="CS50 Shirtificate", align="C", border=1, new_y=)
pdf.image("shirtificate.png", x=0, y=50)
pdf.output("hello.pdf")