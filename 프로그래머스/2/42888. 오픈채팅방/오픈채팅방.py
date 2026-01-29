def solution(record):
    record_list = []


    for rec in record:
        record_list.append(rec.split())

    user2nick = {}

    for arr in record_list:
        if len(arr) == 3:
            user2nick[arr[1]] = arr[2]
        

    answer = []
    for arr in record_list:
        if arr[0] == 'Enter':
            answer.append(f"{user2nick[arr[1]]}님이 들어왔습니다.")
        elif arr[0] == 'Leave':
            answer.append(f"{user2nick[arr[1]]}님이 나갔습니다.")

    return answer
