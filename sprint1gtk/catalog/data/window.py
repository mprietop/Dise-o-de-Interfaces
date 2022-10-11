import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell
from gi.repository import GdkPixbuf
class MainWindow ( Gtk.Window ) :
    flowbox = Gtk.FlowBox()
    
    def __init__(self):
        super().__init__ ( title = "Fotos")
        self.connect ("destroy" , Gtk.main_quit)
        self.set_border_width ( 5)
        self.set_default_size (400 , 400)
        
        header = Gtk.HeaderBar (title = "Celta")
        header.set_subtitle ("Mix")
        header.props.show_close_button = True
        
        self.set_titlebar (header)
        
        scrolled = Gtk . ScrolledWindow()
        scrolled.set_policy (Gtk.PolicyType.NEVER , Gtk . PolicyType . AUTOMATIC)
        scrolled.add (self.flowbox)
        self.add (scrolled)
        
        
        image = Gtk.Image()
        image2 = Gtk.Image()
        image3 = Gtk.Image()
        image4 = Gtk.Image()
        image5 = Gtk.Image()
        #Reescalado de las imagenes
        pisxbuf1 = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/aspas.jpg", 200, 200, False)
        pisxbuf2 = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/gabri veiga.jpg", 200, 200, False)
        pisxbuf3 = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/guidetti wass.jpg", 200, 200, False)
        pisxbuf4 = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/larsen.jpeg", 200, 200, False)
        pisxbuf5 = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/mostovoi.jpg", 200, 200, False)
        
        
        #Una celda para cada imagen
        image.set_from_pixbuf(pisxbuf1)
        cell_one = Cell("Iago Aspas" , image)
        image2.set_from_pixbuf(pisxbuf2)
        cell_two = Cell("Gabri Veiga", image2)
        image3.set_from_pixbuf(pisxbuf3)
        cell_three = Cell("Guidetti y Wass" , image3)
        image4.set_from_pixbuf(pisxbuf4)
        cell_four = Cell("Strand Larsen", image4)
        image5.set_from_pixbuf(pisxbuf5)
        cell_five = Cell("Mostovoi", image5)
        
        #Añadiendo las celdas
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)