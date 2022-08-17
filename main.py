import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        size = .124
        sizee = .124
        super().__init__(**kwargs)
        for i in range(2, 66):
            """creation of buttons"""
            if 2 <= i <= 24:
                if 9 < i < 17 or i == 17 or 25 < i < 33 or i == 33 or 41 < i < 49 or i == 49 or 57 < i < 65 or i == 65:
                    if (i % 2) == 0:
                        self.ids.w_parte.text ="hi"
                    else:
                        self.ids.r_parte.text = "hi"
                else:
                    if (i % 2) != 0:
                        self.ids.w_parte.text ="hi"
                    else:
                        self.ids.r_parte.text = "hi"
            elif 43 <= i <= 65:
                if 9 < i < 17 or i == 17 or 25 < i < 33 or i == 33 or 41 < i < 49 or i == 49 or 57 < i < 65 or i == 65:
                    if (i % 2) == 0:

                        self.ids.w_parte.text = "hi"
                    else:
                        self.ids.r_parte.text = "hi"

                else:
                    if (i % 2) != 0:
                        self.ids.w_parte.text = "hi"
                    else:
                        self.ids.r_parte.text = "hi"
            else:
                if 9 < i < 17 or i == 17 or 25 < i < 33 or i == 33 or 41 < i < 49 or i == 49 or 57 < i < 65 or i == 65:
                    if (i % 2) == 0:

                        self.ids.w_parte.text = "hi"
                    else:
                        self.ids.r_parte.text = "hi"

                else:
                    if (i % 2) != 0:
                        self.ids.w_parte.text = "hi"
                    else:
                        self.ids.r_parte.text = "hi"


class MainWidget(Widget):
    pass


class kmlDamaApp(App):
    pass


kmlDamaApp().run()