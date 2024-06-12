"""
File: group.py
Author: Jeff Martin
Date: 12/23/2021

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

from queue import Queue
from . import pitch, transformations


class OperatorGroup:
    """
    Represents a group of operators. Only compatible with mod 12 and mod 24 systems.
    """
    def __init__(self, utos: list = None, mod: int = 12):
        """
        Creates an OperatorGroup
        :param utos: TTOs
        :param mod: The number of pcs in the system of the group (chromatic: 12, microtonal: 24)
        """
        self._MNUM_12 = {1, 5, 7, 11}
        self._MNUM_24 = {1, 5, 7, 11, 13, 17, 19, 23}
        self._name = ""
        self._num_pcs = mod
        if mod == 12:
            self._operators = [[] for i in range(len(self._MNUM_12))]
        elif mod == 24:
            self._operators = [[] for i in range(len(self._MNUM_24))]
        self._utos = set()
        if utos is not None:
            self.load_utos(utos)

    def __contains__(self, uto: transformations.UTO):
        return uto in self._utos

    def __iter__(self):
        return (uto for uto in self._utos)

    def __list__(self):
        uto_list = list(self._utos)
        return uto_list
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @property
    def name(self):
        """
        Gets the group name
        :return: The group name
        """
        group_name = "G"
        if self._num_pcs == 12:
            for i in range(len(self._MNUM_12) - 1):
                if len(self._operators[i]) == 12:
                    group_name += "*"
                else:
                    for uto in self._operators[i]:
                        group_name += str(uto[0])
                group_name += "/"
            if len(self._operators[len(self._MNUM_12) - 1]) == 12:
                group_name += "*"
            else:
                for uto in self._operators[len(self._MNUM_12) - 1]:
                    group_name += str(uto[0])
        else:
            for i in range(len(self._MNUM_24) - 1):
                if len(self._operators[i]) == 24:
                    group_name += "*"
                else:
                    for j in range(len(self._operators[i]) - 1):
                        group_name += f"{self._operators[i][j][0]},"
                    if len(self._operators[i]) > 0:
                        group_name += str(self._operators[i][len(self._operators[i]) - 1][0])
                group_name += "/"
            if len(self._operators[len(self._MNUM_24) - 1]) == 24:
                group_name += "*"
            else:
                for j in range(len(self._operators[len(self._MNUM_24) - 1]) - 1):
                    group_name += f"{self._operators[len(self._MNUM_24) - 1][j][0]},"
                if len(self._operators[len(self._MNUM_24) - 1]) > 0:
                    group_name += str(self._operators[len(self._MNUM_24) - 1][len(self._operators[len(self._MNUM_24) - 1]) - 1][0])
        return group_name

    @property
    def utos(self):
        """
        The set of UTOs in the group
        :return: The set of UTOs
        """
        return self._utos

    def get_orbits(self):
        """
        Gets the orbits of the group
        :return: The orbits, as a list of sets
        """
        orbits = []
        u = None
        if self._num_pcs == 12:
            u = {pitch.PitchClass(i, 12) for i in range(self._num_pcs)}
        elif self._num_pcs == 24:
            u = {pitch.PitchClass(i, 24) for i in range(self._num_pcs)}
        while len(u) > 0:
            orbit = set()
            q = Queue()
            pc = next(iter(u))
            q.put(pc)
            orbit.add(pc)
            u.remove(pc)
            while not q.empty():
                pc = q.get()
                for op in self._utos:
                    tr = op.transform(pc)
                    if tr not in orbit:
                        orbit.add(tr)
                        q.put(tr)
                        u.remove(tr)
            orbits.append(orbit)

    def left_coset(self, uto):
        """
        Gets a left coset of the group
        :param uto: A UTO
        :return: The left coset
        """
        coset = []
        for u in self._utos:
            coset.append(transformations.left_multiply_utos(uto, u))
        coset.sort()
        return coset

    def load_utos(self, utos: list):
        """
        Loads TTOs into the group
        :param utos: TTOs
        :return:
        """
        self._utos = set()
        for uto in utos:
            match uto[1]:
                case 1:
                    self._operators[0].append(uto)
                case 5:
                    self._operators[1].append(uto)
                case 7:
                    self._operators[2].append(uto)
                case 11:
                    self._operators[3].append(uto)
                case 13:
                    self._operators[4].append(uto)
                case 17:
                    self._operators[5].append(uto)
                case 19:
                    self._operators[6].append(uto)
                case 23:
                    self._operators[7].append(uto)
            self._utos.add(uto)
        for li in self._operators:
            li.sort()

    def right_coset(self, uto):
        """
        Gets a right coset of the group
        :param uto: A UTO
        :return: The right coset
        """
        coset = []
        for u in self._utos:
            coset.append(transformations.left_multiply_utos(u, uto))
        coset.sort()
        return coset
