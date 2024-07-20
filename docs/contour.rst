pctheory.contour
################

.. py:function:: com(a: int, b: int)

    The COM function for two contour pitches. Returns 1 if a < b, 0 if a == b, -1 if a > b

    :param int a: A contour pitch
    :param int b: A contour pitch
    :return: The comparison result
    :rtype: int

.. py:function:: com_mx(cseg1: list, cseg2: list)

    Generates a COM matrix for two contour segments (ordered contour pitch successions).

    :param list cseg1: A contour segment
    :param list cseg2: A contour segment
    :return: The COM matrix
    :rtype: list

.. py:function:: invert(cseg: list)
    
    Inverts a contour segment

    :param list cseg: The contour segment
    :return: The inverted contour segment
    :rtype: list

.. py:function:: retrograde(cseg: list)

    Retrogrades a contour segment

    :param list cseg: The contour segment
    :return: The retrograded contour segment
    :rtype: list

.. py:function:: rotate(cseg: list, n: int)
    
    Rotates a contour segment

    :param list cseg: The contour segment
    :param int n: The index of rotation
    :return: The rotated contour segment
    :rtype: list

.. py:function:: simplify(cseg: list)

    Simplifies a contour segment

    :param list cseg: A contour segment
    :return: A simplified form of the contour segment
    :rtype: list
