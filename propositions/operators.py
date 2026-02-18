# This file is part of the materials accompanying the book
# "Mathematical Logic through Python" by Gonczarowski and Nisan,
# Cambridge University Press. Book site: www.LogicThruPython.org
# (c) Yannai A. Gonczarowski and Noam Nisan, 2017-2022
# File name: propositions/operators.py

"""Syntactic conversion of propositional formulas to use only specific sets of
operators."""

from propositions.syntax import *
from propositions.semantics import *


def to_not_and_or(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'``, ``'&'``, and ``'|'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'``, ``'&'``, and
        ``'|'``.
    """
    # Task 3.5

    our_substitution_map = {
        '->': Formula.parse('(~p|q)'),
        '+': Formula.parse('((p&~q)|(~p&q))'),
        '<->': Formula.parse('((p&q)|(~p&~q))'),
        '-&': Formula.parse('~(p&q)'),
        '-|': Formula.parse('~(p|q)'),
        'T': Formula.parse('~(p&~p)'),
        'F': Formula.parse('(p&~p)'),
    }

    return formula.substitute_operators(our_substitution_map)


def to_not_and(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'`` and ``'&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'`` and ``'&'``.
    """
    # Task 3.6a
    based_formula = to_not_and_or(formula)

    need_map_or = {'|': Formula.parse('~(~p&~q)')}

    return based_formula.substitute_operators(need_map_or)


def to_nand(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'-&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'-&'``.
    """
    # Task 3.6b
    not_and_formula = to_not_and(formula)

    need_map_nand = {
        '~': Formula.parse('(p-&p)'),
        '&': Formula.parse('((p-&q)-&(p-&q))'),
    }

    return not_and_formula.substitute_operators(need_map_nand)


def to_implies_not(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'~'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'~'``.
    """
    # Task 3.6c
    based_formula = to_not_and_or(formula)

    need_map_implies = {'|': Formula.parse('(~p->q)'), '&': Formula.parse('~(p->~q)')}

    return based_formula.substitute_operators(need_map_implies)


def to_implies_false(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'F'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'F'``.
    """
    # Task 3.6d
    implies_not_formula = to_implies_not(formula)

    need_map_false = {'~': Formula.parse('(p->F)')}

    return implies_not_formula.substitute_operators(need_map_false)
