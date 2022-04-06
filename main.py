from tkinter import StringVar, filedialog
import update_visualmenu
import tkinter as tk
import configparser
import create_menu
import tkclass
import os

cfg = configparser.ConfigParser()
button_color = (100, 100, 100)
if os.path.exists('config.ini'):
    cfg.read('config.ini')
    defaultbinds = ['', '', '', '', '', '', '', '', '', '']
    defaultbinds[0] = cfg['DEFAULTBINDS']['key1']
    defaultbinds[1] = cfg['DEFAULTBINDS']['key2']
    defaultbinds[2] = cfg['DEFAULTBINDS']['key3']
    defaultbinds[3] = cfg['DEFAULTBINDS']['key4']
    defaultbinds[4] = cfg['DEFAULTBINDS']['key5']
    defaultbinds[5] = cfg['DEFAULTBINDS']['key6']
    defaultbinds[6] = cfg['DEFAULTBINDS']['key7']
    defaultbinds[7] = cfg['DEFAULTBINDS']['key8']
    defaultbinds[8] = cfg['DEFAULTBINDS']['key9']
    defaultbinds[9] = cfg['DEFAULTBINDS']['key0']
    binds = ['', '', '', '', '', '', '']
    binds[0] = cfg['BINDS']['key1']
    binds[1] = cfg['BINDS']['key2']
    binds[2] = cfg['BINDS']['key3']
    binds[3] = cfg['BINDS']['key4']
    binds[4] = cfg['BINDS']['key5']
    binds[5] = cfg['BINDS']['key6']
    binds[6] = cfg['BINDS']['key7']
    folder = cfg['CONFIG']['folder']
    tf_dir = cfg['CONFIG']['tf_dir']
    is_lastpage = cfg['CONFIG']['is_lastpage'].lower()
    if is_lastpage == 'true':
        is_lastpage = True
    else:
        is_lastpage = False
    number = cfg['CONFIG']['number']
    prefix = cfg['CONFIG']['prefix']
else:
    prefix = ''
    folder = ''
    number = ''
    tf_dir = 'C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf'
    is_lastpage = False
    defaultbinds = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7', 'slot8', 'slot9', 'slot10']
    binds = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7']

directory = None
def searchdir(v):
    directory = filedialog.askdirectory(title='Select Folder')
    v[0].delete(0,tk.END)
    v[0].insert(0,directory)

def createmenu():
    dict_var1_configpath = {}
    dict_var1_configpath['DEFAULTBINDS'] = {}
    dict_var1_configpath['CONFIG'] = {}
    dict_var1_configpath['BINDS'] = {}
    
    cfg['DEFAULTBINDS'] = {}
    cfg['CONFIG'] = {}
    cfg['BINDS'] = {}

    for i in range(10):
        cfg['DEFAULTBINDS'][f'key{i}'] = app.get_entry_by_name(f'entry_var1_defaultbinds{i}')[0].get()
        dict_var1_configpath['DEFAULTBINDS'][f'key{i}'] = app.get_entry_by_name(f'entry_var1_defaultbinds{i}')[0].get()
    for i in range(7):
        cfg['BINDS'][f'key{i+1}'] = app.get_entry_by_name(f'entry_var1_binds{i}')[0].get()
        dict_var1_configpath['BINDS'][f'key{i+1}'] = app.get_entry_by_name(f'entry_var1_binds{i}')[0].get()

    cfg['CONFIG']['prefix'] = app.get_entry_by_name('entry_var1_prefix')[0].get()
    cfg['CONFIG']['folder'] = app.get_entry_by_name('entry_var1_folder')[0].get()
    cfg['CONFIG']['number'] = app.get_entry_by_name('entry_var1_number')[0].get()
    cfg['CONFIG']['tf_dir'] = app.get_entry_by_name('entry_var1_searchdir')[0].get()
    cfg['CONFIG']['is_lastpage'] = str(is_lastpage).lower()
    with open('config.ini', 'w') as f:
        cfg.write(f)
    dict_var1_configpath['CONFIG'] = {}
    dict_var1_configpath['CONFIG']['tf_dir'] = app.get_entry_by_name('entry_var1_searchdir')[0].get()
    dict_var1_configpath['CONFIG']['prefix'] = app.get_entry_by_name('entry_var1_prefix')[0].get()
    dict_var1_configpath['CONFIG']['folder'] = app.get_entry_by_name('entry_var1_folder')[0].get()
    dict_var1_configpath['CONFIG']['number'] = app.get_entry_by_name('entry_var1_number')[0].get()
    dict_var1_configpath['CONFIG']['is_lastpage'] = str(is_lastpage).lower()

    create_menu.main(tf_dir=app.get_entry_by_name('entry_var1_searchdir')[0].get(), conf=dict_var1_configpath, configpathway=False)

