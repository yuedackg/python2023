s={1,2,3,4}
b={4,5,6,7}
print("or:",s|b)
print("and:",s&b)
print("xor:",s^b)
b={1,2,3,4,5}
print(s.issubset(b))
s={1,2}
b={3,4}
print(s.isdisjoint(b))