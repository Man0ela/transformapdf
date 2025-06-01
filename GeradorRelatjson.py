from reportlab.pdfgen import canvas
import json

c = canvas.Canvas("info.pdf")
with open("info.json", mode="r", encoding="utf-8") as arq:
    conteudo = json.load(arq)
    contador = 0
    c.setFont("Helvetica-Bold", 12) #fonte
    for chave,valor in conteudo.items():
        linha = f"{chave}: {valor}" #reune chave com o valor 
        c.drawString(100, 750+contador, linha) 
        contador-=20
c.save()
