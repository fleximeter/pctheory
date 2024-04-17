"""
File: pset.py
Author: Jeff Martin
Date: 11/1/2021

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

from pctheory import pitch, transformations, util
import music21
import numpy as np
import random

_rng = random.Random()
_rng.seed()


class Sieve:
    """
    Represents a Xenakis sieve. Compatible with all Pitch modulos.
    """
    def __init__(self, tuples, base_pitch: int, pc_mod=12):
        """
        Creates a Sieve
        :param tuples: A collection of tuples to add to the sieve.
        :param base_pitch: Pitch 0 for the sieve. This pitch does not actually have to be
        in the sieve - it will just serve as the 0 reference point.
        :param pc_mod: The pitch-class mod of the Sieve
        """
        self._tuples = set()
        self._intervals = []
        self._pc_mod = pc_mod
        self._period = 0
        self._base_pitch = pitch.Pitch(base_pitch.p, pc_mod)
        self.add_tuples(tuples)

    @property
    def base_pitch(self) -> pitch.Pitch:
        """
        The base pitch of the Sieve12 (pitch 0)
        :return: The base pitch
        """
        return self._base_pitch

    @property
    def intervals(self) -> list:
        """
        The intervallic succession of the Sieve12
        :return: The intervallic succession
        """
        return self._intervals

    @property
    def pc_mod(self) -> int:
        """
        The pitch class mod of the Sieve (which specifies the pitch type)
        :return: The pitch class mod
        """
        return self._pc_mod

    @property
    def period(self) -> int:
        """
        The period of the Sieve12
        :return: The period
        """
        return self._period

    @property
    def tuples(self) -> set:
        """
        The tuples in the Sieve12
        :return: The tuples
        """
        return self._tuples

    def add_tuples(self, *args):
        """
        Adds one or more tuples to the Sieve12
        :param args: One or more tuples
        :return: None
        """
        lcm_list = set()
        if type(args[0]) == set or type(args[0]) == list or type(args[0]) == tuple:
            args = args[0]
        for tup in args:
            self._tuples.add(tup)
        for tup in self._tuples:
            lcm_list.add(tup[0])
        self._period = util.lcm(lcm_list)
        r = self.get_range(pitch.Pitch(self._base_pitch.p, self._pc_mod), pitch.Pitch(self._base_pitch.p + self._period, self._pc_mod))
        r = list(r)
        r.sort()
        for i in range(1, len(r)):
            self._intervals.append(r[i].p - r[i - 1].p)

    def get_range(self, p0, p1) -> set:
        """
        Gets all pitches in the sieve between p0 and p1
        :param p0: The low pitch
        :param p1: The high pitch
        :return: A pset
        """
        ps = set()
        p_low = p0.p if type(p0) == pitch.Pitch else p0
        p_high = p1.p + 1 if type(p1) == pitch.Pitch else p1 + 1
        for j in range(p_low, p_high):
            i = j - self._base_pitch.p
            if i >= 0:
                for tup in self._tuples:
                    if i % tup[0] == tup[1]:
                        ps.add(pitch.Pitch(j, self._pc_mod))
        return ps

    def intersection(self, sieve):
        """
        Intersects two Sieves
        :param sieve: A Sieve
        :return: A new Sieve. It will have the same base pitch as self.
        """
        t = set()
        for tup1 in self._tuples:
            for tup2 in sieve.tuples:
                if tup1 == tup2:
                    t.add(tup1)
        return Sieve(t, self._base_pitch, self._pc_mod)

    def is_in_sieve(self, p) -> bool:
        """
        Whether or not a pitch or pset is in the sieve
        :param p: A pitch (Pitch or int) or pset
        :return: True or False
        """
        ps = None
        if type(p) == set:
            ps = p
        elif type(p) == pitch.Pitch:
            ps = {p}
        elif type(p) == int:
            ps = {pitch.Pitch(p, self._pc_mod)}
        for q in ps:
            i = q.p - self._base_pitch.p
            if i < 0:
                return False
            else:
                for tup in self._tuples:
                    if i % tup[0] == tup[1]:
                        break
                else:
                    return False
        return True

    def union(self, sieve):
        """
        Unions two Sieve12s
        :param sieve: A Sieve12
        :return: A new Sieve12. It will have the same base pitch as self.
        """
        t = set()
        for tup in self._tuples:
            t.add(tup)
        for tup in sieve.tuples:
            t.add(tup)
        return Sieve(t, self._base_pitch, self._pc_mod)


def calculate_pm_similarity(pset1: set, pset2: set, ic_roster1=None, ic_roster2=None) -> tuple:
    """
    Gets the pitch-measure (PM) similarity between pset1 and pset2
    :param pset1: A pset
    :param pset2: A pset
    :param ic_roster1: The ic_roster for pset 1. If None, will be calculated.
    :param ic_roster2: The ic_roster for pset 2. If None, will be calculated.
    :return: The PM similarity as a tuple of integers
    *Compatible with all Pitch modulos
    """
    cint = len(pset1.intersection(pset2))
    ic_shared = 0
    if ic_roster1 is None:
        ic_roster1 = get_ic_roster(pset1)
    if ic_roster2 is None:
        ic_roster2 = get_ic_roster(pset2)
    for ic in ic_roster1:
        if ic in ic_roster2:
            if ic_roster1[ic] < ic_roster2[ic]:
                ic_shared += ic_roster1[ic]
            else:
                ic_shared += ic_roster2[ic]
    return (cint, ic_shared)


def generate_random_pset_realizations(pcset: set, lower_boundary: int, upper_boundary: int, num_realizations: int=1, num_duplicate_pitches: int=0, filter_func=None):
    """
    Generates random pset realizations of a given pcset, 
    within the specified upper and lower boundaries
    :param pcset: The pcset to realize
    :param lower_boundary: The lower boundary
    :param upper_boundary: The upper boundary
    :param num_realizations: The number of random realizations to generate
    :param num_duplicate_pitches: The number of additional duplicate pitches to include (for doubling)
    :param filter_func: A function for filtering the pset realizations to force them to match specified criteria
    :return: One or more random pset realizations of the pcset within the given boundaries. If the number of realizations
    is greater than 1, returns a list of psets. Otherwise returns a single pset.
    *Compatible with all Pitch modulos
    """
    if len(pcset) == 0:
        return set()
    else:
        mod = next(iter(pcset)).mod
        lowest_boundary_note = lower_boundary % mod
        
        # Generate all of the possible pitch realizations for each pitch-class
        # within the range provided
        pitch_choices = []
        for pc in pcset:
            choices = []
            candidate_pitch = (pc.pc - lowest_boundary_note) % mod + lower_boundary           
            in_range = True
            while in_range:
                if candidate_pitch > upper_boundary:
                    in_range = False
                else:
                    choices.append(pitch.Pitch(candidate_pitch, mod))
                candidate_pitch += mod
            pitch_choices.append(choices)

        # Generate pset realizations
        realizations = {}
        i = 0
        while len(realizations) < num_realizations and i < 10 * num_realizations:
            # Build the current realization
            realization = set()
            unused_pitches = []
            for bucket in pitch_choices:
                if len(bucket) > 0:
                    idx = _rng.randrange(0, len(bucket))
                    realization.add(bucket[idx])
                    unused_pitches += bucket[:idx] + bucket[idx+1:]

            # Add duplicate pitches 
            for i in range(num_duplicate_pitches):
                idx = _rng.randrange(0, len(unused_pitches))
                realization.add(unused_pitches[idx])
                del unused_pitches[idx]

            if filter_func is None:
                realizations[str(realization)] = realization
            elif filter_func(realization):
                realizations[str(realization)] = realization
            i += 1
        realizations = [realizations[key] for key in realizations]

        if len(realizations) == 1:
            return realizations[0]
        else:
            return realizations


def get_fb_class(pset: set, p0: int) -> list:
    """
    Gets the FB-class of a pset
    :param pset: The pset
    :param p0: The lowest pitch
    :return: The FB-class as a list of integers
    *Compatible with all Pitch modulos
    """
    intlist = []
    if len(pset) > 0 and p0 >= 0:
        mod = pset[0].mod
        for p in pset:
            intlist.append((p.p - p0) % mod)
        intlist.sort()
        if len(intlist) > 0:
            del intlist[0]
    return intlist


def get_ic_matrix(pset: set) -> np.array:
    """
    Gets the pitch ic-matrix
    :param pset: The pset
    :return: The ic-matrix as a list of lists
    *Compatible with all Pitch modulos
    """
    mx = np.empty((len(pset), len(pset)))
    pseg = list(pset)
    pseg.sort()
    for i in range(mx.shape[0]):
        for j in range(mx.shape[1]):
            mx[i][j] = abs(pseg[i].p - pseg[j].p)
    return mx


def get_ic_roster(pset: set) -> dict:
    """
    Gets the pitch ic-roster
    :param pset: The pset
    :return: The ic-roster as a dictionary
    *Compatible with all Pitch modulos
    """
    pseg = list(pset)
    roster = {}
    pseg.sort()
    for i in range(len(pseg) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            interval = abs(pseg[i].p - pseg[j].p)
            if interval not in roster:
                roster[interval] = 1
            else:
                roster[interval] += 1
    return roster


def get_pcint_class(pset: set) -> list:
    """
    Gets the PCINT-class of a pset
    :param pset: The pset
    :return: The PCINT-class as a list of integers
    *Compatible with all Pitch modulos
    """
    intlist = []
    if len(pset) > 0:
        pseg = list(pset)
        pseg.sort()
        mod = pseg[0].mod
        for i in range(1, len(pseg)):
            intlist.append((pseg[i].p - pseg[i - 1].p) % mod)
    return intlist


def get_set_class(pset: set) -> list:
    """
    Gets the set-class of a pset
    :param pset: The pset
    :return: The set-class as a list of integers
    *Compatible with all Pitch modulos
    """
    pseg = list(pset)
    pseg.sort()
    intlist = []
    for i in range(1, len(pseg)):
        intlist.append(pseg[i].p - pseg[i - 1].p)
    return intlist


def invert(pset: set) -> set:
    """
    Inverts a pset
    :param pset: The pset
    :return: The inverted pset
    *Compatible with all Pitch modulos
    """
    pset2 = set()
    if len(pset) > 0:
        mod = next(iter(pset)).mod
        for p in pset:
            pset2.add(pitch.Pitch(p.p * -1, mod))
    return pset2


def m21_make_pset(item) -> set:
    """
    Makes a pset from a music21 object
    :param item: A music21 object
    :return: A pset
    *Compatible only with chromatic psegs
    """
    pset2 = set()
    if type(item) == music21.note.Note:
        pset2.add(pitch.Pitch(item.pitch.midi - 60, 12))
    elif type(item) == music21.pitch.Pitch:
        pset2.add(pitch.Pitch(item.pitch.midi - 60, 12))
    elif type(item) == music21.chord.Chord:
        for p in item.pitches:
            pset2.add(pitch.Pitch(p.midi - 60, 12))
    else:
        raise TypeError("Unsupported music21 type")
    return pset2


def make_pset12(*args) -> set:
    """
    Makes a pset
    :param *args: Pitches
    :return: A pset
    *Compatible only with chromatic psegs
    """
    if type(args[0]) == list:
        args = args[0]
    return {pitch.Pitch(p, 12) for p in args}


def make_pset24(*args) -> set:
    """
    Makes a pset
    :param *args: Pitches
    :return: A pset
    *Compatible only with microtonal psegs
    """
    if type(args[0]) == list:
        args = args[0]
    return {pitch.Pitch(p, 24) for p in args}


def subsets(pset: set) -> list:
    """
    Gets all subsets of a pset, using the bit masking solution from
    https://afteracademy.com/blog/print-all-subsets-of-a-given-set
    :param pset: A pset
    :return: A list containing all subsets of the pset
    *Compatible with all Pitch modulos
    """
    total = 2 ** len(pset)
    t = type(next(iter(pset)))
    sub = []
    pseg = list(pset)
    pseg.sort()
    for index in range(total):
        sub.append([])
        for i in range(len(pset)):
            if index & (1 << i):
                sub[index].append(t(pseg[i].p))
    sub.sort()
    return sub


def to_pcset(pset: set) -> set:
    """
    Makes a pcset out of a pset
    :param pset: A pset
    :return: A pcset
    *Compatible with all Pitch modulos
    """
    if len(pset) > 0:
        mod = next(iter(pset)).mod
        return {pitch.PitchClass(p.pc, mod) for p in pset}
    else:
        return set()


def transform(pset: set, transformation: transformations.UTO) -> set:
    """
    Transforms a pset
    :param pset: A pset
    :param transformation: A transformation
    :return: The transformed set
    *Compatible with all Pitch modulos
    """
    pset2 = set()
    if len(pset) > 0:
        mod = next(iter(pset)).mod
        for p in pset:
            pset2.add(pitch.Pitch(p.p * transformation[1] + transformation[0], mod))
    return pset2


def transpose(pset: set, n: int) -> set:
    """
    Transposes a pset
    :param pset: The pset
    :param n: The index of transposition
    :return: The transposed pset
    *Compatible with all Pitch modulos
    """
    pset2 = set()
    if len(pset) > 0:
        mod = next(iter(pset)).mod
        for p in pset:
            pset2.add(pitch.Pitch(p.p + n, mod))
    return pset2
