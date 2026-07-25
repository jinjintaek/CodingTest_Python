import math
def solution(fees, records):
    answer = []
    curr = {}
    total = {}
    def tc(time):
        hour, minute = time.split(':')
        return 60 * int(hour) + int(minute)
    
    for record in records:
        a,b,c = record.split()
        if c == "IN":
            curr[b] = tc(a)
        if c == "OUT":
            total[b] = total.get(b, 0) + (tc(a) - curr[b])
            curr[b] = None
    
    for k, v in curr.items():
        if v != None:
            total[k] = total.get(k, 0) + (tc("23:59") - v)
    
    
    total = sorted(total.items())
    for time in total:
        if time[1] <= fees[0]:
            answer.append(fees[1])
        elif time[1] > fees[0]:
            answer.append(fees[1] + math.ceil((time[1]-fees[0])/fees[2]) * fees[3])
        
            
    return answer