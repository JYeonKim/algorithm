def solution(array):
    import numpy as np
    array = np.array(array)
    items, counts = np.unique(array, return_counts=True)
    most = 0
    items = [int(item) for item in items]
    counts = [int(cout) for cout in counts]
    for i, c in zip(items, counts):
        if c > most:
            answer = i
            most = c
        elif c == most:
            answer = -1
    return answer