def find_duplicates(input_list):
    element_count = {}
    duplicates = []

    # Đếm số lần xuất hiện của mỗi phần tử
    for item in input_list:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1

    # Tìm các phần tử trùng lặp
    for item, count in element_count.items():
        if count > 1:
            duplicates.append(item)

    return duplicates

# Chương trình chính
if __name__ == "__main__":
    # Nhập danh sách từ người dùng
    input_list = input("Nhập các phần tử của danh sách, cách nhau bằng dấu cách: ").split()
    input_list = [int(x) for x in input_list]
    
    # Tìm và in ra các phần tử trùng lặp
    duplicates = find_duplicates(input_list)
    if duplicates:
        print("Các phần tử trùng lặp:", duplicates)
    else:
        print("Không có phần tử trùng lặp")
