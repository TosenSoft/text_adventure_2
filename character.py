import json
from Tkinter import *


def get_chara(namec):
    ret = Character(namec, None, [])
    return ret


class Character:
    def __init__(self, name="Me", position=None, items=[], used=[], rt=None):
        self.name = name
        self.position = position
        self.items = items
        self.used = used
        self.rt = rt
        self.matt = ['mattonella arancione', 'mattonella gialla', 'mattonella nera', 'mattonella rosa']
        self.vetr = ['vetro bianco', 'vetro nero', 'vetro rosso', 'vetro verde', 'vetro viola']
        self.parts = ['braccio sinistro', 'testa', 'gamba destra', 'gamba sinistra', 'elmo', 'lancia']
        self.cris = ['smeraldo', 'opale', 'rubino', 'topazio', 'quarzo', 'ametista', 'corindone', 'diamante']
        self.fial = ['fiala amaranto', 'fiala arancione', 'fiala blu', 'fiala ciano', 'fiala H', 'fiala Terra di Siena']
        self.doors = ['porta1', 'porta2', 'porta3', 'porta di legno']
        self.tools = ['ingranaggio piccolo', 'ingranaggio medio', 'ingranaggio grosso', 'leva arrugginita',
                      'combustibile']
        self.itlen = 0

    def give_item(self, item):
        if item in self.items:
            i = self.items.pop(item)
            return i
        else:
            return None

    def inspection(self, room, npc):
        if npc in room.npc:
            with open('npc/'+npc+'.json', 'r') as f:
                j = f.read()
                d = json.loads(j)
                d['name'] = npc
                for line in d['description']:
                    self.rt.insert(END, str(line), 'color2')
                self.rt.insert(END, "\n")
                self.rt.see(END)
            f.close()
        else:
            self.rt.insert(END, 'Oggetto non presente in questa stanza.', 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def inspection3(self, item):
        if item in self.items:
            with open('items/'+item+'.json', 'r') as f:
                j = f.read()
                d = json.loads(j)
                d['name'] = item
                for line in d['description']:
                    self.rt.insert(END, str(line), 'color2')
                self.rt.insert(END, "\n")
                self.rt.see(END)
            f.close()
        else:
            self.rt.insert(END, 'Non hai raccolto questo oggetto.', 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def combine_items(self, item1, item2):
        if item1 in self.items and item2 in self.items:
            if (item1 == "maniglia esagonale" and item2 == "cilindro esagonale") or \
                    (item2 == "maniglia esagonale" and item1 == "cilindro esagonale"):
                self.items.remove("maniglia esagonale")
                self.used.append('maniglia esagonale')
                self.items.remove("cilindro esagonale")
                self.used.append('cilindro esagonale')
                self.items.append("chiave esagonale")
                self.rt.insert(END, 'Hai ottenuto una chiave esagonale.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif (item1 == "asta di legno" and item2 == "punta di ferro") or \
                    (item1 == "punta di ferro" and item2 == "asta di legno"):
                self.items.remove("punta di ferro")
                self.used.append('punta di ferro')
                self.items.remove("asta di legno")
                self.used.append('asta di legno')
                self.items.append("lancia")
                self.rt.insert(END, 'Hai ottenuto una lancia.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif (item1 == "fiammiferi" and item2 == "carbone") or \
                    (item1 == "carbone" and item2 == "fiammiferi"):
                self.items.remove("fiammiferi")
                self.used.append('fiammiferi')
                self.items.remove("carbone")
                self.used.append('carbone')
                self.items.append("combustibile")
                self.rt.insert(END, 'Hai ottenuto del combustibile.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            else:
                self.rt.insert(END, 'Questi oggetti non possono combinarsi tra di loro', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
        else:
            self.rt.insert(END, 'Non possiedi questi oggetti.', 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def use_it(self, room, item, npc):
        if npc in room.npc and item in self.items:
            if item == 'chiave esagonale' and npc == 'porta bloccata':
                self.call_events('e1', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'chiave esagonale' and npc == 'porta bloccata':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'libro verde' and npc == 'libreria':
                self.call_events('e2', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'libro verde' and npc == 'libreria':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'post-it1' and npc == 'pulsantiera':
                self.call_events('e3', self.rt)
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
            elif item != 'post-it1' and npc == 'pulsantiera':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'cacciavite' and npc == 'griglia a muro':
                self.call_events('e4', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'cacciavite' and npc == 'griglia a muro':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'post-it2' and npc == 'lapide con pulsanti':
                self.call_events('e5', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'post-it2' and npc == 'lapide con pulsanti':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item in self.matt and npc == 'mosaico':
                self.call_events('e6', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
                self.matt.remove(item)
                if len(self.matt) == 0:
                    self.call_events('e7', self.rt)
                    self.rt.see(END)
            elif item not in self.matt and npc == 'mosaico':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item in self.vetr and npc == 'vetrata':
                self.call_events('e8', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
                self.vetr.remove(item)
                if len(self.vetr) == 0:
                    self.call_events('e9', self.rt)
                    self.rt.see(END)
            elif item not in self.vetr and npc == 'vetrata':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item in self.parts and npc == 'torso di marmo':
                self.call_events('e10', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
                self.parts.remove(item)
                if len(self.parts) == 0:
                    self.call_events('e11', self.rt)
            elif item not in self.parts and npc == 'torso di marmo':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'chiave in ottone' and npc == 'porta in ottone':
                self.call_events('e12', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'chiave in ottone' and npc == 'porta in ottone':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.insert(END, "\n")
                self.rt.see(END)
            elif item in self.cris and npc == 'vano cristalli':
                self.call_events('e13', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
                self.cris.remove(item)
                if len(self.cris) == 0:
                    self.call_events('e14', self.rt)
            elif item not in self.cris and npc == 'vano cristalli':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'post-it4' and npc == 'pulsantiera marmo':
                self.call_events('e15', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'post-it4' and npc == 'pulsantiera marmo':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'post-it3' and npc == 'lapide pulsantiera':
                self.call_events('e16', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'post-it3' and npc == 'lapide pulsantiera':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item in self.fial and npc == 'portafiale':
                self.call_events('e17', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
                self.fial.remove(item)
                if len(self.fial) == 0:
                    self.call_events('e18', self.rt)
            elif item not in self.fial and npc == 'portafiale':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'bilancia' and npc == 'statua di Atena':
                self.call_events('e19', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'bilancia' and npc == 'statua di Atena':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'grimaldello' and npc in self.doors:
                self.call_events('e21', self.rt)
                self.rt.see(END)
                self.doors.remove(npc)
                if item not in self.used:
                    self.used.append(item)
                if len(self.doors) == 0:
                    self.call_events('e23', self.rt)
                    self.rt.see(END)
                    self.items.remove(item)
            elif item != 'grimaldello' and npc in self.doors:
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'maniglia' and npc == 'porta senza maniglia':
                self.call_events('e22', self.rt)
                self.rt.see(END)
                self.used.append(item)
                self.items.remove(item)
            elif item != 'maniglia' and npc == 'porta senza maniglia':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item in self.tools and npc == 'congegno a vapore':
                self.call_events('e24', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
                self.tools.remove(item)
            elif item not in self.tools and npc == 'congegno a vapore':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'secchio' and npc == 'alloggiamento':
                self.call_events('e25', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'secchio' and npc == 'alloggiamento':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
        else:
            self.rt.insert(END, "Non possiedi l'oggetto o stai cercando di interagire con qualcosa che non e' "
                                "qui.", 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def call_events(self, ev, rt):
        with open('events/'+ev+'.json') as f:
            j = f.read()
            d = json.loads(j)
            d['name'] = ev
            for line in d['description']:
                rt.insert(END, str(line), 'color')
            rt.insert(END, "\n")
        f.close()


