pctheory.set_complex
################

.. py:function:: assert_k(s: SetClass, t: SetClass)
    
    Asserts that *s* and *t* are in a K-relationship.
    Source: Morris, "Class Notes for Atonal Music Theory," p. 49
    
    :param SetClass s: A set-class
    :param SetClass t: A set-class
    :return: ``True`` or ``False``
    :rtype: bool
    
.. py:function:: assert_kh(s: SetClass, t: SetClass)
    
    Asserts that *s* and *t* are in a Kh-relationship.
    Source: Morris, "Class Notes for Atonal Music Theory," p. 49
    
    :param SetClass s: A set-class
    :param SetClass t: A set-class
    :return: ``True`` or ``False``
    :rtype: bool

.. py:function:: get_k12(nexus: SetClass)
    
    Gets a K-complex about a provided nexus set.
    
    :param SetClass nexus: A nexus set-class
    :return: The K-complex
    :rtype: list
    *Only compatible with mod 12

.. py:function:: get_kh12(nexus: SetClass)
    
    Gets a Kh-complex about a provided nexus set.
    
    :param SetClass nexus: A nexus set-class
    :return: The Kh-complex
    :rtype: list
    *Only compatible with mod 12
