#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import wx
import subprocess   # interaction with the operating
import logging	  # logging module: Debug, Info, Warning, Error, Critical

logging.basicConfig(filename='logs/crackInitiation.log' ,level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.ERROR)
logging.debug('Start of program')

APP_EXIT = 1
CONFIG_CRACK = 1

class Example(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs) 
		
		self.InitUI()
		self.InitMenuBar()
		self.InitXY()
		self.InitPanel()

	def InitUI(self):
		'''Panel size, posiiton, title'''
		self.SetTitle('Testje')
		self.SetSize((500, 500))
		self.Centre()
		self.Show(True)

	def InitMenuBar(self):
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
	
	def InitXY(self):
		'''XY coordinates'''
		wx.StaticText(self, label='x:', pos=(10,350))
		wx.StaticText(self, label='y:', pos=(10,370))
		self.st1 = wx.StaticText(self, label='', pos=(30, 350))
		self.st2 = wx.StaticText(self, label='', pos=(30, 370))
		self.Bind(wx.EVT_MOVE, self.OnMove)

	def InitPanel(self):
		'''Button'''
		panel = wx.Panel(self)
		self.col = wx.Colour(0, 0, 0)
		buttonOne = wx.ToggleButton(panel, label='conn1', pos=(20, 50))
		self.cpnl  = wx.Panel(panel, pos=(150, 20), size=(110, 110))
		self.cpnl.SetBackgroundColour(self.col)
		buttonOne.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleOnOff)

	def getVersion(self, e):
		try:
			result = subprocess.check_output(['git', 'shortlog', '|', 'grep', '-E', "^[ ]+\w+'", '|', 'wc', '-l'])
		except subprocess.CalledProcessError as err:
			logging.error('ERROR 1001 - Git get version: ' + err)
			return False
		else:
			result = result.decode('utf-8') 
			print('result:' + result)
			self.versie = result.split('\n')
			#print('versie: ' + self.versie)
			logging.debug('...done')

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
		info.SetVersion('4')
		info.SetDescription(description)
		info.SetCopyright('(C) 2017 - 2017 Loek Ververgaard')
		info.SetWebSite('http://www.gtm-as.com')
		info.SetLicence(licence)
		info.AddDeveloper('Loek Ververgaard')
		info.AddDocWriter('Loek Ververgaard')
		info.AddArtist('GTM Advanced Structures')
		info.AddTranslator('Loek Ververgaard')

		wx.AboutBox(info)
		
	def OnQuit(self, e):
		self.Close()

	def onConfig(self, e):
		self.Close()

	def OnMove(self, e):
		x, y = e.GetPosition()
		self.st1.SetLabel(str(x))
		self.st2.SetLabel(str(y))

	def ToggleOnOff(self, e):
		obj = e.GetEventObject()
		isPressed = obj.GetValue()
		
		green = self.col.Green()
		blue = self.col.Red()
		
		if isPressed:
			self.col.Set(255, green, blue)
		else:
			self.col.Set(0, green, blue)
			
		self.cpnl.SetBackgroundColour(self.col)
		self.cpnl.Refresh()

def main():
	
	ex = wx.App()
	Example(None)
	ex.MainLoop()	


if __name__ == '__main__':
	main()