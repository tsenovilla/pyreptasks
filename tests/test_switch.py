# These tests are designed to proof that the Switch class acts at it is attended.

# Import of the switch class

from pyreptasks import Switch


# Definition of some simple functions to be called during the tests.
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def hello_world():
    return "Hello world!"


###################################################################################################
# Correct performance tests
###################################################################################################

# FIRST SWITCH. It will take 4 options [1,2,3,4] and the 4 functions defined
# above. If the switch choice is out of [1,2,3,4] it will returns the string "default case accessed".

my_switch_1 = Switch(
    [1, 2, 3, 4],
    [add, sub, mul, hello_world],
    use_default_case=True,
    default_case="default case accessed",
)

# Test 1: Good performance, the switch returns exactly what is expected.


def test_1():
    assert my_switch_1.exec(1)(3, 4) == 7  # 3+4 = 7
    assert my_switch_1.exec(2)(3, 4) == -1  # 3-4 = -1
    assert my_switch_1.exec(3)(3, 4) == 12  # 3*4 = 12
    assert my_switch_1.exec(4)() == "Hello world!"  # Execution of hello_world function
    assert (
        my_switch_1.exec(32433323239424) == "default case accessed"
    )  # Otherwise, default case


# SECOND SWITCH. Similar to the first one but this time there is not a default case.

my_switch_2 = Switch(["add", "sub", 4.89, 6], [add, sub, mul, hello_world])

# Test 2: Testing the second switch...


def test_2():
    assert my_switch_2.exec("add")(3, 4) == 7  # 3+4 = 7
    assert my_switch_2.exec("sub")(3, 4) == -1  # 3-4 = -1
    assert my_switch_2.exec(4.89)(3, 4) == 12  # 3*4 = 12
    assert my_switch_2.exec(6)() == "Hello world!"  # Execution of hello_world function
    assert my_switch_2.exec(32433323239424) == None  # There is not a default case


###################################################################################################
# CONSTRUCTOR ERRORS. Tests of how the class constructor throw exceptions if the arguments
# are not well passed.
###################################################################################################

# Test 3: The constructor does not receive the 2 mandatory arguments -> TypeError


def test_3():
    try:
        Switch([1, 2], use_default_case=True)
    except TypeError:
        pass


# Test 4: The switch's keys are not a list -> ValueError


def test_4():
    try:
        Switch(3, [1, 2])
    except ValueError:
        pass


# Test 5: The switch's actions are not a list -> ValueError


def test_5():
    try:
        Switch([1, 2], 3)
    except ValueError:
        pass


# Test 6: The lengths of keys and actions lists are different -> ValueError


def test_6():
    try:
        Switch([3], [1, 2])
    except ValueError:
        pass


# Test 7: The optional argument use_default_case is not a boolean -> ValueError


def test_7():
    try:
        Switch([3, 4], [add, hello_world], use_default_case=54)
    except ValueError:
        pass
