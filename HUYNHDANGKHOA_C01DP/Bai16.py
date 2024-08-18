#Xóa số nguyên tố trong set
def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố không"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_non_primes(input_set):
    """Xóa các phần tử không phải là số nguyên tố khỏi set"""
    return {x for x in input_set if is_prime(x)}

def main():
    user_input = input("Nhập vào một tập các phần tử (số nguyên), cách nhau bởi dấu cách: ")
    input_set = {int(s.strip()) for s in user_input.split(' ')}
    prime_set = remove_non_primes(input_set)
    print("Tập các phần tử sau khi xóa các số không phải là số nguyên tố là:", prime_set)

main()
