from Numbers import RNum


class Eq:
    """
    Should have documented this long ago
    Now I forgot what it does 
    I spent 1 hour of analyzing code to remember what it does
    
    ** This class stores more than one substitution (x) and the result f(x) 
    as an infinite terms expression : f(x)=a+bx+cx^2+dx^3 ....
    computed only by giving term of power of x
    //well it also stores the coefficient to each whole sequence like that
    """

    def __init__(self, x, fx):
        self.op = [x]  # array of values of x substituted
        self.co_ef = [RNum(1)]  # coefficient for each sequence
        self.ans = fx

    def get_term(self, n):  # computes the coefficient for the term x of given power
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

#
# m = Solver()
#
# mm = [int(x) for x in input().split()]
# while mm:
#     m.add_pair(mm[0], mm[1])
#     mm = [int(x) for x in input().split()]
#
# print(m.result())

i = 1
while 1:
    input()
    s = 0
    m = Solver()

    for x in range(1, i + 3):
        s+=x**i
        m.add_pair(x,s)
    print(m.result())
    i+=1

