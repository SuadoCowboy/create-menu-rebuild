import tkinter as tk
from tkinter import ttk
import os

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.button = []
        self.buttonnumber = -1
        self.label = []
        self.labelnumber = -1
        self.entry = []
        self.entrynumber = -1
        self.radio = []
        self.radionumber = -1
    def config(self, width=400, height=300, title='Main', bgcolor=(255, 255, 255), bgimg=None, icon=None, style='xpnative', assets_folder=None, resizable=True):
        self.width = width
        self.height = height
        self.master.geometry(f"{width}x{height}")
        self.master.title(title)
        self.style = ttk.Style(self.master)
        self.style.theme_use(style)
        if icon is not None and assets_folder is not None:
            self.master.iconbitmap(os.path.join(assets_folder, icon))
        elif icon is not None and assets_folder is None:
            self.master.iconbitmap(icon)
        if resizable == False:
            self.master.resizable(False, False)
        if bgimg != None:
            self.background_image = background_image = tk.PhotoImage(file=bgimg)
            self.background_label = background_label = tk.Label(self.master, image=background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            self.master.configure(bg=self._from_rgb(bgcolor))
    def _from_rgb(self, rgb):
            r, g, b = rgb
            return f'#{r:02x}{g:02x}{b:02x}'
    def print_button_pressed():
        print('Button pressed')
    def num(self, numm):
        numm += 1
        return numm
    def create_button(self, buttonname=None, text="Button", fg=(0, 0, 0), activefg=(0, 0, 0), bg=(255, 255, 255), bd=0, activebg=(255, 255, 255), font='Arial 12', command=print_button_pressed, x=None, y=None, width=4, height=1):
        if x is None:
            x = self.width//2
        if y is None:
            y = self.height//2
        if buttonname is None:
            buttonname = f'Button_Default {self.num(self.buttonnumber)}'
            self.buttonnumber += 1
        self.button.append([tk.Button(text=text, fg=self._from_rgb(fg), bg=self._from_rgb(bg), bd=bd, font=font, activebackground=self._from_rgb(activebg), activeforeground=self._from_rgb(activefg), command=command, width=width, height=height), buttonname])
        self.button[-1][0].place(x=x, y=y)
        return self.button[-1]
    def create_label(self, labelname=None, text='Text Here', fg=(0, 0, 0), bg=(255, 255, 255), bd=0, x=5, y=5, font='Arial 10',width=7, height=1):
        if labelname is None:
            labelname = f'Label_Default {self.num(self.labelnumber)}'
            self.labelnumber += 1
        self.label.append([tk.Label(self.master, fg=self._from_rgb(fg), font=font, bg=self._from_rgb(bg), bd=bd, width=width, height=height), labelname])
        if text is not None:
            self.label[-1][0].configure(text=text)
        self.label[-1][0].place(x=x, y=y)
        return self.label[-1]
    def create_entry(self, entryname=None, bg=(255, 255, 255), fg=(0, 0, 0), bd=0, font="Arial 24", highlightcolor=(0, 0, 0), justify='left', width=5, x=250, y=250, textvariable=None):
        if entryname is None:
            entryname = f'Entry_Default {self.num(self.entrynumber)}'
            self.entrynumber += 1
        self.entry.append([tk.Entry(self.master, bg=self._from_rgb(bg), fg=self._from_rgb(fg), bd=bd, font=font, highlightcolor=self._from_rgb(highlightcolor), justify=justify, width=width), entryname])
        if textvariable is not None:
            self.entry[-1][0].configure(textvariable=textvariable)
        self.entry[-1][0].place(x=x, y=y)
        return self.entry[-1]
    def create_radio(self, radioname=None, bg=(255, 255, 255), activebackground=(255, 255, 255), activeforeground=(0, 0, 0), bitmap=None, borderwidth=0, command=None, font='Arial 8', fg=(0, 0, 0), width=7, height=1, highlightbackground=(255, 255, 255), highlightcolor=(0, 0, 0), image=None, justify='center', x=0, y=0, selectcolor=(255, 0, 0), state=tk.NORMAL, text='Text Here', variable=None, value=0, selectimage=None):
        if radioname is None:
            radioname = f'Radio_Default {self.num(self.radionumber)}'
            self.entrynumber += 1
        self.radio.append([tk.Radiobutton(self.master, bg=self._from_rgb(bg), activebackground=self._from_rgb(activebackground), activeforeground=self._from_rgb(activeforeground), text=text, borderwidth=borderwidth, font=font, fg=self._from_rgb(fg), width=width, height=height, highlightbackground=self._from_rgb(highlightbackground), highlightcolor=self._from_rgb(highlightcolor), justify=justify, selectcolor=self._from_rgb(selectcolor), state=state, variable=variable, value=value), radioname])
        if bitmap is not None:
            self.radio[-1][0].configure(bitmap=bitmap)
        if command is not None:
            self.radio[-1][0].configure(command=command)
        if image is not None:
            self.radio[-1][0].configure(image=image)
        if selectimage is not None:
            self.radio[-1][0].configure(selectimage=selectimage)
        self.radio[-1][0].place(x=x, y=y)
        return self.radio[-1]
    def get_button_by_name(self, name):
        for buttons in self.button:
            if buttons[1] == name:
                return buttons
    def get_label_by_name(self, name):
        for labels in self.label:
            if labels[1] == name:
                return labels
    def get_entry_by_name(self, name):
        for entrys in self.entry:
            if entrys[1] == name:
                return entrys
    def get_radio_by_name(self, name):
        for radios in self.radio:
            if radios[1] == name:
                return radios
    def get_button_by_id(self, ID):
        return (self.button[ID], ID)
    def get_label_by_id(self, ID):
        return (self.label[ID], ID)
    def get_entry_by_id(self, ID):
        return (self.entry[ID], ID)
    def get_radio_by_id(self, ID):
        return (self.entry[ID], ID)
    def character_limit(self, entry_text, limit=0, char_limit=-1):
        if len(entry_text.get()) > limit:
            string = entry_text.get()[char_limit]
            entry_text.set(string)
    def delete_widget_by_list(self, widget, listt):
        widget[0].destroy()
        for index,widgett in enumerate(listt):
            if widgett[1] == widget[1] and widgett[0] == widget[0]:
                listt.pop(index)