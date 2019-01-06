def permute(s):
    out = []
    
    if len(s) == 1:
        out = [s]
    
    for i in range(len(s)):
        # get the first character
        ch = s[i]
        
        # Get all the characters except the selected one
        rch = s[:i] + s[i+1:]
        
        # Iteratre over the rest of the characters to get the permutations
        for p in permute(rch):
            out += [ch+p]
    return out
