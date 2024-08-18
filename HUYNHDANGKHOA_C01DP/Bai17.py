#Tìm phần tử không trùng trong list*
def find_unique_elements(lst):
    """Tìm các phần tử không trùng lặp trong danh sách"""
    # Tạo một từ điển để đếm tần suất xuất hiện của mỗi phần tử
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    # Lấy các phần tử chỉ xuất hiện một lần
    unique_elements = [element for element, count in element_count.items() if count == 1]
    return unique_elements

def main():
    user_input = input("Nhập vào một danh sách các phần tử, cách nhau bởi dấu cách: ")
    item_list = [s.strip() for s in user_input.split(' ')]
    unique_list = find_unique_elements(item_list)
    print("Các phần tử không trùng lặp trong danh sách là:", unique_list)

main()
