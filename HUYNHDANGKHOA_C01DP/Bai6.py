# Chuyển đổi danh sách chứa chuỗi thành chuỗi duy nhất
def combine_strings(strings):
    return ' '.join(strings)

def main():
    user_input = input("Nhập vào một danh sách các chuỗi, cách nhau bởi dấu phẩy: ")
    string_list = [s.strip() for s in user_input.split(',')]
    combined_string = combine_strings(string_list)
    print("Chuỗi kết hợp là:", combined_string)

main()
