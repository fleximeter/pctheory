pctheory.transformations
################

.. py:class:: OTO

    Represents an ordered tone operator. Originally called a "row operator" or "RO" by Morris, it has been renamed here because this class is also used with mod 24 ordered pitch successions ("pitch segments").
    Objects of this class are subscriptable. [0] is the index of transposition. [1] is whether or not to retrograde (0-no or 1-yes). 
    [2] is the multiplier. Multiplication is performed first, then retrograding, then transposition. The point at which retrogradation occurs does not affect the final result. 
    These operators can be used with pcsegs.
    
    .. py:property:: oto
        
        Gets the ``OTO`` as a tuple. Index 0 is the index of transposition, index 1 is whether or not to retrograde, and
        index 2 is the multiplier.

    .. py:method:: __init__(self, T=0, R=False, M=1)
        
        Creates an ``OTO``.
        
        :param int T: The index of transposition. Alternately, the OTO may be provided as a transformation string (e.g. "T5I").
        :param int R: Whether or not to retrograde
        :param int M: The multiplier
        
    .. py:method:: __eq__(self, other)

        Compares this ``OTO`` with another ``OTO`` for equality.

        :param OTO other: The other ``OTO``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __ge__(self, other)

        Determines if this ``OTO`` is greater than or equal to another ``OTO``.

        :param OTO other: The other ``OTO``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __gt__(self, other)

        Determines if this ``OTO`` is greater than another ``OTO``.

        :param OTO other: The other ``OTO``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __hash__(self)

        Gets the hash value of this ``OTO``.

        :return: The hash value

    .. py:method:: __le__(self, other)

        Determines if this ``OTO`` is less than or equal to another ``OTO``.

        :param OTO other: The other ``OTO``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __lt__(self, other)

        Determines if this ``OTO`` is less than another ``OTO``.

        :param OTO other: The other ``OTO``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __ne__(self, other)

        Compares this ``OTO`` with another ``OTO`` for inequality.

        :param OTO other: The other ``OTO``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __repr__(self)

        Gets a representation of this ``OTO``.

        :return: A representation

    .. py:method:: __str__(self)

        Gets a representation of this ``OTO``.

        :return: A representation
    
    .. py:method:: transform(self, item)
        
        Transforms an item (can be a pitch-class, list, set, or any number of nestings of these objects).
        
        :param item: An item
        :return: The transformed item

    .. py:method:: __call__(self, item)
        
        Same as OTO.transform().

        :param item: An item
        :return: The transformed item

.. py:class:: UTO

    Represents an unordered tone operator. This is a bijective mapping A -> B. Originally called a "twelve-tone operator" or "TTO" by Morris, it has been renamed here because this class is also used with mod 24 sets.
    Objects of this class are subscriptable. [0] is the index of transposition. [1] is the multiplier. Multiplication is performed first, then transposition.

    .. py:property:: uto

        Gets the UTO as a list.

    .. py:method:: __init__(self, T=0, M=1)
        
        Creates a UTO
        
        :param int T: The index of transposition. Alternately, the UTO may be provided as a transformation string (e.g. "T5I").
        :param int M: The index of multiplication
        
    .. py:method:: __eq__(self, other)

        Compares two UTOs for equality.
        
        :param UTO other: The other ``UTO``
        :returns: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __ge__(self, other)

        Determines if this ``UTO`` is greater than or equal to another ``UTO``.
        
        :param UTO other: The other ``UTO``
        :returns: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __gt__(self, other)

        Determines if this ``UTO`` is greater than another ``UTO``.
        
        :param UTO other: The other ``UTO``
        :returns: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __hash__(self)

        Gets the hash value of this ``UTO``.

        :returns: The hash value

    .. py:method:: __le__(self, other)

        Determines if this ``UTO`` is less than or equal to another ``UTO``.
        
        :param UTO other: The other ``UTO``
        :returns: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __lt__(self, other)

        Determines if this ``UTO`` is less than another ``UTO``.
        
        :param UTO other: The other ``UTO``
        :returns: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __ne__(self, other)

        Compares two UTOs for inequality.
        
        :param UTO other: The other ``UTO``
        :returns: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __repr__(self)

        Gets a representation of this ``UTO``.

        :return: A representation

    .. py:method:: __str__(self)

        Gets a representation of this ``UTO``.

        :return: A representation

    .. py:method:: cycles(self, mod: int = 12)
        
        Gets the cycles of the ``UTO``.
        
        :param int mod: The number of possible pcs in the system.
        :return: The cycles, as a list of lists
        :return: list

    .. py:method:: inverse(self, mod: int = 12)
        
        Gets the inverse of the ``UTO``.
        
        :param int mod: The number of possible pcs in the system.
        :return: The inverse
        :rtype: UTO

    .. py:method:: transform(self, item)
        
        Transforms a pcset, pcseg, or pc.
        
        :param item: A pcset, pcseg, or pc
        :return: The transformed item

    .. py:method:: __call__(self, item)
        
        Same as UTO.transform().
        
        :param item: A pcset, pcseg, or pc
        :return: The transformed item

.. py:function:: find_otos(pcseg1: list, pcseg2: list)
    
    Gets all OTO transformations of pcseg1 that contain pcseg2 as an ordered subseg.
    
    :param pcseg1: A pcseg
    :param pcseg2: A pcseg
    :return: A set of OTOs that transform pcseg1 so that it contains pcseg2.
    *Compatible with PitchClasses mod 12 and 24

.. py:function:: find_utos(pcset1: set, pcset2: set)
    
    Finds the UTOS that transform pcset1 so it contains pcset2. pcset2 can be a subset of pcset1.
    
    :param pcset1: A pcset
    :param pcset2: A pcset
    :return: A list of UTOS

.. py:function:: get_otos12()
    
    Gets chromatic OTOs (ROs).
    
    :return: A list of OTOs
    :rtype: list

.. py:function:: get_otos24()
    
    Gets microtonal OTOs.
    
    :return: A list of microtonal OTOs
    :rtype: list

.. py:function:: get_utos12()
    
    Gets the twelve-tone UTOs (TTOs).
    
    :return: A dictionary of UTOs
    :rtype: dict

.. py:function:: get_utos24()
    
    Gets the 24-tone UTOs (24TOs).
    
    :return: A dictionary of UTOs
    :rtype: dict

.. py:function:: left_multiply_utos(*args, mod: int = 12)
    
    Left-multiplies a list of UTOs.

    :param args: A collection of UTOs (can be one argument as a list, or multiple UTOs separated by commas. The highest index is evaluated first, and the lowest index is evaluated last.)
    :param int mod: The number of pcs in the system
    :return: The result
    :rtype: UTO

.. py:function:: make_uto_list(*args)
    
    Makes a UTO list.
    
    :param args: One or more tuples or lists representing UTOs
    :return: A UTO list
    :rtype: list
