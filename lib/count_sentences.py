#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ''):
        self._value = value


    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False
        
    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print('The value must be a string.')


    def count_sentences(self):
     modified_value = self.value.replace('.', '!').replace('?', '!')
     sentences = modified_value.split('!')
     sentences = [sentence for sentence in sentences if sentence.strip() != '']
     
     count = len(sentences)

     print(count)
     return count
    