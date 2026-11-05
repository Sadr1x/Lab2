class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                  
        return f"({self.x}; {self.y})"

    def __repr__(self):                 
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):           
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):           
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, k):              
        return Vector2D(self.x * k, self.y * k)

    __rmul__ = __mul__                  

    def __neg__(self):                  
        return Vector2D(-self.x, -self.y)

    def __eq__(self, other):            
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):            
        return abs(self) < abs(other)

    __hash__ = None                     

    def __abs__(self):                  
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self):                  
        return 2

    def __getitem__(self, i):           
        return (self.x, self.y)[i]


a = Vector2D(3, 4)
b = Vector2D(1, 2)

print("str:", str(a))
print("repr:", repr(a))
print("a + b =", a + b)
print("a - b =", a - b)
print("a * 2 =", a * 2)
print("3 * b =", 3 * b)
print("-a =", -a)
print("a == b:", a == b)
print("b < a:", b < a)
print("abs(a) =", abs(a))
print("len(a) =", len(a))
print("a[0] =", a[0])
