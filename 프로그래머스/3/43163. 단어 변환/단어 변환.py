from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = [False] * len(words)
    
    while queue:
        current, step = queue.popleft()
        
        if current == target:
            return step
        
        for i, word in enumerate(words):
            if not visited[i] and can_convert(current,word):
                visited[i] = True
                queue.append((word, step+1))
                
    return 0

def can_convert(word1, word2):
    diff = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff == 1
