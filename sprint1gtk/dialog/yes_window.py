import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class YesWindow(Gtk.Window):
    label = Gtk.Label(label="Yes")
    
    def __init__(self):
        super().__init__(title="Yes")
        
        self.add(self.label)
        
