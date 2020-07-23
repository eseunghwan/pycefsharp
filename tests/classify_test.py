# -*- coding: utf-8 -*-
from pycefsharp.cef import CefApp, CefView

class View(CefView):
    def __init__(self):
        super().__init__("https://github.com/eseunghwan/pycefsharp", "classify_test")

    def on_load(self):
        print("Loaded!")

    def on_show(self):
        print("Show!")

    def on_close(self):
        print("Closed!")

CefApp().Run(View())
