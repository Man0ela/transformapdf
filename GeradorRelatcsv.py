from reportlab.pdfgen import canvas
import csv
#criar um arquivo em pdf
c=canvas.Canvas("notas.pdf")
#adicione texto ao pdf
with open('notas.csv', mode='r',encoding='utf-8') as arq:
    leitor= csv.reader(arq,delimiter=',')
    linhas=0
    contador=0
    media=0.0
    for coluna in leitor:
        if(linhas==0):
            contador+=1
            c.drawString(100, 750+contador,'Sexto ano:')
            linhas+=1
            
        else:
           contador-=20
           c.drawString(100,750+contador, f'Aluno:{coluna[0]}, Notas:{coluna[1]}')
           media+=float(coluna[1])
           linhas+=1
            
    c.drawString(100,670,f'Media de {linhas} alunos:{media/linhas}')
#salve o pdf
c.save()
