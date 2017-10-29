#!/usr/bin/python2.7
import sys

try:
	import wx
except:
	print("wxPython is not installed. This program requires wxPython to run.")
	if sys.version_info.major >= 3:
		print("""As you are currently running python3, this is most likely because wxPython is not yet available for python3. You should try running with python2 instead.""")
		sys.exit(-1)
	else:
		raise

class mainScreen(wx.Frame):
	def __init__(self, parent, title):
		super(mainScreen, self).__init__(parent, title=title, size=(400, 500))	# size = width by heigth
		self.InitUI()
		self.Centre()	# Center on screen
		self.Show(True)
		
	def InitUI(self):	
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fileMenu.Append(wx.ID_NEW, '&New')
		fileMenu.Append(wx.ID_OPEN, '&Open')
		fileMenu.Append(wx.ID_SAVE, '&Save')
		fileMenu.AppendSeparator()
		
		imp = wx.Menu()
		imp.Append(wx.ID_ANY, 'Import newsfeed list...')
		imp.Append(wx.ID_ANY, 'Import bookmarks...')
		imp.Append(wx.ID_ANY, 'Import mail...')
		fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)

		qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
		fileMenu.AppendItem(qmi)

		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)
		
		self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
		
	def OnQuit(self, e):
		self.Close()

	def OnConfig():
		wireConfig()

	def OnHelp():
		showHelp():


if __name__ == '__main__':
	app = wx.App()
	mainScreen(None, title='crackInitiation')
	app.MainLoop()
