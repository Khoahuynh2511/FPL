#Tính trung bình
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def main():
    user_input = input("Nhập vào một danh sách các số nguyên, cách nhau bởi dấu cách: ")
    number_list = [int(num) for num in user_input.split(' ')]
    average = calculate_average(number_list)
    print(f"Trung bình của các số trong danh sách là: {average}")

main()
