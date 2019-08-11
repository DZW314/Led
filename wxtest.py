import wx
import os


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Test")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.BLACK)
        pnlID = self.panel.GetId()
        print("\nPanel ID is %s" % repr(pnlID))
        pp = self.FindWindowById(pnlID)
        print("\nGet Panel: %s" % repr(pp))

        # create icon
        icon_path = os.path.abspath("./favicon.ico")
        icon = wx.Icon(icon_path, type=wx.BITMAP_TYPE_ICON)
        self.SetIcon(icon)

        # create bitmap
        img_path = os.path.abspath("./IMG.jpg")
        bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_JPEG)
        self.bitmap = wx.StaticBitmap(self.panel, bitmap=bitmap)

        # create buttons
        ok_btn = wx.Button(self.panel, wx.ID_OK)
        cancel_btn = wx.Button(self.panel, wx.ID_CANCEL, pos=(100, 3))

        button = wx.Button(self.panel, pos=(50, 50), label="click")
        self.btnID = button.GetId()
        print("\nButton ID is %s" % repr(self.btnID))
        self.Bind(wx.EVT_BUTTON, self.OnButton, button)

        # create menu
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu.Append(wx.NewId(), "New")
        file_menu.Append(wx.ID_PREFERENCES)
        menu_bar.Append(file_menu, "File")
        self.SetMenuBar(menu_bar)


    def OnButton(self, event):
        print("\nFrame GetChildren:")
        for child in self.GetChildren():
            print("%s" % repr(child))

        print("\nPanel FindWindowByID:")
        button = self.panel.FindWindowById(self.btnID)
        print("%s" % repr(button))

        button.SetLabel("Changed Label")
        self.panel.SetBackgroundColour(wx.LIGHT_GREY)

        print("\nButton GetParent:")
        panel = button.GetParent()
        print("%s" % repr(panel))



        print("\nGet the Application Object:")
        app1 = wx.GetApp()
        print("%s" % repr(app1))

        print("\nGet the Frame from the App:")
        frame = app1.GetTopWindow()
        print("%s" % repr(frame))


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()