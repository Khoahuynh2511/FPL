#Tìm tất cả các cặp phần tử có tổng bằng một giá trị cụ thể**
def find_pairs_with_sum(lst, target_sum):
    """Tìm tất cả các cặp phần tử có tổng bằng target_sum"""
    pairs = []
    seen = set()
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

def main():
    user_input = input("Nhập vào một danh sách các số nguyên, cách nhau bởi dấu cách: ")
    number_list = [int(num) for num in user_input.split(' ')]
    target_sum = int(input("Nhập vào giá trị tổng cần tìm: "))
    pairs = find_pairs_with_sum(number_list, target_sum)
    
    if pairs:
        print("Các cặp phần tử có tổng bằng", target_sum, "là:")
        for pair in pairs:
            print(pair)
    else:
        print("Không có cặp phần tử nào có tổng bằng", target_sum)

main()
