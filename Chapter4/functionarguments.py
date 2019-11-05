

def fun1(*arg1, arg2, arg3):
    print("fun1 called")
    print(f"arg1={arg1}, arg2={arg2}, arg3={arg3}")


# arg2 and arg3 can only be assigned using keyword arguments.
fun1(0, 1, 2, arg2=1, arg3=2)

try:
    # if arg2 or arg3 is not provided, there is a TypeError since some arguments aren't assigned.
    fun1(0, 1, 2)
except TypeError as e:
    print(f"Bad function call: {e}")


def fun2(arg1, arg2, *, arg3="default", arg4):
    print("fun2 called")
    print(f"arg1={arg1}, arg2={arg2}, arg3={arg3}, arg4={arg4}")


try:
    # all arguments found after a star parameter must be assigned using keyword arguments.
    fun2(0, 1, "non-default", 3)
except TypeError as e:
    print(f"Bad function call: {e}")


def fun3(arg1="default", *arg2, arg3):
    print(f"arg1={arg1}, arg2={arg2}, arg3={arg3}")


try:
    # Optional parameters can appear before a starred parameter.
    # If the starred parameter isn't assigned, it defaults to an empty tuple.
    fun3(arg3=3)
except TypeError as e:
    print(f"Bad function call: {e}")


def fun4(**kwargs):
    print(f"kwargs={kwargs}")


try:
    # The default value for **kwargs parameters is an empty dictionary.
    fun4()

    # **kwargs parameters can be assigned using set of name=value pairs.
    fun4(one=1, two=2, three=3)

    # It is also possible to use the mapping unpacking operator (**) to assign to **kwargs parameters.
    fun4(**{"one": 1, "two": 2})

    # While the above call is possible, this one is not because the keywords are required to be strings.
    fun4(**{1: "one", 2: "two"})
except TypeError as e:
    print(f"Bad function call: {e}")


def fun5(i, arg1=list(range(1, 10))):
    arg1[i] = 0
    print(f"range={arg1}")


# Note that the default values for optional parameters are evaluated once at the time the function is defined.
# Special care should be taken for mutable default values.
# As can be seen the following 3 function calls cause side effects.
fun5(0)
fun5(1)
fun5(2)
