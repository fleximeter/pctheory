pctheory.pseg
################

.. py:function:: intervals(pseg: list)
    
    Gets the ordered interval content of a pseg
    
    :param pseg: The pseg
    :return: The ordered interval content as a list
    *Compatible with all Pitch modulos

.. py:function:: invert(pseg: list)
    
    Inverts a pseg
    
    :param pseg: The pseg
    :return: The inverted pseg
    *Compatible with all Pitch modulos

.. py:function:: make_pseg12(*args)
    
    Makes a pseg
    
    :param args: Ps
    :return: A pseg
    *Compatible only with chromatic psegs

.. py:function:: make_pseg24(*args)
    
    Makes a pseg
    
    :param args: Ps
    :return: A pseg
    *Compatible only with microtonal psegs

.. py:function:: multiply_order(pseg: list, n: int)
    
    Multiplies a pseg's order
    
    :param pseg: The pseg
    :param n: The multiplier
    :return: The order-multiplied pseg
    *Compatible with all Pitch modulos

.. py:function:: retrograde(pseg: list)
    
    Retrogrades a pseg
    
    :param pseg: The pseg
    :return: The retrograded pseg
    *Compatible with all Pitch modulos

.. py:function:: rotate(pseg: list, n: int)
    
    Rotates a pseg
    
    :param pseg: The pseg
    :param n: The index of rotation
    :return: The rotated pseg
    *Compatible with all Pitch modulos

.. py:function:: to_pcseg(pseg: list)
    
    Makes a pcseg out of a pseg
    
    :param pseg: A pseg
    :return: A pcseg
    *Compatible with all Pitch modulos

.. py:function:: transpose(pseg: list, n: int)
    
    Transposes a pseg

    :param pseg: The pseg
    :param n: The index of transposition
    :return: The transposed pseg
    *Compatible with all Pitch modulos
