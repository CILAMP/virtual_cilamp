import math


def lerp(a, b, frac):
    return a + frac * (b - a)


class Pulser(object):
    def __init__(self, primary, secondary=None, hz=None):
        self.primary = primary
        self.secondary = secondary
        if not secondary:
            self.secondary = (0, 0, 0)
        self.hz = hz

    def seconds(self, t):
        if not self.hz:
            return self.primary

        cos = math.cos(t * self.hz * math.pi * 2)  # R -> [-1, 1]
        # 1 means full primary, no secondary --> 0
        # -1 means full secondary, no primary --> 1
        norm = 1 - (cos + 1) * 0.5
        # print(norm)
        r = lerp(self.primary[0], self.secondary[0], norm)
        g = lerp(self.primary[1], self.secondary[1], norm)
        b = lerp(self.primary[2], self.secondary[2], norm)
        return tuple(map(int, (r, g, b)))
