import math

def solution(fees, records):
    answer = []
    status = {}
    times = {}
    for record in records:
        r = record.split()
        if r[2] == 'IN':
            status[r[1]] = r[0]
        if r[2] == 'OUT':
            time = timechange(r[0]) - timechange(status[r[1]])
            times[r[1]] = times.get(r[1],0) + time
            status[r[1]] = None 
    for k, v in status.items():
        if v != None:
            time = timechange('23:59') - timechange(v)
            times[k] = times.get(k,0) + time
            
    times = sorted(times.items())
    for time in times:
        if time[1] <= fees[0]:
            price = fees[1]
            answer.append(price)
        else:
            price = math.ceil((time[1] - fees[0]) / fees[2]) * fees[3] + fees[1]
            answer.append(price)
        
    return answer

def timechange(time):
    t = time.split(':')
    return int(t[0]) * 60 + int(t[1])

