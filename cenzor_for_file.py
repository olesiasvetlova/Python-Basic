from format_json_csv import *
list_words = ["never", "been"]
file_name = input('Enter your name file: ')
cenzor(file_name, list_words)
create_json_file(create_total_list(file_name, count_word(file_name, list_words)))
create_csv_file(create_total_list(file_name, count_word(file_name, list_words)), file_name)