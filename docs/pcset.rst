pctheory.pcset
################


.. py:class:: SetClass

    Represents a pitch-class set-class. Compatible with mod12 and mod24.

    .. py:property:: derived_core

        Gets derived core associations

    .. py:property:: dsym

        Gets the degree of symmetry of the set-class.

    .. py:property:: ic_vector

        Gets the IC vector

    .. py:property:: ic_vector_long

        Gets the IC vector in long format

    .. py:property:: ic_vector_str

        Gets the IC vector as a string

    .. py:property:: ic_vector_long_str

        Gets the IC vector in long format as a string

    .. py:property:: is_z_relation

        Whether or not this set-class is Z-related to another set-class
    
    .. py:property:: mod

        The mod index

    .. py:property:: name_carter

        Gets Elliott Carter's number for this set-class

    .. py:property:: name_forte

        Get Allen Forte's name for this set-class

    .. py:property:: name_morris

        Get Robert Morris's name for this set-class. The Morris name is a combination of the Forte name and the prime form name.

    .. py:property:: name_prime
        
        Gets the prime form name for this set-class.

    .. py:property:: num_forte

        Gets the Forte number for this set-class.

    .. py:property:: pcset

        Gets the prime form pitch-class set.

    .. py:property:: weight_right

        Whether or not to calculate the prime form by weighting candidate pitch-class sets from the right (default: ``True``).
        This does not affect the prime form of the vast majority of mod 12 set-classes.

    .. py:method:: __init__(self, pcset=None, pc_mod=None)
        
        Creates a SetClass
        
        :param pcset: A pcset to initialize the SetClass, or else the prime form name of the SetClass.
        :param pc_mod: The modulo of the SetClass. If none is provided, it will be assumed from the pcset. If no pcset is provided, 12 is assumed.

    .. py:method:: __eq__(self, other)

        Compares two ``SetClass`` objects for equality

        :param other: The other ``SetClass`` to compare for equality

    .. py:method:: __hash__(self)

        Gets the hash value of the ``SetClass``.

    .. py:method:: __len__(self)

        Gets the cardinality of the ``SetClass``.

    .. py:method:: __lt__(self, other)

        Compares two ``SetClass`` objects. Returns ``True`` if this set-class is less than the other set-class.
        
        :param other: The other ``SetClass`` to compare

    .. py:method:: __ne__(self, other)

        Compares two ``SetClass`` objects for inequality
        
        :param other: The other ``SetClass`` to compare for inequality

    .. py:method:: __repr__(self)

        Gets a representation of the ``SetClass``.

    .. py:method:: __str__(self)

        Gets a representation of the ``SetClass``.

    .. py:method:: calculate_prime_form(pcset: set, weight_from_right: bool = True, pc_mod: int=12)
        
        Calculates the prime form of a pcset
        
        :param pcset: The pcset
        :param weight_from_right: Whether or not to pack from the right
        :param pc_mod: The PitchClass mod value to use 
        :return: The prime form

    .. py:method:: contains_abstract_subset(self, sc)
        
        Determines if a set-class is an abstract subset of this set-class
        
        :param sc: A set-class
        :return: A boolean

    .. py:method:: get_abstract_complement(self)
        
        Gets the abstract complement of the SetClass
        
        :return: The abstract complement SetClass

    .. py:method:: get_invariance_vector(self)
        
        Gets the invariance vector of the SetClass
        
        :return: The invariance vector, or None if the SetClass has a PitchClass modulo other than 12

    .. py:method:: get_abstract_subset_classes(self)
        
        Gets a set of subset-classes contained in this SetClass

    .. py:method:: get_partition2_subset_classes(self)
        
        Gets a set of set-class partitions of this SetClass

    .. py:method:: get_set_classes12(cardinalities: list=None)
        
        Gets the chromatic set-classes
        
        :param cardinalities: A list of cardinalities if you don't want the entire list of 224 set-classes
        :return: A list of the chromatic set-classes

    .. py:method:: get_z_relation(self)
        
        Gets the Z-relation of the SetClass
        
        :return: The Z-relation of the SetClass

    .. py:method:: is_all_combinatorial_hexachord(self)
        
        Whether or not the SetClass is an all-combinatorial hexachord

        :return: True or False

    .. py:method:: is_valid_name(name: str)
        
        Determines if a chromatic (mod 12) set-class name is valid. Validates prime form, Forte, and Morris names.
        Prime form name format: [xxxx]
        Forte name format: x-x
        Morris name format: (x-x)[xxxx]
        
        :param name: The name
        :return: A boolean

    .. py:method:: load_from_name(self, name: str)
        
        Loads a set-class from a prime-form, Morris, or Forte name
        
        :param name: The name
        
.. py:function:: def get_all_combinatorial_hexachord(name: str)
    
    Gets an all-combinatorial hexachord (ACH) by name (A-F)

    :param name: The name of the hexachord (A-F)
    :return: The hexachord set-class
    *Only produces mod 12 SetClasses

.. py:function:: get_complement(pcset: set)
    
    Gets the complement of a pcset
    
    :param pcset: A pcset
    :return: The complement pcset
    *Compatible with all PitchClass modulos

