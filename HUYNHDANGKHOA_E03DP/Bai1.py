#Đổi chuỗi thành số***
def convert_string_to_number(s):
    number_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    words = s.split()
    result = ""
    for word in words:
        if word in number_words:
            result += number_words[word]
        else:
            return "Chuỗi nhập vào chứa từ không hợp lệ."
    return result

def main():
    while True:
        user_input = input("Nhập chuỗi số từ (ví dụ: 'zero four zero one'): ").lower()
        output = convert_string_to_number(user_input)
        if output == "Chuỗi nhập vào chứa từ không hợp lệ.":
            print(output)
        else:
            print(f"Số chuyển đổi: {output}")
            break

if __name__ == "__main__":
    main()
