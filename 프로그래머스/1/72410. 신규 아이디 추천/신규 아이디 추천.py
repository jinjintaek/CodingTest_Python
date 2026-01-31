def solution(new_id):
    new_id = new_id.lower()
    
    result = ""
    for i in new_id:
        if i.isalnum() or i in ['-','_','.']:
            result += i
    
    new_id = result
    
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    new_id = new_id.strip('.')
    
    if not new_id:
        new_id += "a"
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')
    
    while len(new_id) <3:
        new_id += new_id[-1]
    
    return new_id
            
            