def change_lastpage():
    global is_lastpage, islastpage_bg
    button = app.get_button_by_name('button_var1_islastpage')
    if islastpage_bg == (255, 0, 0):
        islastpage_bg = (0, 255, 0)
        is_lastpage = True
        button[0].config(activebackground=app._from_rgb(islastpage_bg), background=app._from_rgb(islastpage_bg))
    else:
        islastpage_bg = (255, 0, 0)
        is_lastpage = False
        button[0].config(activebackground=app._from_rgb(islastpage_bg), background=app._from_rgb(islastpage_bg))

def updatemenu():
    update_visualmenu.main(app.get_entry_by_name('entry_var2_searchdir')[0].get(), app.get_entry_by_name('entry_var2_folder')[0].get())

def forget(var):
    try:
        if var == 1:
            app.delete_widget_by_list(app.get_button_by_name('button_var1_create'), app.button)
            app.delete_widget_by_list(app.get_entry_by_name('entry_var1_searchdir'), app.entry)
            app.delete_widget_by_list(app.get_button_by_name('button_var1_searchdir'), app.button)
            app.delete_widget_by_list(app.get_label_by_name('label_var1_searchdir'), app.label)
            app.delete_widget_by_list(app.get_label_by_name('label_var1_defaultbinds'), app.label)
            app.delete_widget_by_list(app.get_label_by_name('label_var1_binds'), app.label)
            app.delete_widget_by_list(app.get_label_by_name('label_var1_prefix'), app.label)
            app.delete_widget_by_list(app.get_label_by_name('label_var1_number'), app.label)
            app.delete_widget_by_list(app.get_label_by_name('label_var1_folder'), app.label)
            app.delete_widget_by_list(app.get_entry_by_name('entry_var1_prefix'), app.entry)
            app.delete_widget_by_list(app.get_entry_by_name('entry_var1_number'), app.entry)
            app.delete_widget_by_list(app.get_entry_by_name('entry_var1_folder'), app.entry)
            app.delete_widget_by_list(app.get_button_by_name('button_var1_islastpage'), app.button)

            for i in range(10):
                app.delete_widget_by_list(app.get_entry_by_name(f'entry_var1_defaultbinds{i}'), app.entry)
                app.delete_widget_by_list(app.get_label_by_name(f'label_var1_defaultbinds{i}'), app.label)

            for i in range(7):
                app.delete_widget_by_list(app.get_entry_by_name(f'entry_var1_binds{i}'), app.entry)
                app.delete_widget_by_list(app.get_label_by_name(f'label_var1_binds{i}'), app.label)
        if var == 2:
            app.delete_widget_by_list(app.get_label_by_name('label_var2_searchdir'), app.label)
            app.delete_widget_by_list(app.get_label_by_name('label_var2_folder'), app.label)
            app.delete_widget_by_list(app.get_button_by_name('button_var2_create'), app.button)
            app.delete_widget_by_list(app.get_button_by_name('button_var2_searchdir'), app.button)
            app.delete_widget_by_list(app.get_entry_by_name('entry_var2_searchdir'), app.entry)
            app.delete_widget_by_list(app.get_entry_by_name('entry_var2_folder'), app.entry)
    except:
        pass
