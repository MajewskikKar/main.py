


import numpy as np
from time import time
loop_time = time()
import win32gui, win32ui, win32con
import warnings
#warnings.simplefilter("ignore", DeprecationWarning)
class WindowCapture:

	#properties
	w = 0
	h = 0
	hwnd = None

	 # account for the window border and titlebar and cut them off
	cropped_x = 0
	cropped_y = 0
	offset_x = 0
	offset_y = 0

	#constructor
	def __init__(self, window_name=None):

		if window_name is None:
			self.hwnd = win32gui.GetDesktopWindow()
		else:
			self.hwnd = win32gui.FindWindow(None, 'Literaki — Mozilla Firefox')
			if not self.hwnd:
				raise Exception("Literaki nie są włączone")

		#define your width and height
		window_rect = win32gui.GetWindowRect(self.hwnd)
		self.w = window_rect[2] - window_rect[0]
		self.h = window_rect[3] - window_rect[1]

		# account for the window border and titlebar and cut them off
		border_pixels = 8
		titlebar_pixels = 30
		self.w = self.w - (border_pixels * 2)
		self.h = self.h - titlebar_pixels - border_pixels
		self.cropped_x = border_pixels
		self.cropped_y = titlebar_pixels

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
		self.offset_x = window_rect[0] + self.cropped_x
		self.offset_y = window_rect[1] + self.cropped_y
	def screen(self):

		wDC = win32gui.GetWindowDC(self.hwnd)
		dcObj=win32ui.CreateDCFromHandle(wDC)
		cDC=dcObj.CreateCompatibleDC()
		dataBitMap = win32ui.CreateBitmap()
		dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
		cDC.SelectObject(dataBitMap)
		cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

		#convert to format for openCV
		#dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
		signedIntsArray = dataBitMap.GetBitmapBits(True)
		img = np.fromstring(signedIntsArray, dtype='uint8')
		img.shape = (self.h, self.w, 4)

		# Free Resources
		dcObj.DeleteDC()
		cDC.DeleteDC()
		win32gui.ReleaseDC(self.hwnd, wDC)
		win32gui.DeleteObject(dataBitMap.GetHandle())

		img = img[...,:3]
		img = np.ascontiguousarray(img)

		return img

#	def get_screen_position(self, pos):
#		return (pos[0] + self.offset_x, pos[1] + self.offset_y)

	#show open windows
	# @staticmethod
	def list_window_names():
		def winEnumHandler(hwnd, ctx):
			if win32gui.IsWindowVisible( hwnd ):
				print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )
		win32gui.EnumWindows( winEnumHandler, None )
	def get_screen_position(self, pos):
		return (pos[0] + self.offset_x, pos[1] + self.offset_y)
	#while True:

	#	screenshot = screen()
	#	screenshot = np.array(screenshot)
	#	screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
	#	cv.imshow('frame', screenshot)


		#print( 'FPS {}'.format(1/(time() - loop_time)))
		loop_time=time()

		#if cv.waitKey(1) == ord('q'):
		#	break

print('Done.')
#Window = WindowCapture('Literaki - Mozilla Firefox')
#Window.screen()
