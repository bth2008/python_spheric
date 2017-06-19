import math


class Functions:

    def __init__(self):
        self.a_e = 6371.0

    @staticmethod
    def spher_to_cart(lat, lon):
        x = math.cos(lat) * math.cos(lon)
        y = math.cos(lat) * math.sin(lon)
        z = math.sin(lat)
        return x, y, z

    @staticmethod
    def cart_to_spher(x, y, z):
        lat = math.atan2(z, math.sqrt(x * x + y * y))
        lon = math.atan2(y, x)
        return lat, lon

    @staticmethod
    def rotate(x, y, a):
        c = math.cos(a)
        s = math.sin(a)
        u = x * c + y * s
        v = -x * s + y * c
        return u, v

    def inverse(self, lat1, lon1, lat2, lon2):
        x, y, z = self.spher_to_cart(lat2, lon2)
        x, y = self.rotate(x, y, lon1)
        z, x = self.rotate(z, x, math.pi / 2 - lat1)
        lat, lon = self.cart_to_spher(x, y, z)
        dist = math.pi / 2 - lat
        azi = math.pi - lon
        return dist, azi

    def direct(self, lat1, lon1, dist, azi):
        x, y, z = self.spher_to_cart(math.pi / 2 - dist, math.pi - azi)
        z, x = self.rotate(z, x, lat1 - math.pi / 2)
        x, y = self.rotate(x, y, -lon1)
        lat2, lon2 = self.cart_to_spher(x, y, z)
        return lat2, lon2

    def angular(self, lat1, lon1, lat2, lon2, azi13, azi23):
        failure = False
        dist12, azi21 = self.inverse(lat2, lon2, lat1, lon1)
        dist12, azi12 = self.inverse(lat1, lon1, lat2, lon2)
        cos_beta1 = math.cos(azi13 - azi12)
        sin_beta1 = math.sin(azi13 - azi12)
        cos_beta2 = math.cos(azi21 - azi23)
        sin_beta2 = math.sin(azi21 - azi23)
        cos_dist12 = math.cos(dist12)
        sin_dist12 = math.sin(dist12)
        lat3 = lon3 = 0
        if sin_beta1 == 0. and sin_beta2 == 0.:
            failure = True
            lat3 = 0.
            lon3 = 0.
        elif sin_beta1 == 0.:
            lat3 = lat2
            lon3 = lon2
        elif sin_beta2 == 0.:
            lat3 = lat1
            lon3 = lon1
        elif sin_beta1 * sin_beta2 < 0.:
            if math.fabs(sin_beta1) >= math.fabs(sin_beta2):
                cos_beta2 *= -1
                sin_beta2 *= -1
            else:
                cos_beta1 *= -1
                sin_beta1 *= -1
        else:
            dist13 = math.atan2(math.fabs(sin_beta2) * sin_dist12,
                                cos_beta2 * math.fabs(sin_beta1) + math.fabs(sin_beta2) * cos_beta1 * cos_dist12)
            lat3, lon3 = self.direct(lat1, lon1, dist13, azi13)
        return failure, lat3, lon3

    def linear(self, lat1, lon1, lat2, lon2, dist13, dist23, clockwise):
        failure = False
        if dist13 == 0.:
            lat3 = lat1
            lon3 = lon1
        elif dist23 == 0.:
            lat3 = lat2
            lon3 = lon2
        else:
            dist12, azi12 = self.inverse(lat1, lon1, lat2, lon2)
            cos_beta1 = (math.cos(dist23) - math.cos(dist12) * math.cos(dist13)) / (math.sin(dist12) * math.sin(dist13))
            if math.fabs(cos_beta1) > 1.:
                failure = True
                lat3 = 0.
                lon3 = 0.
            else:
                if clockwise:
                    azi13 = azi12 + math.acos(cos_beta1)
                else:
                    azi13 = azi12 - math.acos(cos_beta1)
                lat3, lon3 = self.direct(lat1, lon1, dist13, azi13)
        return failure, lat3, lon3
