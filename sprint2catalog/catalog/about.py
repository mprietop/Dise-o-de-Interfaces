import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class About(Gtk.Window):
    
    #Una ventana sencilla con un label que se lanza al pulsar en el Menu "Acerca de"
    def __init__(self):
        super().__init__(title="Acerca de")
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        self.set_border_width(15)
        self.set_default_size(200, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.label = Gtk.Label("Mi nombre es Mario Prieto, estudiande de segundo año del ciclo superior DAM")
        
        box.pack_start(self.label, True, True, 0)

        self.add(box)