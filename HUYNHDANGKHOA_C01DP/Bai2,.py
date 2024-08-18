#Đếm số lần xuất hiện của một phần tử
def count_occurrences(lst, element):
    return lst.count(element)

def main():
    user_input = input("Nhập vào một danh sách các phần tử, cách nhau bởi dấu cách: ")
    item_list = user_input.split(' ')
    element_to_count = input("Nhập vào phần tử cần đếm số lần xuất hiện: ")
    result = count_occurrences(item_list, element_to_count)
    print(f"Phần tử '{element_to_count}' xuất hiện {result} lần trong danh sách.")

main()
