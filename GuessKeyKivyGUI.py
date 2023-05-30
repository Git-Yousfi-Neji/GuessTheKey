#pylint:disable=R0201
#pylint:disable=C0303
#pylint:disable=C0115
#pylint:disable=C0301
#pylint:disable=W0612
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock
from datetime import datetime, timedelta
import random 

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
        
        def nothing_correct(self,key):
        	key_digits = set(str(key))
        	while True:
        	       number = random.randint(100, 999)
        	       if set(str(number)).isdisjoint(key_digits):
                        return number
        
        def one_correct_digit_correct_position(self,key):
            key_digits = list(str(key))
            while True:
                number = random.sample(range(10), 3)
                if 0 in number:
                    continue
                number = ''.join(map(str, number))
                common_digits = [d for i, d in enumerate(number) if d == key_digits[i]]
                if len(common_digits) == 1:
                    other_digits = [d for d in number if d not in key_digits]
                    if len(other_digits) == 2:
                        return int(number)
        
        def two_correct_digits_correct_position(self,key):
            key_digits = list(str(key))
            while True:
                number = random.sample(range(10), 3)
                if 0 in number:
                    continue
                number = ''.join(map(str, number))
                common_digits = [d for i, d in enumerate(number) if d == key_digits[i]]
                if len(common_digits) == 2:
                    other_digit = [d for d in number if d not in key_digits]
                    if len(other_digit) == 1:
                        return int(number)

        
        def one_correct_digit_wrong_position(self,key):
            key_digits = list(str(key))
            while True:
                number = random.sample(range(10), 3)
                if 0 in number:
                    continue
                number = ''.join(map(str, number))
                common_digit = [d for d in number if d in key_digits]
                if len(common_digit) == 1:
                    if common_digit[0] != key_digits[number.index(common_digit[0])]:
                        other_digits = [d for d in number if d not in key_digits]
                        if len(other_digits) == 2:
                            return int(number)        
        
        def two_correct_digit_wrong_position(self,key):
            key_digits = list(str(key))
            while True:
                num = random.sample(range(10), 3)
                if num[0] == 0:
                    continue
                num_digits = list(map(str, num))
                common_digits = set(num_digits) & set(key_digits)
                if len(common_digits) == 2 and num_digits.index(list(common_digits)[0]) != key_digits.index(list(common_digits)[0]) and num_digits.index(list(common_digits)[1]) != key_digits.index(list(common_digits)[1]) and len(set(num_digits)) == 3:
                    return int(''.join(num_digits))
        
        def three_correct_digits_wrong_position(self,key):
            key_digits = list(str(key))
            while True:
                num = random.randint(100, 999)
                num_digits = list(str(num))
                common_digits = set(num_digits) & set(key_digits)
                if len(common_digits) == 3:
                    common_positions = [i for i in range(3) if key_digits[i] == num_digits[i]]
                    if len(common_positions) == 0:
                        return num
                        
        def hint(self):
        	hints_dict={
        " Nothing is correct":nothing_correct(self,key),
        " One correct digit and in the correct position":one_correct_digit_correct_position(self,key),
        " Two correct digits and in the correct position":two_correct_digits_correct_position(self,key),
        " One correct digit but in the wrong position":one_correct_digit_wrong_position(self,key),
        " Two correct digits but in the wrong position":two_correct_digit_wrong_position(self,key),
        " Three correct digits but in the wrong position":three_correct_digits_wrong_position(self,key)
        }
        	value,keyy=random.choice(list(hints_dict.items()))
        	return f"{keyy} - {value}"
        
        
        
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

class GuessTheKeyApp(App):
    def build(self):
        return GuessTheKey()

GuessTheKeyApp().run()
