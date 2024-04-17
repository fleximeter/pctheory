"""
File: tables.py
Author: Jeff Martin
Date: 10/31/2021

Copyright © 2021 by Jeffrey Martin. All rights reserved.
Email: jmartin@jeffreymartincomposer.com
Website: https://jeffreymartincomposer.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import importlib.resources
import json


def create_tables_all_trichord():
    """
    Creates tables for all-trichord rows
    :return: Tables
    """
    with importlib.resources.open_text("pctheory", "all_trichord.json") as table_json:
        return json.loads(table_json.read())


def create_tables_all_trichord_babbitt():
    """
    Creates tables for all-trichord (Babbitt) rows
    :return: Tables
    """
    with importlib.resources.open_text("pctheory", "babbitt_trichord.json") as table_json:
        return json.loads(table_json.read())


def create_tables_eleven_interval():
    """
    Creates tables for eleven-interval row generators
    :return: Tables
    """
    with importlib.resources.open_text("pctheory", "eleven_interval.json") as table_json:
        return json.loads(table_json.read())


def create_tables_sc12():
    """
    Creates tables for SetClass12 objects
    :return: Tables
    """
    with importlib.resources.open_text("pctheory", "sc12.json") as table_json:
        return json.loads(table_json.read())


def create_tables_ten_trichord():
    """
    Creates tables for ten-trichord rows
    :return: Tables
    """
    with importlib.resources.open_text("pctheory", "ten_trichord.json") as table_json:
        return json.loads(table_json.read())
