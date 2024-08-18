#Tạo ra tất cả các hoán vị của một danh sách*
from itertools import permutations

def all_permutations(lst):
    """Trả về tất cả các hoán vị của danh sách"""
    return list(permutations(lst))

def main():
    user_input = input("Nhập vào một danh sách các phần tử, cách nhau bởi dấu cách: ")
    item_list = [s.strip() for s in user_input.split(' ')]
    perm_list = all_permutations(item_list)
    print("Tất cả các hoán vị của danh sách là:")
    for perm in perm_list:
        print(perm)

main()
