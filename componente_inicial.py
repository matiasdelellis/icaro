import os
import pygame

class componente_inicial(pygame.sprite.Sprite):
    """
    el componente inicial no tiene conector hembra porque SIEMPRE va a 
    a tener el ide=0
    """
    pulsado=0
    posicion=(0,0)
    rectan=pygame.Rect(0,0,60,60)#rectangulo que representa toda el area del componente
    conector_m=pygame.Rect(0,0,40,10)#conector macho
    ide=0
    color=(80,00,80)
    
    posic_rel_x=0
    posic_rel_y=0
    def __init__(self,x,y,identidad,fondo,ventana,texto):
        pygame.sprite.Sprite.__init__(self)
        #self.imagen=pygame.image.load("imagenes/componentes/inicial.png")
        
        self.ide=identidad
        self.posicion=(x,y)
        self.fondo=fondo
        self.ventana=ventana
        self.texto=texto
        self.fondo.lista_cm.append((0,0,0,0))
        self.fondo.lista_ch.append((0,0,0,0))
        self.fondo.lista_ch_dato.append((0,0,0,0))
        self.fondo.lista_ordenada.append(0)
        self.fondo.lista_fina.append(0)
        self.color_texto=self.fondo.color_texto
    def dibujar(self):
        #self.fondo.screen.blit(self.imagen,self.posicion)
        # el cuerpo del componente
        pygame.draw.rect(self.fondo.screen,self.color,(self.posicion[0],self.posicion[1], 60,40),0)

        # el conector macho
        pygame.draw.rect(self.fondo.screen,self.color,(self.posicion[0]+10,self.posicion[1]+40, 40,10),0)
#        texto.render(str(self.ide),self.color_texto,((self.posicion[0]+10),(self.posicion[1]+10)))
        self.texto.render("inicio",self.color_texto,((self.posicion[0]+10),(self.posicion[1]+10)))

    def update(self):
        posic_mouse= self.ventana.mousexy
        botones_mouse = self.ventana.boton_mouse
        # self.rectan es el rect que representa la totalidad de la figura 
        self.rectan[0]=self.posicion[0]
        self.rectan[1]=self.posicion[1]-10
        # self.conector_m es la ficha "macho"
        self.conector_m[0]=self.rectan[0]+10
        self.conector_m[1]=self.rectan[1]+50
        #cargo la lista de los dos conectores hembra y macho
        self.fondo.lista_cm[self.ide]=(self.conector_m[0],self.conector_m[1],self.conector_m[2],self.conector_m[3])
        if botones_mouse[1]==1 and self.rectan.collidepoint(posic_mouse[0],posic_mouse[1]) and self.pulsado==0:
            self.posic_rel_x=abs(self.posicion[0]-posic_mouse[0])  
            self.posic_rel_y=abs(self.posicion[1]-posic_mouse[1])
            self.pulsado=1
        if botones_mouse[1]==1 and self.rectan.collidepoint(posic_mouse[0],posic_mouse[1]):
            self.posicion=(posic_mouse[0]-self.posic_rel_x,posic_mouse[1]-self.posic_rel_y)
            self.pulsado==1
        if botones_mouse[1]==0:
            self.pulsado=0
        self.dibujar()
        pygame.display.update

