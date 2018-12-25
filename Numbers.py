class RNum:
    """
    Class holding 2 integers a numerator and denominator representing a fraction
    - can deal with negatives ex : -7/9
    - can deal with decimals  ex : 5.7/1.3
    - any operation can be applied on it ex: + , - , * , / , ** 
    - warranty free !! hold your numbers tight cause we ain't giving them back if you lost them
    """
    pr = 1e-10  # precision

    def __init__(self, numerator, denominator):
        """
        - Stores the numerator and denominator.
        - Includes the simplify bonus you requested but here it is in the init 
             as the operations returns new objects and to make sure it is always stored simplified.
        :param numerator: upper part of fraction
        :param denominator: lower part of fraction
        """

        if not denominator:
            raise ZeroDivisionError("Error trying to divide by zero !")
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        # a tuple holding the two integers representing the fraction simplified
        self.val = RNum.simplify(numerator, denominator)

    @staticmethod
    def simplify(up, down):
        """
        A static method takes a fraction and simplifies it.
        I made a search on simplifying methods but I decided to do one on my own
        This algorithm maybe made before, Although I don't think so :3
        
        How it works:
            
            It is on a simple idea which is the reciprocal of a reciprocal of a number
            is the number itself.
            
            But what benefit I earn from just making the reciprocal of the reciprocal.
            What you really earn is it simplifies the fraction a little .
            
            We simplify the simplified using recursion explained in detail further on.
            
            First it changes the fraction into a mixed fraction "a whole number and a fraction"
                if there is no remaining fraction then it returns the whole number over 1
            then it simplifies the reciprocal which makes same steps and simplifies the reciprocal of it's fraction 
            and so on in a recursion until there is no fraction for it's simplified reciprocal
            then it remakes the number adding the whole number to it's simplified fraction
            and returns it as simply as that
            
            I tried to compute it's complexity but I couldn't 
             but what I know that it solves big really big numbers simplifications really fast
            
        :param up: numerator
        :param down: denominator
        :return: a tuple representing the fraction
        """
        whole_number = int(up // down)  # the whole number
        remainder = up % down  # Note (remainder/down) is the fraction part
        if remainder < RNum.pr:  # if no remainder or absolutely small one
            return whole_number, 1  # return the whole number over 1  as it is in a fraction form
        reciprocal = RNum.simplify(down, remainder)  # simplifies the fraction part reciprocal
        fraction = (reciprocal[1] + reciprocal[0] * whole_number, reciprocal[0])  # returning the fraction to it's order

        return fraction

    def __add__(self, other):
        """
        in case of addition
        :param other: RationalNumber to add
        :return:  the RationalNumber result of addition
        """
        if isinstance(other, self.__class__):
            # using cross multiplication
            l_up = self.val[0] * other.val[1]
            r_up = other.val[0] * self.val[1]
            down = self.val[1] * other.val[1]
            return RNum(l_up + r_up, down)
        return RNum(self.val[0] + other * self.val[1], self.val[1])

    def __sub__(self, other):
        """
        in case of subtraction
        :param other: RationalNumber to subtract
        :return:  the RationalNumber result of subtraction
        """
        if isinstance(other, self.__class__):
            # using cross multiplication
            l_up = self.val[0] * other.val[1]
            r_up = other.val[0] * self.val[1]
            down = self.val[1] * other.val[1]
            return RNum(l_up - r_up, down)
        return RNum(self.val[0] - other * self.val[1], self.val[1])

    def __mul__(self, other):
        """
        In case of multiplication
        :param other: RationalNumber to multiply with
        :return:New instance holding the Result of Multiplication 
        """
        if isinstance(other, self.__class__):
            # Numerator with numerator and denominator with denominator
            return RNum(self.val[0] * other.val[0], self.val[1] * other.val[1])
        return RNum(self.val[0] * other, self.val[1])

    def __truediv__(self, other):
        """
        In case of division
        :param other: other number to be divided on
        :return: New instance holding the Result of division
        """
        if isinstance(other, self.__class__):
            # Numerator with denominator and denominator with numerator
            return RNum(self.val[0] * other.val[1], self.val[1] * other.val[0])
        return RNum(self.val[0], self.val[1] * other)

    def __pow__(self, power):
        """
        Raises the Rational Number to a power
        :param power: an integer to raise  
        :return: New instance holding the result 
        """
        return RNum(self.val[0] ** power, self.val[1] ** power)

    def __eq__(self, other):
        """
        In case of Equality
        :param other:  other number to compare
        :return: Boolean
        """

        # compare their values
        return self.val == other.val

    def __repr__(self):
        """
        :return: representation of the fraction 
        """
        return "{}/{}".format(self.val[0], self.val[1])

    def __str__(self):
        """
        :return: representation of the fraction
        """
        return self.__repr__()

    def __ne__(self, other):
        """
        In case of non equality
        :param other: fraction to compare to
        :return: Boolean
        """
        return self.val != other.val

    def __neg__(self):
        """
        :return: Negative of the fraction 
        """
        return RNum(self.val[0] * -1, self.val[1])



