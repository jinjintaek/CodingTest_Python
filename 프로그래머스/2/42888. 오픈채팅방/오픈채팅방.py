def solution(record):
    usr = {}
    result = []
    
    for r in record:
        recs = r.split()
        if len(recs) > 2:
            command, uid, name = recs[0], recs[1], recs[2]
            
            if command == "Enter" or command == "Change":
                usr[uid] = name 
        
    for r in record:
        recs = r.split()
        if recs[0] == "Enter":
            result.append(f"{usr[recs[1]]}님이 들어왔습니다.")
        if recs[0] == "Leave":
            result.append(f"{usr[recs[1]]}님이 나갔습니다.")
    
    return result
    
    