pctheory.set_complex
################

.. py:function:: assert_k(s, t)
    
    Asserts that s and t are in a K-relationship
    Source: Morris, "Class Notes for Atonal Music Theory," p. 49
    
    :param s: A set-class
    :param t: A set-class
    :return: A boolean
    
.. py:function:: assert_kh(s, t)
    
    Asserts that s and t are in a Kh-relationship
    Source: Morris, "Class Notes for Atonal Music Theory," p. 49
    
    :param s: A set-class
    :param t: A set-class
    :return: A boolean

.. py:function:: get_k12(nexus: pcset.SetClass)
    
    Gets a K-complex about a provided nexus set
    
    :param nexus: A nexus set
    :return: The K-complex
    *Only compatible with mod 12

.. py:function:: get_kh12(nexus: pcset.SetClass)
    
    Gets a Kh-complex about a provided nexus set
    
    :param nexus: A nexus set
    :return: The Kh-complex
    *Only compatible with mod 12
