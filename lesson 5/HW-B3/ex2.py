def is_valid_triangle(sides: list) -> bool:
    if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[2] + sides[1] > sides[0]:
        return True
    else:
        return False


def check_input(sides: str) -> list[float] | None:
    sides_list = sides.split(',')
    sides_list_numeric = []
    if len(sides_list) != 3:
        return
    for side in sides_list:
        if '.' in side:
            dot_split = side.split('.')
            if len(dot_split) != 2:
                return
            elif not dot_split[0].isdigit() and not dot_split[1].isdigit():
                return
            elif dot_split[0] == '0' and dot_split[1] == '0':
                return
            else:
                sides_list_numeric.append(float(side))
        elif not side.strip().isdigit() or side == '0':
            return
        else:
            sides_list_numeric.append(float(side))
    if is_valid_triangle(sides_list_numeric):
        return sides_list_numeric


def get_perimeter(sides_list: list) -> float:
    perimeter = sides_list[0] + sides_list[1] + sides_list[2]
    return perimeter


def get_area(perimeter: float, sides_list: list) -> float:
    semi_per: float = perimeter / 2
    area: float = (semi_per * (semi_per - sides_list[0]) * (semi_per - sides_list[1]) * (semi_per - sides_list[2]))
    return area


triangle_sides: list[float] = []
while True:
    sides_input: str = input("insert 3 sides of triangle")
    triangle_sides = check_input(sides_input)
    if triangle_sides:
        break
triangle_perimeter = get_perimeter(triangle_sides)
print(f"The perimeter is: {triangle_perimeter}")
print(f"The area is: {get_area(triangle_perimeter, triangle_sides)}")
