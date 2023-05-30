from datetime import datetime, timedelta
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.clock import Clock
from game.hints import *


class GuessTheKey(BoxLayout):
    def random_key(self):
            while True:
                num = random.randint(100, 999)
                if len(set(str(num))) == 3:
                    return num
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.key = self.random_key()
       
            #+++++++++++++++++++++++
        key=GuessTheKey.random_key(self)
        
        
        
        
        
        #+++++++++++++++++++++++
        # Add title label
        title_label = Label(text="Guess the Key", font_size='35sp', size_hint=(1, 0.1))
        self.add_widget(title_label)
        #==================
        def update_remaining_time(self, *args):
            remaining_time = end_time - datetime.now()
            if remaining_time.total_seconds() <= 0:
                inputText1.disabled=True
                inputText2.disabled=True
                inputText3.disabled=True 
                remain_time.text="You lose, the key was "+str(key)
            else:
                remain_time.text = "Remaining time: " + str(remaining_time.seconds) + " seconds"
            
        end_time = datetime.now() + timedelta(seconds=180)
        
        remain_time= Label(text="remain time", font_size='20sp', size_hint=(1, 0.1))
        Clock.schedule_interval(update_remaining_time, 1)
        self.add_widget(remain_time)
        #==================
        # Add input fields
        input_box = BoxLayout(size_hint=(1, 0.3))
        self.add_widget(input_box)

        inputText1=TextInput(multiline=False, size_hint=(0.5, 0.5), font_size='100sp', input_type='number',halign='center', input_filter='int')
        input_box.add_widget(inputText1)
        inputText2=TextInput(multiline=False, size_hint=(0.5, 0.5), font_size='100sp', input_type='number',halign='center', input_filter='int')
        input_box.add_widget(inputText2)
        inputText3=TextInput(multiline=False, size_hint=(0.5, 0.5), font_size='100sp', input_type='number',halign='center', input_filter='int')
        input_box.add_widget(inputText3)


        # Add hint labels
        hint_box = BoxLayout(orientation='vertical', size_hint=(1, 0.3))
        self.add_widget(hint_box)

        for i in range(5):
            hint_label = Label(text=str(hint(self)), font_size='15sp', size_hint=(1, 0.2) )
            hint_box.add_widget(hint_label)
            
        def clear_text(self):
                inputText1.text = ''
                inputText2.text = ''
                inputText3.text = ''
       
        def checkKey(self):
            #key = GuessTheKey.random_key(self)
            if int(inputText1.text+inputText2.text+inputText3.text)==key:
                popup_content1 = Label(text='Congratulations', font_size='20sp')
                error_popup1 = Popup(title='Info', content=popup_content1, size_hint=(None, None), size=(400, 200), auto_dismiss=True)
                error_popup1.open()
                Clock.schedule_once(lambda dt: error_popup1.dismiss(), 2)
            else:
                popup_content = Label(text='Try again', font_size='20sp')
                error_popup = Popup(title='Error', content=popup_content, size_hint=(None, None), size=(400, 200), auto_dismiss=True)
                error_popup.open()
                Clock.schedule_once(lambda dt: error_popup.dismiss(), 2)
            
            
        # Add submit and clear buttons
        button_box = BoxLayout(size_hint=(1, 0.2), spacing=20, padding=20)
        self.add_widget(button_box)

        submit_button = Button(text='Submit', font_size='20sp', size_hint=(0.4, 1), background_normal='', background_color=[0.5, 0.7, 1, 1])
        
        clear_button = Button(text='Clear', font_size='20sp', size_hint=(0.4, 1), background_normal='', background_color=[1, 0.7, 0.5, 1] )
        clear_button.bind(on_press=clear_text)
        submit_button.bind(on_press=checkKey)

        button_box.add_widget(submit_button)
        button_box.add_widget(clear_button)