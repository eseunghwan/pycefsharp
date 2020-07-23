# -*- coding: utf-8 -*-
from pycefsharp.cef import CefApp, CefView

class View(CefView):
    def __init__(self):
        super().__init__("https://github.com/eseunghwan/pycefsharp", "classify_test")

        self.__views = []

    def OnLoad(self, sender, ev):
        print("Loaded!")

    def OnShow(self, sender, ev):
        print("Show!")

    def OnClose(self, sender, ev):
        print("Closed!")

CefApp().Run(View())
