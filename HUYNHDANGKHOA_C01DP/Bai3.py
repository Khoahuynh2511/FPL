#Sắp xếp danh sách
def sort_list(numbers):
    return sorted(numbers)

def main():
    user_input = input("Nhập vào một danh sách các số nguyên, cách nhau bởi dấu cách: ")
    number_list = [int(num) for num in user_input.split(' ')]
    sorted_list = sort_list(number_list)
    print("Danh sách sau khi sắp xếp tăng dần là:", sorted_list)

main()
