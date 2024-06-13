Dalc
A terminal-base calculator

Abilities:
Many mathematical functions and constants like factorial, sinus, pi, e
Creating personal functions
Creating variables
Creating arrays and matrices
Reading equations from file
Writing equations to file
Viewing files
Showing manual of functions
Saving history of inputs
And ...


Mathematical functions and constants:

To include mathematical functions, constants and arrays, Dalc uses "numpy" module for most of them and for a few functions uses "math" and "statistics" modules
This functions and constants are:
{
abs
absolute
add
all
allclose
amax
amin
any
arange
arccos
arccosh
arcsin
arcsinh
arctan
arctan2
arctanh
argmax
argmin
argsort
argwhere
around
array
array_equal
array_equiv
busday_count
busday_offset
busdaycalendar
cbrt
ceil
clip
comb
compress
concatenate
copysign
correlate
cos
cosh
count_nonzero
cumprod
cumsum
deg2rad
degrees
diagonal
dist
divide
divmod
dot
e
empty
empty_like
equal
erf
erfc
euler_gamma
exp
exp2
expm1
fabs
factorial
floor
floor_divide
fmax
fmin
fmod
format_float_scientific
frexp
fromstring
full
full_like
gamma
gcd
geomspace
greater
greater_equal
heaviside
hypot
identity
inf
inner
is_busday
isclose
isfinite
isinf
isnan
isnat
isqrt
isscalar
lcm
ldexp
less
less_equal
lgamma
linspace
log
log10
log1p
log2
logaddexp
logaddexp2
logical_and
logical_not
logical_or
logical_xor
matrix
max
mean
median
min
mod
mode
modf
moveaxis
multimode
multiply
nan
ndim
negative
nextafter
nonzero
not_equal
ones
ones_like
outer
perm
pi
positive
power
prod
ptp
put
putmask
rad2deg
radians
rand
randint
ravel
remainder
repeat
reshape
resize
rint
roll
rollaxis
round
searchsorted
seed
shape
sign
sin
sinh
size
sort
spacing
sqrt
square
stack
std
subtract
sum
swapaxes
take
tan
tanh
trace
transpose
trunc
ulp
var
where
zeros
zeros_like
}

You can use the `help` function to know how to use them. e.g. `help(factorial)`, `help(gamma)`


Creating personal functions:

To create your own function you can use this method:
`your_function_name = lambda input_variable : your_operation`
e.g. `a = lambda x: x*2`, `b = lambda m,n : m+n`

And to use your functions do this:
`your_function_name(input_numbers)`
e.g. `a(3)`, `b(7, 12)`

Note:
* To use your functions, the number of your inputs must match the number of your function inputs. (in the examples ebove, `a` has one input and `b` has two inputs)
* To create several functions, the number of functions must be one (so all of your variables have the same function) or equal to number of variables (so all of your variables have their corresponding function).
This raise an error: `a = lambda x: x+6, lambda y: sin(y)`, `x, y, z = lambda a: a*5, lambda b: b *5 +6`
* Your function names can only include lowercase and uppercase english letters, numbers and underscore("_"). And can't be started with numbers.
* Your function names can't be these names : `clean`, `clear`, `cleax`, `exit`, `help`, `history`, `print`, `quit`, `read`, `reboot`, `reset`, `restart`, `view`, `write`.


Creating variables:

To create a variable you can use this way:
`variable_name = number or operation`
e.g. `r = 7`, `s = sin(20)`
And for use them, use the `variable_name`. (write `r` or `s` in our examples)

To create several variables with one value use this method:
`variable_1, variable_2, variable_3, variable_4 = number or operation`
e.g. `x, y, z = 12`, `a, b, c = radians(90)`

To create several variables with several values use this method:
`variable_1, variable_2, variable_3, variable_4 = number_or_operation_1, number_or_operation_2, number_or_operation_3, number_or_operation_4`
e.g. `a,b,c,d = 4, 15, sin(20), 100`, `m, n = log(20), 9.4`

Note:
* To create several variables, the number of values must be one (so all of your variables have the same value) or equal to number of variables (so all of your variables have their corresponding value). (This raise an error: `a = 3, 5`, `x, y, z = 4, 10`)
* The variable name can only include lowercase and uppercase english letters, numbers and underscore("_"). And can't be started with numbers.
* Your variables names can't be these name : `clean`, `clear`, `cleax`, `exit`, `help`, `history`, `print`, `quit`, `read`, `reboot`, `reset`, `restart`, `view`, `write`.


Reading equations from file:

By This way you can calculate equations from a file:
`read("file_path")`
e.g. `read("equations.txt")`

Note:
* Each line in the file must follow to Dalc rules, like define function and assign to variables.


Writing equations to file:

By This way you can write an equation to a file:
`write(a_equation, "a_file_path")`
e.g. `write(5+6, "test.txt")` `write(cos(80), "file.txt")`

Note
* If the file exists, writes the data in it, otherwise creates the file and then writes the data in it.
* If the file exists and contains contents, removes them and then writes the data in it.


Viewing files:

By This way you can view a text, an equation or a file:
`view("A sample text")`, `view(8*9)`, `view("file.txt")`


Showing manual of functions:

By This way you can see manual of functions:
`help(a_function)`
e.g. `help(tan)`, `help(matrix)`, `help(view)`


Meta commands:

This commands are for:
`clear` ->     Clears the screen.
`exit`, `quit` ->     Prints the user exit text, then exits the program.
`restart`, `reboot`, `reset` -> Restarts the program.
`cleax` ->     Clears the screen, prints the user exit text, then exits the program.
`history` ->     Shows the history.
`clean` ->     Clears the entire history file in `history_path`.


Access to history:

By This way you can access the history:
`!history_number`
e.g. `!25` (This command run the 25th records of the history)
(With `history` command you can see your history)

Note:
* By runnig the program, a file is created as the history file. ("dalc_history.txt")

