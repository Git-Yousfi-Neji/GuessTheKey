import random


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