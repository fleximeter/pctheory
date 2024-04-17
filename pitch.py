"""
File: pitch.py
Author: Jeff Martin
Date: 10/30/2021

Copyright © 2021, 2023 by Jeffrey Martin. All rights reserved.
Email: jmartin@jeffreymartincomposer.com
Website: https://www.jeffreymartincomposer.com

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

_hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


class PitchClass:
    def __init__(self, pc: int=0, mod: int=12):
        """
        Creates a PitchClass
        :param pc: The pitch class integer
        :param mod: The mod number (12 for default chromatic pitch-classes, 
        24 for quarter-tone pitch-classes)
        """
        self._mod = mod
        self._pc = pc % mod

    def __add__(self, other):
        if type(other) == PitchClass:
            if self._mod == other._mod:
                return PitchClass(self.pc + other.pc, self._mod)
            else:
                raise ArithmeticError("Cannot add two pitch-classes with different mod values.")
        elif type(other) == int:
            return PitchClass(self.pc + other, self._mod)
        else:
            raise TypeError("PitchClasses can only be added to other PitchClasses of the same modulo, or to integers.")

    def __eq__(self, other):
        if type(other) == PitchClass:
            return self.pc == other.pc and self._mod == other._mod
        else:
            raise TypeError("PitchClasses can only be compared to other PitchClasses.")

    def __ge__(self, other):
        if type(other) == PitchClass:
            if self._mod == other._mod:
                return self.pc >= other.pc
            else:
                raise ArithmeticError("Cannot compare two pitch-classes with different mod values for >=.")
        else:
            raise TypeError("PitchClasses can only be compared to other PitchClasses.")

    def __gt__(self, other):
        if type(other) == PitchClass:
            if self._mod == other._mod:
                return self.pc > other.pc
            else:
                raise ArithmeticError("Cannot compare two pitch-classes with different mod values for >.")
        else:
            raise TypeError("PitchClasses can only be compared to other PitchClasses.")

    def __hash__(self):
        return hash(f"pc{self._pc}-{self._mod}")

    def __le__(self, other):
        if type(other) == PitchClass:
            if self._mod == other._mod:
                return self.pc <= other.pc
            else:
                raise ArithmeticError("Cannot compare two pitch-classes with different mod values for <=.")
        else:
            raise TypeError("PitchClasses can only be compared to other PitchClasses.")

    def __lt__(self, other):
        if type(other) == PitchClass:
            if self._mod == other._mod:
                return self.pc < other.pc
            else:
                raise ArithmeticError("Cannot compare two pitch-classes with different mod values for <.")
        else:
            raise TypeError("PitchClasses can only be compared to other PitchClasses.")

    def __mul__(self, other):
        if type(other) == PitchClass:
            if self._mod == other._mod:
                return PitchClass(self.pc * other.pc, self._mod)
            else:
                raise ArithmeticError("Cannot multiply two pitch-classes with different mod values.")
        elif type(other) == int:
            return PitchClass(self.pc * other, self._mod)
        else:
            raise TypeError("PitchClasses can only be multiplied by other PitchClasses of the same modulo, or by integers.")

    def __ne__(self, other):
        if type(other) == PitchClass:
            return self.pc != other.pc or self._mod != other._mod
        else:
            raise TypeError("PitchClasses can only be compared to other PitchClasses.")

    def __repr__(self):
        # return "<pctheory.pitch.PitchClass object at " + str(id(self)) + ">: " + self.pc_char
        return self.pc_str

    def __str__(self):
        return self.pc_str

    def __sub__(self, other):
        if type(other) == PitchClass:
            if self._mod == other._mod:
                return PitchClass(self.pc - other.pc, self._mod)
            else:
                raise ArithmeticError("Cannot subtract two pitch-classes with different mod values.")
        elif type(other) == int:
            return PitchClass(self.pc - other, self._mod)
        else:
            raise TypeError("PitchClasses can only be subtracted by other PitchClasses of the same modulo, or by integers.")

    @property
    def mod(self):
        """
        The pitch-class modulo
        :return: The pitch-class modulo
        """
        return self._mod

    @property
    def pc(self):
        """
        The pitch-class integer
        :return: The pitch-class integer
        """
        return self._pc

    @pc.setter
    def pc(self, value: int):
        """
        The pitch-class integer
        :param value: The new pitch-class integer
        :return:
        """
        self._pc = value % 12
        if self._pc < 0:
            self._pc += 12

    @property
    def pc_str(self):
        """
        The pitch-class string
        :return: The pitch-class string
        """
        if 10 < self._mod <= 16:
            return _hex_map[self._pc]
        elif self.mod > 16:
            return f"{self._pc:0>2}"
        else:
            return str(self._pc)
        

class Pitch(PitchClass):
    """
    Represents a pitch
    """
    def __init__(self, p: int=0, pc_mod: int=12, pname: str=0):
        """
        Creates a Pitch
        :param p: The pitch integer
        :param pc_mod: The modulo for the underlying PitchClass
        :param pname: The pitch name as a string (optional, for display purposes)
        """
        super().__init__(p, pc_mod)
        self._p = p
        self._pname = pname

    def __add__(self, other):
        if type(other) == Pitch:
            if self._mod == other._mod:
                return Pitch(self.p + other.p, self._mod)
            else:
                raise ArithmeticError("Cannot add two Pitches with different PitchClass mod values.")
        elif type(other) == int:
            return Pitch(self.p + other, self._mod)
        else:
            raise TypeError("Pitches can only be added to other Pitches of the same PitchClass modulo, or to integers.")

    def __eq__(self, other):
        if type(other) == Pitch:
            return self._p == other._p and self._mod == other._mod
        else:
            raise TypeError("Pitches can only be compared to other Pitches.")

    def __ge__(self, other):
        if type(other) == Pitch:
            if self._mod == other._mod:
                return self.p >= other.p
            else:
                raise ArithmeticError("Cannot compare two Pitches with different PitchClass mod values for >=.")
        else:
            raise TypeError("Pitches can only be compared to other Pitches.")

    def __gt__(self, other):
        if type(other) == Pitch:
            if self._mod == other._mod:
                return self.p > other.p
            else:
                raise ArithmeticError("Cannot compare two Pitches with different PitchClass mod values for >.")
        else:
            raise TypeError("Pitches can only be compared to other Pitches.")

    def __hash__(self):
        return hash(f"p{self._p}-{self._mod}")

    def __le__(self, other):
        if type(other) == Pitch:
            if self._mod == other._mod:
                return self.p <= other.p
            else:
                raise ArithmeticError("Cannot compare two Pitches with different PitchClass mod values for <=.")
        else:
            raise TypeError("Pitches can only be compared to other Pitches.")

    def __lt__(self, other):
        if type(other) == Pitch:
            if self._mod == other._mod:
                return self.p < other.p
            else:
                raise ArithmeticError("Cannot compare two Pitches with different PitchClass mod values for <.")
        else:
            raise TypeError("Pitches can only be compared to other Pitches.")

    def __mul__(self, other):
        if type(other) == Pitch:
            if self._mod == other._mod:
                return Pitch(self.p * other.p, self._mod)
            else:
                raise ArithmeticError("Cannot multiply two Pitches with different PitchClass mod values.")
        elif type(other) == int:
            return Pitch(self.p * other, self._mod)
        else:
            raise TypeError("Pitches can only be multiplied by other Pitches of the same PitchClass modulo, or by integers.")

    def __ne__(self, other):
        if type(other) == Pitch:
            return self._p != other._p or self._mod != other._mod
        else:
            raise TypeError("Pitches can only be compared to other Pitches.")

    def __repr__(self):
        # return "<pctheory.pitch.Pitch object at " + str(id(self)) + ">: " + str(self._p)
        return str(self._p)

    def __str__(self):
        return str(self._p)

    def __sub__(self, other):
        if type(other) == Pitch:
            if self._mod == other._mod:
                return Pitch(self.p - other.p, self._mod)
            else:
                raise ArithmeticError("Cannot subtract two Pitches with different PitchClass mod values.")
        elif type(other) == int:
            return Pitch(self.p - other, self._mod)
        else:
            raise TypeError("Pitches can only be subtracted by other Pitches of the same PitchClass modulo, or by integers.")

    @property
    def p(self):
        """
        The pitch integer
        :return: The pitch integer
        """
        return self._p

    @p.setter
    def p(self, value: int):
        """
        The pitch integer
        :param value: The new pitch integer
        :return:
        """
        self._p = value
        self.pc = self._p

    @property
    def pname(self):
        """
        The pitch name of the pitch
        :return: The pitch name
        """
        return self._pname

    @pname.setter
    def pname(self, value: str):
        """
        The pitch name of the pitch
        :param value: The new name
        :return:
        """
        self._pname = value

    @property
    def midi(self):
        """
        The MIDI version of the pitch integer
        :return: The MIDI version of the pitch integer. If the pitch is 
        microtonal or anything other than a 12-tone chromatic pitch, 
        the MIDI value will be an appropriate floating-point number.
        """
        if self._mod == 12:
            return 60 + self._p
        else:
            return 60 + self._p // self._mod * 12 + self._pc * 12 / self._mod

    @midi.setter
    def midi(self, value):
        """
        The MIDI version of the pitch integer
        :param value: The new MIDI version of the pitch integer
        :return:
        """
        self._p = value - 60
        self.pc = self._p
