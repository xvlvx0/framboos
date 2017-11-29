#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import wx 
import wx.lib.inspection

class Mywin(wx.Frame):
    def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title)

        panel = wx.Panel(self) 
        verticalbox = wx.BoxSizer(wx.VERTICAL) 
        
        # ------------------------------------------------------------
        namebox = wx.StaticBox(panel, -1, 'Name:') 
        nameboxSizer = wx.StaticBoxSizer(namebox, wx.VERTICAL) 
        namebox = wx.BoxSizer(wx.HORIZONTAL) 
        fn = wx.StaticText(panel, -1, "First Name") 
        nm1 = wx.TextCtrl(panel, -1, style = wx.ALIGN_LEFT)
        ln = wx.StaticText(panel, -1, "Last Name") 
        nm2 = wx.TextCtrl(panel, -1, style = wx.ALIGN_LEFT) 

        namebox.Add(fn, 0, wx.ALL|wx.CENTER, 5) 
        namebox.Add(nm1, 0, wx.ALL|wx.CENTER, 5)
        namebox.Add(ln, 0, wx.ALL|wx.CENTER, 5) 
        namebox.Add(nm2, 0, wx.ALL|wx.CENTER, 5) 
        nameboxSizer.Add(namebox, 0, wx.ALL|wx.CENTER, 10)  

        # ------------------------------------------------------------
        buttonbox = wx.StaticBox(panel, -1, 'Buttons:') 
        buttonboxSizer = wx.StaticBoxSizer(buttonbox, wx.VERTICAL) 

        horizontalbox = wx.BoxSizer(wx.HORIZONTAL) 
        okButton = wx.Button(panel, -1, 'OK') 
        horizontalbox.Add(okButton, 0, wx.ALL|wx.LEFT, 10) 
        cancelButton = wx.Button(panel, -1, 'Cancel') 
        horizontalbox.Add(cancelButton, 0, wx.ALL|wx.LEFT, 10) 
        
        buttonboxSizer.Add(horizontalbox, 0, wx.ALL|wx.LEFT, 10) 

        # ------------------------------------------------------------
        connectorbox = wx.StaticBox(panel, -1, 'Connectors:')
        connectorboxSizer = wx.StaticBoxSizer(connectorbox, wx.VERTICAL)
        
        connectors = {'Conn-1', 'Conn-2', 'Conn-3', 'Conn-4', 'Conn-5', 'Conn-6', 'Conn-7', 
                    'Conn-8', 'Conn-9', 'Conn-10', 'Conn-11', 'Conn-12', 'Conn-13', 'Conn-14'}
        
        hzFirstBox = wx.StaticBox(panel, -1, 'Conn-1:')
        i = 1
        for conn in connectors:
            butConn1 = wx.ToggleButton(panel, 1, , (20, 25))
            hzFirstBox.Add(butConn1, 0, wx.ALL|wx.LEFT, 10)

        hzSecondBox = wx.StaticBox(panel, -1, 'Conn-1:')
        while (i<(connectors/2)):


        connectorboxSizer.Add(connectorbox, 0, wx.ALL|wx.LEFT, 10)


        

        # ------------------------------------------------------------
        verticalbox.Add(nameboxSizer,0, wx.ALL|wx.CENTER, 5) 
        verticalbox.Add(buttonboxSizer,0, wx.ALL|wx.CENTER, 5) 
        verticalbox.Add(connectorboxSizer,0, wx.ALL|wx.CENTER, 5) 
        panel.SetSizer(verticalbox) 
        self.Centre() 

        panel.Fit() 
        self.Show()

app = wx.App() 
Mywin(None, 'staticboxsizer demo') 
wx.lib.inspection.InspectionTool().Show()
app.MainLoop()