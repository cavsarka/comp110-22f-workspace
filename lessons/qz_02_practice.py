def function(dict1: dict[int, str], list1: list[int]) -> dict[int, str]:
    return_dict = {}
    for item in list1:
        for key in dict1:
            if item == key:
                return_dict[key] = dict1[key]
    return return_dict

print(function({1: "Joe", 2: "Pablo", 3: "Jason"}, [1, 3]))




def score():
    points = 3

def bonus(points):
    points += 7
    return points

points = 0
print(score())
print(bonus(points))

