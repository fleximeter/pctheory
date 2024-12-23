# `pctheory`
`pctheory` is a Python library for using atonal music theory. It is useful for both computer-assisted composition in Python and analysis. Some of the many useful features include:
- Set-classes
    - Generate all abstract subsets of a set-class
    - Get Forte and Carter names for a set-class
    - Work with microtonal sets
    - Generate set-class-complexes
- Rows
    - Generate a twelve-tone matrix
    - Generate a rotational array
    - Generate an invariance matrix
    - Load a random all-interval, all-trichord, ten-trichord, or Babbit ten-trichord row
    
`pctheory` is much more specialized than `music21`, and offers substantially more functionality in atonal theory. Additionally, it does not use `music21` objects, so there is less computational overhead when using `pctheory`. It is not difficult to create `music21` objects from `pctheory` objects, which allows `pctheory` to be used along with `music21`.

## Installation
`pctheory` is a Python package and can be installed with the command `pip install pctheory` from the terminal on your computer (Command Prompt or PowerShell on Windows, Terminal on Linux or macOS). Note that you need Python 3.10 or newer.

If the `pip install` command fails, you will need to build the wheel yourself. Create a virtual environment with the packages `build`, `setuptools`, and `wheel` installed. Then run the command `python -m build` from the root of this repository. The wheel will be found in the `dist/` directory.

## Quick start
There are three Jupyter notebooks in this repository that you can consult to get started with `pctheory`.

## System Requirements
`pctheory` requires Python 3.10 or newer.

## Documentation
Documentation can be found at https://pctheory.readthedocs.io/en/latest/.

## Copyright and license
`pctheory` is copyright © 2024 by Jeffrey Martin. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. To view the GNU General Public License v.3.0, visit https://www.gnu.org/licenses/gpl-3.0.en.html.