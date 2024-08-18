#Mua trái cây
def get_even_weight_bags(fruits):
    """Trả về các túi trái cây có khối lượng chẵn"""
    even_weight_bags = {fruit: [weight for weight in weights if weight % 2 == 0] for fruit, weights in fruits.items()}
    return even_weight_bags

def main():
    Fruits = {
        'Xoài': [2, 3, 5], 
        'Dưa hấu': [4, 6, 2], 
        'Mận': [1, 2, 3]
    }
    
    even_weight_bags = get_even_weight_bags(Fruits)
    
    print("Các túi trái cây có khối lượng chẵn mà khách hàng có thể chọn:")
    for fruit, weights in even_weight_bags.items():
        if weights:  # Kiểm tra nếu danh sách không rỗng
            print(f"{fruit}: {weights}")

main()
