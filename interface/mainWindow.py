#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import wx
import wx.lib.inspection
import subprocess   # interaction with the operating
import logging	  # logging module: Debug, Info, Warning, Error, Critical

logging.basicConfig(filename='/home/loek/github/framboos/logs/crackInitiation.log' ,level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.ERROR)
logging.debug('Start of program')

APP_EXIT = 1
CONFIG_CRACK = 1

class MainWindow(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs) 
		
		'''Panel size, posiiton, title'''
		self.SetTitle('Crack Initiation')
		self.SetSize((500, 500))
		self.Centre()
		self.Show(True)
		
		self.InitMenuBar()		# Setup the menubar
		#self.InitStatusBar()	# Setup the statusbar
		self.InitPanel()
		self.InitXY()			# Show the x,y position of the top left corner of the panel
		self.InitMouse()		# Show the actual x,y position of the mouse

	def InitMenuBar(self):
		menubar = wx.MenuBar()
		
		menuFile = wx.Menu()
		menuEdit = wx.Menu()
		menuHelp = wx.Menu()
		
		''' Menubar - File '''
		# Quit
		subFile_Quit = wx.MenuItem(menuFile, APP_EXIT, '&Quit\tCtrl+Q')
		menuFile.AppendItem(subFile_Quit)
		self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
		###
		menubar.Append(menuFile, '&File')

		''' Menubar - Edit '''
		# Configd result
		subEdit_Config = wx.MenuItem(menuEdit, CONFIG_CRACK, 'Config\tAlt+C')
		menuEdit.AppendItem(subEdit_Config)
		self.Bind(wx.EVT_MENU, self.onConfig, id=CONFIG_CRACK)
		###
		menubar.Append(menuEdit, '&Edit')
		
		''' Menubar - Help '''
		# About
		menuHelp.Append(100, '&About')
		self.Bind(wx.EVT_MENU, self.OnAboutBox, id=100)
		###
		menubar.Append(menuHelp, '&Help')
		
		''' Finish the menubar '''
		self.SetMenuBar(menubar)

	def InitStatusBar(self):
		statusbar = self.CreateStatusBar()
		#self.statusbar.SetStatusText('This goes in your statusbar')

	def InitPanel(self):
		self.panel = wx.Panel(self)
		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

	def InitXY(self):
		'''XY Panel coordinates'''
		xyText1 = wx.StaticText(self.panel, label='Panel Location', pos=(5,5))
		xyText2 = wx.StaticText(self.panel, label='x:', pos=(120,5))
		xyText3 = wx.StaticText(self.panel, label=', y:', pos=(165,5))
		self.xyText4 = wx.StaticText(self.panel, label='0', pos=(132, 5))
		self.xyText5 = wx.StaticText(self.panel, label='0', pos=(185, 5))
		self.Bind(wx.EVT_MOVE, self.OnMove)

	def InitMouse(self):
		# '''XY Mouse coordinates'''
		MouseXYtext1 = wx.StaticText(self.panel, label='Mouse Location', pos=(5,25))
		MouseXYtext2 = wx.StaticText(self.panel, label='x:', pos=(120,25))
		MouseXYtext3 = wx.StaticText(self.panel, label=', y:', pos=(165,25))
		self.MouseXYtext4 = wx.StaticText(self.panel, label='0', pos=(132, 25))
		self.MouseXYtext5 = wx.StaticText(self.panel, label='0', pos=(185, 25))
		#self.Bind(wx.EVT_MOTION, self.OnMouseMove)
		self.Bind(wx.EVT_SET_CURSOR, self.OnMouseMove)

	def getVersion(self):
		# path = os.path.dirname(os.path.abspath(__file__))
		# command = "git shortlog | grep -E '^[ ]+\w+' | wc -l"
		# result = subprocess.Popen(command, cwd=path)
		# logging.debug("result: " + str(result))
		#try:
		#	result = subprocess.check_output(['git', 'shortlog', '|', 'grep', '-E', "'^[ ]+\w+'", '|', 'wc', '-l'])
		# except subprocess.CalledProcessError as err:
		#	 logging.error('ERROR 1001 - Git get version: ' + str(err))
		#	 return False
		# else:
		#	 result = result.decode('utf-8') 
		#	 logging.debug('GetVersion, result:' + result)
		#	 versie = result.split('\n')
		#	 return versie
		#	 logging.debug("Versie: " + str(versie))
		#	 logging.debug('...done')
		return "V0.99."+str(30)

	def OnAboutBox(self, event):
		#logging.debug("OnAboutBox, event: " + repr(event))

		info = wx.AboutDialogInfo()

		info.SetName('Crack Initiation')
		version = self.getVersion()
		logging.debug("OnAboutBox, version: " + version)
		info.SetVersion(version)
		info.SetDescription("""Crack Initiation is an addon to the MTS Load Frame, it can monitor up to 14 crackinitiation points, and output to the MTS.""")
		info.SetCopyright('(C) 2017 - 2017 Loek Ververgaard')
		info.SetWebSite('http://www.gtm-as.com')
		info.AddDeveloper('Loek Ververgaard')
		info.AddDocWriter('Loek Ververgaard')
		info.AddArtist('GTM Advanced Structures')
		info.AddTranslator('Loek Ververgaard')

		wx.AboutBox(info)
		
	def OnQuit(self, event):
		self.Close()

	def onConfig(self, event):
		self.Close()

	def OnMove(self, event):
		x, y = event.GetPosition()
		self.xyText4.SetLabel(str(x))
		self.xyText5.SetLabel(str(y))

	def OnMouseMove(self, event):
		mouseX, mouseY = wx.GetMousePosition();
		self.MouseXYtext4.SetLabel(str(mouseX))
		self.MouseXYtext5.SetLabel(str(mouseY))

	def OnLeftDown(self, event):
		print('*')

if __name__ == '__main__':
	app = wx.App()		# Manditory for wx
	MainWindow(None)	# Call the class, None means parent frame
	#wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()		# Call the App() as a mainloop, catch all
