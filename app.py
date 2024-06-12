import tkinter as tk
from tkinter import messagebox
from global_alignment import *
from local_alignment import *
class SequenceAlignmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sequence Alignment")
        self.create_widgets()

    def on_button_clicked(self):
        self.score_label.config(text='')
        self.align1_label.config(text='')
        self.align2_label.config(text='')

        seq1 = self.seq1_entry.get()
        seq2 = self.seq2_entry.get()
        match_score = int(self.match_score.get())
        mismatch_score = int(self.mismatch_score.get())
        gap_score = int(self.gap_score.get())

        try:
            if self.selected_option.get() == 'global':
                ans = GlobalAlignment(seq1,seq2,match_score,mismatch_score,gap_score)
                matrix = ans.generate_matrix()
                ans._traceback()
                score = ans.score
                align1 = ''.join(ans.aligned_seq1)
                align2 = ''.join(ans.aligned_seq2)
            elif self.selected_option.get() == 'local':
                scoring_matrix, traceback_matrix = local_alignment(seq1, seq2, match_score, mismatch_score, gap_score)
                score, align1, align2 = traceback_alignment(scoring_matrix, traceback_matrix,seq1,seq2)
            else:
                messagebox.showerror("Error", f"Invalid Option {self.selected_option.get()}")
                return

            self.score_label.config(text="Score: " + str(score))
            self.align1_label.config(text="Aligned Sequence 1: " + align1)
            self.align2_label.config(text="Aligned Sequence 2: " + align2)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_widgets(self):
        self.seq1_label = tk.Label(self.root, text="Enter a sequence:")
        self.seq1_label.grid(row=0, column=0)
        self.seq1_entry = tk.Entry(self.root)
        self.seq1_entry.grid(row=0, column=1)

        self.seq2_label = tk.Label(self.root, text="Enter a sequence:")
        self.seq2_label.grid(row=1, column=0)
        self.seq2_entry = tk.Entry(self.root)
        self.seq2_entry.grid(row=1, column=1)

        self.selected_option = tk.StringVar()
        self.global_option = tk.Radiobutton(self.root, text="Global Alignment", variable=self.selected_option, value="global")
        self.local_option = tk.Radiobutton(self.root, text="Local Alignment", variable=self.selected_option, value="local")

        self.global_option.grid(row=2, column=0)
        self.local_option.grid(row=2, column=1)

        self.button = tk.Button(self.root, text="submit", command = self.on_button_clicked)
        self.button.grid(row=0, column=2)

        self.score_label = tk.Label(self.root, text = '')
        self.score_label.grid(row = 3, column = 2, columnspan = 2)

        self.align1_label = tk.Label(self.root, text = '')
        self.align1_label.grid(row = 1, column = 2, columnspan = 2)

        self.align2_label = tk.Label(self.root, text = '')
        self.align2_label.grid(row = 2, column = 2, columnspan = 2)

        self.match_label = tk.Label(self.root, text = 'Match Score: ')
        self.match_label.grid(row =4, column=0)
        self.match_score = tk.Entry(self.root)
        self.match_score.insert(0,'1')
        self.match_score.grid(row=4, column=1)

        self.mismatch_label = tk.Label(self.root, text = 'Mismatch Penalty: ')
        self.mismatch_label.grid(row = 5, column=0)
        self.mismatch_score = tk.Entry(self.root)
        self.mismatch_score.insert(0,'-1')
        self.mismatch_score.grid(row=5, column=1)

        self.gap_label = tk.Label(self.root, text = 'Gap Penalty')
        self.gap_label.grid(row =6, column=0)
        self.gap_score = tk.Entry(self.root)
        self.gap_score.insert(0,'-2')
        self.gap_score.grid(row=6, column=1)
if __name__ == "__main__":
    root = tk.Tk()
    app = SequenceAlignmentApp(root)
    root.mainloop()