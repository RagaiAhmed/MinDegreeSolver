from Numbers import RNum

RNum.pr = 0.5


class Eq:
    def __init__(self, x, fx, deg):
        self.t = []
        self.deg = deg - 1
        self.ans = fx

        n=x
        while deg:
            self.t.append(n)
            n *= x
            deg -= 1

    def norm(self, val, deg):
        fact = self.t[deg] / val
        for i in range(len(self.t)):
            self.t[i] /= fact
        self.ans /= fact

    def solve(self, other):
        self.norm(other.t[-1], -1)

        for deg in range(self.deg+1):
            self.t[deg] -= other.t[deg]
        self.ans -= other.ans
        self.deg -= 1
        self.t.pop()

    def f_ans(self, vals):
        for i in range(0, self.deg):
            self.t[i] *= vals[i]
            self.ans -= self.t[i]
        return self.ans / self.t[-1]


sol = input().split()
par = []
while sol:
    par.append(sol)
    sol = input().split()
deg = len(par)

eqs = []
for sol in par:
    eqs.append(Eq(RNum(int(sol[0]), 1), RNum(int(sol[1]), 1), deg))

if deg: deg -= 1

while deg:
    for i in range(deg):
        eqs[i].solve(eqs[i + 1])
    deg -= 1
vals = []
for deg in range(0, len(par)):
    vals.append(eqs[deg].f_ans(vals))
    deg -= 1

print(",".join([str(x)for x in vals]))
