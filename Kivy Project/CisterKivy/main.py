import random
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton
from kivymd.uix.tab import MDTabsBase
from kivy.graphics import Color, Line

Builder.load_string('''
<CanvasWidget>

    canvas:

<RelojWidget>:
    FloatLayout:
        orientation: 'vertical'
        MDTextField:
            id: txtInicio
            hint_text: "Número inicial"
            pos_hint: {"center_x": .99, "center_y": .9}
            max_text_length: 4
            hint_text_color_normal: 0, 0, 0, 1
            font_size:"16dp"

        MDTextField:
            id: txtFin
            hint_text: "Número final"
            pos_hint: {"center_x": 2.5, "center_y": .9}
            max_text_length: 4
            hint_text_color_normal: 0, 0, 0, 1
            font_size:"16dp"
    FloatLayout:
        orientation: 'vertical'
        Label:
            id: lblArabigo
            text: str(round(root.number))
            text_size: self.size
            pos_hint: {"center_x": .4, "center_y": 1}
            color: (0, 0, 1, 1)
            font_size: 50
            font_name: "Comic"
        BoxLayout:
            orientation: 'horizontal'
            spacing: 50
            pos_hint: {"center_x": 0, "center_y": .6}
            MDFillRoundFlatButton:
                text: 'START'
                on_press: root.start()
                text_color: (1, 209 / 255, 60 / 255, 1)  # Azul
                line_color:(1, 209 / 255, 60 / 255, 1) # Amarillo
                md_bg_color:(56/255, 62/255, 241/255, 0.81) # Azul
                font_style: 'Button'

            MDFillRoundFlatButton:
                text: 'STOP'
                on_press: root.stop()
                text_color: (1, 209 / 255, 60 / 255, 1)  # Azul
                line_color:(1, 209 / 255, 60 / 255, 1) # Amarillo
                md_bg_color:(56/255, 62/255, 241/255, 0.81) # Azul
                font_style: 'Button'

            MDFillRoundFlatButton:
                text: 'REINICIAR'
                on_press: root.number = 0
                text_color: (1, 209 / 255, 60 / 255, 1)  # Azul
                line_color:(1, 209 / 255, 60 / 255, 1) # Amarillo
                md_bg_color:(56/255, 62/255, 241/255, 0.81) # Azul
                font_style: 'Button'



    # Create the Label


<MainWidget@MDBoxLayout>:
    orientation: "vertical"
    MDToolbar:
        title: "La orden del Císter"
        md_bg_color: app.theme_cls.primary_dark
    MDTabs:
        text_color_normal: 1, 1, 1, 1
		text_color_active: 1, 209/255, 60/255, 1
		tab_indicator_anim: 'True'
		anim_threshold: 0.5

        Tab:
            id: tabConversor
            title: "Conversor"
            icon: "abjad-hebrew"
            text_icon_color: .2, .2, .2, 1

            MDBoxLayout:
                orientation: "vertical"
                spacing: 370

                MDTextField:
                    id: txt1

                    hint_text: "Introduce un número entre el 1 y el 9999"
                    pos_hint: {"center_x": .99, "center_y": .5}
                    max_text_length: 4
                    hint_text_color_normal: 0, 0, 0, 1
                    font_size:"16dp"
                MDBoxLayout:
                    orientation: "horizontal"
                    id: lobtn



        Tab:
            id: tabContador
            title: "Contador"
            icon: "counter"

        Tab:
            title: "Juego"
            id: tabJuego
            icon: "nintendo-game-boy"
            text_icon_color: .2, .2, .2, 1

            MDTextField:
                id: respuesta
                pos_hint: {"center_x": .5, "center_y": .5}
                max_text_length: 4
                hint_text_color_normal: 0, 0, 0, 1
                font_size:"16dp"
                hint_text: "Acierta el número"




''')
width = 500
height = 700
# dimensiones del movil
# width = 1080
# height = 2250

Window.size = (width, height)

altura = height / 6

x200 = width / 2
x300 = width / 1.34
y100 = height / 6 + altura
y150 = height / 4 + altura
y300 = height / 2 + altura

seg1 = (x200, y100, x200, y300)
seg2 = (x200, y100, x300, y100)
seg3 = (x200, y150, x300, y150)
seg4 = (x200, y100, x300, y150)
seg5 = (x200, y150, x300, y100)
seg6 = (x300, y100, x300, y150)

# Registramos todos los números
num1 = [1, 1, 0, 0, 0, 0]
num2 = [1, 0, 1, 0, 0, 0]
num3 = [1, 0, 0, 1, 0, 0]
num4 = [1, 0, 0, 0, 1, 0]
num5 = [1, 1, 0, 0, 1, 0]
num6 = [1, 0, 0, 0, 0, 1]
num7 = [1, 1, 0, 0, 0, 1]
num8 = [1, 0, 1, 0, 0, 1]
num9 = [1, 1, 1, 0, 0, 1]

