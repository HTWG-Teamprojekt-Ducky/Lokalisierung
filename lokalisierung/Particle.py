from lokalisierung import Tile


class Particle:

    def __init__(self, p_x, p_y, weight, name, angle=-1):
        self.p_x = p_x
        self.p_y = p_y
        self.tile: Tile = None
        self.weight = weight
        self.name = name
        self.angle = angle

    def __repr__(self):
        return 'Particle ' + str(self.name)

    def set_tile(self, map):
        self.tile = map.search_tile(int(self.p_x), int(self.p_y))

    def distance_to_wall(self):
        if self.tile.type == "straight/E" or self.tile.type == "straight/W":  # returns the distance to the closest wall (the wall can be above or under the particle)
            distance = self.p_y % 1
            if distance >= 0.5:
                return 1 - distance - self.tile.WhiteTapeWidth
            return distance - self.tile.WhiteTapeWidth
        if self.tile.type == "straight/N" or self.tile.type == "straight/S":  # returns the disctance to the closest wall (the wall can be on the left or on the right)
            distance = self.p_x % 1
            if distance >= 0.5:
                return 1 - distance
            return distance
        if self.tile.type == "3way_left/S":
            return self.p_x % 1
        if self.tile.type == "3way_left/N":
            return 1 - self.p_x % 1
        if self.tile.type == "3way_left/W":
            return self.p_y % 1
        if self.tile.type == "3way_left/E":
            return 1 - self.p_y % 1
        if self.tile.type == "curve_left/S":
            print("hi im a curve")

    def angle_to_wall_straight(self):
        if self.tile.type == "straight/E" or self.tile.type == "straight/W":
            if self.direction() == 'NE':
                return self.angle
            if self.direction() == 'SE':
                return self.angle - 360
            if self.direction() == 'NW':
                return self.angle - 180
            if self.direction() == 'SW':
                return self.angle % 90
        if self.tile.type == "straight/N" or self.tile.type == "straight/S":
            if self.direction() == 'NE':
                return self.angle - 90
            if self.direction() == 'NW':
                return self.angle % 90
            if self.direction() == 'SW':
                return self.angle - 270
            if self.direction() == 'SE':
                return self.angle % 90

    def angle_to_wall_3way(self):
        if self.tile.type == "3way_left/S":
            if self.direction() == 'SW':
                return self.angle - 270
            if self.direction() == 'SE':
                return self.angle % 90
            return 'nothing'
        if self.tile.type == "3way_left/N":
            if self.direction() == 'NE':
                return self.angle - 90
            if self.direction() == 'NW':
                return self.angle % 90
            return 'nothing'
        if self.tile.type == "3way_left/W":
            if self.direction() == 'NW':
                return self.angle - 180
            if self.direction() == 'SW':
                return self.angle % 90
            return 'nothing'
        if self.tile.type == "3way_left/E":
            if self.direction() == 'NE':
                return self.angle
            if self.direction() == 'SE':
                return self.angle - 360
            return 'nothing'

    def angle_to_wall(self):
        if self.tile.type == "straight/E" or self.tile.type == "straight/W" or self.tile.type == "straight/N" or self.tile.type == "straight/S":
            return self.angle_to_wall_straight()
        if self.tile.type == "3way_left/S" or self.tile.type == "3way_left/N" or self.tile.type == "3way_left/W" or self.tile.type == "3way_left/E" or self.tile.type == "curve_left/S":
            return self.angle_to_wall_3way()


    def direction(self):
        if self.angle < 90:
            return 'NE'
        if self.angle < 180:
            return 'NW'
        if self.angle < 270:
            return 'SW'
        if self.angle < 360:
            return 'SE'

