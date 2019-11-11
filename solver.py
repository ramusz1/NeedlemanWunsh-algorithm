import numpy as np
from directions import Directions

class NeedlemanWunshSolver:

    def __init__(self, same=5, diff=-5, gap_penalty=-2):
        self.same = same
        self.diff = diff
        self.gap_penalty = gap_penalty

    # returns score matrix and directions
    # directions encodes arrows at each position in H matrix
    # each field is a boolean vector, if a arrow exists in given direction
    # [arrow_up, arrow_left, arrow_diagonal]
    def solve(self, seq_a, seq_b):

        score_mat = self._get_score_matrix((len(seq_a)+1, len(seq_b)+1))

        directions = Directions(score_mat.shape) 

        for i in range(1, score_mat.shape[0]):
            for j in range(1, score_mat.shape[1]):
                from_up = score_mat[i - 1][j] + self.gap_penalty
                from_left = score_mat[i][j-1] + self.gap_penalty
                if seq_a[i-1] == seq_b[j-1]:
                    from_diag = score_mat[i-1][j-1] + self.same
                else:
                    from_diag = score_mat[i-1][j-1] + self.diff

                best_score = max(from_up, from_left, from_diag)
                score_mat[i][j] = best_score
                is_left = from_left == best_score
                is_up = from_up == best_score
                is_diag = from_diag == best_score
                directions.set_directions(i, j, is_left, is_up, is_diag)
                
        return score_mat, directions, self._get_final_score_from_score_mat(score_mat)

    def _get_score_matrix(self, shape):
        score_mat = np.zeros(shape)
        # fill first row and column
        score_mat[0][0] = 0
        for i in range(1, shape[1]):
            score_mat[0][i] = score_mat[0][i-1] + self.gap_penalty
        
        for i in range(1, shape[0]):
            score_mat[i][0] = score_mat[i-1][0] + self.gap_penalty

        return score_mat

    @staticmethod
    def _get_final_score_from_score_mat(score_mat):
        return score_mat[-1][-1]
