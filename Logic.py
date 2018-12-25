from Numbers import RNum

RNum.pr = 1e-10


class Eq:
    def __init__(self, x, fx, deg, zero):
        self.t = [RNum(zero, 1)]
        self.deg = deg
        self.ans = fx
        self.avail = {0}
        while deg:
            self.t.append(x)
            self.avail.add(deg)
            x *= x
            deg -= 1

    def norm(self, val, deg):
        fact = self.t[deg] / val
        for i in range(len(self.t)):
            self.t[i] /= fact
        self.ans /= fact

    def solve(self, other):
        n = other.avail.difference(self.avail)
        if len(n): raise TypeError

        common = self.avail.intersection(other.avail).pop()
        self.avail.remove(common)
        other.avail.remove(common)

        self.norm(other.t[common], common)

        for deg in range(self.deg):
            self.t[deg] -= other.t[deg]
        self.ans -= other.ans

    def f_ans(self, vals):
        for i in range(self.deg - 1):
            self.t[i] *= vals[i]
            self.ans -= self.t[i]
        return self.ans / self.t[-1]


sol = input().split()
par = []
while sol:
    par.append(sol)
    sol = input().split()
deg = len(par) - 1
eqs = []
for sol in par:
    eqs.append(Eq(RNum(int(sol[0]), 1), RNum(int(sol[1]), 1), deg))
while deg:
    for i in range(deg):
        eqs[i].solve(eqs[i + 1])
    deg -= 1
vals = [0]
for deg in range(0, len(par)):
    vals.append(eqs[deg].f_ans(vals))
    deg -= 1
print(vals)
