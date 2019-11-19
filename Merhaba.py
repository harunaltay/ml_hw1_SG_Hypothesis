from builtins import print
from Point import Point

# read file, build Points list ---------------------------------------

file = open('ML_hw1_data.txt', 'r')

line = file.readline()
num_of_points = int(line)

list_of_points = []

for i in range(num_of_points):
    line = file.readline().strip()
    point = Point(line)
    list_of_points.append(point)

# print("list of all points:")
# for item in list_of_points:
#     print(item)

# find the highest y ------------------------------------------------

max_y = -1000.0
# print(type(max_y))
max_class = -1
# print(type(max_class))

for item in list_of_points:
    if item.y > max_y:
        max_y = item.y
        max_class = item.class_of_point

# print(max_y, max_class)

# find inner and outer classes --------------------------------------

class_outer = max_class
class_inner = -1

for item in list_of_points:
    if item.class_of_point != class_outer:
        class_inner = item.class_of_point
        break

print("inner class:", class_inner)
print("outer class:", class_outer)
print()

# build inner and outer points --------------------------------------

points_inner = []
points_outer = []

for item in list_of_points:
    if item.class_of_point == class_inner:
        points_inner.append(item)
    else:
        points_outer.append(item)

print("points_inner:")
for item in points_inner:
    print(item)
print()

print("points_outer:")
for item in points_outer:
    print(item)
print()

# find the most Specific rectangle/hypothesis -----------------------

inner_x_max = -1000.0
inner_x_min = 1000.0
inner_y_max = -1000.0
inner_y_min = 1000.0

for item in points_inner:
    if item.x > inner_x_max:
        inner_x_max = item.x
    if item.x < inner_x_min:
        inner_x_min = item.x
    if item.y > inner_y_max:
        inner_y_max = item.y
    if item.y < inner_y_min:
        inner_y_min = item.y

print("The Most Specific Hypothesis:")
print("inner_x_max:", inner_x_max)
print("inner_x_min:", inner_x_min)
print("inner_y_max:", inner_y_max)
print("inner_y_min:", inner_y_min)
print()

# find the most General rectangle/hypothesis ------------------------

outer_x_max = -1000.0
outer_x_min = 1000.0
outer_y_max = -1000.0
outer_y_min = 1000.0

for item in points_outer:
    if item.x > outer_x_max:
        outer_x_max = item.x
    if item.x < outer_x_min:
        outer_x_min = item.x
    if item.y > outer_y_max:
        outer_y_max = item.y
    if item.y < outer_y_min:
        outer_y_min = item.y

print("ilklenmiş değerleri")
print("outer_x_max:", outer_x_max)
print("outer_x_min:", outer_x_min)
print("outer_y_max:", outer_y_max)
print("outer_y_min:", outer_y_min)
print()

print("outer'leri tara")
for item in points_outer:
    if inner_x_min < item.x < inner_x_max:
        # kolonda
        if item.y > inner_y_max:
            print("top", item)
            if outer_y_max > item.y:
                outer_y_max = item.y
        if item.y < inner_y_min:
            print("bottom", item)
            if outer_y_min < item.y:
                outer_y_min = item.y

    if inner_y_min < item.y < inner_y_max:
        # yatay satırda
        if item.x > inner_x_max:
            print("right", item)
            if outer_x_max > item.x:
                outer_x_max = item.x
        if item.x < inner_x_min:
            print("left", item)
            if outer_x_min < item.x:
                outer_x_min = item.x

print()
print("The Most General Hypothesis:")
print("outer_x_max:", outer_x_max)
print("outer_x_min:", outer_x_min)
print("outer_y_max:", outer_y_max)
print("outer_y_min:", outer_y_min)
print()
