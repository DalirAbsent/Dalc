from math import comb, dist, erf, erfc, factorial, gamma, isqrt, lgamma, perm, ulp
from statistics import multimode, mode
from numpy.random import randint, rand, seed
from numpy import (
        abs, absolute, add, all, allclose, amax, amin, any, arange,
        arccos, arccosh, arcsin, arcsinh, arctan, arctan2, arctanh,
        argmax, argmin, argsort, argwhere, around, array, array_equal,
        array_equiv, busday_count, busday_offset, busdaycalendar, cbrt,
        ceil, clip, compress, concatenate, copysign, correlate, cos, cosh,
        count_nonzero, cumprod, cumsum, deg2rad, degrees, diagonal, divide,
        divmod, dot, e, empty, empty_like, equal, euler_gamma, exp, exp2,
        expm1, fabs, floor, floor_divide, fmax, fmin, fmod, format_float_scientific,
        frexp, fromstring, full, full_like, gcd, geomspace, greater, greater_equal,
        heaviside, hypot, identity, inf, inner, is_busday, isclose, isfinite, isinf,
        isnan, isnat, isscalar, lcm, ldexp, less, less_equal, linspace, log, log10,
        log1p, log2, logaddexp, logaddexp2, logical_and, logical_not, logical_or,
        logical_xor, matrix, max, mean, median, min, mod, modf, moveaxis, multiply,
        nan, ndim, negative, nextafter, nonzero, not_equal, ones, ones_like, outer, pi,
        power, prod, positive, ptp, put, putmask, rad2deg, radians, ravel, remainder,
        repeat, reshape, resize, rint, roll, rollaxis, round, searchsorted, shape,
        sign, sin, sinh, size, sort, spacing, sqrt, square, stack, std, subtract,
        sum, swapaxes, take, tan, tanh, trace, transpose, trunc, var, where, zeros, zeros_like
        )


# Mathematical constants
constants: dict = {
                'e': e,
                'euler_gamma': euler_gamma,
                'inf': inf,
                'nan': nan,
                'pi': pi
                }


# Mathematical functions
functions: dict = {
                'abs': abs,
                'absolute': absolute,
                'add': add,
                'all': all,
                'allclose': allclose,
                'amax': amax,
                'amin': amin,
                'any': any,
                'arange': arange,
                'arccos': arccos,
                'arccosh': arccosh,
                'arcsin': arcsin,
                'arcsinh': arcsinh,
                'arctan': arctan,
                'arctan2': arctan2,
                'arctanh': arctanh,
                'argmax': argmax,
                'argmin': argmin,
                'argsort': argsort,
                'argwhere': argwhere,
                'around': around,
                'array': array,
                'array_equal': array_equal,
                'array_equiv': array_equiv,
                'busday_count': busday_count,
                'busday_offset': busday_offset,
                'busdaycalendar': busdaycalendar,
                'cbrt': cbrt,
                'ceil': ceil,
                'clip': clip,
                'comb': comb,
                'compress': compress,
                'concatenate': concatenate,
                'copysign': copysign,
                'correlate': correlate,
                'cos': cos,
                'cosh': cosh,
                'count_nonzero': count_nonzero,
                'cumprod': cumprod,
                'cumsum': cumsum,
                'deg2rad': deg2rad,
                'degrees': degrees,
                'diagonal': diagonal,
                'dist': dist,
                'divide': divide,
                'divmod': divmod,
                'dot': dot,
                'empty': empty,
                'empty_like': empty_like,
                'equal': equal,
                'erf': erf,
                'erfc': erfc,
                'exp': exp,
                'exp2': exp2,
                'expm1': expm1,
                'fabs': fabs,
                'factorial': factorial,
                'floor': floor,
                'floor_divide': floor_divide,
                'fmax': fmax,
                'fmin': fmin,
                'fmod': fmod,
                'format_float_scientific': format_float_scientific,
                'frexp': frexp,
                'fromstring': fromstring,
                'full': full,
                'full_like': full_like,
                'gamma': gamma,
                'gcd': gcd,
                'geomspace': geomspace,
                'greater': greater,
                'greater_equal': greater_equal,
                'heaviside': heaviside,
                'hypot': hypot,
                'identity': identity,
                'inner': inner,
                'is_busday': is_busday,
                'isclose': isclose,
                'isfinite': isfinite,
                'isinf': isinf,
                'isnan': isnan,
                'isnat': isnat,
                'isqrt': isqrt,
                'isscalar': isscalar,
                'lcm': lcm,
                'ldexp': ldexp,
                'less': less,
                'less_equal': less_equal,
                'lgamma': lgamma,
                'linspace': linspace,
                'log': log,
                'log10': log10,
                'log1p': log1p,
                'log2': log2,
                'logaddexp': logaddexp,
                'logaddexp2': logaddexp2,
                'logical_and': logical_and,
                'logical_not': logical_not,
                'logical_or': logical_or,
                'logical_xor': logical_xor,
                'matrix': matrix,
                'max': max,
                'mean': mean,
                'median': median,
                'min': min,
                'mod': mod,
                'mode': mode,
                'modf': modf,
                'moveaxis': moveaxis,
                'multimode': multimode,
                'multiply': multiply,
                'ndim': ndim,
                'negative': negative,
                'nextafter': nextafter,
                'nonzero': nonzero,
                'not_equal': not_equal,
                'ones': ones,
                'ones_like': ones_like,
                'outer': outer,
                'perm': perm,
                'positive': positive,
                'power': power,
                'prod': prod,
                'ptp': ptp,
                'put': put,
                'putmask': putmask,
                'rad2deg': rad2deg,
                'radians': radians,
                'rand': rand,
                'randint': randint,
                'ravel': ravel,
                'remainder': remainder,
                'repeat': repeat,
                'reshape': reshape,
                'resize': resize,
                'rint': rint,
                'roll': roll,
                'rollaxis': rollaxis,
                'round': round,
                'searchsorted': searchsorted,
                'seed': seed,
                'shape': shape,
                'sign': sign,
                'sin': sin,
                'sinh': sinh,
                'size': size,
                'sort': sort,
                'spacing': spacing,
                'sqrt': sqrt,
                'square': square,
                'stack': stack,
                'std': std,
                'subtract': subtract,
                'sum': sum,
                'swapaxes': swapaxes,
                'take': take,
                'tan': tan,
                'tanh': tanh,
                'trace': trace,
                'transpose': transpose,
                'trunc': trunc,
                'ulp': ulp,
                'var': var,
                'where': where,
                'zeros': zeros,
                'zeros_like': zeros_like,
                }


operations: dict = {**constants, **functions}
