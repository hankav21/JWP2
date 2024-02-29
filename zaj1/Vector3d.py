import math


class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def norm(self):
        return math.sqrt(self.x^2+self.y^2+self.z^2)
    
    def __add__(self, other):
        return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z )
    
    def __sub__(self, other):
        return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z )
    
    def __mul__(self, skalar):
        return Vector3d(self.x * skalar, self.y * skalar, self.z * skalar )
    
    #iloczyn skalarny wewktorow
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    #iloczyn vektorowy
    def cross(self, other):
        return Vector3d(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)
    
  
    
    #Sprawdzenie ortogonalności wektorów
    def are_orthogonal(self, other):
        if self.dot( other) == 0: return True
        else: return False

#Przykład uzycia
vektor1 = Vector3d(1,2,3)
print(vektor1)
print(vektor1.get_x())
vektor1.set_x(4)
print(vektor1.get_x())
print("V1: ", vektor1)
print("Długosc vektora: " , vektor1.norm())

vektor2 = Vector3d(6,6,6)
vektor3 = vektor1 + (vektor2)
print("V2: ", vektor2)
print("V3 = v1 + v2: ", vektor3)

print("V3 - V2: ", vektor3 - (vektor2))
print("Mnozenie vektora przez skalar", vektor1 * 2)
print("iloczyn wektorowy: ", vektor1.cross(vektor2))
print("spr ortogonalnosci vektorow ", vektor1.are_orthogonal(vektor3))