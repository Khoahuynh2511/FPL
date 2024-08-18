def new_func():
    #Bài 1 - Khởi tạo danh sách và truy xuất phần tử
# Khởi tạo danh sách chứa các số nguyên từ 1 đến 10
    numbers = list(range(1, 11))

# 1. In ra phần tử đầu tiên của danh sách
    print("Phần tử đầu tiên của danh sách:", numbers[0])

# 2. In ra phần tử cuối cùng của danh sách bằng cách dùng chỉ số âm
    print("Phần tử cuối cùng của danh sách:", numbers[-1])

# 3. In ra một đoạn từ phần tử thứ 3 đến phần tử thứ 6
    print("Phần từ thứ 3 đến phần tử thứ 6:", numbers[2:6])

# 4. In ra một đoạn từ phần tử thứ 4 đến phần tử cuối cùng của danh sách
    print("Phần từ thứ 4 đến phần tử cuối cùng:", numbers[3:])

# 5. Thay đổi giá trị của phần tử thứ 2 thành 20 và in lại danh sách sau khi thay đổi
    numbers[1] = 20
    print("Danh sách sau khi thay đổi phần tử thứ 2 thành 20:", numbers)

# 6. Thay đổi giá trị của các phần tử trong đoạn từ phần tử thứ 2 đến phần tử thứ 5 thành 0 và in lại danh sách sau khi thay đổi
    numbers[1:5] = [0, 0, 0, 0]
    print("Danh sách sau khi thay đổi các phần tử từ thứ 2 đến thứ 5 thành 0:", numbers)

new_func()