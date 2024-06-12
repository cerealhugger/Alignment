class Node():
    def __init__(self, value=0, prev=None):
        self.val = value
        self.prev = prev
class GlobalAlignment():
    def __init__(self, seq1: str, seq2: str, match_score=1, mismatch_score=-1, gap_score=-2):
        self.matrix = []
        self.score = 0
        self.seq1 = "-" + seq1
        self.seq2 = "_" + seq2
        self.aligned_seq1 = []
        self.aligned_seq2 = []
        self.match_score = match_score
        self.mismatch_penalty = mismatch_score
        self.gap_penalty = gap_score

    def _init_matrix(self):
        self.matrix = [[Node() for _ in range(len(self.seq1)+1)] for _ in range(len(self.seq2)+1)]
        self.matrix[0][0] = ' '
        for i in range(1, len(self.seq1)+1):
            self.matrix[0][i] = self.seq1[i-1]
            self.matrix[1][i] = Node(0 + self.gap_penalty * (i-1),self.matrix[1][i-1])

        for j in range(1,len(self.seq2)+1):
            self.matrix[j][0] = self.seq2[j-1]
            self.matrix[j][1] = Node(0 + self.gap_penalty * (j-1), self.matrix[j-1][1])

    def _fill_matrix(self):
        for i in range(2, len(self.seq2)+1):
            for j in range(2, len(self.seq1)+1):
                match = self.matrix[i - 1][j - 1].val + (
                    self.match_score if self.seq2[i-1] == self.seq1[
                        j-1] else self.mismatch_penalty)
                delete = self.matrix[i - 1][j].val + self.gap_penalty
                insert = self.matrix[i][j - 1].val + self.gap_penalty
                best_score = max(match, delete, insert)

                if best_score == match:
                    prev = self.matrix[i - 1][j - 1]
                elif best_score == delete:
                    prev = self.matrix[i - 1][j]
                else:
                    prev = self.matrix[i][j - 1]

                self.matrix[i][j] = Node(best_score, prev)
        self.score = self.matrix[len(self.seq2)][len(self.seq1)].val
        
    def generate_matrix(self):
        self._init_matrix()
        self._fill_matrix()
        return self.matrix

    def _traceback(self):
        i, j = len(self.seq2), len(self.seq1)
        current_cell = self.matrix[i][j]

        while current_cell.prev is not None:
            if current_cell.prev == self.matrix[i - 1][j - 1]:  # match/mismatch
                self.aligned_seq1.append(self.seq1[j-1])
                self.aligned_seq2.append(self.seq2[i-1])
                i, j = i - 1, j - 1
            elif current_cell.prev == self.matrix[i - 1][j]:  # deletion
                self.aligned_seq1.append('-')
                self.aligned_seq2.append(self.seq2[i-1])
                i -= 1
            else:  # insertion
                self.aligned_seq1.append(self.seq1[j-1])
                self.aligned_seq2.append('-')
                j -= 1

            current_cell = current_cell.prev
        # the last item is -
        self.aligned_seq1.pop()
        self.aligned_seq2.pop()
        self.aligned_seq1.reverse()
        self.aligned_seq2.reverse()


def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            if isinstance(cell, Node):
                print(f'{cell.val:>4}', end=' ')
            elif isinstance(cell, str):
                print(f'{cell:>4}', end=' ')
        print()


def run():
    seq1 = "AGCT"
    seq2 = "GCAT"
    result = GlobalAlignment(seq1, seq2)
    matrix = result.generate_matrix()
    print_matrix(matrix)
    result._traceback()
    print(f'Aligned sequence 1: {''.join(result.aligned_seq1)}')
    print(f'Aligned sequence 2: {''.join(result.aligned_seq2)}')
    print(f'score: {result.score}')

if __name__ == '__main__':
    run()
