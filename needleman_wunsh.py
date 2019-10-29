import numpy as np

def compare_sequences(a, b, same=5, diff=-5, gap_penalty=-2):
    H = np.zeros((len(a)+1, len(b)+1))
    # fill first row and column
    H[0][0] = 0
    for i in range(1, H.shape[1]):
        H[0][i] = H[0][i-1] + gap_penalty
    
    for i in range(1, H.shape[0]):
        H[i][0] = H[i-1][0] + gap_penalty

    # init paths
    paths = np.zeros( (H.shape[0], H.shape[1], 3 ) )

    for i in range(1, H.shape[0]):
        for j in range(1, H.shape[1]):
            from_up = H[i - 1][j] + gap_penalty
            from_left = H[i][j-1] + gap_penalty
            if a[i-1] == b[j-1]:
                from_diag = H[i-1][j-1] + same
            else:
                from_diag = H[i-1][j-1] + diff

            H[i][j] = max(from_up, from_left, from_diag)
            # TODO as function
            paths[i][j] = np.array([from_up, from_left, from_diag]) == H[i][j]
            
    return H, paths

def get_paths_from_directions(directions, seq_a, seq_b, curr_seq_a = '', curr_seq_b = '', pos=None):
    if pos is None:
        x, y = directions.shape[0] - 1, directions.shape[1] - 1
    else:
        x, y = pos

    if x == 0 and y == 0:
        print('a: ', curr_seq_a[::-1], '\nb: ', curr_seq_b[::-1], '\n')
        return 

    if x == 0: # now we go always from left
        print('a: ', '_' * y + curr_seq_a[::-1], '\nb: ', seq_b[:y] + curr_seq_b[::-1], '\n')
        return 
    
    if y == 0:
        print('a: ', seq_a[:x] + curr_seq_a[::-1], '\nb: ', '_' * x + curr_seq_b[::-1], '\n')        
        return

    if directions[x][y][0]: # from up (first dim is height)
        next_seq_a = curr_seq_a + seq_a[x-1]
        next_seq_b = curr_seq_b + '_'
        get_paths_from_directions(directions, seq_a, seq_b, next_seq_a, next_seq_b, (x-1, y))

    if directions[x][y][1]: # from left (second dim is width)
        next_seq_a = curr_seq_a + '_'
        next_seq_b = curr_seq_b + seq_b[y-1]
        get_paths_from_directions(directions, seq_a, seq_b, next_seq_a, next_seq_b, (x, y-1))
        
    if directions[x][y][2]: # from diag
        next_seq_a = curr_seq_a + seq_a[x-1]
        next_seq_b = curr_seq_b + seq_b[y-1]
        get_paths_from_directions(directions, seq_a, seq_b, next_seq_a, next_seq_b, (x-1, y-1) )

