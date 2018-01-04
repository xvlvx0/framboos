#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import wx

class ShapedButton(wx.PyControl):
    def __init__(self, parent, normal, pressed=None, disabled=None):
        super(ShapedButton, self).__init__(parent, -1, style=wx.BORDER_NONE)
        self.normal = normal
        self.pressed = pressed
        self.disabled = disabled
        self.region = wx.RegionFromBitmapColour(normal, wx.Colour(0, 0, 0, 0))
        self._clicked = False
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)

    def DoGetBestSize(self):
        return self.normal.GetSize()

    def Enable(self, *args, **kwargs):
        super(ShapedButton, self).Enable(*args, **kwargs)
        self.Refresh()

    def Disable(self, *args, **kwargs):
        super(ShapedButton, self).Disable(*args, **kwargs)
        self.Refresh()

    # def post_event(self):
    #     event = wx.CommandEvent()
    #     event.SetEventObject(self)
    #     event.SetEventType(wx.EVT_BUTTON.typeId)
    #     wx.PostEvent(self, event)

    def on_size(self, event):
        event.Skip()
        self.Refresh()

    def on_paint(self, event):
        dc = wx.AutoBufferedPaintDC(self)
        dc.SetBackground(wx.Brush(self.GetParent().GetBackgroundColour()))
        dc.Clear()
        bitmap = self.normal
        if self.clicked:
            bitmap = self.pressed or bitmap
        if not self.IsEnabled():
            bitmap = self.disabled or bitmap
        dc.DrawBitmap(bitmap, 0, 0)

    def set_clicked(self, clicked):
        if clicked != self._clicked:
            self._clicked = clicked
            self.Refresh()

    def get_clicked(self):
        return self._clicked

    clicked = property(get_clicked, set_clicked)
    def on_left_down(self, event):
        x, y = event.GetPosition()
        if self.region.Contains(x, y):
            self.clicked = not self.clicked
            print('clicked is: ' + str(self.clicked))

def main():
    def on_button(event):
        print('Button was clicked.')
    app = wx.App()
    frame = wx.Frame(None, -1, 'Shaped Button Demo')
    panel = wx.Panel(frame, -1)
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.AddStretchSpacer(1)

    buttonNames = []
    for i in range(0, 10):
        buttonNames.append('button'+str(i))
        
    for bName in buttonNames:
        bName = ShapedButton(panel, 
                    wx.Bitmap('Switch_OFF.png'), 
                    wx.Bitmap('Switch_ON.png'), 
                    wx.Bitmap('Switch_GRAY.png'))
        bName.Bind(wx.EVT_BUTTON, on_button)
        sizer.Add(bName, 0, wx.ALIGN_CENTER)

    sizer.AddStretchSpacer(1)
    panel.SetSizer(sizer)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()