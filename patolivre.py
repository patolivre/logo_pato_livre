from Tkinter import *
from math import *
from threading import Thread
from time import sleep



class Pato(object): 
    def __init__(self,width=800,height=600):
       self.y = 20
       self.tamanho = 40
       self.width = width
       self.height = height
       self.espacamento_entre_linhas = 25
       self.proporcoes_cabeca = ( (320,160), (320,240), (320,240))
       self.proporcoes_corpo = [80,560,640,720,640,560,480,240,320,360]
       self.proporcao_largura = width / 800.0
       self.tela = Canvas(Tk(), width=self.width, height=self.height)
       self.horizontal_center = self.width  / 2
       self.vertical_center = self.height / 2
       self.tela.pack()

    def rounded_rectangle(self, x=0, y = 200,largura=200, cor="black"):
        largura = largura *  self.proporcao_largura
        tamanho=self.tamanho
        if x == 0:
          x = self.horizontal_center - (largura / 2)
        circunferencia = int(tamanho / 2)
        raio = int(circunferencia/ 2)
 
        if (largura > tamanho):
          self.tela.create_rectangle(x, y, x+largura, y+circunferencia, fill='red')
          self.tela.create_oval( x - raio, y, x + raio,y + circunferencia, fill='green')
          self.tela.create_oval( x + largura-raio, y, x + largura+raio, y + circunferencia,
                  fill='blue')
        else:
          x = x + largura / 4
          self.tela.create_oval(x, y, x + circunferencia, y + circunferencia,
      fill='yellow')

    def cabeca(self):
       for x, largura in self.proporcoes_cabeca:
            self.rounded_rectangle(x=x*self.proporcao_largura,y=self.y, largura=largura)
            self.y += self.espacamento_entre_linhas

    def corpo(self): 
        for largura in self.proporcoes_corpo:
           self.rounded_rectangle(y=self.y, largura=largura)
           self.y += self.espacamento_entre_linhas

    def pernas(self,entre_pernas = 40):
        for largura  in [32, 42, 56]:
            direita_x = self.horizontal_center - (largura/ 2)
            self.rounded_rectangle(x = direita_x + entre_pernas, y=self.y,
                    largura=largura)
            self.rounded_rectangle(x = direita_x - entre_pernas, y=self.y,
                    largura=largura)
            self.y += self.espacamento_entre_linhas

    def desenhar(self):
        self.cabeca()
        self.corpo()
        self.pernas(entre_pernas=60)


patolivre = Pato(width=800, height=600)
patolivre.desenhar()

    


mainloop()
