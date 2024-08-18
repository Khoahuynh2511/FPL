#Xóa phần tử theo giá trị
def remove_all_occurrences(lst, value):
    return [int(x) for x in lst if x != value]

def main():
    user_input = input("Nhập vào một danh sách các phần tử, cách nhau bởi dấu cách: ")
    item_list = [s.strip() for s in user_input.split(' ')]
    element_to_remove = input("Nhập vào phần tử cần xóa: ").strip()
    updated_list = remove_all_occurrences(item_list, element_to_remove)
    print("Danh sách sau khi xóa phần tử:", sorted(updated_list))

main()
