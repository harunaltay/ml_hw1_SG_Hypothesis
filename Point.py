
class Point:

    def __init__(self, line_raw):
        my_list = line_raw.strip().split(' ')
        self.x = float(my_list[0])
        self.y = float(my_list[1])
        self.class_of_point = int(my_list[2])

    def __str__(self):
        txt = "({0}, {1}) : {2}".format(str(self.x), str(self.y), str(self.class_of_point))
        return txt

    def __repr__(self):
        return self.__str__()

