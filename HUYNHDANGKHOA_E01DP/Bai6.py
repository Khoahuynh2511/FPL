# 1. Cho trước một set: {1, 2, 3, 4, 5}. Hãy in ra số lượng phần tử của set1.
set1 = {1, 2, 3, 4, 5}
print("Số lượng phần tử của set1:", len(set1))

# 2. Cho phép nhập vào nhiều số dương vào một danh sách đến khi nhập số 0 thì dừng.
# Sau đó loại đi những phần tử trùng nhau và lưu vào set2.
numbers = []

while True:
    number = int(input("Nhập một số dương (nhập 0 để dừng): "))
    if number == 0:
        break
    elif number > 0:
        numbers.append(number)
    else:
        print("Vui lòng nhập một số dương!")

print("Danh sách các số đã nhập:", numbers)
set2 = set(numbers)
print("Set2 sau khi loại bỏ các phần tử trùng:", set2)

# 3. Hãy cho biết các phần tử chỉ xuất hiện trong set1 hoặc set2.
only_in_set1_or_set2 = set1.symmetric_difference(set2)
print("Các phần tử chỉ xuất hiện trong set1 hoặc set2:", only_in_set1_or_set2)

# 4. Cho phép nhập vào một số. Hãy xóa số đó khỏi set2.
number_to_remove = int(input("Nhập một số cần xóa khỏi set2: "))
set2.discard(number_to_remove)  # Sử dụng discard để không gây lỗi nếu số không tồn tại
print("Set2 sau khi xóa số", number_to_remove, ":", set2)

# 5. Hãy tạo set gồm các số chính phương nhỏ hơn 100.
square_numbers = {x*x for x in range(10)}
print("Set gồm các số chính phương nhỏ hơn 100:", square_numbers)
