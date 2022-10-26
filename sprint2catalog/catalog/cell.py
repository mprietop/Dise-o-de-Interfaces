import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from detail_window import DetailWindow

class Cell(Gtk.EventBox):
    
    def __init__(self, name, label, image):
        super().__init__()
        self.name = name
        self.image = image
        self.label = label
        
        #Creo la box con la imagen y un label(nombre)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)
        
    #método que cuando clicas una celda vuelve a utilizar la imagen y se la pasa junto con el label a la detail window
    def on_click(self, widget, event):
        image = Gtk.Image()
        image.set_from_pixbuf(self.image.get_pixbuf())
        
        label = Gtk.Label(label=self.label)
        dwin= DetailWindow(image, self.name, label)
        dwin.show_all()
        
