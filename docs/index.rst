.. ``pctheory`` documentation master file, created by
   sphinx-quickstart on Mon Jul 15 12:34:14 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pctheory documentation
======================

Introduction
------------
``pctheory`` is a Python module for working with atonal theory. It has classes that model chromatic pitch-classes, microtonal pitch-classes, pitches, and transformations. To make collections, you use standard Python objects, including list, set, and tuple types.

To distinguish chromatic and microtonal pitches and pitch-classes, the term “chromatic system” is used to refer to aspects of atonal theory that apply to twelve‐note equal‐temperament. The term “microtonal system” refers to aspects of atonal theory that apply to twenty‐four‐note equal‐temperament. The term “twelve‐tone system” refers specifically to Arnold Schoenberg's technique of using ordered twelve‐note aggregates; a completely different concept.

Any scale, chord, or other collection of pitches or pitch-classes can be modeled as a mathematical set, called a pitch-class set (pcset) or pitch set (pset). An ordered succession of pitches or pitch-classes is called a pitch-class segment (pcseg) or pitch segment (pseg). A partially-ordered set (poset) is (for the purposes of this module) an ordered succession of sets, lists, and/or individual pitches/pitch-classes. Any melody or musical line can be modeled as a pseg, or more abstractly as a pcseg, while chords can be modeled as either psegs, pcsegs, psets, or pcsets depending on which makes the most sense in any given situation.

Uses of pctheory
----------------
``pctheory`` is a general-purpose platform for the use of atonal theory. There is, of course, no requirement that the music be atonal. Many of the features implemented in ``pctheory`` can be readily used in a tonal or quasi-tonal context. ``pctheory`` makes it easy to manipulate complex chords (whether “tonal”‐sounding or not), determine relationships between different kinds of chords or pitch-class collections, and perform many calculations quickly and accurately. For example, ``pctheory`` allows you to easily create and use rotational arrays (as used in Stravinsky's music). This could be useful for both composition and analysis. One interesting feature of ``pctheory`` is its inclusion of tools for working with pitch directly, rather than through the abstraction of pitch-class. This is applicable to music that uses fixed-pitch formations.

Because ``pctheory`` is a Python module, it is easy to write simple programs in Python to investigate pitch, pitch-class, and operator relations. If you want to generate all pentachordal set-classes and select only those that contain ic3, you can write a short program that uses ``pctheory`` to do this for you. If you want to study all of the subset-classes of a set-class, it is easy to generate them with pctheory. If you want to generate several different invariance matrices, this can be easily done. There is no need to work it out on paper. If you want to transform an array, ``pctheory`` can do that with a single method call. Perhaps you want to study all of the pcsets in a set-class. They can be generated with a single method call as well. If you need to know Elliott Carter's number for a particular chromatic chord, that functionality is part of the SetClass12 class, so there is no need to open a reference book. The same goes for standard properties like Forte names and ic vectors.

Prerequisites
-------------
``pctheory`` requires Python 3.10 or newer, as well as the additional modules ``networkx``, ``numpy``, ``pyvis``, and ``regex``.

Installation
------------
``pctheory`` is a Python package and can be installed with the command

.. code-block:: console

    (.venv) $ pip install pctheory

Copyright and license
---------------------
``pctheory`` is copyright © 2022 by Jeffrey Martin. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. To view the GNU General Public License v.3.0, visit https://www.gnu.org/licenses/gpl-3.0.en.html.

Further reading
---------------
Following is a list of books and articles that provide helpful background for pctheory. ``pctheory`` uses terms and conventions from Robert Morris's work.

Eckardt, Jason. “Surface Elaboration of Pitch-Class Sets Using Nonpitched Musical Dimensions.” *Perspectives of New Music* 43 no. 1 (Winter, 2005), 120-140.

Forte, Allen. *The Structure of Atonal Music*. New Haven: Yale University Press, 1973.

Link, John. “Harmony in Elliott Carter's Late Music.” *Music Theory Online* 25 no. 1 (April, 2019).

Mead, Andrew. *An Introduction to the Music of Milton Babbitt*. Princeton: Princeton University Press, 1994.

Morris, Robert D. *Class Notes for Advanced Atonal Music Theory*. 2 volumes. Lebanon, NH: Frog Peak Music, 2001.

Morris, Robert D. *Class Notes for Atonal Music Theory*. Lebanon, NH: Frog Peak Music, 1991.

Morris, Robert D. *Composition With Pitch Classes: A Theory of Compositional Design*. New Haven: Yale University Press, 1987.

Nauert, Paul. “Field Notes: A Study of Fixed-Pitch Formations.” *Perspectives of New Music* 41 no. 1 (Winter, 2003), 180-239.

Scott, Damon, and Eric J. Isaacson. “The Interval Angle: A Similarity Measure for Pitch-Class Sets.” *Perspectives of New Music* 36 no. 2 (Summer, 1998), 107-142.

Straus, Joseph. *Introduction to Post-Tonal Theory*. Fourth edition. New York: W. W. Norton and Co., 2016.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   contour
   group
   pcarray
   pcseg
   pcset
   pitch
   pseg
   pset
   set_complex
   tables
   transformations
   util
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
