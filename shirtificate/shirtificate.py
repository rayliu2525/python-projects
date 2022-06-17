from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font(family="Courier", size=40, style="B")
pdf.cell(txt="CS50 Shirtificate", align="C",  w=0, h=30)
pdf.image("shirtificate.png", x=0, y=50)
pdf.set_text_color(r=255, g=255, b=255)
pdf.set_font_size(size=30)
pdf.text(x=40, y=120, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")