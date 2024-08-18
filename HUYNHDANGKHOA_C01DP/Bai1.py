#Viết một hàm nhận vào một danh sách số nguyên và trả về tổng của tất cả các số đó.
def sum_of_list(numbers):
    return sum(numbers)

def main():
    user_input = input("Nhập vào một danh sách các số nguyên, cách nhau bởi dấu cách: ")
    number_list = [int(num) for num in user_input.split(' ')]
    result = sum_of_list(number_list)
    print("Tổng của danh sách là:", result)

main()
