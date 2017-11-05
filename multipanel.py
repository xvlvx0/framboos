#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# gotoclass.py

import wx

class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(390, 350))
            
        self.InitUI()
        self.Centre()
        self.Show()     
        
    def InitUI(self):
    
        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        VirtBoxData = wx.BoxSizer(wx.VERTICAL)

        '''DataWindow'''
        DataWindow = wx.BoxSizer(wx.HORIZONTAL)
        VirtBoxData.Add(DataWindow, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        #VirtBoxData.Add((-1, 10))

        '''Name box for logwindow'''
        HorBoxLog = wx.BoxSizer(wx.HORIZONTAL)
        StaticTextLog = wx.StaticText(panel, label='Log:')
        StaticTextLog.SetFont(font)
        HorBoxLog.Add(StaticTextLog)
        VirtBoxData.Add(HorBoxLog, flag=wx.LEFT | wx.TOP, border=10)

        #VirtBoxData.Add((-1, 10))

        '''LogWindow'''
        LogWindow = wx.BoxSizer(wx.HORIZONTAL)
        ActiveTextLog = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        LogWindow.Add(ActiveTextLog, proportion=1, flag=wx.EXPAND)
        VirtBoxData.Add(LogWindow, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)

        #VirtBoxData.Add((-1, 25))

        # '''Add 3 check boxes'''
        # hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        # cb1 = wx.CheckBox(panel, label='Case Sensitive')
        # cb1.SetFont(font)
        # hbox4.Add(cb1)
        # cb2 = wx.CheckBox(panel, label='Nested Classes')
        # cb2.SetFont(font)
        # hbox4.Add(cb2, flag=wx.LEFT, border=10)
        # cb3 = wx.CheckBox(panel, label='Non-Project classes')
        # cb3.SetFont(font)
        # hbox4.Add(cb3, flag=wx.LEFT, border=10)
        # vbox.Add(hbox4, flag=wx.LEFT, border=10)
        # ## Finally add to vbox
        # vbox.Add((-1, 25))
        # '''Done'''

        # '''Ok and close buttons'''
        # hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        # btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        # hbox5.Add(btn1)
        # btn2 = wx.Button(panel, label='Close', size=(70, 30))
        # hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        # ## Finally add to vbox
        # vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
        # '''done'''

        '''Add everyting to the panel'''
        panel.SetSizer(VirtBoxData)

if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Go To Class')
    app.MainLoop()