selected_var = None
def create_label(var):
    global selected_var
    if var == 1 and selected_var != 1:
        selected_var = 1
        forget(2)
        sv_var1_searchdir = StringVar()
        app.create_button(buttonname='button_var1_create', text='Create', bg=button_color, command=createmenu, x=w//2-50, y=h//2+135, font='Arial 10', width=6, height=1)
        app.create_label(labelname='label_var1_searchdir', text='tf folder:', width=8, bg=app_background, x=30, y=100, fg=(255, 255, 255))
        app.create_entry(entryname='entry_var1_searchdir', x=100, y=100, textvariable=sv_var1_searchdir, bd=1, width=33, font='Arial 10')[0].insert(0, tf_dir)
        app.create_button(buttonname='button_var1_searchdir', text='Search', bg=button_color, command=lambda: searchdir(app.get_entry_by_name('entry_var1_searchdir')), x=340, y=100, font='Arial 10', width=6)
        
        app.create_label(labelname='label_var1_defaultbinds', text='DEFAULT BINDS', x=100, y=(h//2-70), width=16)
        app.create_label(labelname='label_var1_binds', text='MENU BINDS', x=240, y=(h//2-70), width=16)
        
        sv_var1_folder = StringVar()
        app.create_entry(entryname='entry_var1_folder', textvariable=sv_var1_folder, font='Arial 9', x=290, y=h//2+76, width=12)
        app.create_label(labelname='label_var1_folder', font='Arial 9', x=237, y=h//2+76, text='Folder')
        
        sv_var1_prefix = StringVar()
        app.create_entry(entryname='entry_var1_prefix', textvariable=sv_var1_prefix, font='Arial 9', x=290, y=h//2+94, width=5)
        app.create_label(labelname='label_var1_prefix', font='Arial 9', x=237, y=h//2+94, text='Prefix')

        sv_var1_number = StringVar()
        app.create_entry(entryname='entry_var1_number', textvariable=sv_var1_number, font='Arial 9', x=290, y=h//2+112, width=3)
        app.create_label(labelname='label_var1_number', font='Arial 9', x=237, y=h//2+112, text='Page')

        app.get_entry_by_name('entry_var1_folder')[0].insert(0, folder)
        app.get_entry_by_name('entry_var1_prefix')[0].insert(0, prefix)
        app.get_entry_by_name('entry_var1_number')[0].insert(0, number)

        app.create_button(buttonname='button_var1_islastpage', font='Arial 10', x=w//2+50, y=h//2+135, text='Last Page', height=1, width=8, bg=islastpage_bg, activebg=islastpage_bg, command=change_lastpage)

        defaultbinds_string = {}
        for i in range(10):
            defaultbinds_string[i] = StringVar()            
            app.create_entry(entryname=f'entry_var1_defaultbinds{i}', textvariable=defaultbinds_string[i], font='Arial 9', width=12, x=150, y=(h//2-50)+(i*18))
            x = app.get_entry_by_name(f'entry_var1_defaultbinds{i}')[0]
            if i == 0:
                x.insert(0, defaultbinds[-1])
            else:
                x.insert(0, defaultbinds[i-1])
            if i == 0 or i < 10:
                app.create_label(labelname=f'label_var1_defaultbinds{i}', font='Arial 9', text=f'key{i}', x=97, y=(h//2-50)+(i*18))
            else:
                app.create_label(labelname=f'label_var1_defaultbinds{i}', font='Arial 9', text=f'key{i+1}', x=97, y=(h//2-50)+(i*18))
        binds_string = {}
        for i in range(7):
            binds_string[i] = StringVar()
            app.create_entry(entryname=f'entry_var1_binds{i}', textvariable=binds_string[i], font='Arial 9', width=12, x=290, y=(h//2-50)+(i*18))
            x = app.get_entry_by_name(f'entry_var1_binds{i}')[0]
            x.delete(0, tk.END)
            x.insert(0, binds[i])
            app.create_label(labelname=f'label_var1_binds{i}', font='Arial 9', text=f'key{i+1}', x=237, y=(h//2-50)+(i*18))

    if var == 2 and selected_var != 2:
        selected_var = 2
        forget(1)
        sv_var2_searchdir = StringVar()
        app.create_button(buttonname='button_var2_create', text='Update', bg=button_color, command=updatemenu, x=250, y=125, font='Arial 10', width=6, height=1)
        app.create_label(labelname='label_var2_searchdir', text='tf folder:', width=8, bg=app_background, x=30, y=100, fg=(255, 255, 255))
        app.create_entry(entryname='entry_var2_searchdir', x=100, y=100, textvariable=sv_var2_searchdir, bd=1, width=33, font='Arial 10')[0].insert(0, tf_dir)
        app.create_button(buttonname='button_var2_searchdir', text='Search', bg=button_color, command=lambda: searchdir(app.get_entry_by_name('entry_var2_searchdir')), x=340, y=100, font='Arial 10', width=6)
        sv_var2_folder = StringVar()
        app.create_entry(entryname='entry_var2_folder', textvariable=sv_var2_folder, font='Arial 9', x=154, y=125, width=12)
        app.create_label(labelname='label_var2_folder', font='Arial 9', x=100, y=125, text='Folder')

def select():
    if int(var.get()) == 1:
        create_label(1)
    if int(var.get()) == 2:
        create_label(2)

w, h = 400, 400
islastpage_bg = (255, 0, 0)
is_lastpage = False
root = tk.Tk()
app = tkclass.Application(root)
app_background = (40, 40, 40)
app.config(title='Create Menu V2.0', icon='icon.ico', resizable=False, width=w, height=h, bgcolor=app_background)
var = tk.IntVar()
R1 = app.create_radio(radioname='radio_v1', x=15, y=10, command=select, text='Create menu', bg=app_background, width=10, activebackground=button_color, activeforeground=(255, 255, 255), fg=(255, 255, 255), highlightbackground=(255, 255, 255), highlightcolor=(255, 255, 255), selectcolor=(255, 255, 255),variable=var, value=1)
R2 = app.create_radio(radioname='radio_v2', x=14, y=30, command=select, text='Update \"visual\" menu', width=17, bg=app_background, activebackground=button_color, activeforeground=(255, 255, 255), fg=(255, 255, 255), highlightbackground=(255, 255, 255), highlightcolor=(255, 255, 255), selectcolor=(255, 255, 255), variable=var, value=2)

app.mainloop()