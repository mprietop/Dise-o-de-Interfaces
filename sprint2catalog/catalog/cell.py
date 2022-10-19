import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from detail_window import DetailWindow

class Cell(Gtk.EventBox):
    
    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.label2 = Gtk.Label("Foto de "+self.name)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)
        
    def on_click(self, widget, event):
        image = self.asignar_imagen(self.name)
        dwin= DetailWindow(image, self.name, self.label2)
        dwin.show_all()

    def asignar_imagen(self, name):
            image = Gtk.Image()
            pixbuf = None
            if name == "Iago Aspas":
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/aspas.jpg", 200, 200, False)

            elif name == "Gabri Veiga":
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/gabri veiga.jpg", 200, 200, False)

            elif name == "Guidetti y Wass":
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/guidetti wass.jpg", 200, 200, False)

            elif name == "Strand Larsen":
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/larsen.jpeg", 200, 200, False)

            else:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:/msys64.2/home/mario/Dise-o-de-Interfaces/sprint1gtk/catalog/data/unedited/mostovoi.jpg", 200, 200, False)


            image.set_from_pixbuf(pixbuf)
            return image