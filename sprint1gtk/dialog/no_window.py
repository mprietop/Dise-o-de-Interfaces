import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NoWindow(Gtk.Window):
    
    
    def __init__(self):
        label = Gtk.Label(label="No")
        super().__init__(title="No")
        
        self.add(label)