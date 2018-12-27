def is_balanced(s):
    
    if len(s) % 2 != 0:
        return False
        
    opening = set('([{')
    matches  = set ( [('(',')'), ('[',']'), ('{','}')])
    
    stack = []
    for parentheses in s:

        if parentheses in opening:
            stack.append(parentheses)
        else:
            
            if len(stack) == 0:
                return False
                
            last_parentheses = stack.pop()
            
            if (last_parentheses,parentheses) not in matches:
                return False
    
    return len(stack) == 0
