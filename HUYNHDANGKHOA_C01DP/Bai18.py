#Tính tổng giá trị trong dictionary
def calculate_total_price(items):
    """Tính tổng tiền của các mặt hàng trong từ điển"""
    return sum(items.values())

def main():
    food_convience_store = {'Mì tôm': 4.5, 'Coca': 10.0, 'Bánh quy': 25.0, 'Khăn giấy': 8.0}
    total_price = calculate_total_price(food_convience_store)
    print("Tổng tiền của các mặt hàng là:", total_price)

main()
