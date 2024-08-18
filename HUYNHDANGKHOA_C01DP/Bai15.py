#Hệ mặt trời
def check_planets(planets):

    full_planets_set = {'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'}
    current_planets_set = set(planets)
    planets_to_add = full_planets_set - current_planets_set
    planets_to_remove = current_planets_set - full_planets_set
    
    return planets_to_add, planets_to_remove

def main():

    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Plutos', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    planets_to_add, planets_to_remove = check_planets(planets)
    print("Các hành tinh cần thêm vào:", planets_to_add)
    print("Các hành tinh cần loại bỏ:", planets_to_remove)

main()
