import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell
from gi.repository import GdkPixbuf

class MainWindow (Gtk.Window) :
    flowbox = Gtk.FlowBox()
    
    def __init__(self, data_source):
        #dándole titulo, que se pueda cerrar así como el borde y el tamaño inicial
        super().__init__ ( title = "Fotos")
        self.connect ("destroy" , Gtk.main_quit)
        self.set_border_width (15)
        self.set_default_size (400 , 400)
        
        header = Gtk.HeaderBar (title = "Celta")
        header.set_subtitle ("Mix")
        header.props.show_close_button = True
        
        self.set_titlebar(header)
        
        #configuración para que se pueda hacer scroll
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER , Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)
        
        #sacando los datos de la lista resultante de recorrer el json y crear imágenes con esos datos
        for item in data_source:
            cell = Cell(item.get("name"), item.get("gtk_image"))
            self.flowbox.add(cell)
        