import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell
from gi.repository import GdkPixbuf
from about import About
class MainWindow (Gtk.Window) :
    
    vbox = Gtk.VBox(False, 2)
    
    def __init__(self, data_source):
        #dándole titulo, que se pueda cerrar así como el borde y el tamaño inicial
        super().__init__ ( title = "Fotos")
        self.connect ("destroy" , Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(100 , 500)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        header = Gtk.HeaderBar (title = "Celta")
        header.set_subtitle ("Mix")
        header.props.show_close_button = True
        
        self.set_titlebar(header)
        
        #creacion de la barra de Menú
        mb = Gtk.MenuBar()
        ayudamenu = Gtk.Menu()
        ayuda = Gtk.MenuItem("Ayuda")
        ayuda.set_submenu(ayudamenu)
       
        acerca = Gtk.MenuItem("Acerca de")
        acerca.connect("button-release-event", self.on_click)
        ayudamenu.append(acerca)

        mb.append(ayuda)

        

        flowbox = Gtk.FlowBox()
        #configuración para que se pueda hacer scroll
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER , Gtk.PolicyType.AUTOMATIC)
        scrolled.add(flowbox)
        
        
        self.vbox.pack_start(mb, False, False, 0)
        self.vbox.pack_start(scrolled, True, True, 0)
        
        self.add(self.vbox)
        
        #sacando los datos de la lista resultante de recorrer el json y crear imágenes con esos datos 
        #y creando una celda con cada imagen y nombre
        for item in data_source:
            cell = Cell(item.get("name"), item.get("description"),item.get("gtk_image"))
            flowbox.add(cell)
            
    #Cuando de pulsa el MenuItem "Acerca de" se va a About
    def on_click(self, widget, event):
        acerca = About()
        acerca.show_all()
        