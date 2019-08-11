#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'DZW'
__mtime__ = '2019/8/9'
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
import wx

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """
    def __init__(self, *args, **kw):
        #ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        #create a panel in the frame
        pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        st = wx.StaticText(pnl, label = "Hello World!", pos =(100,100))
        font = st.GetFont()
        font.PointSize +=10
        font = font.Bold()
        st.SetFont(font)

        #create a menu bar
        self.makeMenuBar()

        # self.makeNoteBook()

        openBn = wx.Button(pnl, label="Open", pos=(10, 50), size=(50, 24))

        #and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

    # def makeNoteBook(self):
    #     mainWindow = wx.Notebook()
        


    def makeMenuBar(self):
        #Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                                    "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()

        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        #Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)

    def OnHello(self, event):
        wx.MessageBox("hh")

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython sample",
                      "About Hello world 2",
                      wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title="Hello world")
    frm.Show()
    app.MainLoop()




