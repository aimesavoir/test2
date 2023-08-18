from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

class MainApp (MDApp):
    def build(self):
        win1=Builder.load_file('kv1.kv')
        win2=Builder.load_file('kv2.kv')
        win3=Builder.load_file('kv3.kv')
        win4=Builder.load_file('kv4.kv')
        win5=Builder.load_file('kv5.kv')
        self.screen=ScreenManager()
        self.screen.add_widget(win1)
        self.screen.add_widget(win2)
        self.screen.add_widget(win3)
        self.screen.add_widget(win4)
        self.screen.add_widget(win5)
        return self.screen
    def click1(self):
        self.screen.current='scren2'
        self.screen.transition.direction='left'
    def click2(self):
        self.screen.current='scren3'
        self.screen.transition.direction='left'
    def click3(self):
        self.screen.current='scren4'
        self.screen.transition.direction='left'
    def click4(self):
        self.screen.current='scren5'
        self.screen.transition.direction='left'
    def back(self):
        self.screen.current='scren1'
        self.screen.transition.direction='right'                

MainApp().run()        