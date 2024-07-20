pctheory.pcarray
################

.. py:class:: RotationalArray

    Represents a rotational array

    .. py:property:: array
        
        Gets the rotational array

    .. py:property:: pcseg

        Gets the pcseg

    .. py:method:: __init__(self, pcseg=None)

        Creates a rotational array

        :param pcseg: A pcseg to import

    .. py:method:: __repr__(self)

        Gets a string representation of the ``RotationalArray``

        :returns: The representation
        :rtype: str

    .. py:method:: __str__(self)

        Gets the ``RotationalArray`` as a string

        :returns: The array
        :rtype: str

    .. py:method:: __getitem__(self, i: int, j: int)

        Gets the pc at the specified row and column

        :param int i: The row
        :param int j: The column
        :return: The pc
        :rtype: PitchClass

    .. py:method:: get_column(self, j: int)

        Gets a column of the rotational array

        :param int j: The column index
        :return: The column
        :rtype: list

    .. py:method:: get_row(self, i: int)

        Gets a row of the rotational array

        :param int i: The row index
        :return: The row
        :rtype: list

    .. py:method:: import_pcseg(self, pcseg: list)

        Imports a pcseg

        :param list pcseg: A pcseg

.. py:function:: str_simple_array(array, col_delimiter=" ", row_delimiter="\n")

    Converts an array of pcs to string

    :param array: The array to convert
    :param col_delimiter: The column delimiter
    :param row_delimiter: The row delimiter
    :return: The string
    :rtype: str

.. py:function:: make_array_chain(array, length: int)

    Makes a chain of arrays

    :param array: An array
    :param length: The length
    :param alt_ret: Whether or not to alternately retrograde the arrays.
    :return: A chained array
    :rtype: list
