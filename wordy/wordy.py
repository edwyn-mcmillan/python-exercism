def answer(question):
    if 'What is' not in question:
        raise ValueError("unknown operation")

    question = question.replace('plus','+')
    question = question.replace('minus','-')
    question = question.replace('multiplied by','*')
    question = question.replace('divided by','/')
    operations = [op for op in question[7:-1].split(' ') if op != '']

    for i in range(len(operations)):
        if operations[i].lstrip('-').isdigit():
            operations[i] = int(operations[i])
        else:
            if (i % 2 == 0):
                raise ValueError("syntax error")
            if operations[i] not in ['+','-','*','/']:
                raise ValueError("unknown operation")
        
    if(len(operations) % 2 == 0):
        raise ValueError("syntax error")
        
    answer = operations.pop(0)
    while len(operations) > 0:
        if operations[0] == '+':
             answer = answer + operations[1]
        elif operations[0] == '-':
             answer = answer - operations[1]
        elif operations[0] == '*':
             answer = answer * operations[1]
        elif operations[0] == '/':
            answer = answer / operations[1]
        operations = operations[2:]
    return answer