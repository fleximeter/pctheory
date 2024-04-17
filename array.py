"""
File: array.py
Author: Jeff Martin
Date: 2/2/2022

Copyright © 2022 by Jeffrey Martin. All rights reserved.
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

from . import transformations
from . import pcseg as ps


class RotationalArray:
    """
    Represents a rotational array
    """
    def __init__(self, pcseg=None):
        """
        Creates a rotational array
        :param pcseg: A pcseg to import
        """
        self._array = None
        self._pcseg = None
        if pcseg is not None:
            self.import_pcseg(pcseg)

    def __repr__(self):
        return "<pctheory.pcseg.RotationalArray object at " + str(id(self)) + ">: " + str(self._array)

    def __str__(self):
        chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B']
        lines = ""
        for i in range(len(self._array) - 1):
            for j in range(len(self._array[i])):
                lines += chars[self._array[i][j].pc] + " "
            lines += "\n"
        for j in range(len(self._array[len(self._array) - 1])):
            lines += chars[self._array[len(self._array) - 1][j].pc] + " "
        return lines

    @property
    def array(self):
        """
        Gets the rotational array
        :return: The rotational array
        """
        return self._array

    @property
    def pcseg(self):
        """
        Gets the pcseg
        :return: The pcseg
        """
        return self._pcseg

    def __getitem__(self, i: int, j: int):
        """
        Gets the pc at the specified row and column
        :param i: The row
        :param j: The column
        :return: The pc
        """
        return self._array[i][j]

    def get_column(self, j: int):
        """
        Gets a column of the rotational array
        :param j: The column index
        :return: The column
        """
        c = []
        for i in range(len(self._array)):
            c.append(self._array[i][j])
        return c

    def get_row(self, i: int):
        """
        Gets a row of the rotational array
        :param i: The row index
        :return: The row
        """
        return self._array[i]

    def import_pcseg(self, pcseg: list):
        """
        Imports a pcseg
        :param pcseg: A pcseg
        :return: None
        """
        self._pcseg = ps.transpose(pcseg, 12 - pcseg[0].pc)
        self._array = []
        for i in range(len(self._pcseg)):
            self._array.append(ps.rotate(ps.transpose(self._pcseg, -self._pcseg[i].pc), len(self._pcseg) - i))


def str_simple_array(array, col_delimiter=" ", row_delimiter="\n"):
    """
    Converts an array of pcs to string
    :param array: The array to convert
    :param col_delimiter: The column delimiter
    :param row_delimiter: The row delimiter
    :return: The string
    """
    str_temp = ""
    for i in range(len(array) - 1):
        row = ""
        for j in range(len(array[i]) - 1):
            row += f"{array[i][j]}{col_delimiter}"
        if len(array[i]) > 0:
            row += f"{array[i][len(array[i]) - 1]}"
        row += row_delimiter
        str_temp += row
    row = ""
    for j in range(len(array[len(array) - 1]) - 1):
        row += f"{array[len(array) - 1][j]}{col_delimiter}"
    if len(array[len(array) - 1]) > 0:
        row += f"{array[len(array) - 1][len(array[len(array) - 1]) - 1]}"
    str_temp += row    
    return str_temp


def make_array_chain(array, length: int):
    """
    Makes a chain of arrays
    :param array: An array
    :param length: The length
    :param alt_ret: Whether or not to alternately retrograde the arrays.
    :return: A chained array
    """
    array1 = []  # The final array
    pcset_start = set()  # The begin-set of the array
    pcset_end = set()  # The end-set of the array

    # Populate the begin-set and end-set
    for i in range(len(array)):
        pcset_start.add(array[i][0])
        pcset_end.add(array[i][len(array[i]) - 1])

    # Add the first array to the final array
    for i in range(len(array)):
        row = []
        for j in range(len(array[i])):
            if type(array[i][j]) == list:
                row.append(list(array[i][j]))
            elif type(array[i][j]) == set:
                row.append(set(array[i][j]))
            else:
                row.append(array[i][j])
        array1.append(row)

    # Add the other arrays
    for i in range(1, length):
        # Get the current end-set
        pcset_end_temp = set()
        for j in range(len(array1)):
            pcset_end_temp.add(array1[j][len(array1[j]) - 1])

        # Get the row operator we need for the transformation, and transform the array
        r = transformations.OTO()
        transformation = transformations.find_utos12(pcset_start, pcset_end_temp)
        r.oto = [transformation[0][0], 0, transformation[0][1]]
        m = r.transform(array1)
        m.reverse()

        # Add the transformed array content to the end of the large array
        for j in range(len(array1)):
            for k in range(len(m)):
                if m[k][0] == array1[j][len(array1[j]) - 1]:
                    for n in range(1, len(m[k])):
                        array1[j].append(m[k][n])
                    del m[k]
                    break

    return array1
