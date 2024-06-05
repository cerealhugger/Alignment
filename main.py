from global_alignment import GlobalAlignment, Node
def valid_sequence(seq):
    for char in seq:
        if char not in ['A','G','C','T']:
            raise ValueError(f"Invalid character {char}")
    return True

def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            if isinstance(cell, Node):
                print(f'{cell.val:>4}', end=' ')
            elif isinstance(cell, str):
                print(f'{cell:>4}', end=' ')
        print()
def score_scale():
    match_score = int(input('Enter match score: '))
    mismatch_score = int(input('Enter mismatch score: '))
    gap_score = int(input('Enter gap score: '))
    return match_score, mismatch_score, gap_score
def main():
    seq1 = input("Enter a sequence: ")
    seq2 = input("Enter another sequence: ")

    if valid_sequence(seq1) and valid_sequence(seq2):
        ans = input("Global Alignment or Local Alignment? Type 'G' or 'L' to generate: ")
        if ans == 'G':
            ans = input("Do you want to change default scoring scale? Type 'Y' or 'N' to continue: ")
            if ans == 'Y':
                match_score, mismatch_score, gap_score = score_scale()
                alignment = GlobalAlignment(seq1, seq2, match_score, mismatch_score,gap_score)
            else:
                alignment = GlobalAlignment(seq1, seq2)
            matrix = alignment.generate_matrix()
            print_matrix(matrix)
            score = alignment.score
            print("Score: " + str(score))

if __name__ == "__main__":
    main()
