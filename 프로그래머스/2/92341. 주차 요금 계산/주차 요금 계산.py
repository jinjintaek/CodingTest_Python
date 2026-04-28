import math

def solution(fees, records):
    
    latest_time = {}
    total_time = {}
    answer = []
    
    for record in records:
        r = record.split()
        t, n, s = r[0], r[1], r[2]
        if s == 'IN':
            latest_time[n] = t
        if s == 'OUT':
            gap = tc(t) - tc(latest_time[n])
            total_time[n] = total_time.get(n, 0) + gap
            latest_time[n] = None
    for k, v in latest_time.items():
        if v != None:
            gap = tc('23:59') - tc(latest_time[k])
            total_time[k] = total_time.get(k, 0) + gap
            
    total_time = sorted(total_time.items())
    
    for tt in total_time:
        time = tt[1]
        answer.append(max(math.ceil((time - fees[0]) / fees[2]) * fees[3] + fees[1], fees[1]))
    
    return answer
    
def tc(time):
    tt = time.split(':')
    return int(tt[0]) * 60 + int(tt[1])
    
        