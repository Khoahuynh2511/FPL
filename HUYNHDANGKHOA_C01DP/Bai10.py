#Xóa các phần tử là số nguyên tố
def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố không"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_primes(lst):
    """Trả về danh sách mới đã loại bỏ các số nguyên tố"""
    return [x for x in lst if not is_prime(x)]

def main():
    user_input = input("Nhập vào một danh sách các số nguyên, cách nhau bởi dấu cách: ")
    number_list = [int(num) for num in user_input.split(' ')]
    non_prime_list = remove_primes(number_list)
    print("Danh sách sau khi loại bỏ các số nguyên tố là:", sorted(non_prime_list))

main()
