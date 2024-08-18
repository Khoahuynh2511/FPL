#Bài 3 - Thêm và xóa phần tử
# Khởi tạo danh sách rỗng
my_list = []
print("Danh sách ban đầu:", my_list)

# 1. Thêm các số từ 1 đến 5 vào danh sách sử dụng hàm `append`
for i in range(1, 6):
    my_list.append(i)
print("Sau khi thêm số từ 1 đến 5:", my_list)

# 2. Tạo danh sách mới và mở rộng danh sách ban đầu
new_list = list(range(6, 11))
my_list.extend(new_list)
print("Sau khi mở rộng với số từ 6 đến 10:", my_list)

# 3. Chèn số 20 vào vị trí thứ 3
my_list.insert(2, 20)
print("Sau khi chèn số 20 vào vị trí thứ 3:", my_list)

# 4. Xóa số 5 khỏi danh sách
my_list.remove(5)
print("Sau khi xóa số 5:", my_list)

# 5. Loại bỏ và in ra phần tử cuối cùng
last_element = my_list.pop()
print("Phần tử cuối cùng được loại bỏ:", last_element)
print("Danh sách sau khi loại bỏ phần tử cuối cùng:", my_list)

# 6. Xóa tất cả các phần tử trong danh sách
my_list.clear()
print("Sau khi xóa tất cả các phần tử:", my_list)

# 7. Thêm các số từ 30 đến 35 vào danh sách
my_list.extend(range(30, 36))
print("Sau khi thêm số từ 30 đến 35:", my_list)

# 8. Loại bỏ và in ra phần tử ở vị trí thứ 2
second_element = my_list.pop(1)
print("Phần tử ở vị trí thứ 2 được loại bỏ:", second_element)
print("Danh sách sau khi loại bỏ phần tử thứ 2:", my_list)

# 9. Xóa tất cả các phần tử trong danh sách
my_list.clear()
print("Sau khi xóa tất cả các phần tử lần cuối:", my_list)
