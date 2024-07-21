pctheory.util
################

.. py:function:: factor(n)
    
    Factors a positive integer
    
    :param n: An integer
    :returns: A list of factors, in sorted order, including duplicates

.. py:function:: lcm(integers)
    
    Computes the LCM of a list of positive integers
    
    :param integers: A list of positive integers
    :return: The LCM

.. py:function:: map_to_chromatic(scale_map, sequence)
    
    Maps one sequence of items to another sequence of items. This is useful for doing 
    things like mapping scale degrees 0-6 to actual chromatic pitches. You only need
    to provide a map for one octave, and all transpositions will be accounted for.
    
    :param scale_map: The scale map
    :param sequence: The sequence to map
    :return: The mapped sequence

.. py:function:: norgard(n: int)
    
    Generates the first n numbers of OEIS A004718 (Per Nørgård's infinity series)
    
    :param n: The number of terms to compute
    :return: The series
