class Moon:
    x: int = 0
    y: int = 0
    z: int = 0
    v_x: int = 0
    v_y: int = 0
    v_z: int = 0

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(
            self.x, self.y, self.z, self.v_x, self.v_y, self.v_z
        )

    @staticmethod
    def _velocity_dimension(dimension: str) -> str:
        return f"v_{dimension}"

    def gravity(self, other):
        for dimension in "xyz":
            velocity_dimension = self._velocity_dimension(dimension)
            this_velocity = getattr(self, velocity_dimension)
            other_velocity = getattr(other, velocity_dimension)
            this_position = getattr(self, dimension)
            other_position = getattr(other, dimension)
            if this_position < other_position:
                setattr(self, velocity_dimension, this_velocity + 1)
                setattr(other, velocity_dimension, other_velocity - 1)
            elif this_position > other_position:
                setattr(self, velocity_dimension, this_velocity - 1)
                setattr(other, velocity_dimension, other_velocity + 1)

    def move(self):
        for dimension in "xyz":
            velocity_dimension = self._velocity_dimension(dimension)
            position = getattr(self, dimension)
            velocity = getattr(self, velocity_dimension)
            setattr(self, dimension, position + velocity)
