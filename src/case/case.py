"""A module to allow python to have a 'case' statement (otherwise known
as 'switch')

It is recommended to import this module using:
from case import case
as there are no other functions intended for external use in this
module.

See the docstring for the 'case' function for more infomation.
"""

__version__ = '0.1'
__author__ = 'bright lego'


from typing import Callable, Iterable, Mapping, Tuple, Any


def _validate_expr(expr: bool) -> None:
    """Validates the output of the boolean expression"""

    if not isinstance(expr,bool):
        raise TypeError(f"'{expr}' should be a boolean value or the \
output of a boolean expression")


def _validate_func(func: Callable) -> None:
    """Validates the function"""

    if not callable(func):
        raise TypeError(f"'{func}' should be a function or other callable")


def _validate_args(args: Tuple) -> None:
    """Validates the 'normal' arguments"""

    if not isinstance(args, tuple):
        raise TypeError(f"'{args}' should be a tuple")


def _validate_kwargs(kwargs: Mapping[str, Any]) -> None:
    """Validates the key word arguments"""

    if not isinstance(kwargs, Mapping):
        raise TypeError(f"'{kwargs}' should be a dictionary that maps \
key words to arguments")


def _validate_case(c: Iterable) -> None:
    """Validates a 'line' of case"""

    if not isinstance(c, Iterable):
        raise TypeError(f"'{c}' should be a tuple or other iterable")

    if not 2 <= len(c) <= 4:
        raise ValueError(f"'{c}' should have a length between 2 and 4")



def _seperate_case(c: Tuple[bool, Callable, Tuple, Mapping]) -> Tuple[bool, \
                                            Callable, Tuple, Mapping[str, Any]]:
    """Seperates a single case tuple and outputs the result"""

    expr: bool
    func: Callable
    args: Tuple
    kwargs: Mapping[str, Any]

    args = ()
    kwargs = {}


    expr = c[0]
    func = c[1]

    if len(c) >= 3:
        args = c[2]

    if len(c) == 4:
        kwargs = c[3]

    return expr, func, args, kwargs


def case(*cases: Tuple[bool, Callable, Tuple, Mapping]) -> Any:
    """Acts as a case (or switch) for arbritary functions and an arbrirary
    Number of cases.

    Each element should be:
    (
        output of a boolean expression,
        function name,
        arguments for the function (optional),
        keyword arguments for the function (optional)
    )

    Note: There must be 'normal' arguments (even if it is an empty tuple)
          before the keyword arguments

    For Example:
    from case import case

    a = 2

    case(
        (a == 1, print, ('a is 1')),
        (a == 2, print, ('a is 2','and not 3'), {'sep': ': '}),
        (a == 3, print)
    )

    Output:
    a is 2: and not 3
    """

    expr: bool
    func: Callable
    args: Tuple[Any, ...]
    kwargs: Mapping[str, Any]

    for c in cases:

        _validate_case(c)

        expr, func, args, kwargs = _seperate_case(c)

        _validate_expr(expr)
        _validate_func(func)
        _validate_args(args)
        _validate_kwargs(kwargs)

        if expr:
            return func(*args, **kwargs)
