"""
File: poset.py
Author: Jeff Martin
Date: 11/7/2021

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

from . import pitch, pcset


def filter_poset_positions(posets: list, position_filter: list, exclude=False):
    """
    Filters a list of posets
    :param posets: The posets
    :param position_filter: The filter (length of filter must match length of each poset). Each position in the filter
    must be either None or a pcset.
    :param exclude: Whether the filter searches for inclusion or exclusion
    :return: A filtered list
    """
    filtered = []
    for po in posets:
        match = True
        for i in range(len(po)):
            # A position filter of None means we don't care what's in that position
            if position_filter[i] is not None:
                # If we are filtering for exclusion
                if exclude:
                    if type(po[i]) == set:
                        if len(po[i].intersection(position_filter[i])) > 0:
                            match = False
                    else:
                        if po[i] in position_filter[i]:
                            match = False
                # If we are filtering for inclusion
                else:
                    if type(po[i]) == set:
                        if not po[i].issubset(position_filter[i]):
                            match = False
                    else:
                        if po[i] not in position_filter[i]:
                            match = False
        if match:
            filtered.append(po)
    return filtered


def generate_chains_weak(p0: pitch.PitchClass, sc_list: list, max_2_similarity: float = 0.4,
                         min_2_similarity: float = 0, max_3_similarity: float = 1, min_3_similarity: float = 0,
                         pn=None):
    """
    Generates all possible "weak" chains of pcsets that match the specified input criteria. The result is a list of
    posets of the form
    <pc_0 {...} pc_1 {...} pc_2 {...}>
    where a member of each set-class in the list appears in order. The unordered set is unioned with the immediately
    adjacent free pcs to form the actual set corresponding to the set-class in the list.
    This is a weaker form of the "strong" chains in Morris 1987, where there must be complete overlap between adjacent
    pcsets. In these chains, only one pc overlaps between adjacent pcsets.
    :param p0: The starting pitch
    :param sc_list: The list of set-class names
    :param max_2_similarity: The maximum adjacent similarity percentage (expressed as a decimal). Specifies
    the maximum percentage of a set that can be duplicated in an adjacent set. For example, 0.4 means that 2 out of 5
    pcs in a pentachord may be duplicated in each adjacent set. A value of 1 means that no similarity restrictions
    are imposed (since we are allowing up to 100% similarity). A value that is too low to allow at least 1 duplicate
    pc will prevent the algorithm from generating any chains at all (since we need at least one duplicate between
    each pair of adjacent pcsets).
    :param min_2_similarity: The corresponding minimum of max_2_similarity
    :param max_3_similarity: Like max_2_similarity, except this covers three adjacent pcsets. The default value is 1,
    which imposes no similarity restrictions.
    :param min_3_similarity: The corresponding minimum of max_3_similarity
    :param pn: The ending pitch (if left as None, no ending pitch will be separated out of the last sets)
    :return: A list of weak chains. The list will be empty if it was impossible to generate any chains matching the
    provided specifications.
    """
    chain_build = []   # The chains will be stored here
    chain_build2 = []      # (a temporary storage place for chains)
    sc = pcset.SetClass()  # The set-class object for pcset generation

    # Consider the first pcset and initialize the chains
    sc.load_from_name(sc_list[0])
    corpus = pcset.get_corpus(sc.pcset)

    # If a pcset in the corpus matches the starting pc, we can use that pcset to start a chain.
    for frozen_pcset in corpus:
        pcset2 = set(frozen_pcset)
        if p0 in pcset2:
            pcset2.remove(p0)
            chain_build.append([p0, pcset2])

    # Continue building chains in the same manner as before
    for i in range(1, len(sc_list)):
        sc.load_from_name(sc_list[i])
        corpus = pcset.get_corpus(sc.pcset)
        for frozen_pcset in corpus:
            pcset2 = set(frozen_pcset)
            # Now we need to look at each chain we already have
            for j in range(len(chain_build)):
                # Temporarily reconstruct the previous set
                tempset = set(chain_build[j][len(chain_build[j]) - 1])
                tempset.add(chain_build[j][len(chain_build[j]) - 2])

                # Calculate the similarity of the last set with the current one (sim2)
                intersect = tempset.intersection(pcset2)
                sim2 = len(intersect) / len(pcset2)

                # Calculate the similarity of the last two sets with the current one (sim3)
                sim3 = min_3_similarity
                if len(chain_build[j]) >= 4:
                    tempset2 = set(chain_build[j][len(chain_build[j]) - 3])
                    tempset2.add(chain_build[j][len(chain_build[j]) - 4])
                    tempset2.add(chain_build[j][len(chain_build[j]) - 2])
                    union1 = tempset.union(tempset2)
                    intersect2 = union1.intersection(pcset2)
                    sim3 = len(intersect2) / len(pcset2)

                # If the similarity conditions are satisfied, we can continue building the chains
                if max_2_similarity >= sim2 >= min_2_similarity and max_3_similarity >= sim3 >= min_3_similarity:
                    # We consider each pc that can be used as an intersection point
                    for pc in intersect:
                        # We cannot use the same pc as an intersection point twice in a row.
                        if pc != chain_build[j][len(chain_build[j]) - 2]:
                            new_chain = []
                            # Unfortunately we need to manually copy the data structures to avoid disaster
                            for item in chain_build[j]:
                                if type(item) == set:
                                    new_chain.append(set(item))
                                else:
                                    new_chain.append(item)
                            new_chain.append(pc)
                            new_chain.append(set(pcset2))
                            # Remove the intersecting pc from its surrounding sets
                            new_chain[len(new_chain) - 3].remove(pc)
                            new_chain[len(new_chain) - 1].remove(pc)
                            chain_build2.append(new_chain)

        # Clear out the previous generation of chains and add in the new chains
        chain_build = chain_build2
        chain_build2 = []

    # If the last pitch is specified, we need to separate it out and prune the chains that don't have it.
    if pn is not None:
        for chain in chain_build:
            if pn in chain[len(chain) - 1]:
                chain.append(pn)
                chain[len(chain) - 2].remove(pn)
                chain_build2.append(chain)
        return chain_build2

    return chain_build
