#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'DZW'
__mtime__ = '2019/8/12'
# code is far away from bugs with the god animal protecting
    I love animals. They are so funny. 
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃   *   ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃ Bless ┣┓
              ┃ NoBUG ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""

import os
import wx

class MyApp(wx.App):
    def OnInit(self):
        # wx.MessageBox("Hi")
        self.frame = MakeFrame(None, title="tt")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


class MakeFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MakeFrame, self).__init__(*args, **kw)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.RED)


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
