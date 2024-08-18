#Kiểm tra danh sách có chứa các số nguyên tố hay không
def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố không"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_prime(numbers):
    """Kiểm tra xem danh sách có chứa số nguyên tố không"""
    for number in numbers:
        if is_prime(number):
            return True
    return False

def main():
    user_input = input("Nhập vào một danh sách các số nguyên, cách nhau bởi dấu cách: ")
    number_list = [int(num) for num in user_input.split(' ')]
    if contains_prime(number_list):
        print("Danh sách có chứa số nguyên tố")
    else:
        print("Danh sách không chứa số nguyên tố.")

main()
