from Numbers import RNum

RNum.pr = 0.5


class Eq:
    def __init__(self, x, fx):
        self.op = [x]
        self.co_ef = [RNum(1)]
        self.ans = fx

    def get_term(self, n):
        tot = RNum(0)
        for x in range(len(self.op)):
            tot += (self.op[x] ** n) * self.co_ef[x]
        return tot

    def norm(self, n, val):
        self.__imul__(val / self.get_term(n))

    def __iadd__(self, other):
        self.op.extend(other.op)
        self.co_ef.extend(other.co_ef)
        self.ans += other.ans
        return self

    def __imul__(self, other):
        for c in range(len(self.co_ef)):
            self.co_ef[c] *= other
        self.ans *= other
        return self

    def __isub__(self, other):
        self.op.extend(other.op)
        for c in other.co_ef:
            self.co_ef.append(-c)
        self.ans -= other.ans
        return self

    def __itruediv__(self, other):
        return self.__imul__(RNum(1, other))


class Solver:
    def __init__(self):
        self.deg = 0

        self.eqs = []

    def add_pair(self, x, fx):
        eq = Eq(x, fx)
        for i in range(self.deg):
            eq.norm(i, self.eqs[i].get_term(i))
            eq -= self.eqs[i]
        fc = eq.get_term(self.deg)
        for i in range(self.deg):
            self.eqs[i].norm(self.deg, fc)
            self.eqs[i] -= eq

        self.eqs.append(eq)
        self.deg += 1

    def result(self):
        l = []
        for i in range(self.deg):
            l.append(self.eqs[i].ans / self.eqs[i].get_term(i))
        return l


m = Solver()

m.add_pair(1, 1)
m.add_pair(2, 2)
m.add_pair(3,4)
print(m.result())
