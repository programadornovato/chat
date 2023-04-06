from rivescript import RiveScript
from tkinter import *
from tkinter import ttk

'''
Objeto Chat se encarga de crear el formulario, 
recibir las preguntas y responderlas con inteligencia artificial
'''
class Chat:
    def __init__(self,ventana):
        #Inicializamos la inteligencia artificial de Rivescript
        self.bot = RiveScript()
        self.bot.load_file('ejemplo.rive')
        self.bot.sort_replies()

        #Inicializamos la ventana de tipo GUI
        self.ventana=ventana
        self.ventana.title("ChatBot")
        #Creamos un marco que contendra los diferentes elementos
        marco=LabelFrame(self.ventana,text="ChatBot")
        marco.grid(row=0,column=0,columnspan=3,pady=20)
        #Creamos un label que tendra con el texto Respuestas
        Label(marco,text="Respuestas").grid(row=0,column=0)
        #Colocamos un elemento Text para mostrar las respuestas
        self.entRespuesta=Text(marco)
        self.entRespuesta.grid(row=0,column=1,padx=10,pady=10,ipady=60)
        self.entRespuesta.focus()
        #Colocamos un entry para recibir las Preguntas
        Label(marco,text="Preguntas").grid(row=1,column=0)
        self.entPregunta=Entry(marco)
        self.entPregunta.grid(row=1,column=1,padx=10,pady=10,ipady=7,ipadx=120)
        self.entPregunta.bind('<Return>', self.preguntar)
        self.entPregunta.focus()
        #Colocamos un boton la funcion preguntar que recibira una pregunta y retornara una respuesta gestionada por la IA
        btnPreguntarCrear=Button(marco,text="Preguntar",command=self.preguntar,bg="green",fg="white")
        btnPreguntarCrear.grid(row=2,columnspan=2,sticky=W+E)

    #Funcion que leera el entry entPregunta que generara un respuesta via rivescript y se muestra en entRespuesta
    def preguntar(self,event=None):
        reply = self.bot.reply("localuser", self.entPregunta.get())
        reply = reply.replace("\\n", "\\\n")
        reply = reply.replace("\\", "")
        self.entRespuesta.insert(END,"Tu: "+self.entPregunta.get()+"\n\n")
        self.entRespuesta.insert(END,"Bot: "+reply+"\n")
        self.entPregunta.delete(0,END)

if __name__=="__main__":
    ventana=Tk()
    Chat(ventana)
    ventana.mainloop()
