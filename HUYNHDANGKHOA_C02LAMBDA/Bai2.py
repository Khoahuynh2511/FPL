
# Đếm số dòng trong tập tin
def count_lines_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

filename = 'Test.txt'  
line_count = count_lines_in_file(filename)
print("Số dòng trong tập tin là:", line_count)


# from collections import Counter
# import re
# Cách 1: Xác định từ xuất hiện nhiều nhất trong tập tin
# def most_common_word_in_file(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         text = file.read().lower()  
#         words = re.findall(r'\b\w+\b', text)  
#         word_counts = Counter(words)  
#         most_common_word, frequency = word_counts.most_common(2)[0]
#         return most_common_word, frequency

# # Ví dụ sử dụng
# filename = 'Test.txt'  # Thay thế bằng tên tập tin của bạn
# most_common_word, frequency = most_common_word_in_file(filename)
# print("Từ xuất hiện nhiều nhất là:", most_common_word, "với tần suất:", frequency)

# Cách 2:
import re

def most_common_word_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read() #Có thể + upper/lower để đồng bộ hóa  
        words = re.findall(r'\b\w+\b', text) # hoặc là text.split() 
        word_counts = {}  
        print("Các từ có trong file:",words)

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        most_common_word = None
        max_frequency = 0

        for word, frequency in word_counts.items():
            if frequency > max_frequency:
                most_common_word = word
                max_frequency = frequency
        return most_common_word, max_frequency

filename = 'Test.txt' 
most_common_word, frequency = most_common_word_in_file(filename)
print(f"Từ xuất hiện nhiều nhất là: {most_common_word} với tần suất: {frequency}")
