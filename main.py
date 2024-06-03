def valid_sequence(seq):
    for char in seq:
        if char not in ['A','G','C','T']:
            raise ValueError(f"Invalid character {char}")
    return True

def print_blank_alignment(seq1, seq2):
    matrix = [['-' for _ in range(len(seq1)+1)] for _ in range (len(seq2)+1)]
    for i in range(1, len(seq1)+1):
        matrix[0][i] = seq1[i-1]
    for j in range(1, len(seq2)+1):
        matrix[j][0] = seq2[j-1]

    for row in matrix:
        print("\t".join(row))

def main():
    seq1 = input("Enter a sequence: ")
    seq2 = input("Enter another sequence: ")

    if valid_sequence(seq1) and valid_sequence(seq2):
        print_blank_alignment(seq1, seq2)

    score = 0
    print("Score: " + str(score))

if __name__ == "__main__":
    main()
