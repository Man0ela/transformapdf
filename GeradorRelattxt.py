from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
txt_pdf=canvas.Canvas("receita.pdf")
with open('receita.txt',mode='r',encoding='utf-8') as arq:
    largura,altura=A4
    conteudo=arq.readlines()
    contador=0
    if conteudo:
        titulo=conteudo[0].strip()
        txt_pdf.setFont("Helvetica", 16) #fonte
        txt_pdf.drawCentredString(largura / 2, altura - 50, titulo)  #ceentraliza o título
        txt_pdf.setFont("Helvetica", 12)
        y_posicao = altura - 100  #ajuste para não sobrepor o título
        espacamento = 20  #espaço entre as linhas
        for linha in conteudo[1:]:
            txt_pdf.drawString(100, y_posicao, linha.strip())  #adiciona texto ao PDF
            y_posicao -= espacamento
txt_pdf.save()

