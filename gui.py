from game import *
from gui_map import *
from room import *
import time
import shelve


class Gui:
    def __init__(self):
        self.root = Tk()
        self.timer_start = 0
        self.root.title("TextAdventure")
        self.root.geometry('1120x620')
        self.root.configure(background='#ADD8E6')
        self.root.resizable(0, 0)
        self.frame1 = Frame(self.root)
        self.frame1.configure(background='#ADD8E6')
        self.frame2 = Frame(self.root)
        self.frame2.configure(background='#ADD8E6')
        self.frame3 = Frame(self.frame2)
        self.frame4 = Frame(self.frame2)
        self.frame3.configure(background='#ADD8E6')
        self.frame4.configure(background='#ADD8E6')
        self.frame5 = Frame(self.frame4)
        self.frame5.configure(background='#ADD8E6')
        self.frame3.pack(side=TOP)
        self.frame4.pack(side=BOTTOM)
        self.frame1.pack(side=LEFT)
        self.frame2.pack(side=RIGHT)
        self.frame5.pack(side=BOTTOM)
        self.label2 = Label(self.frame4, text="Direzioni", fg="black", bg='#ADD8E6')
        self.label2.pack()
        self.scr = Scrollbar(self.frame1)
        self.scr.pack(side=RIGHT, fill=Y)
        self.tx1 = Text(self.frame1, bg="black", bd=3, fg="green", height=40, width=110, yscrollcommand=self.scr.set,
                        wrap=WORD)
        self.can1 = Canvas(self.frame2, bg="black", height=180, width=220)
        self.can1.pack(anchor=E)
        self.ga = Game(self.tx1, self.timer_start)
        self.map = Map(self.can1, self.ga.newchar.position.id)
        self.tx1.pack(fill=BOTH, expand=1)
        self.tx1.tag_configure('color', foreground='#476045', font=('Tempus Sans ITC', 12, 'bold'))
        self.tx1.tag_configure('color2', foreground='#708090', font=('Tempus Sans ITC', 12, 'bold'))
        self.tx1.tag_configure('color3', foreground='#FA8072', font=('Tempus Sans ITC', 12, 'bold'))
        self.tx1.tag_configure('color5', foreground='#BAA135', font=('Tempus Sans ITC', 12, 'bold'))
        self.tx1.pack(side=LEFT)
        self.scr.config(command=self.tx1.yview)
        self.btn1 = Button(self.frame4, text="N", fg="#CC0033", bg='#589796',  relief=GROOVE, width=2,
                           command=lambda: self.nord_map()).pack(anchor=CENTER)
        self.btn2 = Button(self.frame4, text="S", fg="#CC0033", bg='#589796',  relief=GROOVE, width=2,
                           command=lambda: self.sud_map()).pack(side=BOTTOM)
        self.btn3 = Button(self.frame4, text="W", fg="#CC0033", bg='#589796',  relief=GROOVE, width=2,
                           command=lambda: self.west_map()).pack(side=LEFT)
        self.btn4 = Button(self.frame4, text="E", fg="#CC0033", bg='#589796',  relief=GROOVE, width=2,
                           command=lambda: self.est_map()).pack(side=RIGHT)
        self.btn11 = Button(self.frame4, text="UP", fg="#CC0033", bg='#589796', relief=GROOVE,  width=2,
                            command=lambda: self.up_map()).pack(anchor=CENTER)
        self.btn12 = Button(self.frame4, text="DW", fg="#CC0033", bg='#589796',  relief=GROOVE, width=2,
                            command=lambda: self.down_map()).pack(anchor=CENTER)
        self.label4 = Label(self.frame5, text="Comandi", fg="black", bg='#ADD8E6').pack()
        self.btn5 = Button(self.frame5, text="Combina", fg='#8A0707', bg='#589796', width=8, relief=GROOVE,
                           command=lambda: self.comb()).pack()
        self.btn7 = Button(self.frame5, text="Esamina", fg='#8A0707', bg='#589796',  width=8, relief=GROOVE,
                           command=lambda: self.exami()).pack()
        self.btn13 = Button(self.frame5, text="Inventario", fg='#8A0707', bg='#589796',  width=8, relief=GROOVE,
                            command=lambda: self.inv()).pack()
        self.btn8 = Button(self.frame5, text="Osserva", fg='#8A0707', bg='#589796',  width=8, relief=GROOVE,
                           command=lambda: self.oxe()).pack()
        self.btn9 = Button(self.frame5, text="Prendi", fg='#8A0707', bg='#589796',  width=8, relief=GROOVE,
                           command=lambda: self.prn()).pack()
        self.btn10 = Button(self.frame5, text="Usa", fg='#8A0707', bg='#589796',  width=8, relief=GROOVE,
                            command=lambda: self.ux()).pack()
        self.btn15 = Button(self.frame5, text="Salva", fg='#8A0707', bg='#589796',  width=8, relief=GROOVE,
                            command=lambda: self.save_game()).pack()
        self.btn16 = Button(self.frame5, text="Carica", fg='#8A0707', bg='#589796',  width=8, relief=GROOVE,
                            command=lambda: self.load_game()).pack()
        self.btn14 = Button(self.frame5, text="Esci", fg='#8A0707', bg='#589796',  width=8, relief=GROOVE,
                            command=lambda: self.esc(self.root)).pack()
        self.timer_start = time.time()
        self.ga.newchar.call_events('e0', self.tx1)
        self.ga.__init__(self.tx1, self.timer_start)
        self.ga.look(self.tx1)
        mainloop()

    def esc(self, w):
        r = Tk()
        r.geometry('190x80')
        r.title('TextAdventure')
        r.configure(background='#ADD8E6')
        r.resizable(0, 0)
        Label(r, text="Sei sicuro di voler uscire?", fg="red", bg='#ADD8E6').pack(anchor=CENTER)
        Button(r, text="SI", fg="white", bg='#589796', width=4, command=lambda: self.esc_cmd(w, r)).pack(anchor=CENTER)
        Button(r, text="NO", fg="white", bg='#589796', width=4, command=lambda: r.destroy()).pack(anchor=CENTER)

    def esc_cmd(self, w, w2):
        w2.destroy()
        r = Tk()
        r.geometry('190x40')
        r.title('TextAdventure')
        r.configure(background='#ADD8E6')
        r.resizable(0, 0)
        Label(r, text="Grazie per aver giocato! :-)", fg="red", bg='#ADD8E6').pack(anchor=CENTER)
        Button(r, text="Esci", fg="red", bg='#589796', command=lambda: r.destroy()).pack(anchor=CENTER)
        w.destroy()
        self.ga.do_esci()

    def prn(self):
        r = Tk()
        r.title('Prendi')
        r.geometry('140x130')
        r.configure(background='#ADD8E6')
        r.resizable(0, 0)
        a1 = self.ga.loc.items
        if len(a1) != 0:
            a0 = self.ga.newchar.items
            a2 = self.ga.newchar.used
            a3 = a0 + a2
            b1 = []
            for i in range(len(a1)):
                if a1[i] not in a3:
                    b1.append(a1[i])
            buttons = []
            for j in range(len(b1)):
                b = Button(r, text=b1[j], fg="white", bg='#589796', width=20, command=lambda j=j: self.prn_cmd(r, b1[j]))
                b.pack(anchor=CENTER)
                buttons.append(b)
            r.mainloop()
        else:
            Label(r, text="STANZA VUOTA.", fg="red", bg='#ADD8E6').pack(anchor=CENTER)

    def prn_cmd(self, wn, it):
        self.ga.do_prendi(str(it))
        wn.destroy()

    def inv(self):
        r = Tk()
        r.title("Inventario")
        r.geometry('200x180')
        r.configure(background='#ADD8E6')
        r.resizable(0, 0)
        a = self.ga.newchar.items
        scr = Scrollbar(r)
        scr.pack(side=RIGHT, fill=Y)
        t = Text(r, bg="black", bd=3, fg="green", height=40, width=70, yscrollcommand=scr.set, wrap=WORD)
        t.tag_configure('color4', foreground='#BAA135', justify=CENTER, font=('Tempus Sans ITC', 10, 'bold'))
        t.pack(side=LEFT)
        scr.config(command=t.yview)
        for i in range(len(a)):
            t.insert(END, str(a[i]), 'color4')
            t.insert(END, "\n")
        Button(r, text='Ok', fg='red', command=lambda: r.destroy()).pack(anchor=CENTER)

    def comb(self):
        r = Tk()
        r.title('Combina')
        r.geometry('320x200')
        r.configure(background='#ADD8E6')
        r.resizable(0, 0)
        Label(r, text="SCEGLI DUE OGGETTI DA COMBINARE TRA LORO", fg="red", bg='#ADD8E6').pack()
        a = self.ga.newchar.items
        if len(a) != 0:
            var = StringVar(r)
            var.set('Primo Oggetto')
            opt = OptionMenu(r, var, *a)
            opt.configure(background='#589796', fg='white')
            opt.pack(anchor=CENTER, padx=10, pady=10)
            var2 = StringVar(r)
            var2.set('Secondo Oggetto')
            opt2 = OptionMenu(r, var2, *a)
            opt2.configure(background='#589796', fg='white')
            opt2.pack(anchor=CENTER, padx=10, pady=10)
            Button(r, text="Ok", fg="white", bg='#589796', command=lambda: self.comb_cmd(r, var.get(), var2.get())).pack(anchor=CENTER)
        else:
            Label(r, text="NON HAI OGGETTI.", fg="red", bg='#ADD8E6').pack(anchor=CENTER)

    def comb_cmd(self, w, i1, i2):
        self.ga.do_combina(str(i1), str(i2))
        w.destroy()

    def exami(self):
        r = Tk()
        r.title('Ispeziona un oggetto chiave')
        r.geometry('320x200')
        r.configure(background='#ADD8E6')
        r.resizable(0, 0)
        Label(r, text="SCEGLI UN OGGETTO CHIAVE DA ANALIZZARE", fg="red", bg='#ADD8E6').pack()
        a = self.ga.loc.npc
        if len(a) != 0:
            var = StringVar(r)
            var.set('Oggetti')
            opt = OptionMenu(r, var, *a)
            opt.configure(background='#589796', fg='white')
            opt.pack(anchor=CENTER, padx=10, pady=10)
            Button(r, text="Ok", fg="white", bg='#589796', command=lambda: self.exami_cmd(r, var.get())).pack(anchor=CENTER)
        else:
            Label(r, text="NESSUN OGGETTO CHIAVE.", fg="red", bg='#ADD8E6').pack(anchor=CENTER)

    def exami_cmd(self, w, i1):
        self.ga.do_esamina(str(i1))
        w.destroy()

    def oxe(self):
        r = Tk()
        r.title('Analizza oggetto')
        r.geometry('380x200')
        r.configure(background='#ADD8E6')
        r.resizable(0, 0)
        Label(r, text="SCEGLI UN OGGETTO DELL'INVENTARIO DA ANALIZZARE", fg="red", bg='#ADD8E6').pack()
        a = self.ga.newchar.items
        if len(a) != 0:
            var = StringVar(r)
            var.set('Oggetti')
            opt = OptionMenu(r, var, *a)
            opt.configure(background='#589796', fg='white')
            opt.pack(anchor=CENTER, padx=10, pady=10)
            Button(r, text="Ok", fg='white', bg='#589796', command=lambda: self.oxe_cmd(r, var.get())).pack(anchor=CENTER)
        else:
            Label(r, text="INVENTARIO VUOTO.", fg="red", bg='#ADD8E6').pack(anchor=CENTER)

    def oxe_cmd(self, w, i1):
        self.ga.do_oss(str(i1))
        w.destroy()

    def ux(self):
        r = Tk()
        r.title('Usa un oggetto')
        r.geometry('320x200')
        r.configure(background='#ADD8E6')
        r.resizable(0, 0)
        Label(r, text="SCEGLI UN OGGETTO DA USARE", fg="red", bg='#ADD8E6').pack()
        a = self.ga.loc.npc
        b = self.ga.loc.npcis
        c = a+b
        if len(c) != 0:
            var = StringVar(r)
            var.set('NPC')
            opt = OptionMenu(r, var, *c)
            opt.configure(background='#589796', fg='white')
            opt.pack(anchor=CENTER, padx=10, pady=10)
            d = self.ga.newchar.items
            if len(d) != 0:
                var2 = StringVar(r)
                var2.set('Oggetti')
                opt2 = OptionMenu(r, var2, *d)
                opt2.configure(background='#589796', fg='white')
                opt2.pack(anchor=CENTER, padx=10, pady=10)
                Button(r, text="Ok", fg="white", bg='#589796', command=lambda: self.ux_cmd(r, var2.get(), var.get()))\
                    .pack(anchor=CENTER)
            else:
                Label(r, text="INVENTARIO VUOTO.", fg="red", bg='#ADD8E6').pack(anchor=CENTER)
        else:
            Label(r, text="NIENTE CON CUI INTERAGIRE.", fg="red", bg='#ADD8E6').pack(anchor=CENTER)

    def ux_cmd(self, wd, i1, i2):
        self.ga.do_usa(str(i1), str(i2))
        wd.destroy()

    def nord_map(self):
        self.ga.do_n()
        map_loc = self.map.getroomid(self.ga.newchar.position.id)
        self.map.create_plane(self.can1, self.map.getplane(self.ga.newchar.position.id))
        self.map.create_doors(self.can1, self.map.getdoors(self.ga.newchar.position.id))
        self.map.mylocation(self.can1, map_loc)
        self.map.visited.append(map_loc)

    def sud_map(self):
        self.ga.do_s()
        map_loc = self.map.getroomid(self.ga.newchar.position.id)
        self.map.create_plane(self.can1, self.map.getplane(self.ga.newchar.position.id))
        self.map.create_doors(self.can1, self.map.getdoors(self.ga.newchar.position.id))
        self.map.mylocation(self.can1, map_loc)
        self.map.visited.append(map_loc)

    def est_map(self):
        self.ga.do_e()
        map_loc = self.map.getroomid(self.ga.newchar.position.id)
        self.map.create_plane(self.can1, self.map.getplane(self.ga.newchar.position.id))
        self.map.create_doors(self.can1, self.map.getdoors(self.ga.newchar.position.id))
        self.map.mylocation(self.can1, map_loc)
        self.map.visited.append(map_loc)

    def west_map(self):
        self.ga.do_w()
        map_loc = self.map.getroomid(self.ga.newchar.position.id)
        self.map.create_plane(self.can1, self.map.getplane(self.ga.newchar.position.id))
        self.map.create_doors(self.can1, self.map.getdoors(self.ga.newchar.position.id))
        self.map.mylocation(self.can1, map_loc)
        self.map.visited.append(map_loc)

    def up_map(self):
        self.ga.do_up()
        map_pl = self.map.getplane(self.ga.newchar.position.id)
        dor_pl = self.map.getdoors(self.ga.newchar.position.id)
        self.can1.delete('all')
        if self.ga.upflag:
            self.map.start_p += 1
        else:
            pass
        self.map.idd = self.map.c.create_text(110, 160, fill='#FA8072', text=self.map.planes[self.map.start_p],
                                              font=('Tempus Sans ITC', 8, 'bold'))
        self.map.create_plane(self.can1, map_pl)
        self.map.create_doors(self.can1, dor_pl)
        map_loc = self.map.getroomid(self.ga.newchar.position.id)
        self.map.mylocation(self.can1, map_loc)
        self.map.visited.append(map_loc)

    def down_map(self):
        self.ga.do_dw()
        map_pl = self.map.getplane(self.ga.newchar.position.id)
        dor_pl = self.map.getdoors(self.ga.newchar.position.id)
        self.can1.delete('all')
        if self.ga.dwflag:
            self.map.start_p -= 1
        else:
            pass
        self.map.idd = self.map.c.create_text(110, 160, fill='#FA8072', text=self.map.planes[self.map.start_p],
                                              font=('Tempus Sans ITC', 8, 'bold'))
        self.map.create_plane(self.can1, map_pl)
        self.map.create_doors(self.can1, dor_pl)
        map_loc = self.map.getroomid(self.ga.newchar.position.id)
        self.map.mylocation(self.can1, map_loc)
        self.map.visited.append(map_loc)

    def save_game(self):
        self.timesave = time.time()
        files = shelve.open('savegame', 'c')
        if not os.path.exists(os.path.dirname('savegame')):
            files['times'] = 0
        self.text = str(self.tx1.get('0.0', END))
        files['screen'] = self.text
        files['inventory'] = self.ga.newchar.items
        files['used'] = self.ga.newchar.used
        files['location'] = self.ga.newchar.position
        files['room'] = self.ga.loc
        files['visited'] = self.map.visited
        files['closed'] = self.ga.closed_rooms
        files['times'] += self.timesave - self.timer_start
        files['matt'] = self.ga.newchar.matt
        files['vetr'] = self.ga.newchar.vetr
        files['parts'] = self.ga.newchar.parts
        files['cris'] = self.ga.newchar.cris
        files['fial'] = self.ga.newchar.fial
        files['doors'] = self.ga.newchar.doors
        files['tools'] = self.ga.newchar.tools
        files['invlen'] = self.ga.maxitlen
        files['steps'] = self.ga.footsteps
        files.close()

    def load_game(self):
        self.timer_start = time.time()
        self.ga.start_time = self.timer_start
        files = shelve.open('savegame', 'r')
        self.ga.newchar.items = files['inventory']
        self.ga.newchar.used = files['used']
        self.ga.newchar.position = files['location']
        self.ga.loc = files['room']
        if self.ga.loc == None:
            self.ga.loc = get_room(47, self.ga.dbfile)
        if self.ga.newchar.position == None:
            self.ga.newchar.position = get_room(47, self.ga.dbfile)
        self.map.visited = files['visited']
        self.ga.closed_rooms = files['closed']
        self.text = files['screen']
        self.ga.newchar.matt = files['matt']
        self.ga.newchar.vetr = files['vetr']
        self.ga.newchar.parts = files['parts']
        self.ga.newchar.cris = files['cris']
        self.ga.newchar.fial = files['fial']
        self.ga.newchar.doors = files['doors']
        self.ga.newchar.tools = files['tools']
        self.ga.maxitlen = files['invlen']
        self.ga.footsteps = files['steps']
        self.ga.load_time += files['times']
        files.close()
        self.tx1.delete('1.0', END)
        self.tx1.insert('0.0', self.text, 'color2')
        self.can1.delete('all')
        self.map.create_plane(self.can1, self.map.getplane(self.ga.newchar.position.id))
        self.map.mylocation(self.can1, self.map.getroomid(self.ga.newchar.position.id))
        self.ga.look(self.tx1)

if __name__ == "__main__":
    g = Gui()
