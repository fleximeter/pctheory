"""
File: set_complex.py
Author: Jeff Martin
Date: 11/5/2021

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

from . import pcset


set_classes12 = pcset.SetClass.get_set_classes12()


def assert_k(s, t):
    """
    Asserts that s and t are in a K-relationship
    Source: Morris, "Class Notes for Atonal Music Theory," p. 49
    :param s: A set-class
    :param t: A set-class
    :return: A boolean
    """
    t_bar = t.get_abstract_complement()
    return t.contains_abstract_subset(s) or \
           t_bar.contains_abstract_subset(s) or \
           s.contains_abstract_subset(t) or \
           s.contains_abstract_subset(t_bar)


def assert_kh(s, t):
    """
    Asserts that s and t are in a Kh-relationship
    Source: Morris, "Class Notes for Atonal Music Theory," p. 49
    :param s: A set-class
    :param t: A set-class
    :return: A boolean
    """
    t_bar = t.get_abstract_complement()
    return (t.contains_abstract_subset(s) or s.contains_abstract_subset(t)) and \
        (t_bar.contains_abstract_subset(s) or s.contains_abstract_subset(t_bar))


def get_k12(nexus: pcset.SetClass):
    """
    Gets a K-complex about a provided nexus set
    :param nexus: A nexus set
    :return: The K-complex
    """
    k = []
    for sc in set_classes12:
        if assert_k(nexus, sc):
            k.append(sc)
    return k


def get_kh12(nexus: pcset.SetClass):
    """
    Gets a Kh-complex about a provided nexus set
    :param nexus: A nexus set
    :return: The Kh-complex
    """
    kh = []
    for sc in set_classes12:
        if assert_kh(nexus, sc):
            kh.append(sc)
    return kh
