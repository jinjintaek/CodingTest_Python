def solution(arr):
    count = 0
    
    while True:
        next_arr = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                next_arr.append(num // 2)
            elif num < 50 and num % 2 != 0:
                next_arr.append(num * 2 + 1)
            else:
                next_arr.append(num)
                
        if arr == next_arr:
            return count
        
        arr = next_arr
        count += 1
    return count