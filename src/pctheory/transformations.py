"""
File: transformations.py
Author: Jeff Martin
Date: 10/30/2021

Copyright © 2021 by Jeffrey Martin. All rights reserved.
Email: jmartin@jeffreymartincomposer.com
Website: https://jeffreymartincomposer.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from pctheory.pitch import PitchClass
import re


class OTO:
    """
    Represents an ordered tone operator (OTO). If used with a twelve-tone row, it is a row operator (RO).
    Objects of this class are subscriptable. [0] is the index of transposition. [1] is whether or not to
    retrograde (0-no or 1-yes). [2] is the multiplier. Multiplication is performed first, then retrograding,
    then transposition. These operators can be used with pcsegs.
    """
    def __init__(self, T=0, R=False, M=1):
        """
        Creates an OTO
        :param T: The index of transposition
        :param R: Whether or not to retrograde
        :param M: The multiplier
        """
        if type(T) == str:
            if transformation_string := re.fullmatch(r'T(\d|10|11)(R)?(I|MI|M(\d+)?)?', T):
                g = transformation_string.groups()
                if g[3]:
                    self._t = int(g[0])
                    self._m = int(g[3])
                elif not g[2]:
                    self._t = int(g[0])
                    self._m = 1
                elif g[2] == 'I':
                    self._t = int(g[0])
                    self._m = 11
                elif g[2] == 'M':
                    self._t = int(g[0])
                    self._m = 5
                elif g[2] == 'MI':
                    self._t = int(g[0])
                    self._m = 7
                if g[1] == 'R':
                    self._r = True
                else:
                    self._r = False
            else:
                raise ValueError("The transformation string is invalid.")
        elif type(T) == int and type(M) == int and type(R) == bool:
            self._t = T
            self._r = R
            self._m = M
        else:
            raise TypeError("The T and M values must be integers, and the R value " \
                "must be a boolean, or the T value must be a transformation string.")



    def __eq__(self, other):
        return self._t == other._t and self._r == other._r and self._m == other._m
    
    def __ge__(self, other):
        if self._r > other._r:
            return True
        elif self._r == other._r and self._m > other._m:
            return True
        elif self._r == other._r and self._m == other._m and self._t >= other._t:
            return True
        else:
            return False
        
    def __gt__(self, other):
        if self._r > other._r:
            return True
        elif self._r == other._r and self._m > other._m:
            return True
        elif self._r == other._r and self._m == other._m and self._t > other._t:
            return True
        else:
            return False
    
    def __hash__(self):
        return self._t * 1000 + self._r * 100 + self._m

    def __le__(self, other):
        if self._r < other._r:
            return True
        elif self._r == other._r and self._m < other._m:
            return True
        elif self._r == other._r and self._m == other._m and self._t <= other._t:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self._r < other._r:
            return True
        elif self._r == other._r and self._m < other._m:
            return True
        elif self._r == other._r and self._m == other._m and self._t < other._t:
            return True
        else:
            return False

    def __ne__(self, other):
        return self._t != other._t or self._r != other._r or self._m != other._m

    def __repr__(self):
        if self._r and self._m != 1:
            return f"T{self._t}RM{self._m}"
        elif self._m != 1:
            return f"T{self._t}M{self._m}"
        elif self._r:
            return f"T{self._t}R"
        else:
            return f"T{self._t}"

    def __str__(self):
        if self._r and self._m != 1:
            return f"T{self._t}RM{self._m}"
        elif self._m != 1:
            return f"T{self._t}M{self._m}"
        elif self._r:
            return f"T{self._t}R"
        else:
            return f"T{self._t}"

    @property
    def T(self):
        """
        Gets the index of transposition of the OTO.
        :return: The index of transposition
        """
        return self._t
    
    @property
    def R(self):
        """
        Gets the retrograde status of the OTO.
        :return: The retrograde status
        """
        return self._r
 
    @property
    def M(self):
        """
        Gets the index of multiplication of the OTO.
        :return: The index of multiplication
        """
        return self._m

    def __call__(self, item):
        """
        Transforms an item (can be a pitch-class, list, set, or any number of nestings of these objects)
        :param item: An item
        :return: The transformed item
        """
        new_item = None
        if type(item) == list:
            new_item = []
            for item2 in item:
                t = type(item2)
                if t == list:
                    new_item.append(self.transform(item2))
                elif t == set:
                    new_item.append(self.transform(item2))
                elif t == PitchClass:
                    new_item.append(PitchClass(item2.pc * self._m + self._t, item2.mod))
                else:
                    raise ArithmeticError("Cannot transform a type other than a PitchClass.")
            if self._r:
                new_item.reverse()
        elif type(item) == set:
            new_item = set()
            for item2 in item:
                t = type(item2)
                if t == list:
                    new_item.add(self.transform(item2))
                elif t == set:
                    new_item.add(self.transform(item2))
                elif t == PitchClass:
                    new_item.append(PitchClass(item2.pc * self._m + self._t, item2.mod))
                else:
                    raise ArithmeticError("Cannot transform a type other than a PitchClass.")
        else:
            new_item = type(item)(item.pc * self._m + self._t)
        return new_item

    def transform(self, item):
        return __call__(item)

class UTO:
    """
    Represents an unordered tone operator (UTO), which can be used as a twelve-tone operator (TTO)
    or 24-tone operator (24TO). Objects of this class are subscriptable.
    [0] is the index of transposition. [1] is the multiplier. Multiplication is performed first,
    then transposition.
    """
    def __init__(self, T=0, M=1):
        """
        Creates a UTO
        :param T: The index of transposition
        :param M: The index of multiplication
        """
        if type(T) == str:
            if transformation_string := re.fullmatch(r'T(\d|10|11)(I|MI|M(\d+)?)?', T):
                g = transformation_string.groups()
                if g[2]:
                    self._t = int(g[0])
                    self._m = int(g[2])
                elif not g[1]:
                    self._t = int(g[0])
                    self._m = 1
                elif g[1] == 'I':
                    self._t = int(g[0])
                    self._m = 11
                elif g[1] == 'M':
                    self._t = int(g[0])
                    self._m = 5
                elif g[1] == 'MI':
                    self._t = int(g[0])
                    self._m = 7
            else:
                raise ValueError("The transformation string is invalid.")
        elif type(T) == int and type(M) == int:
            self._t = T
            self._m = M
        else:
            raise TypeError("The T and M values must be integers, or the T value must be a transformation string.")

    def __eq__(self, other):
        return self._t == other._t and self._m == other._m

    def __ge__(self, other):
        if self._m > other._m:
            return True
        elif self._m == other._m and self._t >= other._t:
            return True
        else:
            return False

    def __gt__(self, other):
        if self._m > other._m:
            return True
        elif self._m == other._m and self._t > other._t:
            return True
        else:
            return False

    def __hash__(self):
        return self._t * 100 + self._m

    def __le__(self, other):
        if self._m < other._m:
            return True
        elif self._m == other._m and self._t <= other._t:
            return True
        else:
            return False

    def __lt__(self, other):
        if self._m < other._m:
            return True
        elif self._m == other._m and self._t < other._t:
            return True
        else:
            return False

    def __ne__(self, other):
        return self._t != other._t or self._m != other._m

    def __repr__(self):
        if self._m != 1:
            return f"T{self._t}M{self._m}"
        else:
            return f"T{self._t}"

    def __str__(self):
        if self._m != 1:
            return f"T{self._t}M{self._m}"
        else:
            return f"T{self._t}"
    
    @property
    def T(self):
        """
        Gets the transposition of the UTO
        """
        return self._t

    @property
    def M(self):
        """
        Gets the multiplication of the UTO
        """
        return self._m

    def cycles(self, mod: int = 12) -> list:
        """
        Gets the cycles of the UTO
        :param mod: The number of possible pcs in the system
        :return: The cycles, as a list of lists
        """
        int_list = [i for i in range(mod)]
        cycles = []
        while len(int_list) > 0:
            cycle = [int_list[0]]
            pc = cycle[0]
            pc = (pc * self._m + self._t) % mod
            while pc != cycle[0]:
                cycle.append(pc)
                int_list.remove(pc)
                pc = cycle[len(cycle) - 1]
                pc = (pc * self._m + self._t) % mod
            cycles.append(tuple(cycle))
            del int_list[0]
        return tuple(cycles)

    def inverse(self, mod: int = 12) -> 'UTO':
        """
        Gets the inverse of the UTO
        :param mod: The number of possible pcs in the system
        :return: The inverse
        """
        return UTO((-self._m * self._t) % mod, self._m)

    def __call__(self, item):
        """
        Transforms a pcset, pcseg, or pc
        :param item: A pcset, pcseg, or pc
        :return: The transformed item
        """
        t = type(item)
        if t == PitchClass:
            return PitchClass(item.pc * self._m + self._t, item.mod)
        else:
            new_item = t()
            if t == set:
                for i in item:
                    new_item.add(self.transform(i))
            if t == list:
                for i in item:
                    new_item.append(self.transform(i))
            return new_item
        
    def transform(self, item):
        return self.__call__(item)


def find_otos(pcseg1: list, pcseg2: list):
    """
    Gets all OTO transformations of pcseg1 that contain pcseg2 as an ordered subseg
    :param pcseg1: A pcseg
    :param pcseg2: A pcseg
    :return: A set of OTOs that transform pcseg1 so that it contains pcseg2.
    *Compatible with PitchClasses mod 12 and 24
    """
    otos = None
    oto_set = set()

    if len(pcseg1) > 0 and len(pcseg2) > 0:
        mod = pcseg1[0].mod
        if mod == 12:
            otos = get_otos12()
        elif mod == 24:
            otos = get_otos24()
        else:
            return oto_set
        
        for oto in otos:
            pcseg3 = otos[oto].transform(pcseg1)
            # Search each transformation in t
            done_searching = False
            for i in range(len(pcseg3)):
                if len(pcseg2) > len(pcseg3) - i:
                    break
                done_searching = True
                for j in range(i, i + len(pcseg2)):
                    if pcseg3[j] != pcseg2[j - i]:
                        done_searching = False
                        break
                if done_searching:
                    oto_set.add(otos[oto])
                    break

    return oto_set


def find_utos(pcset1: set, pcset2: set):
    """
    Finds the UTOS that transform pcset1 so it contains pcset2. pcset2 can be a subset of pcset1.
    :param pcset1: A pcset
    :param pcset2: A pcset
    :return: A list of UTOS
    """
    utos_final = set()

    if len(pcset1) > 0 and len(pcset2) > 0:
        mod = next(iter(pcset1)).mod
        if mod == 12:
            utos = get_utos12()
        elif mod == 24:
            utos = get_utos24()
        else:
            return utos_final
        
        for uto in utos:
            pcset1_transformed = utos[uto].transform(pcset1)
            valid = True
            for pc in pcset2:
                if pc not in pcset1_transformed:
                    valid = False
                    break
            if valid:
                utos_final.add(utos[uto])

    return utos_final


def get_otos12() -> list:
    """
    Gets chromatic OTOs (ROs)
    :return: A list of OTOs
    """
    otos = {}
    for i in range(12):
        otos[f"T{i}"] = OTO(i, 0, 1)
        otos[f"T{i}R"] = OTO(i, 1, 1)
        otos[f"T{i}M"] = OTO(i, 0, 5)
        otos[f"T{i}RM"] = OTO(i, 1, 5)
        otos[f"T{i}MI"] = OTO(i, 0, 7)
        otos[f"T{i}RMI"] = OTO(i, 1, 7)
        otos[f"T{i}I"] = OTO(i, 0, 11)
        otos[f"T{i}RI"] = OTO(i, 1, 11)
    return otos


def get_otos24() -> list:
    """
    Gets microtonal OTOs
    :return: A list of microtonal OTOs
    """
    otos = {}
    for i in range(24):
        otos[f"T{i}"] = OTO(i, 0, 1)
        otos[f"T{i}R"] = OTO(i, 1, 1)
        otos[f"T{i}M5"] = OTO(i, 0, 5)
        otos[f"T{i}RM5"] = OTO(i, 1, 5)
        otos[f"T{i}M7"] = OTO(i, 0, 7)
        otos[f"T{i}RM7"] = OTO(i, 1, 7)
        otos[f"T{i}M11"] = OTO(i, 0, 11)
        otos[f"T{i}RM11"] = OTO(i, 1, 11)
        otos[f"T{i}M13"] = OTO(i, 0, 13)
        otos[f"T{i}RM13"] = OTO(i, 1, 13)
        otos[f"T{i}M17"] = OTO(i, 0, 17)
        otos[f"T{i}RM17"] = OTO(i, 1, 17)
        otos[f"T{i}M19"] = OTO(i, 0, 19)
        otos[f"T{i}RM19"] = OTO(i, 1, 19)
        otos[f"T{i}I"] = OTO(i, 0, 23)
        otos[f"T{i}RI"] = OTO(i, 1, 23)
    return otos


def get_utos12() -> dict:
    """
    Gets the twelve-tone UTOs (TTOs)
    :return: A dictionary of UTOs
    """
    utos = {}
    for i in range(12):
        utos[f"T{i}"] = UTO(i, 1)
        utos[f"T{i}M"] = UTO(i, 5)
        utos[f"T{i}MI"] = UTO(i, 7)
        utos[f"T{i}I"] = UTO(i, 11)
    return utos


def get_utos24() -> dict:
    """
    Gets the 24-tone UTOs (24TOs)
    :return: A dictionary of UTOs
    """
    utos = {}
    for i in range(24):
        utos[f"T{i}"] = UTO(i, 1)
        utos[f"T{i}M5"] = UTO(i, 5)
        utos[f"T{i}M7"] = UTO(i, 7)
        utos[f"T{i}M11"] = UTO(i, 11)
        utos[f"T{i}M13"] = UTO(i, 13)
        utos[f"T{i}M17"] = UTO(i, 17)
        utos[f"T{i}M19"] = UTO(i, 19)
        utos[f"T{i}I"] = UTO(i, 23)
    return utos


def left_multiply_utos(*args, mod: int = 12) -> UTO:
    """
    Left-multiplies a list of UTOs
    :param args: A collection of UTOs (can be one argument as a list, or multiple UTOs separated by commas.
    The highest index is evaluated first, and the lowest index is evaluated last.
    :param mod: The number of pcs in the system
    :return: The result
    """
    utos = args

    # If the user provided a list object
    if len(args) == 1:
        if type(args[0]) == list:
            utos = args[0]

    if len(utos) == 0:
        return None
    elif len(utos) == 1:
        return utos[0]
    else:
        n = utos[len(utos) - 1].T
        m = utos[len(utos)-1].M
        for i in range(len(utos)-2, -1, -1):
            tr_n = utos[i].T
            mul_n = utos[i].M
            m = m * mul_n
            n = mul_n * n + tr_n
        return UTO(n % mod, m % mod)


def make_uto_list(*args) -> list:
    """
    Makes a UTO list
    :param args: One or more tuples or lists representing UTOs
    :return: A UTO list
    """
    uto_list = []
    for uto in args:
        uto_list.append(UTO(uto.T, uto.M))
    return uto_list
