"""
File: pcset.py
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

import networkx
import pyvis
from . import pitch, tables, transformations
import numpy as np
import re


name_tables = tables.create_tables_sc12()


class SetClass:
    """
    Represents a pc-set-class
    """
    def __init__(self, pcset=None, pc_mod: int=12):
        """
        Creates a SetClass
        :param pcset: A pcset to initialize the SetClass
        """
        if pcset is not None and len(pcset) > 0:
            self._NUM_PC = next(iter(pcset)).mod
        else:
            self._NUM_PC = pc_mod
        self._dsym = self._NUM_PC * 2
        self._ic_vector = [0 for i in range(self._NUM_PC // 2)]
        self._ic_vector_long = [0 for i in range(self._NUM_PC // 2 + 1)]
        self._name_carter = None
        self._name_forte = None
        self._name_morris = "()[]"
        self._name_prime = "[]"
        self._num_forte = None
        self._pcset = set()
        self._weight_right = True
        if pcset is not None:
            self.pcset = pcset

    def __eq__(self, other):
        if type(other) == SetClass:
            return self.pcset == other.pcset and self._NUM_PC == other._NUM_PC
        else:
            raise TypeError("SetClasses can only be compared to other SetClasses.")

    def __hash__(self):
        return hash(self._name_prime)

    def __len__(self):
        return len(self._pcset)

    def __lt__(self, other):
        if type(other) == SetClass:
            if self._NUM_PC != other._NUM_PC:
                raise ArithmeticError("Cannot compare two SetClasses with different mod values for <.")
            elif self._NUM_PC == 12:
                return len(self) < len(other) or (len(self) == len(other) and self._num_forte < other._num_forte)
            else:
                return len(self._pcset) < len(other._pcset) and self._name_prime < other._name_prime
        else:
            raise TypeError("SetClasses can only be compared to other SetClasses.")

    def __ne__(self, other):
        if type(other) == SetClass:
            return self._pcset != other._pcset or self._NUM_PC != other._NUM_PC
        else:
            raise TypeError("SetClasses can only be compared to other SetClasses.")

    def __repr__(self):
        # return f"<pctheory.pcset.SetClass object at {(id(self))}>: {repr(self._pcset)}"
        if self._NUM_PC == 12:
            return self._name_morris
        elif self._NUM_PC == None or self._NUM_PC <= 0:
            return "()[]"
        else:
            return self._name_prime

    def __str__(self):
        if self._NUM_PC == 12:
            return self._name_morris
        elif self._NUM_PC == None or self._NUM_PC <= 0:
            return "()[]"
        else:
            return self._name_prime
    
    @property
    def derived_core(self):
        """
        Gets derived core associations
        :return: The derived core associations (or None if not derived core)
        """
        global name_tables
        if self.name_prime in name_tables["carterDerivedCoreTable"]:
            return [name for name in name_tables["carterDerivedCoreTable"][self.name_prime]]
        else:
            return None

    @property
    def dsym(self):
        """
        Gets the degree of symmetry of the set-class.
        :return: The degree of symmetry
        """
        return self._dsym

    @property
    def ic_vector(self):
        """
        Gets the IC vector
        :return: The IC vector
        """
        return self._ic_vector

    @property
    def ic_vector_long(self):
        """
        Gets the IC vector in long format
        :return: The IC vector in long format
        """
        return self._ic_vector_long

    @property
    def ic_vector_str(self):
        """
        Gets the IC vector as a string
        :return: The IC vector
        """
        global name_tables
        if self._NUM_PC < 16:
            s = "["
            for a in self._ic_vector:
                s += name_tables["hexChars"][a]
            s += "]"
            return s
        else:
            return str(self._ic_vector)

    @property
    def ic_vector_long_str(self):
        """
        Gets the IC vector in long format as a string
        :return: The IC vector in long format
        """
        global name_tables
        if self._NUM_PC < 16:
            s = "["
            for a in self._ic_vector_long:
                s += name_tables["hexChars"][a]
            s += "]"
            return s
        else:
            return str(self._ic_vector)

    @property
    def is_z_relation(self):
        """
        Whether or not this set-class is Z-related to another set-class
        :return: A boolean
        """
        if self._name_forte is not None and "Z" in self._name_forte:
            return True
        return False
    
    @property
    def mod(self):
        """
        Gets the modulo for PCs in this SetClass
        :return: The modulo
        """
        return self._NUM_PC

    @property
    def name_carter(self):
        """
        Gets the Carter name for a set-class
        :return: The Carter name
        """
        return self._name_carter

    @property
    def name_forte(self):
        """
        Gets the Forte name for a set-class
        :return: The Forte name
        """
        return self._name_forte

    @property
    def name_morris(self):
        """
        Gets the Morris name for a set-class
        :return: The Morris name
        """
        return self._name_morris

    @property
    def name_prime(self):
        """
        Gets the prime-form name (Rahn) for a set-class
        :return: The prime-form name
        """
        return self._name_prime

    @property
    def num_forte(self):
        """
        Get the number part of the Forte name
        :return: The number part of the Forte name
        """
        return self._num_forte

    @property
    def pcset(self):
        """
        Gets the pcset prime form
        :return: The pcset prime form
        """
        return self._pcset

    @pcset.setter
    def pcset(self, value):
        """
        Updates the pcset prime form based on an existing pcset or pcseg
        :param value: The new pcset or pcseg
        :return:
        """
        if type(value) == set or type(value) == list:
            for item in value:
                if type(item) != pitch.PitchClass:
                    raise TypeError("Cannot import sets into a SetClass if they are not composed exclusively of PitchClass objects.")
                elif item.mod != self.mod:
                    raise ArithmeticError(f"Cannot import sets into a SetClass with a different PitchClass modulo. This SetClass has modulo {self.mod}. You tried to import with a modulo of {item.mod}.")
            self._pcset = SetClass.calculate_prime_form(value, self._weight_right, self._NUM_PC)
            self._make_names()
        else:
            raise TypeError("Cannot import types other than sets and lists into a SetClass.")

    @property
    def weight_right(self):
        """
        Whether or not to weight from the right
        :return: A Boolean
        """
        return self._weight_right

    @weight_right.setter
    def weight_right(self, value: bool):
        """
        Whether or not to weight from the right
        :param value: A Boolean
        :return:
        """
        self._weight_right = value
        self._pcset = SetClass.calculate_prime_form(self._pcset, self._weight_right, self._NUM_PC)

    @staticmethod
    def calculate_prime_form(pcset: set, weight_from_right: bool = True, pc_mod: int=12):
        """
        Calculates the prime form of a pcset
        :param pcset: The pcset
        :param weight_from_right: Whether or not to pack from the right
        :param pc_mod: The PitchClass mod value to use 
        :return: The prime form
        """
        prime_set = set()
        if len(pcset) > 0:
            lists_to_weight = []
            pclist = [pc.pc for pc in pcset]
            inverted = [pc * -1 % pc_mod for pc in pclist]
            prime_list = None

            # Add regular forms
            for i in range(len(pclist)):
                lists_to_weight.append([])
                for i2 in range(i, len(pclist)):
                    lists_to_weight[i].append(pclist[i2])
                for i2 in range(0, i):
                    lists_to_weight[i].append(pclist[i2])
                initial_pitch = lists_to_weight[i][0]
                for i2 in range(0, len(lists_to_weight[i])):
                    lists_to_weight[i][i2] -= initial_pitch
                    if lists_to_weight[i][i2] < 0:
                        lists_to_weight[i][i2] += pc_mod
                lists_to_weight[i].sort()

            # Add inverted forms
            for i in range(len(pclist)):
                lists_to_weight.append([])
                for i2 in range(i, len(pclist)):
                    lists_to_weight[i + len(pclist)].append(inverted[i2])
                for i2 in range(0, i):
                    lists_to_weight[i + len(pclist)].append(inverted[i2])
                initial_pitch = lists_to_weight[i + len(pclist)][0]
                for i2 in range(0, len(lists_to_weight[i])):
                    lists_to_weight[i + len(pclist)][i2] -= initial_pitch
                    if lists_to_weight[i + len(pclist)][i2] < 0:
                        lists_to_weight[i + len(pclist)][i2] += pc_mod
                lists_to_weight[i + len(pclist)].sort()

            # Weight lists
            if weight_from_right:
                prime_list = SetClass._weight_from_right(lists_to_weight, pc_mod)
            else:
                prime_list = SetClass._weight_left(lists_to_weight, pc_mod)

            # Create pcset
            for pc in prime_list:
                prime_set.add(pitch.PitchClass(pc, pc_mod))

        return prime_set

    def contains_abstract_subset(self, sc):
        """
        Determines if a set-class is an abstract subset of this set-class
        :param sc: A set-class
        :return: A boolean
        """
        if type(sc) != SetClass:
            raise TypeError(f"Cannot subset items of type {type(sc)} from items of type SetClass.")
        elif sc.mod != self.mod:
            raise ArithmeticError(f"Cannot subset SetClasses of modulo {sc.mod} from SetClasses of modulo {self.mod}.")
        else:
            t_sets = []
            tni_sets = invert(sc.pcset)
            for i in range(self._NUM_PC):
                t_sets.append(transpose(sc.pcset, i))
                t_sets.append(transpose(tni_sets, i))
            for pcs in t_sets:
                if pcs.issubset(self.pcset):
                    return True
            return False

    def get_abstract_complement(self):
        """
        Gets the abstract complement of the SetClass
        :return: The abstract complement SetClass
        """
        complement_set_class = SetClass(pc_mod=self._NUM_PC)
        complement_set_class.pcset = get_complement(self._pcset)
        return complement_set_class

    def get_invariance_vector(self):
        """
        Gets the invariance vector of the SetClass
        :return: The invariance vector, or None if the SetClass has a PitchClass modulo other than 12
        """
        if self._NUM_PC == 12:
            iv = [0, 0, 0, 0, 0, 0, 0, 0]
            c = get_complement(self._pcset)
            utos = transformations.get_utos12()
            for i in range(self._NUM_PC):
                h = [utos[f"T{i}"].transform(self._pcset), utos[f"T{i}I"].transform(self._pcset),
                    utos[f"T{i}M"].transform(self._pcset), utos[f"T{i}MI"].transform(self._pcset)]
                for j in range(4):
                    if h[j] == self._pcset:
                        iv[j] += 1
                    if h[j].issubset(c):
                        iv[4 + j] += 1
            return iv
        else:
            return None

    def get_abstract_subset_classes(self):
        """
        Gets a set of subset-classes contained in this SetClass
        :return:
        """
        subset_pcsets = subsets(self._pcset)
        subset_classes = set()
        for s in subset_pcsets:
            subset_classes.add(SetClass(s, pc_mod=self._NUM_PC))
        return subset_classes

    def get_partition2_subset_classes(self):
        """
        Gets a set of set-class partitions of this SetClass
        :return:
        """
        p2 = partitions2(self._pcset)
        partitions2_set = set()
        for partition in p2:
            partitions2_set.add((SetClass(partition[0]), SetClass(partition[1])))
        return partitions2_set

    @staticmethod
    def get_set_classes12(cardinalities: list=None):
        """
        Gets the chromatic set-classes
        :param cardinalities: A list of cardinalities if you don't want the entire list of 224 set-classes
        :return: A list of the chromatic set-classes
        """
        set_classes = []
        for name in name_tables["forteToSetNameTable"]:
            if cardinalities is not None:
                split = name.split('-')
                if int(split[0]) in cardinalities:
                    sc = SetClass(pc_mod=12)
                    sc.load_from_name(name)
                    set_classes.append(sc)
            else:
                sc = SetClass(pc_mod=12)
                sc.load_from_name(name)
                set_classes.append(sc)
        return set_classes

    def get_z_relation(self):
        """
        Gets the Z-relation of the SetClass
        :return: The Z-relation of the SetClass
        """
        if self._NUM_PC != 12:
            raise ArithmeticError("Cannot get Z-related sets for SetClasses with PitchClass modulo other than 12.")
        else:
            global name_tables
            zset = SetClass()
            f = self.name_forte
            if "Z" in f:
                zset.load_from_name(name_tables["zNameTable"][f])
            return zset

    def is_all_combinatorial_hexachord(self):
        """
        Whether or not the SetClass is an all-combinatorial hexachord
        :return: True or False
        """
        if self._name_prime in name_tables["allCombinatorialHexachords"] and self._NUM_PC == 12:
            return True
        else:
            return False

    @staticmethod
    def is_valid_name(name: str):
        """
        Determines if a chromatic (mod 12) set-class name is valid. Validates prime form, Forte, and Morris names.
        Prime form name format: [xxxx]
        Forte name format: x-x
        Morris name format: (x-x)[xxxx]
        :param name: The name
        :return: A boolean
        """
        global name_tables
        if "[" in name and "-" in name:
            name = name.split(")")
            name[0] = name[0].replace("(", "")
            if name[0] in name_tables["forteToSetNameTable"] and name[1] in name_tables["setToForteNameTable"]:
                return True
        elif "-" in name:
            if name in name_tables["forteToSetNameTable"]:
                return True
        elif name in name_tables["setToForteNameTable"] or name in name_tables["setToForteNameTableLeftPacking"]:
            return True
        return False

    def load_from_name(self, name: str):
        """
        Loads a set-class from a prime-form, Morris, or Forte name
        :param name: The name
        :return:
        """
        global name_tables
        morris_matcher = re.compile(r'\(?\d+-z?\d+\)?\[\d+\]', re.IGNORECASE)
        forte_matcher = re.compile(r'\d+-z?\d+', re.IGNORECASE)
        text_cleaner = re.compile(r'\(|\)|\[|\]|\s')
        low_mod_prime_form_matcher = re.compile(r'\[|\([0-9a-zA-Z]+\]|\)')
        high_mod_prime_form_matcher = re.compile(r'\[|\([0-9a-zA-Z]+\]|\)')
        name = name.upper()
        prime_form_name = name

        if self._NUM_PC == 12:
            prime_form_name = f"[{text_cleaner.sub('', name)}]"
            # If it's a Morris name
            if morris_matcher.search(name):
                prime_form_name = name.split("[")[1]

            # If it's a Forte name
            elif forte_matcher.search(name):
                # Allow Forte names with or without Z, since it isn't fair to expect people to memorize 
                # which set-classes have Z-relations
                name2 = name.split('-')
                name2 = "-Z".join(name2)
                if name in name_tables["forteToSetNameTable"]:
                    prime_form_name = name_tables["forteToSetNameTable"][name]
                elif name2 in name_tables["forteToSetNameTable"]:
                    prime_form_name = name_tables["forteToSetNameTable"][name2]
                else:
                    raise Exception("Invalid Forte name.")

            elif prime_form_name not in name_tables["setToForteNameTable"]:
                raise Exception("Invalid set-class name.")
            
            prime_form_chars = [c for c in text_cleaner.sub('', prime_form_name)]
            pcset = set([pitch.PitchClass(name_tables["hexToInt"][pn], self._NUM_PC) for pn in prime_form_chars])
            self.pcset = pcset
            if self.name_prime != f"[{text_cleaner.sub('', prime_form_name)}]":
                raise Exception("Invalid set-class name.")
        
        elif self._NUM_PC <= 16 and low_mod_prime_form_matcher.search(name):
            prime_form_name = text_cleaner.sub('', name)
            prime_form_chars = [c for c in prime_form_name]
            pcset = set([pitch.PitchClass(name_tables["hexToInt"][pn], self._NUM_PC) for pn in prime_form_chars])
            self.pcset = pcset
            if self.name_prime != f"[{text_cleaner.sub('', name)}]":
                raise Exception("Invalid set-class name.")

        elif self._NUM_PC > 16:
            name = text_cleaner(name)
            name = name.split(",")
            pcset = set([pitch.PitchClass(int(chunk), self._NUM_PC) for chunk in name])
            self.pcset = pcset
        
        else:
            raise Exception("Invalid set-class name.")

    def _make_names(self):
        """
        Makes the names for the set-class
        :return:
        """
        global name_tables
        pc_list = [pc.pc for pc in self._pcset]
        pc_list.sort()
        self._name_carter = None
        self._name_morris = None
        self._name_forte = None
        self._num_forte = None

        if self._NUM_PC <= 16:
            self._name_prime = "[" + "".join([name_tables["hexChars"][pc] for pc in pc_list]) + "]"
        else:
            self._name_prime = "[" + ", ".join([f"{pc:0>2}" for pc in pc_list]) + "]"

        if self._NUM_PC == 12:
            if self._name_prime != "[]":
                if self._name_prime in name_tables["setToForteNameTableLeftPacking"]:
                    self._name_forte = name_tables["setToForteNameTableLeftPacking"][self._name_prime]
                else:
                    self._name_forte = name_tables["setToForteNameTable"][self._name_prime]
            else:
                self._name_forte = "0-1"
            self._name_carter = ""
            if self._name_forte in name_tables["forteToCarterNameTable"]:
                self._name_carter = name_tables["forteToCarterNameTable"][self._name_forte]
            self._name_morris = "(" + self._name_forte + ")" + self._name_prime
            forte_num = self.name_forte.split('-')[1]
            forte_num = forte_num.strip('Z')
            self._num_forte = int(forte_num)

        # Calculate the IC vector
        self._ic_vector_long = [0 for i in range(self._NUM_PC // 2 + 1)]
        for pc in self._pcset:
            for pc2 in self._pcset:
                interval = (pc2.pc - pc.pc) % self._NUM_PC
                if interval > self._NUM_PC // 2:
                    interval = interval * -1 + self._NUM_PC
                self._ic_vector_long[interval] += 1
        for i in range(1, len(self._ic_vector_long)):
            self._ic_vector_long[i] //= 2
        self._ic_vector = self._ic_vector_long[1:]

        # Get the degree of symmetry
        if len(self._pcset) > 0:
            c = get_corpus(self._pcset)
            self._dsym = (self._NUM_PC * 2) // len(c)
        else:
            self._dsym = self._NUM_PC * 2

    @staticmethod
    def _weight_from_right(pclists: list, pc_mod: int=12):
        """
        Weights pclists from the right
        :param pclists: Pclists
        :param pc_mod: The PitchClass mod value to use 
        :return: The most weighted form
        """
        for i in range(len(pclists[0]) - 1, -1, -1):
            if len(pclists) > 1:
                # The smallest item at the current index
                smallest_item = pc_mod - 1

                # Identify the smallest item at the current index
                for j in range(len(pclists)):
                    if pclists[j][i] < smallest_item:
                        smallest_item = pclists[j][i]

                # Remove all lists with larger items at the current index
                j = 0
                while j < len(pclists):
                    if pclists[j][i] > smallest_item:
                        del pclists[j]
                    else:
                        j += 1

            else:
                break
        return pclists[0]

    @staticmethod
    def _weight_left(pclists: list, pc_mod: int=12):
        """
        Weights pclists left
        :param pclists: Pclists
        :param pc_mod: The PitchClass mod value to use 
        :return: The most weighted form
        """
        if len(pclists) > 1:
            # The smallest item at the current index
            smallest_item = pc_mod - 1

            # Identify the smallest item at the last index
            for j in range(0, len(pclists)):
                if pclists[j][len(pclists[0]) - 1] < smallest_item:
                    smallest_item = pclists[j][len(pclists[0]) - 1]

            # Remove all lists with larger items at the current index
            j = 0
            while j < len(pclists):
                if pclists[j][len(pclists[0]) - 1] > smallest_item:
                    del pclists[j]
                else:
                    j += 1

            # Continue processing, but now pack from the left
            for i in range(0, len(pclists[0])):
                if len(pclists) > 1:
                    smallest_item = pc_mod - 1

                    # Identify the smallest item at the current index
                    for j in range(len(pclists)):
                        if pclists[j][i] < smallest_item:
                            smallest_item = pclists[j][i]

                    # Remove all lists with larger items at the current index
                    j = 0
                    while j < len(pclists):
                        if pclists[j][i] > smallest_item:
                            del pclists[j]
                        else:
                            j += 1
                else:
                    break
        return pclists[0]


def get_all_combinatorial_hexachord(name: str):
    """
    Gets an all-combinatorial hexachord (ACH) by name (A-F)
    :param name: The name of the hexachord (A-F)
    :return: The hexachord set-class
    *Only produces mod 12 SetClasses
    """
    sc = SetClass(pc_mod=12)
    sc.load_from_name(name_tables["allCombinatorialHexachordNames"][name])
    return sc


def get_complement(pcset: set):
    """
    Gets the complement of a pcset
    :param pcset: A pcset
    :return: The complement pcset
    *Compatible with all PitchClass modulos
    """
    universal = set()
    if len(pcset) > 0:
        mod = next(iter(pcset)).mod
        for i in range(mod):
            universal.add(pitch.PitchClass(i, mod))
    return universal - pcset


def get_complement_map_utos(pcset: set):
    """
    Gets all UTOs that map a pcset into its complement
    :param pcset: A pcset
    :return: A set of UTOs
    *Compatible with PitchClasses mod 12 and 24
    """
    utos = set()
    mod = next(iter(pcset)).mod
    c = get_complement(pcset)
    if mod == 12:
        uto = transformations.get_utos12()
        for i in range(12):
            tx = uto[f"T{i}"].transform(pcset)
            m5x = uto[f"T{i}M5"].transform(pcset)
            m7x = uto[f"T{i}M7"].transform(pcset)
            m11x = uto[f"T{i}M11"].transform(pcset)
            if tx.issubset(c):
                utos.add(uto[f"T{i}"])
            if m5x.issubset(c):
                utos.add(uto[f"T{i}M5"])
            if m7x.issubset(c):
                utos.add(uto[f"T{i}M7"])
            if m11x.issubset(c):
                utos.add(uto[f"T{i}M11"])
    else:
        uto = transformations.get_utos24()
        for i in range(24):
            tx = uto[f"T{i}"].transform(pcset)
            m5x = uto[f"T{i}M5"].transform(pcset)
            m7x = uto[f"T{i}M7"].transform(pcset)
            m11x = uto[f"T{i}M11"].transform(pcset)
            m13x = uto[f"T{i}M13"].transform(pcset)
            m17x = uto[f"T{i}M17"].transform(pcset)
            m19x = uto[f"T{i}M19"].transform(pcset)
            m23x = uto[f"T{i}M23"].transform(pcset)
            if tx.issubset(c):
                utos.add(uto[f"T{i}"])
            if m5x.issubset(c):
                utos.add(uto[f"T{i}M5"])
            if m7x.issubset(c):
                utos.add(uto[f"T{i}M7"])
            if m11x.issubset(c):
                utos.add(uto[f"T{i}M11"])
            if m13x.issubset(c):
                utos.add(uto[f"T{i}M13"])
            if m17x.issubset(c):
                utos.add(uto[f"T{i}M17"])
            if m19x.issubset(c):
                utos.add(uto[f"T{i}M19"])
            if m23x.issubset(c):
                utos.add(uto[f"T{i}M23"])
    return utos


def get_corpus(pcset: set):
    """
    Gets all transformations of a provided pcset
    :param pcset: A pcset
    :return: A set of all transformations of the pcset
    *Compatible with all PitchClass modulos
    """
    pcsets = set()
    if len(pcset) > 0:
        mod = next(iter(pcset)).mod
        for i in range(mod):
            pcsets.add(frozenset(transpose(pcset, i)))
            pcsets.add(frozenset(transpose(invert(pcset), i)))
    return pcsets


def get_self_map_utos(pcset: set):
    """
    Gets all UTOs that map a pcset into itself
    :param pcset: A pcset
    :return: A set of UTOs
    *Compatible with PitchClasses mod 12 and 24
    """
    utos = set()
    t = type(next(iter(pcset)))
    if t == pitch.PitchClass12:
        uto = transformations.get_utos12()
        for i in range(12):
            tx = uto[f"T{i}"].transform(pcset)
            m5x = uto[f"T{i}M5"].transform(pcset)
            m7x = uto[f"T{i}M7"].transform(pcset)
            m11x = uto[f"T{i}M11"].transform(pcset)
            if tx == pcset:
                utos.add(uto[f"T{i}"])
            if m5x == pcset:
                utos.add(uto[f"T{i}M5"])
            if m7x == pcset:
                utos.add(uto[f"T{i}M7"])
            if m11x == pcset:
                utos.add(uto[f"T{i}M11"])
    else:
        uto = transformations.get_utos24()
        for i in range(24):
            tx = uto[f"T{i}"].transform(pcset)
            m5x = uto[f"T{i}M5"].transform(pcset)
            m7x = uto[f"T{i}M7"].transform(pcset)
            m11x = uto[f"T{i}M11"].transform(pcset)
            m13x = uto[f"T{i}M13"].transform(pcset)
            m17x = uto[f"T{i}M17"].transform(pcset)
            m19x = uto[f"T{i}M19"].transform(pcset)
            m23x = uto[f"T{i}M23"].transform(pcset)
            if tx == pcset:
                utos.add(uto[f"T{i}"])
            if m5x == pcset:
                utos.add(uto[f"T{i}M5"])
            if m7x == pcset:
                utos.add(uto[f"T{i}M7"])
            if m11x == pcset:
                utos.add(uto[f"T{i}M11"])
            if m13x == pcset:
                utos.add(uto[f"T{i}M13"])
            if m17x == pcset:
                utos.add(uto[f"T{i}M17"])
            if m19x == pcset:
                utos.add(uto[f"T{i}M19"])
            if m23x == pcset:
                utos.add(uto[f"T{i}M23"])
    return utos


def convert_to_pcset12(pcset: set) -> set:
    """
    Converts a microtonal pcset (mod 24) to a chromatic pcset (mod 12). Microtonal pitch classes
    are rounded down to the nearest chromatic pitch class.
    :param args: A microtonal pcset (mod 24)
    :return: A chromatic pcset (mod 12)
    """
    return {pitch.PitchClass(pc.pc // 2, 12) for pc in pcset}


def convert_to_pcset24(pcset: set) -> set:
    """
    Converts a chromatic pcset (mod 12) to a microtonal pcset (mod 24).
    :param args: A chromatic pcset (mod 12)
    :return: A microtonal pcset (mod 24)
    """
    return {pitch.PitchClass(pc.pc * 2, 24) for pc in pcset}
    

def invert(pcset: set):
    """
    Inverts a pcset
    :param pcset: The pcset
    :return: The inverted pcset
    *Compatible with all PitchClass modulos
    """
    pcset2 = set()
    if len(pcset) > 0:
        for pc in pcset:
            pcset2.add(pitch.PitchClass(pc.pc * -1, pc.mod))
    return pcset2


def is_all_combinatorial_hexachord(pcset: set):
    """
    Whether or not a pcset is an all-combinatorial hexachord
    :param pcset: A pcset
    :return: True or False
    *Only compatible with mod 12 SetClasses    
    """
    sc = SetClass(pcset)
    if sc.name_prime in name_tables["allCombinatorialHexachords"]:
        return True
    else:
        return False


def make_pcset12(*args):
    """
    Makes a chromatic pcset (mod 12)
    :param args: Integers that represent pitch classes
    :return: A pcset
    """
    if type(args[0]) == list:
        args = args[0]
    return {pitch.PitchClass(pc, 12) for pc in args}


def make_pcset24(*args):
    """
    Makes a microtonal pcset (mod 24)
    :param args: Integers that represent pitch classes
    :return: A pcset
    """
    if type(args[0]) == list:
        args = args[0]
    return {pitch.PitchClass(pc, 24) for pc in args}


def make_subset_graph(set_class, smallest_cardinality=1, show_graph=False, size=(800, 1100)):
    """
    Makes a subset graph
    :param set_class: A set-class
    :param smallest_cardinality: The smallest cardinality to include in the graph
    :param show_graph: Whether or not to generate a visualization of the graph
    :param size: The size of the visualized graph
    :return: A graph
    """
    subset_graph = networkx.DiGraph()
    set_classes = list(set_class.get_abstract_subset_classes())
    for sc in set_classes:
        if len(sc.pcset) >= smallest_cardinality:
            subset_graph.add_node(sc.name_prime)
    for i in range(0, len(set_classes)):
        for j in range(0, i):
            if set_classes[i].contains_abstract_subset(set_classes[j]) and len(set_classes[j].pcset) >= smallest_cardinality:
                subset_graph.add_edge(set_classes[i].name_prime, set_classes[j].name_prime)
        for j in range(i + 1, len(set_classes)):
            if set_classes[i].contains_abstract_subset(set_classes[j]) and len(set_classes[j].pcset) >= smallest_cardinality:
                subset_graph.add_edge(set_classes[i].name_prime, set_classes[j].name_prime)
    if show_graph:
        net = pyvis.network.Network(f"{size[0]}px", f"{size[1]}px", directed=True, bgcolor="#eeeeee",
                                    font_color="#333333", heading="Subset Graph")
        net.toggle_hide_edges_on_drag(False)
        net.barnes_hut()
        net.from_nx(subset_graph, default_node_size=40)
        for node in net.nodes:
            node["title"] = node["id"]
            node["color"] = "#41b535"
        for edge in net.edges:
            edge["color"] = "#1c4219"
        net.show("subset_graph.html")
    return subset_graph


def multiply(pcset: set, n: int):
    """
    Multiplies a pcset
    :param pcset: The pcset
    :param n: The multiplier
    :return: The multiplied pcset
    *Compatible with all PitchClass modulos
    """
    pcset2 = set()
    if len(pcset) > 0:
        for pc in pcset:
            pcset2.add(pitch.PitchClass(pc.pc * n, pc.mod))
    return pcset2


def partitions2(pcset: set):
    """
    Gets all partitions of a pcset (size 2 or 1)
    :param pcset: A pcset
    :return: A list of all partitions
    *Compatible with all PitchClass modulos
    """
    subs = subsets(pcset)
    partitions_dict = {}
    partitions_list = []
    len_pcset = (len(pcset) + 1) // 2 if len(pcset) % 2 else len(pcset) // 2
    for sub in subs:
        if len(sub) <= len_pcset:
            s = frozenset(sub)
            d = frozenset(pcset.difference(sub))
            if d not in partitions_dict:
                partitions_dict[s] = d
    for s in partitions_dict:
        partitions_list.append((set(s), set(partitions_dict[s])))
    return partitions_list


def permutations(pcset: set):
    """
    Generates all permutations of a pcset. Uses a swapping notion derived from the Bauer-Mengelberg/Ferentz algorithm
    for generating all-interval twelve-tone rows.
    Note: The number of permutations will be n! where n is the length of the pcset. The amount of pcsegs is therefore
    O(n!). You may not want to try generating all permutations of a twelve-note set.
    You have been warned.
    :param pcs: A pcset
    :return: A list of pcsegs
    *Compatible with all PitchClass modulos
    """
    current_permutation = [pc.pc for pc in pcset]
    current_permutation.sort()
    
    # Determine the type of pitch-class, and the number of possible pitch-classes
    mod = next(iter(pcset)).mod
    
    all_permutations = []  # This will hold the final list of permutations
    critical_index = 0     # The index of the critical digit

    # This array keeps track of all numbers we have found past the critical index.
    flags = np.zeros((mod), dtype=np.int8)
    
    while critical_index > -1:
        all_permutations.append([pitch.PitchClass(pc, mod) for pc in current_permutation])
        critical_index = -1
        next_higher_digit = 0
        
        # Examine the permutation to find the critical digit
        for i in range(len(current_permutation) - 1, 0, -1):
            flags[current_permutation[i]] = 1
            
            # If we've found the critical index
            if current_permutation[i-1] < current_permutation[i]:
                flags[current_permutation[i-1]] = 1
                critical_index = i - 1
                
                # Find the next highest number so we can do the swap
                for j in range(current_permutation[critical_index] + 1, mod):
                    if flags[j]:
                        next_higher_digit = j
                        flags[j] = 0
                        break

                # Swap the critical digit
                current_permutation[critical_index] = next_higher_digit

                # Repopulate the permutation
                for j in range(mod):
                    if flags[j]:
                        critical_index += 1
                        current_permutation[critical_index] = j
                        flags[j] = 0
                break
    return all_permutations


def set_class_filter12(name: str, sets: list):
    """
    Filters a list of pcsets
    :param name: The name to find
    :param sets: A list of sets to filter
    :return: A filtered list
    *Compatible with all PitchClass modulos. For pcsets of modulo 12, also supports Forte and Morris names.
    """
    newlist = []
    sc = SetClass()
    for s in sets:
        sc.pcset = s
        if sc.name_prime == name or sc.name_forte == name or sc.name_morris == name:
            newlist.append(s)
    return newlist


def subsets(pcset: set):
    """
    Gets all subsets of a pcset, using the bit masking solution from
    https://afteracademy.com/blog/print-all-subsets-of-a-given-set
    :param pcset: A pcset
    :return: A list containing all subsets of the pcset
    """
    total = 2 ** len(pcset)
    sub = []
    if total > 1:
        mod = next(iter(pcset)).mod
        pcseg = list(pcset)
        pcseg.sort()
        for index in range(total):
            sub.append([])
            for i in range(len(pcset)):
                if index & (1 << i):
                    sub[index].append(pitch.PitchClass(pcseg[i].pc, mod))
        sub.sort()
    return sub


def transform(pcset, string):
    """
    Transforms a pcset with a provided transformation string
    - Tn: transpose
    - I: invert
    - Mn: multiply
    :param pcset: The pcset to transform
    :param string: The transformation string
    :return: The transformed pcset
    """
    pcset2 = set.copy(pcset)
    i = len(string) - 1
    while i >= 0:
        num = 0
        place_exp = 0
        while str.isdigit(string[i]) and i > 0:
            num += int(string[i]) * 10 ** place_exp
            place_exp += 1
            i -= 1
        match string[i]:
            case 'T':
                pcset2 = transpose(pcset2, num)
            case 'I':
                pcset2 = invert(pcset2)
            case 'M':
                pcset2 = multiply(pcset2, num)
        i -= 1
    return pcset2


def transpose(pcset: set, n: int):
    """
    Transposes a pcset
    :param pcset: The pcset
    :param n: The index of transposition
    :return: The transposed pcset
    *Compatible with all PitchClass modulos
    """
    pcset2 = set()
    if len(pcset) > 0:
        mod = next(iter(pcset)).mod
        for pc in pcset:
            pcset2.add(pitch.PitchClass(pc.pc + n, mod))
    return pcset2


def transpositional_combination(pcset1: set, pcset2: set):
    """
    Transpositionally combines (TC) two pcsets. This is Boulez's "multiplication."
    :param pcset1: A pcset
    :param pcset2: A pcset
    :return: The TC pcset
    *Compatible with all PitchClass modulos
    """
    pcset3 = set()
    if len(pcset1) > 0 and len(pcset2) > 0:
        mod = next(iter(pcset1)).mod
        for pc2 in pcset2:
            for pc1 in pcset1:
                pcset3.add(pitch.PitchClass(pc1.pc + pc2.pc, mod))
    return pcset3


def visualize(pcset: set):
    """
    Visualizes a pcset
    :param pcset: A pcset
    :return: A visualization
    *Compatible with all PitchClass modulos
    """
    line = ""
    if len(pcset) > 0:
        mod = next(iter(pcset)).mod
        for i in range(mod):
            if pitch.PitchClass(i, mod) in pcset:
                line += "X"
            else:
                line += " "
    return line
