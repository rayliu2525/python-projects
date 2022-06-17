from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.add_page()
pdf.add_page()
pdf.image("shirtificate.png", x=0, y=0)
pdf.output("hello.pdf")