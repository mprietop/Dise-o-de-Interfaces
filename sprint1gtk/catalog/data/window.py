import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

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
        
        cell_one = Cell("Iago Aspas" , Gtk.Image.new_from_file("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/edited/aspas.jpg"))
        cell_two = Cell("Gabri Veiga" , Gtk.Image.new_from_file("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/edited/gabri veiga.jpg" ))
        cell_three = Cell("Guidetti y Wass" , Gtk.Image.new_from_file("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/edited/guidetti wass.jpg" ))
        cell_four = Cell("Strand Larsen", Gtk.Image.new_from_file("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/edited/larsen.jpeg"))
        cell_five = Cell("Mostovoi", Gtk.Image.new_from_file("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/edited/mostovoi.jpg"))
        
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)