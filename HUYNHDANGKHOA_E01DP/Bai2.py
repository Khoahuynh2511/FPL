#Bài 2 - List Comprehension

#Tạo một danh sách chứa các số chẵn từ 1 đến 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Các số chẵn từ 1 đến 20:", even_numbers)

#Tạo một danh sách mới chứa bình phương của từng số trong danh sách ban đầu
squared_numbers = [x**2 for x in even_numbers]
print("Bình phương của các số trong danh sách:", squared_numbers)

# Danh sách mới giữ lại các số dương, lấy bình phương các số âm từ danh sách ban đầu
adjusted_list = [x if x >= 0 else x**2 for x in even_numbers]
print("Danh sách sau khi điều chỉnh:", adjusted_list)