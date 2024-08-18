import string
import re
from collections import Counter

def preprocess_text(text):
    # Loại bỏ dấu câu và ký tự đặc biệt, chuyển đổi thành chữ thường
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()  # Loại bỏ khoảng trắng thừa
    return text

def count_sentences_before_preprocessing(text):
    # Đếm số câu dựa trên các dấu chấm câu như . ! ?
    sentences = re.split(r'[.!?]', text)
    # Loại bỏ các phần tử rỗng trong danh sách
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(sentences)

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [sentence for sentence in sentences if sentence.strip()]  # Loại bỏ câu rỗng
    return len(sentences)

def split_words(text):
    words = text.split()
    return words

def word_statistics(words):
    word_count = Counter(words)
    return word_count

def most_common_words(word_count, n=5):
    return word_count.most_common(n)

def word_length_statistics(words):
    lengths = [len(word) for word in words]
    min_length = min(lengths)
    max_length = max(lengths)
    avg_length = sum(lengths) / len(lengths)
    return min_length, max_length, avg_length

def display_statistics(text):
    sentence_count_before = count_sentences_before_preprocessing(text)
    print(f"Số câu trước khi tiền xử lý: {sentence_count_before}")
    
    processed_text = preprocess_text(text)
    
    print("\n--- Thống kê văn bản ---")
    print(f"Đoạn văn bản đã xử lý: {processed_text}")
    
    word_count = count_words(processed_text)
    print(f"Số từ: {word_count}")
    
    sentence_count = count_sentences(processed_text)
    print(f"Số câu: {sentence_count}")
    
    words = split_words(processed_text)
    print(f"Tách từ: {words}")
    
    word_count_stats = word_statistics(words)
    print("\nThống kê từ:")
    for word, count in word_count_stats.items():
        print(f"{word}: {count} lần")
    
    common_words = most_common_words(word_count_stats)
    print("\nTừ khóa phổ biến nhất:")
    for word, count in common_words:
        print(f"{word}: {count} lần")
    
    min_length, max_length, avg_length = word_length_statistics(words)
    print("\nThống kê độ dài từ:")
    print(f"Từ ngắn nhất: {min_length} ký tự")
    print(f"Từ dài nhất: {max_length} ký tự")
    print(f"Độ dài trung bình của các từ: {avg_length:.2f} ký tự")

def main():
    choice = input("Bạn muốn nhập đoạn văn bản từ (1) bàn phím hay (2) file? Nhập 1 hoặc 2: ").strip()
    if choice == '1':
        text = input("Nhập đoạn văn bản: ").strip()
    elif choice == '2':
        file_path = input("Nhập đường dẫn file: ").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print("Không tìm thấy file. Vui lòng thử lại.")
            return
    else:
        print("Lựa chọn không hợp lệ.")
        return

    display_statistics(text)

if __name__ == "__main__":
    main()

