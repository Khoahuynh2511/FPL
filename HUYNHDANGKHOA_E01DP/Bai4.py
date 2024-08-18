#Bài 4 - Một số hàm khác
import random

# Khởi tạo một danh sách ngẫu nhiên chứa 10 số nguyên từ 1 đến 1000
numbers = [random.randint(1, 100) for _ in range(10)]
print("Danh sách ngẫu nhiên ban đầu:", numbers)

# Tạo một chỉ số ngẫu nhiên để truy cập phần tử
random_index = random.randint(0, len(numbers) - 1)
random_element = numbers[random_index]
print(f"Phần tử ngẫu nhiên tại chỉ số {random_index} là: {random_element}")

# 3. Sử dụng hàm `sort` để sắp xếp danh sách theo thứ tự tăng dần
numbers.sort()
print("Danh sách sau khi sắp xếp tăng dần:", numbers)

# Sắp xếp giảm dần
numbers.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", numbers)

# 4. Sử dụng hàm `copy` để sao chép danh sách này sang một danh sách mới
new_numbers = numbers.copy()
print("Danh sách mới sau khi sao chép:", new_numbers)

# 5. Sử dụng hàm `count` để đếm số lần một phần tử xuất hiện trong danh sách
count_of_random_element = numbers.count(random_element)
print(f"Số lần phần tử '{random_element}' xuất hiện trong danh sách:", count_of_random_element)