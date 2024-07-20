pctheory.group
##############

.. py:class:: OperatorGroup

    Represents a group of operators. Only compatible with mod 12 and mod 24 systems.

    .. py:property:: name

        Represents the name of the group, as a ``str``

    .. py:property:: utos

        Gets the set of unordered tone operators (UTOs, traditionally "twelve-tone operators" for mod-12) in the group.

    .. py:method:: __init__(self, utos: list = None, mod: int = 12)

        Creates an ``OperatorGroup``

        :param list utos: A list of operators (traditionally, TTOs) that define the group.
        :param int mod: The number of pitch classes in the system of the group (chromatic: 12, microtonal: 24)

    .. py:method:: __contains__(self, uto: transformations.UTO)

        Overloaded ``in`` to check the presence of a given operator in the group.

        :param UTO uto: An operator
        :return: ``True`` or ``False``
        :rtype: bool

    .. py:method:: __iter__(self)

        Returns an iterator for the group.

        :returns: An iterator

    .. py:method:: __list__(self)

        Converts the group to a ``list``

        :returns: A list of the operators in the group
        :rtype: list

    .. py:method:: __str__(self)

        Returns a string representation of the group names

        :returns: The group name
        :rtype: str

    .. py:method:: __repr__(self)

        Returns a string representation of the group names

        :returns: The group name
        :rtype: str

    .. py:method:: get_orbits(self)

        Gets the orbits of the group

        :return: The orbits, as a list of sets
        :rtype: list

    .. py:method:: left_coset(self, uto)

        Gets a left coset of the group

        :param UTO uto: A UTO
        :return: The left coset
        :rtype: list

    .. py:method:: load_utos(self, utos: list)
        
        Loads UTOs into the group
        :param list utos: UTOs

    .. py:method:: right_coset(self, uto)

        Gets a right coset of the group

        :param UTO uto: A UTO
        :return: The right coset
        :rtype: list

