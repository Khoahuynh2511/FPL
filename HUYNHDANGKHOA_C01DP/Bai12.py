#Tách danh sách thành các phần con theo giá trị nhất định
def split_list_by_value(lst, value):
    """Chia danh sách thành hai danh sách con dựa trên giá trị"""
    less_than_or_equal = [x for x in lst if x <= value]
    greater_than = [x for x in lst if x > value]
    return less_than_or_equal, greater_than

def main():
    user_input = input("Nhập vào một danh sách các phần tử, cách nhau bởi dấu cách: ")
    item_list = [int(s.strip()) for s in user_input.split(' ')]
    split_value = int(input("Nhập vào giá trị để chia danh sách: "))
    less_than_or_equal, greater_than = split_list_by_value(item_list, split_value)
    print("Danh sách các phần tử nhỏ hơn hoặc bằng", split_value, "là:", less_than_or_equal)
    print("Danh sách các phần tử lớn hơn", split_value, "là:", greater_than)

main()
