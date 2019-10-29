import numpy as np

class NeedlemanWunshSolver:

    def __init__(self, same=5, diff=-5, gap_penalty=-2, max_number_paths=1000, output_path=None):
        self.same = same
        self.diff = diff
        self.gap_penalty = gap_penalty
        self.max_number_paths = max_number_paths
        self.output_path = output_path

    # returns score matrix and directions
    # directions encodes arrows at each position in H matrix
    # each field is a boolean vector, if a arrow exists in given direction
    # [arrow_up, arrow_left, arrow_diagonal]
    def find_score_matrix_with_directions(self, seq_a, seq_b):

        H = self._get_score_matrix((len(seq_a)+1, len(seq_b)+1))

        directions = np.zeros( (H.shape[0], H.shape[1], 3 ) )

        for i in range(1, H.shape[0]):
            for j in range(1, H.shape[1]):
                from_up = H[i - 1][j] + self.gap_penalty
                from_left = H[i][j-1] + self.gap_penalty
                if seq_a[i-1] == seq_b[j-1]:
                    from_diag = H[i-1][j-1] + self.same
                else:
                    from_diag = H[i-1][j-1] + self.diff

                H[i][j] = max(from_up, from_left, from_diag)
                directions[i][j] = self._get_arrows(from_up, from_left, from_diag, H[i][j])
                
        return H, directions

    def _get_score_matrix(self, shape):
        H = np.zeros(shape)
        # fill first row and column
        H[0][0] = 0
        for i in range(1, H.shape[1]):
            H[0][i] = H[0][i-1] + self.gap_penalty
        
        for i in range(1, H.shape[0]):
            H[i][0] = H[i-1][0] + self.gap_penalty

        return H

    def _get_arrows(self, score_from_up, score_from_left, score_from_diag, best_score):
        return np.array([score_from_up, score_from_left, score_from_diag]) == best_score

    def find_possible_alignments(self, directions, seq_a, seq_b, curr_seq_a = '', curr_seq_b = '', pos=None, printed_sequences=0):
        if pos is None:
            x, y = directions.shape[0] - 1, directions.shape[1] - 1
        else:
            x, y = pos

        if x == 0 and y == 0:
            self._write_result('a: ', curr_seq_a[::-1], '\nb: ', curr_seq_b[::-1], '\n')
            return printed_sequences + 1

        # fast forward without recurence and just append what is required
        if x == 0:
            self._write_result('_' * y + curr_seq_a[::-1], seq_b[:y] + curr_seq_b[::-1])
            return printed_sequences + 1
        
        if y == 0:
            self._write_result(seq_a[:x] + curr_seq_a[::-1], '_' * x + curr_seq_b[::-1])        
            return printed_sequences + 1

        # check arrows and run function from new position in directions matrix
        if printed_sequences < self.max_number_paths and self._is_arrow_up( directions[x][y]):
            next_seq_a = curr_seq_a + seq_a[x-1]
            next_seq_b = curr_seq_b + '_'
            printed_sequences = self.find_possible_alignments(directions, seq_a, seq_b, next_seq_a, next_seq_b, (x-1, y), printed_sequences)

        if printed_sequences < self.max_number_paths and self._is_arrow_left( directions[x][y]):
            next_seq_a = curr_seq_a + '_'
            next_seq_b = curr_seq_b + seq_b[y-1]
            printed_sequences = self.find_possible_alignments(directions, seq_a, seq_b, next_seq_a, next_seq_b, (x, y-1), printed_sequences)
            
        if printed_sequences < self.max_number_paths and self._is_arrow_diag( directions[x][y]):
            next_seq_a = curr_seq_a + seq_a[x-1]
            next_seq_b = curr_seq_b + seq_b[y-1]
            printed_sequences = self.find_possible_alignments(directions, seq_a, seq_b, next_seq_a, next_seq_b, (x-1, y-1), printed_sequences)
        
        return printed_sequences
    
    @staticmethod
    def _is_arrow_left(arrow):
        return arrow[0]
    
    @staticmethod
    def _is_arrow_up(arrow):
        return arrow[1]

    @staticmethod
    def _is_arrow_diag(arrow):
        return arrow[2]

    def _write_result(self, seq_a, seq_b):
        output_string = self._get_output_string(seq_a, seq_b)
        if self.output_path is None:
            print(output_string)
        with open(self.output_path, '+a') as f:
            f.write(output_string)
    
    @staticmethod
    def _get_output_string(seq_a, seq_b):
        return f'\na: {seq_a}\nb: {seq_b}\n'
