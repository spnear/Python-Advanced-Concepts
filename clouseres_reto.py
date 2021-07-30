def make_division_by(x):
    def division(n: int):
        assert(n)!=0, "you cant divide by zero"
        return n/x
    return division


division_by_3 = make_division_by(3)
print(division_by_3(18))

division_by_5 = make_division_by(5)
print(division_by_5(100))

division_by_18 = make_division_by(18)
print(division_by_18(54))

