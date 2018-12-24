class Eq:
    def __init__(self, x, fx, deg):
        self.t = [1]
        self.deg = deg
        deg -= 1
        while deg:
            self.t.append(x)
            x *= x
            deg -= 1
        self.ans = fx

    def div(self, nw):
        fact = self.t[-1] / nw
        for i in range(len(self.t)):
            self.t[i] /= fact
        self.ans /= fact

    def solve(self, other):
        self.div(other.t[-1])
        for deg in range(self.deg):
            self.t[deg] -= other.t[deg]
        self.ans -= other.ans
        self.t.pop()
        self.deg -= 1

    def f_ans(self, vals):
        for i in range(len(vals)):
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
    eqs.append(Eq(int(sol[0]), int(sol[1]), deg))
while deg:
    for i in range(deg - 1):
        eqs[i].solve(eqs[i + 1])
    deg -= 1
vals = []
for deg in range(0,len(par)):
    vals.append(eqs[deg].f_ans(vals))
    deg -= 1
print(vals)
