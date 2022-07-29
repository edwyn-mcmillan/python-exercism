"""Solution to Ellen's Alien Game exercise."""

def new_aliens_collection(positions):
    return list(map(lambda position: Alien(position[0], position[1]), positions))


class Alien:

    total_aliens_created = 0

    def __init__(self, x_, y_):
        self.x_coordinate = x_
        self.y_coordinate = y_
        self.health = 3

        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return bool(self.health >= 1)

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object):
        # return bool(self.x_coordinate == other_object.x_coordinate and self.y_coordinate == other_object.y_coordinate)
        return None
