from src.lab04.io_txt_csv import read_text, write_csv, sorted_word_counts, frequencies_from_text
from src.lib.text import *
from src.lib.text_stats import text_stats
file_input_path = "data/lab04/input.txt"
file_read = read_text(file_input_path)
freqs = [(key, value) for key, value in count_freq(tokenize(file_read)).items()]
write_csv(freqs, 'data/report.csv', ("word", "count"))
text_stats(file_read)