import math

def solution(fees, records):
    total_time = {}
    current_time = {}
    for record in records:
        t,n,s = record.split()
        if s == "IN":
            current_time[n] = tc(t)
        else:
            total_time[n] = total_time.get(n, 0) + (tc(t) - current_time[n])
            current_time[n] = None
            
    for k, v in current_time.items():
        if v != None:
            total_time[k] = total_time.get(k, 0) + (tc("23:59") - v)
    
    total_time = sorted(total_time.items())
    
    
    
    answer = []
    for (k, v) in total_time:
        if v > fees[0]:
            answer.append(fees[1]+ math.ceil((v-fees[0])/fees[2]) * fees[3])
        else:
            answer.append(fees[1])
        
    return answer

def tc(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)
        
            
        