def solution(arr):
    indices = []
    for i in range(len(arr)):
        if arr[i] == 2:
            indices.append(i)
    if not indices:
        return [-1]
    return arr[indices[0] : indices[-1] + 1]