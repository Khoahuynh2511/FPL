#Tìm phần tử lớn nhất và nhỏ nhất
def find_min_max(numbers):
    return min(numbers), max(numbers)

def main():
    user_input = input("Nhập vào một danh sách các số nguyên, cách nhau bởi dấu cách: ")
    number_list = [int(num) for num in user_input.split(' ')]
    min_value, max_value = find_min_max(number_list)
    print(f"Giá trị nhỏ nhất trong danh sách là: {min_value}")
    print(f"Giá trị lớn nhất trong danh sách là: {max_value}")

main()
