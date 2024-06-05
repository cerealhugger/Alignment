def generate_matrix(rows, cols, default_value=0):
    """
    Generate a matrix with the specified number of rows and columns,
    initialized with a default value.
    """
    return [[default_value] * cols for _ in range(rows)]

def input_alignment_params():
    """
    Ask the user for input: sequences, match score, mismatch score, and gap penalty.
    """
    match_score = int(input("Enter the match score: "))
    mismatch_score = int(input("Enter the mismatch score: "))
    gap_penalty = int(input("Enter the gap penalty: "))
    return match_score, mismatch_score, gap_penalty

def local_alignment(seq1, seq2, match_score=2, mismatch_score=-1, gap_penalty=-1):
    """
    Perform Smith-Waterman alignment between two sequences.
    """
    # Initialize the scoring matrix
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    scoring_matrix = generate_matrix(rows, cols)
    traceback_matrix = generate_matrix(rows, cols)

    # Fill the scoring matrix
    for i in range(1, rows):
        for j in range(1, cols):
            match = scoring_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
            delete = scoring_matrix[i-1][j] + gap_penalty
            insert = scoring_matrix[i][j-1] + gap_penalty
            scoring_matrix[i][j] = max(0, match, delete, insert)
            if scoring_matrix[i][j] == match:
                traceback_matrix[i][j] = 1  # Diagonal move (match/mismatch)
            elif scoring_matrix[i][j] == delete:
                traceback_matrix[i][j] = 2  # Upward move (gap in sequence 2)
            elif scoring_matrix[i][j] == insert:
                traceback_matrix[i][j] = 3  # Leftward move (gap in sequence 1)

    return scoring_matrix, traceback_matrix

def traceback_alignment(scoring_matrix, traceback_matrix, seq1, seq2):
    """
    Traceback to find the optimal alignment.
    """
    rows, cols = len(scoring_matrix), len(scoring_matrix[0])
    max_score = max(max(row) for row in scoring_matrix)
    max_i, max_j = max((i, j) for i, row in enumerate(scoring_matrix) for j, score in enumerate(row) if score == max_score)

    alignment_seq1 = ''
    alignment_seq2 = ''
    i, j = max_i, max_j
    while i > 0 and j > 0 and scoring_matrix[i][j] != 0:
        if traceback_matrix[i][j] == 1:
            alignment_seq1 = seq1[i-1] + alignment_seq1
            alignment_seq2 = seq2[j-1] + alignment_seq2
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == 2:
            alignment_seq1 = seq1[i-1] + alignment_seq1
            alignment_seq2 = '-' + alignment_seq2
            i -= 1
        elif traceback_matrix[i][j] == 3:
            alignment_seq1 = '-' + alignment_seq1
            alignment_seq2 = seq2[j-1] + alignment_seq2
            j -= 1

    return max_score, alignment_seq1, alignment_seq2

# Main program
def main():
    seq1, seq2, match_score, mismatch_score, gap_penalty = input_alignment_params()
    scoring_matrix, traceback_matrix = local_alignment(seq1, seq2, match_score, mismatch_score, gap_penalty)
    print("\nScoring Matrix:")
    for row in scoring_matrix:
        print(row)
    '''
    print("\nTraceback Matrix:")
    for row in traceback_matrix:
        print(row)
    '''
    score, align1, align2 = traceback_alignment(scoring_matrix, traceback_matrix, seq1, seq2)
    print("\nAlignment Score:", score)
    print("Sequence 1:", align1)
    print("Sequence 2:", align2)

if __name__ == "__main__":
    main()