pctheory.pitch
################

.. py:class:: PitchClass

    Represents a pitch-class

    .. py:property:: mod

        The pitch-class modulo

    .. py:property:: pc

        The pitch-class, as an integer

    .. py:property:: pc_str

        The pitch-class, as a string

    .. py:method:: __init__(self, pc: int=0, mod: int=12)
        
        Creates a PitchClass
        
        :param pc: The pitch class integer
        :param mod: The mod number (12 for default chromatic pitch-classes, 
        24 for quarter-tone pitch-classes)

    .. py:method:: __add__(self, other)

        Adds a ``PitchClass`` or integer to this ``PitchClass``.

        :param other: The other item to add
        :return: A new ``PitchClass``

    .. py:method:: __eq__(self, other)

        Compares two ``PitchClass``es for equality.

        :param other: The other ``PitchClass``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __ge__(self, other)

        Determines if this ``PitchClass`` is greater than or equal to another ``PitchClass``.

        :param other: The other ``PitchClass``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __gt__(self, other)

        Determines if this ``PitchClass`` is greater than another ``PitchClass``.

        :param other: The other ``PitchClass``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __hash__(self)

        Gets the hash value of this ``PitchClass``.

        :return: The hash value

    .. py:method:: __le__(self, other)

        Determines if this ``PitchClass`` is less than or equal to another ``PitchClass``.

        :param other: The other ``PitchClass``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __lt__(self, other)

        Determines if this ``PitchClass`` is less than  another ``PitchClass``.

        :param other: The other ``PitchClass``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __mul__(self, other)

        Multiplies a ``PitchClass`` or integer by this ``PitchClass``.

        :param other: The item to multiply by
        :return: A new ``PitchClass``

    .. py:method:: __ne__(self, other)

        Compares two ``PitchClass``es for equality.

        :param other: The other ``PitchClass``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __repr__(self)

        Gets a representation of this ``PitchClass``.

        :return: A representation

    .. py:method:: __str__(self)

        Gets a representation of this ``PitchClass``.

        :return: A representation

    .. py:method:: __sub__(self, other)

        Subtracts a ``PitchClass`` or integer from this ``PitchClass``.

        :param other: The item to subtract
        :return: A new ``PitchClass``

.. py:class:: Pitch(PitchClass)

        Represents a pitch

    .. py:property:: p

        The pitch number

    .. py:property:: pname

        The pitch name

    .. py:property:: midi

        The MIDI number

    .. py:method:: __init__(self, p: int=0, pc_mod: int=12, pname: str=0)
        
        Creates a Pitch
        
        :param p: The pitch integer
        :param pc_mod: The modulo for the underlying PitchClass
        :param pname: The pitch name as a string (optional, for display purposes)

    .. py:method:: __add__(self, other)

        Adds a ``Pitch`` or integer to this ``Pitch``.

        :param other: The other item to add
        :return: A new ``Pitch``

    .. py:method:: __eq__(self, other)

        Compares two ``Pitch``es for equality.

        :param other: The other ``Pitch``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __ge__(self, other)

        Determines if this ``Pitch`` is greater than or equal to another ``Pitch``.

        :param other: The other ``Pitch``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __gt__(self, other)

        Determines if this ``Pitch`` is greater than another ``Pitch``.

        :param other: The other ``Pitch``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __hash__(self)

        Gets the hash value of this ``Pitch``.

        :return: The hash value

    .. py:method:: __le__(self, other)

        Determines if this ``Pitch`` is less than or equal to another ``Pitch``.

        :param other: The other ``Pitch``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __lt__(self, other)

        Determines if this ``Pitch`` is less than  another ``Pitch``.

        :param other: The other ``Pitch``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __mul__(self, other)

        Multiplies a ``Pitch`` or integer by this ``Pitch``.

        :param other: The item to multiply by
        :return: A new ``Pitch``

    .. py:method:: __ne__(self, other)

        Compares two ``Pitch``es for equality.

        :param other: The other ``Pitch``
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __repr__(self)

        Gets a representation of this ``Pitch``.

        :return: A representation

    .. py:method:: __str__(self)

        Gets a representation of this ``Pitch``.

        :return: A representation

    .. py:method:: __sub__(self, other)

        Subtracts a ``Pitch`` or integer from this ``Pitch``.

        :param other: The item to subtract
        :return: A new ``Pitch``
