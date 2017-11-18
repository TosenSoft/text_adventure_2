import cmd
import errno
import os
import shutil
import tempfile
import time

from character import *
from room import *


class Game(cmd.Cmd):
    def __init__(self, txar, timer_start):
        cmd.Cmd.__init__(self)
        self.start_time = timer_start
        self.end_time = 0
        self.load_time = 0
        self.txar = txar
        self.dbfile = tempfile.mktemp()
        shutil.copyfile('rooms.db', self.dbfile)
        self.closed_rooms = [3, 7, 8, 14, 16, 19, 20, 23, 26, 28, 30, 33, 35, 38, 39, 45, 46, 48, 49, 50, 40]
        self.newchar = Character()
        self.newchar.rt = self.txar
        self.loc = get_room(5, self.dbfile)
        self.newchar.position = self.loc
        self.maxitlen = 0
        self.footsteps = 0
        self.upflag = 0
        self.dwflag = 0

    def move(self, dire):
        newroom = self.loc._neighbor(dire)
        if newroom in self.closed_rooms:
            self.txar.insert(END, "Stanza non accessibile ora.", 'color3')
            self.txar.see(END)
            self.txar.insert(END, "\n")
            self.dwflag = 0
            self.upflag = 0
        else:
            if newroom is None:
                self.txar.insert(END, "Non puoi andare da quella parte.", 'color3')
                self.txar.see(END)
                self.txar.insert(END, "\n")
                self.dwflag = 0
                self.upflag = 0
            else:
                if newroom == 41 and 'lanterna' not in self.newchar.items:
                    self.txar.insert(END, "Troppo buio per scendere, serve una lanterna.", 'color3')
                    self.txar.see(END)
                    self.txar.insert(END, "\n")
                    self.dwflag = 0
                    self.upflag = 0
                else:
                    if dire == 'up':
                        self.upflag = 1
                    elif dire == 'dw':
                        self.dwflag = 1
                    else:
                        self.dwflag = 0
                        self.upflag = 0
                    self.loc = get_room(newroom, self.dbfile)
                    self.newchar.position = self.loc
                    self.footsteps += 1
                    self.look(self.txar)

    def look(self, txar):
        txar.insert(END, "\n")
        txar.insert(END, 'Ti trovi qui: %s' % self.loc.name, 'color3')
        txar.insert(END, "\n")
        txar.insert(END, "\n")
        for line in self.loc.description:
            txar.insert(END, str(line), 'color2')
        txar.insert(END, "\n")
        txar.insert(END, "\n")
        txar.insert(END, "Oggetti nella stanza:", 'color2')
        self.loc.show_item(self.newchar, self.txar)
        txar.insert(END, "\n")
        txar.insert(END, "Oggetti chiave nella stanza:", 'color2')
        self.loc.show_keyitems(self.txar)
        self.txar.see(END)
        txar.insert(END, "\n")
        txar.insert(END, "\n")

    def do_n(self):
        """vai a nord"""
        self.move('n')

    def do_s(self):
        """vai a sud"""
        self.move('s')

    def do_e(self):
        """vai ad est"""
        self.move('e')

    def do_w(self):
        """vai ad ovest"""
        self.move('w')

    def do_up(self):
        """sali le scale"""
        self.move('up')

    def do_dw(self):
        """scendi le scale"""
        self.move('dw')

    def do_usa(self, item_id, nn):
        """usa un oggetto"""
        self.newchar.use_it(self.loc, item_id, nn)
        if nn == 'libreria' and item_id == 'libro verde':
            self.closed_rooms[0] = 0
        elif nn == 'porta bloccata' and item_id == 'chiave esagonale':
            self.closed_rooms[1] = 0
        elif nn == 'pulsantiera' and item_id == 'post-it1':
            self.closed_rooms[2] = 0
        elif nn == 'griglia a muro' and item_id == 'cacciavite':
            self.closed_rooms[3] = 0
        elif nn == 'lapide con pulsanti' and item_id == 'post-it2':
            self.closed_rooms[4] = 0
        elif nn == 'mosaico' and len(self.newchar.matt) == 0:
            self.closed_rooms[7] = 0
        elif nn == 'vetrata' and len(self.newchar.vetr) == 0:
            self.closed_rooms[5] = 0
        elif nn == 'torso di marmo' and len(self.newchar.parts) == 0:
            self.closed_rooms[6] = 0
        elif nn == 'porta in ottone' and item_id == 'chiave in ottone':
            self.closed_rooms[10] = 0
        elif nn == 'vano cristalli' and len(self.newchar.cris) == 0:
            self.closed_rooms[8] = 0
        elif nn == 'pulsantiera marmo' and item_id == 'post-it4':
            self.closed_rooms[9] = 0
        elif nn == 'lapide pulsantiera' and item_id == 'post-it3':
            self.closed_rooms[11] = 0
        elif nn == 'portafiale' and len(self.newchar.fial) == 0:
            self.closed_rooms[12] = 0
        elif nn == 'statua di Atena' and item_id == 'bilancia':
            self.closed_rooms[14] = 0
        elif nn == 'porta di legno' and item_id == 'grimaldello':
            self.closed_rooms[16] = 0
        elif nn == 'porta senza maniglia' and item_id == 'maniglia':
            self.closed_rooms[15] = 0
        elif nn == 'porta1' and item_id == 'grimaldello':
            self.closed_rooms[17] = 0
        elif nn == 'porta2' and item_id == 'grimaldello':
            self.closed_rooms[18] = 0
        elif nn == 'porta3' and item_id == 'grimaldello':
            self.closed_rooms[19] = 0
        if len(self.newchar.tools) == 0:
            self.newchar.call_events('e26', self.txar)
            self.txar.see(END)
        if len(self.newchar.tools) == 0 and 'secchio' in self.newchar.used:
            self.closed_rooms[20] = 0

    def do_prendi(self, item_id):
        """prendi un oggetto dalla stanza"""
        newitem = self.loc.give_item(item_id)
        if newitem != None:
            self.newchar.items.append(item_id)
            self.newchar.itlen += 1
            if self.newchar.itlen > self.maxitlen:
                self.maxitlen = self.newchar.itlen
            self.txar.insert(END, "Hai preso: "+item_id, 'color5')
            self.txar.see(END)
            self.txar.insert(END, "\n")
        else:
            self.txar.insert(END, "Questo oggetto non e' presente nella stanza", 'color3')
            self.txar.see(END)
            self.txar.insert(END, "\n")
        if item_id == 'tesoro':
            self.end_time = time.time()
            tm = self.end_time-self.start_time
            self.newchar.call_events('ef', self.txar)
            tm += self.load_time
            if tm > 3600:
                m, s = divmod(tm, 60)
                h, m = divmod(m, 60)
                if h == 1:
                    self.txar.insert(END, 'Hai finito in: 1 ora, %s minuti e %s secondi!' % (int(m), int(s)), 'color3')
                elif h > 1:
                    self.txar.insert(END, 'Hai finito in: %s ore, %s minuti e %s secondi!' % (int(h), int(m), int(s)), 'color3')
                self.txar.insert(END, "\n")
                self.txar.insert(END, "@TOSENSOFT TEAM", 'color5')
                self.txar.see(END)
                self.register_htime(h, m, s)
            else:
                m, s = divmod(tm, 60)
                self.txar.insert(END, 'Hai finito in: %s minuti e %s secondi!' % (int(m), int(s)), 'color3')
                self.txar.insert(END, "\n")
                self.txar.insert(END, "@TOSENSOFT TEAM", 'color5')
                self.txar.see(END)
                self.register_time(m, s)
        elif item_id == 'struttura alare':
            self.newchar.call_events('e20', self.txar)
            self.txar.see(END)
            self.closed_rooms[13] = 0

    def do_esci(self):
        """esci dal gioco"""
        return True

    def do_combina(self, it_1, it_2):
        """combina due oggetti compatibili"""
        self.newchar.combine_items(it_1, it_2)

    def do_esamina(self, npe):
        """esamina un oggetto chiave"""
        self.newchar.inspection(self.newchar.position, npe)

    def do_oss(self, itt):
        """osserva un oggetto preso da una stanza (devi averlo raccolto)"""
        self.newchar.inspection3(itt)

    def register_time(self, timemin, timesec):
        filename = "times/partite.txt"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
            with open(filename, "w") as f:
                f.write('------------------NUOVA-PARTITA------------------\n')
                f.write('%s\n' % time.asctime(time.localtime(self.start_time)))
                f.write('Hai completato il gioco in %s minuti e %s secondi!\n' % (int(timemin), int(timesec)))
                f.write('Massima dimensione del tuo inventario: %d elementi!\n' % self.maxitlen)
                f.write('Distanza percorsa: %d passi!\n' % self.footsteps)
            f.close()
        else:
            with open(filename, 'a') as f:
                f.write('------------------NUOVA-PARTITA------------------\n')
                f.write('%s\n' % time.asctime(time.localtime(self.start_time)))
                f.write('Hai completato il gioco in %s minuti e %s secondi!\n' % (int(timemin), int(timesec)))
                f.write('Massima dimensione del tuo inventario: %d elementi!\n' % self.maxitlen)
                f.write('Distanza percorsa: %d passi!\n' % self.footsteps)
            f.close()

    def register_htime(self, timeh, timemin, timesec):
        filename = "times/partite.txt"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
            with open(filename, "w") as f:
                f.write('------------------NUOVA-PARTITA------------------\n')
                f.write('%s\n' % time.asctime(time.localtime(self.start_time)))
                if timeh == 1:
                    f.write('Hai completato il gioco in %s ora, %s minuti e %s secondi!\n' % (int(timeh), int(timemin), int(timesec)))
                elif timeh > 1:
                    f.write('Hai completato il gioco in %s ore, %s minuti e %s secondi!\n' % (int(timeh), int(timemin), int(timesec)))
                f.write('Massima dimensione del tuo inventario: %d elementi!\n' % self.maxitlen)
                f.write('Distanza percorsa: %d passi!\n' % self.footsteps)
            f.close()
        else:
            with open(filename, 'a') as f:
                f.write('------------------NUOVA-PARTITA------------------\n')
                f.write('%s\n' % time.asctime(time.localtime(self.start_time)))
                if timeh == 1:
                    f.write('Hai completato il gioco in %s ora, %s minuti e %s secondi!\n' % (int(timeh), int(timemin), int(timesec)))
                elif timeh > 1:
                    f.write('Hai completato il gioco in %s ore, %s minuti e %s secondi!\n' % (int(timeh), int(timemin), int(timesec)))
                f.write('Massima dimensione del tuo inventario: %d elementi!\n' % self.maxitlen)
                f.write('Distanza percorsa: %d passi!\n' % self.footsteps)
            f.close()

if __name__ == "__main__":
    g = Game(None, None)
    g.cmdloop()