.. py:function:: get_complement_map_utos(pcset: set)
    
    Gets all UTOs that map a pcset into its complement
    
    :param pcset: A pcset
    :return: A set of UTOs
    *Compatible with PitchClasses mod 12 and 24

.. py:function:: get_corpus(pcset: set)
    
    Gets all transformations of a provided pcset
    
    :param pcset: A pcset
    :return: A set of all transformations of the pcset
    *Compatible with all PitchClass modulos

.. py:function:: get_self_map_utos(pcset: set)
    
    Gets all UTOs that map a pcset into itself
    
    :param pcset: A pcset
    :return: A set of UTOs
    *Compatible with PitchClasses mod 12 and 24

.. py:function:: convert_to_pcset12(pcset: set)
    
    Converts a microtonal pcset (mod 24) to a chromatic pcset (mod 12). Microtonal pitch classes
    are rounded down to the nearest chromatic pitch class.
    
    :param args: A microtonal pcset (mod 24)
    :return: A chromatic pcset (mod 12)
    
.. py:function:: convert_to_pcset24(pcset: set)
    
    Converts a chromatic pcset (mod 12) to a microtonal pcset (mod 24).
    
    :param args: A chromatic pcset (mod 12)
    :return: A microtonal pcset (mod 24)

.. py:function:: invert(pcset: set)
    
    Inverts a pcset
    
    :param pcset: The pcset
    :return: The inverted pcset
    *Compatible with all PitchClass modulos

.. py:function:: is_all_combinatorial_hexachord(pcset: set)
    
    Whether or not a pcset is an all-combinatorial hexachord
    
    :param pcset: A pcset
    :return: True or False
    *Only compatible with mod 12 SetClasses

.. py:function:: make12(*args)
    
    Makes a chromatic pcset (mod 12)
    
    :param args: Integers that represent pitch classes
    :return: A pcset

.. py:function:: make_pcset12(*args)
    
    Makes a chromatic pcset (mod 12). Alias for make12.
    
    :param args: Integers that represent pitch classes
    :return: A pcset

.. py:function:: make24(*args)
    
    Makes a microtonal pcset (mod 24)

    :param args: Integers that represent pitch classes
    :return: A pcset

.. py:function:: make_pcset24(*args)
    
    Makes a microtonal pcset (mod 24). Alias for make24.

    :param args: Integers that represent pitch classes
    :return: A pcset


.. py:function:: make_subset_graph(set_class, smallest_cardinality=1, show_graph=False, size=(800, 1100))
    
    Makes a subset graph
    
    :param set_class: A set-class
    :param smallest_cardinality: The smallest cardinality to include in the graph
    :param show_graph: Whether or not to generate a visualization of the graph
    :param size: The size of the visualized graph
    :return: A graph

.. py:function:: multiply(pcset: set, n: int)
    
    Multiplies a pcset
    
    :param pcset: The pcset
    :param n: The multiplier
    :return: The multiplied pcset
    *Compatible with all PitchClass modulos

.. py:function:: partitions2(pcset: set)
    
    Gets all partitions of a pcset (size 2 or 1)
    
    :param pcset: A pcset
    :return: A list of all partitions
    *Compatible with all PitchClass modulos

.. py:function:: permutations(pcset: set)
    
    Generates all permutations of a pcset. Uses a swapping notion derived from the Bauer-Mengelberg/Ferentz algorithm
    for generating all-interval twelve-tone rows.
    Note: The number of permutations will be n! where n is the length of the pcset. The amount of pcsegs is therefore
    O(n!). You may not want to try generating all permutations of a twelve-note set.
    You have been warned.
    
    :param pcs: A pcset
    :return: A list of pcsegs
    *Compatible with all PitchClass modulos

.. py:function:: set_class_filter12(name: str, sets: list)
    
    Filters a list of pcsets
    
    :param name: The name to find
    :param sets: A list of sets to filter
    :return: A filtered list
    *Compatible with all PitchClass modulos. For pcsets of modulo 12, also supports Forte and Morris names.

.. py:function:: subsets(pcset: set)
    
    Gets all subsets of a pcset
    
    :param pcset: A pcset
    :return: A list containing all subsets of the pcset
    
.. py:function:: transform(pcset, string)
    
    Transforms a pcset with a provided transformation string
    - Tn: transpose
    - I: invert
    - Mn: multiply
    
    :param pcset: The pcset to transform
    :param string: The transformation string
    :return: The transformed pcset

.. py:function:: transpose(pcset: set, n: int)
    
    Transposes a pcset
    
    :param pcset: The pcset
    :param n: The index of transposition
    :return: The transposed pcset
    *Compatible with all PitchClass modulos

.. py:function:: transpositional_combination(pcset1: set, pcset2: set)
    
    Transpositionally combines (TC) two pcsets. This is Boulez's "multiplication."
    
    :param pcset1: A pcset
    :param pcset2: A pcset
    :return: The TC pcset
    *Compatible with all PitchClass modulos

.. py:function:: visualize(pcset: set)
    
    Visualizes a pcset
    
    :param pcset: A pcset
    :return: A visualization
    *Compatible with all PitchClass modulos
