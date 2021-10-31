class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.thickness = thickness

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        thick = self.thickness
        total = leng * wid * w * thick / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {thick} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()