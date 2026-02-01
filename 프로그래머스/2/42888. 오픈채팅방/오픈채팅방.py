def solution(record):
    
    user2nick = {}
    
    for rec in record:
        arr = rec.split()
        if len(arr) > 2:
            user2nick[arr[1]] = arr[2]
    
    answer = []
    
    for rec in record:
        arr = rec.split()
        if arr[0] == "Enter":
            answer.append(f"{user2nick[arr[1]]}님이 들어왔습니다.")
        elif arr[0] == "Leave":
            answer.append(f"{user2nick[arr[1]]}님이 나갔습니다.")
            
    return answer
            
        