numeros = (num1, num2, num3, num4, num5, num6, num7, num8, num9)
segmentos = (seg1, seg2, seg3, seg4, seg5, seg6)


class MiBoton(MDRoundFlatButton):
    pass


class Tab(MDBoxLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class CanvasWidget(Widget):
    pass


class CanvasWidget2(Widget):
    pass


class CanvasWidget3(Widget):
    pass


class RelojWidget(BoxLayout):
    number = NumericProperty()

    # To increase the time / count
    def increment_time(self, interval):
        # txtFin
        self.number += .1
        Example.pinta2(Example(), int(self.number))

    # To start the count
    def start(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)

    # To stop the count / time
    def stop(self):
        Clock.unschedule(self.increment_time)


class Example(MDApp):
    painter = CanvasWidget()
    painter2 = CanvasWidget2()
    painter3 = CanvasWidget3()
    eligeCanvas = 0
    numeroJuego = 0

    def build(self):
        self.theme_cls.primary_palette = "Indigo"

        parent = Factory.MainWidget()

        # desde aqui se llama a la propiedad id de los widgets para declarar los tabs
        tab1 = parent.ids["tabConversor"]
        tab2 = parent.ids["tabContador"]
        tab3 = parent.ids["tabJuego"]

        # desde aqui podemos controlar el estilo de los botones y sus propiedades
        pintabtn = MDFillRoundFlatButton(text='Pinta',
                                         text_color=(1, 209 / 255, 60 / 255, 1),  # Azul
                                         line_color=(1, 209 / 255, 60 / 255, 1),  # Amarillo
                                         md_bg_color=(56 / 255, 62 / 255, 241 / 255, 0.81),  # Azul
                                         font_style='Button',
                                         pos_hint={"center_x": .10, "center_y": .1})

        playbtn = MDFillRoundFlatButton(text='Play',
                                        text_color=(1, 209 / 255, 60 / 255, 1),  # Azul
                                        line_color=(1, 209 / 255, 60 / 255, 1),  # Amarillo
                                        md_bg_color=(56 / 255, 62 / 255, 241 / 255, 0.81),  # Azul
                                        font_style='Button',
                                        pos_hint={"center_x": .10, "center_y": .1})

        checkbtn = MDFillRoundFlatButton(text='Comprobar',
                                         text_color=(1, 209 / 255, 60 / 255, 1),  # Azul
                                         line_color=(1, 209 / 255, 60 / 255, 1),  # Amarillo
                                         md_bg_color=(56 / 255, 62 / 255, 241 / 255, 0.81),  # Azul
                                         font_style='Button',
                                         pos_hint={"center_x": .10, "center_y": .1})

        # desde aqui asignamos el evento al botón
        pintabtn.bind(on_release=self.pinta)
        playbtn.bind(on_release=self.numrandom)
        checkbtn.bind(on_release=self.compruebaRespuesta)
        # aqui se añade el boton al tab (widget padre)
        tab1.add_widget(pintabtn)

        # añadimos el canvas al tab1
        tab1.add_widget(self.painter)

        # le ponemos nombre al Widget reloj
        self.reloj = RelojWidget()

        tab2.add_widget(self.reloj)

        tab2.add_widget(self.painter2)

        tab3.add_widget(self.painter3)
        tab3.add_widget(playbtn)
        tab3.add_widget(checkbtn)

        '''
                tab2 = parent.ids["tabContador"]
                pintabtn2 = MDRoundFlatButton(text='Pinta', line_color=(0, 0, 1, 1))
                pintabtn2.bind(on_release=self.pinta2)
                tab2.add_widget(pintabtn2)
                self.painter2 = CanvasWidget2()
                tab2.add_widget(self.painter2)
                '''

        return parent

    def pinta(self, obj):
        self.eligeCanvas = 1
        self.painter.canvas.clear()
        numero = self.root.ids.txt1.text
        self.calculaCifras(numero)

    def pinta2(self, numerotab2):
        self.eligeCanvas = 2
        self.painter2.canvas.clear()
        self.calculaCifras(numerotab2)

    def numrandom(self, obj):
        self.numeroJuego = random.randint(1, 9999)
        self.eligeCanvas = 3
        self.painter3.canvas.clear()
        print(self.numeroJuego)
        self.calculaCifras(self.numeroJuego)

    def compruebaRespuesta(self, obj):
        resp = int(self.root.ids.respuesta.text)
        numeroCorrecto = self.numeroJuego

        if resp == numeroCorrecto:
            toast("Acierto!!")
        else:
            toast("Fallaste!! - El número correcto era:" + str(numeroCorrecto))

    # hacer que el metodo diferencie en que canvas debe pintar para reutilizar el codigo
    def calculaCifras(self, numero):
        cifras = list(str(numero))
        if 0 < len(cifras) <= 4:
            if len(cifras) == 1:
                self.calcula1(cifras)
            elif len(cifras) == 2:
                self.cacula10(cifras)
            elif len(cifras) == 3:
                self.calcula100(cifras)
            elif len(cifras) == 4:
                self.calcula1000(cifras)

    def calcula1(self, cifras):
        numero1 = cifras[0]
        self.pintaNumero1Kivy(numero1)

    def cacula10(self, cifras):
        numero2 = cifras[0]
        numero1 = cifras[1]
        self.pintaNumero2Kivy(numero2)
        self.pintaNumero1Kivy(numero1)

    def calcula100(self, cifras):
        numero3 = cifras[0]
        numero2 = cifras[1]
        numero1 = cifras[2]
        self.pintaNumero3Kivy(numero3)
        self.pintaNumero2Kivy(numero2)
        self.pintaNumero1Kivy(numero1)

    def calcula1000(self, cifras):
        numero4 = cifras[0]
        numero3 = cifras[1]
        numero2 = cifras[2]
        numero1 = cifras[3]
        self.pintaNumero4Kivy(numero4)
        self.pintaNumero3Kivy(numero3)
        self.pintaNumero2Kivy(numero2)
        self.pintaNumero1Kivy(numero1)

    def pintaNumero1Kivy(self, numero):
        cont1 = 0
        numero3 = int(numero)
        if numero3 == 0:
            print("nothing")
        else:
            num = numeros[(numero3 - 1)]
            for n in num:
                if n == 1:
                    if cont1 > 0:
                        segmod2 = list(segmentos[cont1])
                        if segmod2[1] == y100:
                            segmod2[1] = y300
                        elif segmod2[1] == y150:
                            segmod2[1] = height / 2.4 + altura
                        if segmod2[3] == y100:
                            segmod2[3] = y300
                        elif segmod2[3] == y150:
                            segmod2[3] = height / 2.4 + altura
                        self.pintaCanvas(segmod2)
                    else:
                        self.pintaCanvas(segmentos[cont1])
                cont1 = cont1 + 1

    def pintaNumero2Kivy(self, numero):
        cont4 = 0
        numero4 = int(numero)
        if numero4 == 0:
            print("nothing")
        else:
            num4 = numeros[(numero4 - 1)]
            for n in num4:
                if n == 1:
                    if cont4 > 0:
                        segmod3 = list(segmentos[cont4])
                        if segmod3[0] == segmod3[2]:
                            segmod3[0] = width / 4
                            segmod3[2] = width / 4
                        if segmod3[2] == x300:
                            segmod3[2] = width / 4
                        if segmod3[1] == y100:
                            segmod3[1] = y300
                        elif segmod3[1] == y150:
                            segmod3[1] = height / 2.4 + altura
                        if segmod3[3] == y100:
                            segmod3[3] = y300
                        elif segmod3[3] == y150:
                            segmod3[3] = height / 2.4 + altura
                        self.pintaCanvas(segmod3)
                    else:
                        self.pintaCanvas(segmentos[cont4])
                cont4 = cont4 + 1

    def pintaNumero3Kivy(self, numero):
        cont3 = 0
        num3 = int(numero)
        if num3 == 0:
            print("nothing")
        else:
            numero3 = numeros[(num3 - 1)]
            for n in numero3:
                if n == 1:
                    self.pintaCanvas(segmentos[cont3])
                cont3 = cont3 + 1

    def pintaNumero4Kivy(self, numero):
        cont2 = 0
        numero2 = int(numero)
        if numero2 == 0:
            print("nothing")
        else:
            num2 = numeros[(numero2 - 1)]
            for n in num2:
                if n == 1:
                    if cont2 > 0:
                        segmod = list(segmentos[cont2])
                        if segmod[0] == segmod[2]:
                            segmod[0] = width / 4
                            segmod[2] = width / 4
                        else:
                            segmod[2] = width / 4
                        self.pintaCanvas(segmod)
                    else:
                        self.pintaCanvas(segmentos[cont2])
                cont2 = cont2 + 1

    def pintaCanvas(self, seg):
        # aqui se evalúa si tenemos que pintar en el tab correspondiente
        # mediante el valor de eligeCanvas si es 1, 2 o 3 para
        # pintar en cada espacio que le toque
        if self.eligeCanvas == 1:
            with self.painter.canvas:
                self.lineador(seg)
        elif self.eligeCanvas == 2:
            with self.painter2.canvas:
                # este es el color de la linea que se pinta
                segCont = (seg[0] + width / 6, seg[1], seg[2] + width / 6, seg[3])
                self.lineador(segCont)
        elif self.eligeCanvas == 3:
            with self.painter3.canvas:
                # este es el color de la linea que se pinta
                self.lineador(seg)

    def lineador(self, seg):
        # este es el color de la linea que se pinta
        Color(203 / 255, 205 / 255, 1, 1)
        Line(points=[seg], width=10)


if __name__ == '__main__':
    Example().run()
