import wx
import pprint

about_txt = """Users of this instrument must enter some details about themselves
"""

class DataXferBoolValidator(wx.PyValidator):
     def __init__(self, data):
         wx.PyValidator.__init__(self)
         self.data = data

     def Clone(self):
         return DataXferBoolValidator(self.data)

     def Validate(self,win):

         return True

     def TransferToWindow(self):
         textCtrl = self.GetWindow()
         textCtrl.SetValue(self.data.get(self.key, ""))
         return True 

     def TransferFromWindow(self):
         textCtrl = self.GetWindow()
         self.data[self.key] = textCtrl.GetValue()
         return True

          
class DataXferValidator(wx.PyValidator):
     def __init__(self, data, key):
         wx.PyValidator.__init__(self)
         self.data = data
         self.key = key

     def Clone(self):
         """
         Note that every validator must implement the Clone() method.
         """
         return DataXferValidator(self.data, self.key)

     def Validate(self, win):
         textCtrl = self.GetWindow()
         text = textCtrl.GetValue()

         if len(text) == 0:
             wx.MessageBox("The field highlighted in red must contain some text", "Error")
             textCtrl.SetBackgroundColour("red")
             textCtrl.SetFocus()
             textCtrl.Refresh()
             return False
         else:
             textCtrl.SetBackgroundColour(
                 wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
             textCtrl.Refresh()


         return True

     def TransferToWindow(self):
         textCtrl = self.GetWindow()
         textCtrl.SetValue(self.data.get(self.key, ""))
         return True 

     def TransferFromWindow(self):
         textCtrl = self.GetWindow()
         self.data[self.key] = textCtrl.GetValue()
         return True



class MyDialog(wx.Dialog):
    def __init__(self, data):
        wx.Dialog.__init__(self, None, -1, "Validators: data transfer", size=(1000,700),
                           style =wx.DEFAULT_DIALOG_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.CLOSE_BOX ) )

        # Create the text controls
        about   = wx.StaticText(self, -1, about_txt)
        user_l  = wx.StaticText(self, -1, "Username:")
        labhead_l = wx.StaticText(self, -1, "Lab head:")
        chargeacc_l = wx.StaticText(self, -1, "Charging account:")
        taskcode_l = wx.StaticText(self, -1, "Task code:")
        acctick_l = wx.StaticText(self, -1, "Tick if you don't know your account details: ")

        user_t  = wx.TextCtrl(self, validator=DataXferValidator(data, "user"))
        labhead_t = wx.TextCtrl(self, validator=DataXferValidator(data, "labhead"))
        chargeacc_t = wx.TextCtrl(self, validator=DataXferValidator(data, "chargeacc"))
        taskcode_t = wx.TextCtrl(self, validator=DataXferValidator(data, "taskcode"))
        acctick_t = wx.CheckBox(self, validator=DataXferValidator(data, "acctick"))

        # Use standard button IDs
        okay   = wx.Button(self, wx.ID_OK)
        okay.SetDefault()

        
        # Layout with sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(about, 0, wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, 5)
        
        fgs = wx.FlexGridSizer(3, 2, 5, 5)
        fgs.Add(user_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(user_t, 0, wx.EXPAND)
        fgs.Add(labhead_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(labhead_t, 0, wx.EXPAND)
        fgs.Add(chargeacc_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(chargeacc_t, 0, wx.EXPAND)
        fgs.Add(taskcode_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(taskcode_t, 0, wx.EXPAND)
        fgs.Add(acctick_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(acctick_t, 0, wx.EXPAND)
        fgs.AddGrowableCol(1)
        sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)

        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
        

app = wx.PySimpleApp()

data = { "user" : "" }
dlg = MyDialog(data)
dlg.ShowModal()
dlg.Destroy()

wx.MessageBox("You entered these values:\n\n" +
              pprint.pformat(data))

app.MainLoop()
