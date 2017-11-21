#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import wx
import subprocess   # interaction with the operating
import logging	  # logging module: Debug, Info, Warning, Error, Critical

logging.basicConfig(filename='logs/crackInitiation.log' ,level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
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
		#self.InitXY()			# Show the x,y position of the top left corner of the panel
		#self.InitPanel()		# Setup the actual connectors
		#self.InitLogPanel()	# Start the logpanel

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
	
	def InitXY(self):
		#panel = wx.Panel(self)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		VirtBoxXY = wx.BoxSizer(wx.VERTICAL)

		'''XY Panel coordinates'''
		xyWindow = wx.BoxSizer(wx.HORIZONTAL)

		xyText1 = wx.StaticText(self, label='Panel Location, ', pos=(5,5))
		xyWindow.Add(xyText1, flag=wx.RIGHT, border=8)
		
		xyText2 = wx.StaticText(self, label='x:', pos=(120,5))
		xyWindow.Add(xyText2, flag=wx.RIGHT, border=8)
		
		xyText3 = wx.StaticText(self, label='y:', pos=(160,5))
		xyWindow.Add(xyText3, flag=wx.RIGHT, border=8)
		
		self.xyText4 = wx.StaticText(self, label='0', pos=(130, 5))
		self.xyText5 = wx.StaticText(self, label='0', pos=(170, 5))
		self.Bind(wx.EVT_MOVE, self.OnMove)

		VirtBoxXY.Add(xyWindow, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		'''Add extra space'''
		#VirtBoxData.Add((-1, 10))

		# '''XY Mouse coordinates'''
		MouseXYWindow = wx.BoxSizer(wx.HORIZONTAL)

		MouseXYtext1 = wx.StaticText(self, label='Mouse Location, ', pos=(5,25))
		MouseXYWindow.Add(MouseXYtext1, flag=wx.RIGHT, border=8)
		
		MouseXYtext2 = wx.StaticText(self, label='x:', pos=(120,25))
		MouseXYWindow.Add(MouseXYtext2, flag=wx.RIGHT, border=8)
		
		MouseXYtext3 = wx.StaticText(self, label='y:', pos=(160,25))
		MouseXYWindow.Add(MouseXYtext3, flag=wx.RIGHT, border=8)
		
		#self.MouseXYtext4 = wx.StaticText(self, label='0', pos=(130, 25))
		#MouseXYWindow.Add(MouseXYtext4, flag=wx.RIGHT, border=8)
		
		#self.MouseXYtext5 = wx.StaticText(self, label='0', pos=(170, 25))
		#MouseXYWindow.Add(MouseXYtext5, flag=wx.RIGHT, border=8)
		
		self.Bind(wx.EVT_MOTION, self.OnMouseMove)

		VirtBoxXY.Add(MouseXYWindow, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		'''Add everyting to the panel'''
		#panel.SetSizer(VirtBoxXY)
		self.SetSizer(VirtBoxXY)

	def InitPanel(self):
		panel = wx.Panel(self)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		VirtBoxData = wx.BoxSizer(wx.VERTICAL)

		'''DataWindow'''
		DataWindow = wx.BoxSizer(wx.HORIZONTAL)
		# self.col = wx.Colour(0, 0, 0)
		# buttonOne = wx.ToggleButton(panel, label='conn1', pos=(5, 100))
		# self.cpnl  = wx.Panel(panel, pos=(5, 150), size=(110, 110))
		# self.cpnl.SetBackgroundColour(self.col)
		# buttonOne.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleOnOff)
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
		return str(12)

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
		mouseX = wx.GetMousePosition().x;
		mouseY = wx.GetMousePosition().y;
		self.MouseXYtext4.SetLabel(str(mouseX))
		self.MouseXYtext5.SetLabel(str(mouseY))

	def ToggleOnOff(self, event):
		obj = event.GetEventObject()
		isPressed = obj.GetValue()
		
		green = self.col.Green()
		blue = self.col.Red()
		
		if isPressed:
			self.col.Set(255, green, blue)
		else:
			self.col.Set(0, green, blue)
			
		self.cpnl.SetBackgroundColour(self.col)
		self.cpnl.Refresh()

if __name__ == '__main__':
	app = wx.App()		# Manditory for wx
	MainWindow(None)	# Call the class, None means parent frame
	app.MainLoop()		# Call the App() as a mainloop, catch all