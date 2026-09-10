def solution(arr):
    answer = [[]]
    row_count = len(arr)
    col_count = len(arr[0])
    if row_count>col_count:
        diff = row_count - col_count
        for row in arr:
            row.extend([0] * diff)
            
    elif col_count > row_count:
        diff = col_count - row_count
        for _ in range(diff):
            arr.append([0] * col_count)
            
    return arr