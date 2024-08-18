#Tìm phần tử có số lần xuất hiện nhiều nhất trong list*s
def find_most_frequent_element(lst):
    """Tìm phần tử có số lần xuất hiện nhiều nhất trong danh sách"""
    if not lst:
        return None
    
    frequency_dict = {}
    for element in lst:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    most_frequent_element = max(frequency_dict, key=frequency_dict.get)
    return most_frequent_element, frequency_dict[most_frequent_element]

def main():
    user_input = input("Nhập vào một danh sách các phần tử, cách nhau bởi dấu cách: ")
    item_list = [s.strip() for s in user_input.split(' ')]
    element, frequency = find_most_frequent_element(item_list)
    
    if element is not None:
        print(f"Phần tử có số lần xuất hiện nhiều nhất là {element} với {frequency} lần xuất hiện.")
    
main()
