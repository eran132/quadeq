import math

def get_discriminant(a, b, c):
    d = b**2-4*a*c
    return d

def calculate(a, b, c):
    a, b, c = int(a), int(b), int(c)
    d = get_discriminant(a, b, c)
    if d < 0:
        print("This equation has no real solution")
        return 0
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        print("This equation:", a, "(X^^2) + (", b, "X) +", c, " has one solutions: ", x)
        return 1
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
        x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
        print("This equation:", a, "(X^^2 )+(", b, "X) +", c, " has two solutions: ", x1, " and", x2)
        return 2



import unittest

class TestStringMethods(unittest.TestCase):
    def test_is_last_coef_neg(self):
        self.assertTrue(-3+math.sqrt(3**2-4*2*-9)/2*2, 0)

if __name__ == '__main__':
    unittest.main()

#a,b,c = input("Enter the coefficients of a, b and c separated by commas: ").split(',')
#a,b,c = int(a),int(b),int(c)
#calculate(a, b, c)


# d = b**2-4*a*c # discriminant
#
# if d < 0:
#     print("This equation has no real solution")
# elif d == 0:
#     x = (-b+math.sqrt(b**2-4*a*c))/2*a
#     print("This equation:", a, "(X^^2) + (", b, "X) +", c, " has one solutions: ", x)
# else:
#     x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
#     x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
#     print("This equation:", a, "(X^^2 )+(", b, "X) +", c, " has two solutions: ", x1, " and", x2)
