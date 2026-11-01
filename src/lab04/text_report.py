from src.lab04.io_txt_csv import read_text, write_csv, sorted_word_counts, frequencies_from_text
from src.lib.text import *
from src.lib.text_stats import text_stats
import sys
file_input_path = "data/lab04/input.txt"
import argparse
is_arg_input = input('Ввод с указанием кодировки?(y/n):')
if is_arg_input == 'y':
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_file")
    parser.add_argument("--encoding", default='utf-8')
    args = parser.parse_args()
    file_read = read_text(args.input_file, args.encoding)
else:
    file_read = read_text(file_input_path)
freqs = [(key, value) for key, value in count_freq(tokenize(file_read)).items()]
freqs.sort(key=lambda x: (-x[1], x[0]))
write_csv(freqs, 'data/report.csv', ("word", "count"))
text_stats(file_read)