#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
ZetCode wxPython tutorial

In this example, we manually create 
a menu item.

author: Jan Bodnar
website: www.zetcode.com
last modified: September 2011
'''

import wx

APP_EXIT = 1
CONFIG_CRACK = 1

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):

        menubar = wx.MenuBar()

        ''' Menubar - File '''
        fileMenu = wx.Menu()
        # Quit
        menuQuit = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        fileMenu.AppendItem(menuQuit)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
        # Config
        menuConfig = wx.MenuItem(fileMenu, CONFIG_CRACK, 'Config\tAlt+F')
        fileMenu.AppendItem(menuConfig)
        self.Bind(wx.EVT_MENU, self.onConfig, id=CONFIG_CRACK)

        menubar.Append(fileMenu, '&File')

        ''' Menubar - Help '''
        menuHelp = wx.Menu()
        menuHelp.Append(100, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id=100)
        
        menubar.Append(menuHelp, '&Help')

        self.SetMenuBar(menubar)

        self.SetSize((500, 500))
        self.SetTitle('Icons and shortcuts')
        self.Centre()
        self.Show(True)

    def OnAboutBox(self, e):
        description = """File Hunter is an advanced file manager for the Unix operating system. 
                        Features include powerful built-in editor, 
                        advanced search capabilities, powerful batch renaming, 
                        file comparison, extensive archive handling and more."""

        licence = """File Hunter is free software; you can redistribute 
                    it and/or modify it under the terms of the GNU General Public License as 
                    published by the Free Software Foundation; either version 2 of the License, 
                    or (at your option) any later version.

                    File Hunter is distributed in the hope that it will be useful, 
                    but WITHOUT ANY WARRANTY; without even the implied warranty of 
                    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
                    See the GNU General Public License for more details. You should have 
                    received a copy of the GNU General Public License along with File Hunter; 
                    if not, write to the Free Software Foundation, Inc., 59 Temple Place, 
                    Suite 330, Boston, MA  02111-1307  USA"""


        info = wx.AboutDialogInfo()

        #info.SetIcon(wx.Icon('hunter.png', wx.BITMAP_TYPE_PNG))
        info.SetName('Crack Initiation')
        info.SetVersion('0.1')
        info.SetDescription(description)
        info.SetCopyright('(C) 2007 - 2014 Jan Bodnar')
        info.SetWebSite('http://www.zetcode.com')
        info.SetLicence(licence)
        info.AddDeveloper('Jan Bodnar')
        info.AddDocWriter('Jan Bodnar')
        info.AddArtist('The Tango crew')
        info.AddTranslator('Jan Bodnar')

        wx.AboutBox(info)
        
    def OnQuit(self, e):
        self.Close()

    def onConfig(self, e):
        self.Close()

    def getVersion():
        num = "git shortlog | grep -E '^[ ]+\w+' | wc -l"
        return 

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()