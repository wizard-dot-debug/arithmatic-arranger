def arithmatic_arranger(x,y=True):
    if len(x) > 5:
        return 'Error: Too many problems.'
    
    x_top = []
    x_bottom = []
    x_result = []
    x_line = []
    
    for i in x:
        parts = i.split()
        number_1 = parts[0]
        symbol = parts[1]
        number_2 = parts[2]
        result = []
        if len(number_1) or len(number_2) > 4:
            return 'Error: Numbers can not be more than four.'
        elif symbol != '+' or '-':
            return 'Error: Operator must be\'+\' or \'-\'.'
        elif result != str(eval(x)):
            return 'Error: Numbers must only contain digits.'
        max_length = max(len(number_1), len(number_2))
        x_top.append(number_1.rjust(max_length+2))
        x_bottom.append(symbol + ' ' + number_2.rjust(max_length-2))
        x_result.append(result.rjust(max_length))
        x_line.append('-'*max_length)
        
    arranged_x = ''
    if x_top:
        arranged_x += '  '.join(x_top) + '\n'
    elif x_bottom:
        arranged_x += '  '.join(x_bottom) + '\n'
    elif x_line:
        arranged_x += '  '.join(x_line) + '\n'
    elif x_result:
        arranged_x += '  '.join(x_result) + '\n'
    
    return arranged_x 


def call():
    x = list(input('Give The Numbers: '))
    print(f'\n arrithmetic arranger: {arithmatic_arranger(x)}')
    
call()
        
        
        
        
        
    