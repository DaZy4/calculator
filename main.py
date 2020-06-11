from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.config import Config 


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 300)


class CalcApp(App):
	def backspace(self, instance):
		self.formula = repr(self.formula)[1:-2]
		self.lbl_update()

	def lbl_update(self):
		self.lbl.text = self.formula

	def oper(self, instance):
		try:
			self.formula = str(eval(self.formula))
			self.lbl_update()
		except:
			pass

	def clear(self, instance):
		self.formula = ''
		self.lbl_update()


	def add_number(self, instance):
		self.formula += instance.text
		self.lbl_update()

	def build(self):
		self.formula = ''

		self.lbl = Label(text='0', size_hint=(1,.3))


		bl = BoxLayout(orientation='vertical')
		gl = GridLayout(cols=4)

		gl.add_widget(Button(text='(', on_press=self.add_number))
		gl.add_widget(Button(text='<-', on_press=self.backspace))
		gl.add_widget(Button(text=')', on_press=self.add_number))
		gl.add_widget(Button(text='/', on_press=self.add_number))

		gl.add_widget(Button(text='7', on_press=self.add_number))
		gl.add_widget(Button(text='8', on_press=self.add_number))
		gl.add_widget(Button(text='9', on_press=self.add_number))
		gl.add_widget(Button(text='* ', on_press=self.add_number))

		gl.add_widget(Button(text='4', on_press=self.add_number))
		gl.add_widget(Button(text='5', on_press=self.add_number))
		gl.add_widget(Button(text='6', on_press=self.add_number))
		gl.add_widget(Button(text='+', on_press=self.add_number))

		gl.add_widget(Button(text='1', on_press=self.add_number))
		gl.add_widget(Button(text='2', on_press=self.add_number))
		gl.add_widget(Button(text='3', on_press=self.add_number))
		gl.add_widget(Button(text='-', on_press=self.add_number))

		gl.add_widget(Button(text='C', on_press=self.clear))
		gl.add_widget(Button(text='0', on_press=self.add_number))
		gl.add_widget(Button(text='.', on_press=self.add_number))
		gl.add_widget(Button(text='=', on_press=self.oper))

		bl.add_widget(self.lbl)

		bl.add_widget(gl)

		return bl

CalcApp().run()