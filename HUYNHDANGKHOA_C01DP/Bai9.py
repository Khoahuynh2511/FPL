#Xóa các phần tử trùng lặp
def unique_elements(lst):
    """Trả về danh sách mới chỉ chứa các phần tử duy nhất từ danh sách ban đầu"""
    return list(set(lst))

def main():
    user_input = input("Nhập vào một danh sách các phần tử, cách nhau bởi dấu cách: ")
    item_list = [int(num) for num in user_input.split(' ')]
    unique_list = unique_elements(item_list)
    print("Danh sách các phần tử duy nhất là:", sorted(unique_list))

main()
