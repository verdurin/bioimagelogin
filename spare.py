#!/usr/bin/env python

"""Take a microscope user's details when they logon to use the instrument"""

import wx
import sys

class Frame(wx.Frame):
    def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                 size=(1000,700), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU) | wx.FRAME_TOOL_WINDOW):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
             
        panel = wx.Panel(self, -1)
        
        
        text = wx.StaticText(panel, -1, "User name and account details", (20, 10))
        text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        text.SetSize(text.GetBestSize())
        
        text1 = wx.StaticText(panel, -1, "Logon screen", (20, 50))
        text1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        
        text2 = wx.StaticText(panel, -1, "Username:", (20,100))
        usertextctrl = wx.TextCtrl(panel, -1, size=(125, -1), pos=(150,100))
        usertext = usertextctrl.GetValue()
            
             
        text3 = wx.StaticText(panel, -1, "Password:", (20, 150))
        password = wx.TextCtrl(panel, -1, "", size=(125, -1), pos=(150, 150), style=wx.TE_PASSWORD)
        
        
        text4 = wx.StaticText(panel, -1, "Lab head:", (20, 220))
        labtextctrl = wx.TextCtrl(panel, -1, "", size=(180, -1), pos=(150, 220))
        labtext = labtextctrl.GetValue()
        
        
        text5 = wx.StaticText(panel, -1, "Charging account:", pos=(20, 280))
        accounttextctrl = wx.TextCtrl(panel, -1, "", size=(125, -1), pos=(150, 280))
        accounttext = accounttextctrl.GetValue()
        
    
        text6 = wx.StaticText(panel, -1, "Task code:", pos=(20, 330))
        taskcodetextctrl = wx.TextCtrl(panel, -1, "", size=(125, -1), pos=(150, 330))
        taskcodetext = taskcodetextctrl.GetValue()
        
    
        cb1box = wx.CheckBox(panel, -1, "Tick if you don't know your account details", pos=(20, 380))
        cb1 = cb1box.GetValue()
        
        
        text7 = wx.StaticText(panel, -1, "If ticked, please enter your e-mail address:", pos=(20, 420))
        emailtextctrl = wx.TextCtrl(panel, -1, "", size=(175, -1), pos=(330, 420))
        emailtext = emailtextctrl.GetValue()
        
        
        cb2box = wx.CheckBox(panel, -1, "Multiphoton", pos=(20, 500))
        cb2 = cb2box.GetValue()
        
        
        cb3box = wx.CheckBox(panel, -1, "Confocal", pos=(20, 530))
        cb3 = cb3box.GetValue()
        
        
        finish = wx.Button(panel, -1, "Done", pos=(20, 600))
        self.Bind(wx.EVT_BUTTON, self.OnClick, finish)
        finish.SetToolTipString("Click here to finish recording your details")
        
    def OnClick(self, event):
        
        #print usertext
        #print taskcodetext
        self.Close()
        

    


class App(wx.App):
    
    def __init__(self, redirect=True, filename="spare-output"):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        self.frame = Frame(parent=None, id=-1, title='Microscope usage details')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        
        
        return True

    

if __name__ == '__main__':
    app = App(redirect=True)
    app.MainLoop()
    output = open('/tmp/spareoutput', 'w')
    output.close()