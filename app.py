import tkinter
from tkinter import font
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Practica1 - LFP")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ create two frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_left.grid(row=0,column=0,sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        # ============ frame_left ============
        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.options = customtkinter.CTkLabel(master=self.frame_left,text="Opciones",text_font=("Roboto Medium",16))
        self.options.grid(row=1,column=0,pady=10, padx=10)

        self.fileUpload = customtkinter.CTkButton(master=self.frame_left,text="Cargar Archivos",command=self.button_event)
        self.fileUpload.grid(row=2,column=0,pady=10,padx=20)

        self.manageCourses = customtkinter.CTkButton(master=self.frame_left,text="Gestionar Cursos",command=self.button_event)
        self.manageCourses.grid(row=3,column=0,pady=10,padx=20)

        self.credits = customtkinter.CTkButton(master=self.frame_left,text="Conteo de Creditos",command=self.button_event)
        self.credits.grid(row=4,column=0,pady=10,padx=20)

        self.credits = customtkinter.CTkButton(master=self.frame_left,text="Salir",fg_color="#D35B58",hover_color="#C77C78",command=self.quit)
        self.credits.grid(row=9,column=0,pady=10,padx=20)

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.data = customtkinter.CTkLabel(master=self.frame_right,text="Lenguajes Formales y de Programación\n" +"Brandon Andy J. Tejaxún Pichiyá\n" +"202112030",height=100,corner_radius=6,fg_color=("white", "gray38"),justify=tkinter.LEFT)
        self.data.grid(column=0,row=0,columnspan=2,rowspan=4,sticky="nwe",padx=20,pady=20)
        self.data.config(font=('Roboto Medium',13))

    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
