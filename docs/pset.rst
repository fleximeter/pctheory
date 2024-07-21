pctheory.pset
################

.. py:class:: Sieve

    .. py:property:: base_pitch

        The base pitch of the Sieve (pitch 0)

    .. py:property:: intervals

        The intervallic succession of the Sieve

    .. py:property:: pc_mod

        The pitch class mod of the Sieve (which specifies the pitch type)

    .. py:property:: period

        The period of the Sieve

    .. py:property:: tuples

        The tuples in the Sieve

    .. py:method:: __init__(self, tuples, base_pitch: int, pc_mod=12)
        
        Creates a Sieve
        
        :param tuples: A collection of tuples to add to the sieve.
        :param base_pitch: Pitch 0 for the sieve. This pitch does not actually have to be
        in the sieve - it will just serve as the 0 reference point.
        :param pc_mod: The pitch-class mod of the Sieve
        
    .. py:method:: add_tuples(self, *args)
        
        Adds one or more tuples to the Sieve12
        
        :param args: One or more tuples

    .. py:method:: get_range(self, p0, p1)
        
        Gets all pitches in the sieve between p0 and p1
        
        :param p0: The low pitch
        :param p1: The high pitch
        :return: A pset

    .. py:method:: intersection(self, sieve)
        
        Intersects two Sieves
        
        :param sieve: A Sieve
        :return: A new Sieve. It will have the same base pitch as self.

    .. py:method:: is_in_sieve(self, p)
        
        Whether or not a pitch or pset is in the sieve
        
        :param p: A pitch (Pitch or int) or pset
        :return: True or False

    .. py:method:: union(self, sieve)
        
        Unions two Sieves
        
        :param sieve: A Sieve
        :return: A new Sieve. It will have the same base pitch as self.

.. py:function:: calculate_pm_similarity(pset1: set, pset2: set, ic_roster1=None, ic_roster2=None)
    
    Gets the pitch-measure (PM) similarity between pset1 and pset2
    
    :param pset1: A pset
    :param pset2: A pset
    :param ic_roster1: The ic_roster for pset 1. If None, will be calculated.
    :param ic_roster2: The ic_roster for pset 2. If None, will be calculated.
    :return: The PM similarity as a tuple of integers
    *Compatible with all Pitch modulos

.. py:function:: generate_random_pset_realizations(pcset: set, lower_boundary: int, upper_boundary: int, num_realizations: int=1, num_duplicate_pitches: int=0, filter_func=None)
    
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

.. py:function:: get_fb_class(pset: set, p0: int)
    
    Gets the FB-class of a pset
    
    :param pset: The pset
    :param p0: The lowest pitch
    :return: The FB-class as a list of integers
    *Compatible with all Pitch modulos

.. py:function:: get_ic_matrix(pset: set)
    
    Gets the pitch ic-matrix
    
    :param pset: The pset
    :return: The ic-matrix as a list of lists
    *Compatible with all Pitch modulos

.. py:function:: get_ic_roster(pset: set)
    
    Gets the pitch ic-roster
    
    :param pset: The pset
    :return: The ic-roster as a dictionary
    *Compatible with all Pitch modulos

.. py:function:: get_pcint_class(pset: set)
    
    Gets the PCINT-class of a pset
    
    :param pset: The pset
    :return: The PCINT-class as a list of integers
    *Compatible with all Pitch modulos

.. py:function:: get_set_class(pset: set)
    
    Gets the set-class of a pset
    
    :param pset: The pset
    :return: The set-class as a list of integers
    *Compatible with all Pitch modulos

.. py:function:: invert(pset: set)
    
    Inverts a pset
    
    :param pset: The pset
    :return: The inverted pset
    *Compatible with all Pitch modulos

.. py:function:: make_pset12(*args)
    
    Makes a pset
    
    :param *args: Pitches
    :return: A pset
    *Compatible only with chromatic psegs

.. py:function:: make_pset24(*args)
    
    Makes a pset
    
    :param *args: Pitches
    :return: A pset
    *Compatible only with microtonal psegs
    
.. py:function:: subsets(pset: set)
    
    Gets all subsets of a pset
    
    :param pset: A pset
    :return: A list containing all subsets of the pset
    *Compatible with all Pitch modulos

.. py:function:: to_pcset(pset: set)
    
    Makes a pcset out of a pset
    
    :param pset: A pset
    :return: A pcset
    *Compatible with all Pitch modulos

.. py:function:: transform(pset: set, transformation: transformations.UTO)
    
    Transforms a pset
    
    :param pset: A pset
    :param transformation: A transformation
    :return: The transformed set
    *Compatible with all Pitch modulos

.. py:function:: transpose(pset: set, n: int)
    
    Transposes a pset
    
    :param pset: The pset
    :param n: The index of transposition
    :return: The transposed pset
    *Compatible with all Pitch modulos
