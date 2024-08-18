#Tạo dictionary từ hai list**
# def create_dictionary(keys, values):
#     """Tạo một dictionary từ hai danh sách keys và values"""
#     return dict(zip(keys, values))

# def main():
#     keys = ['Mì tôm', 'Coca', 'Bánh quy', 'Khăn giấy']
#     values = [4.5, 10.0, 25.0, 8.0]

#     food_dict = create_dictionary(keys, values)
#     print("Dictionary được tạo từ hai danh sách là:", food_dict)

# main()
def create_dictionary(keys, values):
    """Tạo một dictionary từ hai danh sách keys và values"""
    return dict(zip(keys, values))

def main():
    n = int(input("Nhập vào số phần tử của hai danh sách: "))
    
    keys = []
    values = []

    print("Nhập vào các phần tử cho danh sách keys:")
    for i in range(n):
        key = input(f"Phần tử thứ {i+1}: ")
        keys.append(key)
    
    print("Nhập vào các phần tử cho danh sách values:")
    for i in range(n):
        value = float(input(f"Phần tử thứ {i+1}: "))
        values.append(value)
    
    food_dict = create_dictionary(keys, values)
    
    print("Dictionary được tạo từ hai danh sách là:", food_dict)

main()

