from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image("shirtificate.png", x=5, y=50)
pdf.output("hello.pdf")