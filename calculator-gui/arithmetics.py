import math

class Caculator():
    '''Performs basic arithmetic operations'''
    def __init__(self) -> None:
        self.result = '0'

    def execute(self, user_input):
        '''perfoms addition, substraction, multiplication, floor division and classic division'''
        try:
            input = user_input.replace('×', '*')
            input = input.replace('÷', '/')
            input = input.replace('^', '**')
            self.result = eval(input)
            return self.result
        except SyntaxError:
            return 'Error: Invalid character present'
        except:
            return 'Unknown error'
        
    def square_of(self, number):
        '''Gets number squared'''
        self.result = eval(number+'**2')
        return self.result
    
    def square_root_of(self, number):
        for char in str(number):
            if char not in '+-÷×^*/':
                if Caculator.int_value(number):
                    self.result = math.sqrt(int(number))
                else:
                    self.result = math.sqrt(float(number))
        ans = str(self.result)
        if len(ans) > 2  and str(ans)[-2] == '.' and str(ans)[-1] == '0':
           self.result = ans[:-2]
        return self.result

    def int_value(value):
        try:
            int(value)
        except ValueError:
            return False

    def clear_dot_zero(self, answer):
        answer = str(answer)[:-2]
        return answer
