from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.toast.kivytoast.kivytoast import toast

kv='''
Manager:
    Fir:
    Sec:        

<Fir>:
    name:'home'
    MDLabel:
        text:'HELLO'







'''








class Fir(Screen):
    pass
    
    
class Sec(Screen):
    pass
    
    
class Manager(ScreenManager):
    pass


class Demo(MDApp):
    def build(self):
        self.u=Builder.load_string(kv)
        return self.u
        
        
Demo().run()        
        