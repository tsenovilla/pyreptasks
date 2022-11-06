# These tests are designed to proof that the Switch class acts at it is attended.

# Import of the switch class

from pyreptasks.switch import Switch


# Definition of some simple functions to be called during the tests.
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def hello_world():
    return "Hello world!"

###################################################################################################
# Correct performance tests
###################################################################################################

# FIRST SWITCH. It will take 4 integer options [1,2,3,4] and the 4 functions defined
# above. If the switch choice is out of [1,2,3,4] it will returns the string "default case accessed".

my_switch_1 = Switch([1,2,3,4],[add,sub,mul,hello_world],use_default_case=True,default_case="default case accessed")

# Test 1: Good performance, the switch returns exactly what expected.

def test_1():
    assert my_switch_1.exec(1)(3,4) == 7 # 3+4 = 7
    assert my_switch_1.exec(2)(3,4) == -1 #3-4 = -1
    assert my_switch_1.exec(3)(3,4) == 12 #3*4 = 12
    assert my_switch_1.exec(4)() == "Hello world!" #Execution of hello_world function
    assert my_switch_1.exec(32433323239424) == "default case accessed" #Otherwise, default case

# Test 2: The defined switch is integer (argument by default), so if it try to execute the switch
# with a non-integer argument, it will raise a ValueError.
def test_2():
    try:
        my_switch_1.exec("Test")
    except ValueError:
        pass

# SECOND SWITCH. Similar to the first one but this time the keys are not restricted to be 
# integers. Also, there is not a default case

my_switch_2  = Switch(["add","sub",4.89,6],[add,sub,mul,hello_world],integer_switch=False)

# Test 3: Same idea of test 1 but without using integer keys

def test_3():
    assert my_switch_2.exec("add")(3,4) == 7 # 3+4 = 7
    assert my_switch_2.exec("sub")(3,4) == -1 #3-4 = -1
    assert my_switch_2.exec(4.89)(3,4) == 12 #3*4 = 12
    assert my_switch_2.exec(6)() == "Hello world!" #Execution of hello_world function
    assert my_switch_2.exec(32433323239424) == None #There is not a default case

# Test 4: Now, if we exec the switch using "Test" as key there is not any error, due to the 
# switch is not integer. 
def test_4():
    my_switch_2.exec("Test")

###################################################################################################
# CONSTRUCTOR ERRORS. Tests of how the class constructor throw exceptions if the arguments
# are not well passed.
###################################################################################################

# Test 5: The constructor does not receive the 2 mandatory arguments -> TypeError

def test_5():
    try:
        Switch([1,2],integer_switch=False)
    except TypeError:
        pass

# Test 6: The switch's keys are not a list -> ValueError

def test_6():
    try:
        Switch(3,[1,2])
    except ValueError:
        pass

# Test 7: The switch's actions are not a list -> ValueError

def test_7():
    try:
        Switch([1,2],3)
    except ValueError:
        pass

# Test 8: The lengths of keys and actions lists are different -> ValueError

def test_8():
    try:
        Switch([3],[1,2])
    except ValueError:
        pass

# Test 9: The optional argument use_default_case is not a boolean -> ValueError

def test_9():
    try:
        Switch([3,4],[add,hello_world],use_default_case=54)
    except ValueError:
        pass


# Test 10: The optional argument integer_switch is not a boolean -> ValueError

def test_10():
    try:
        Switch([hello_world,3],[1,2],integer_switch="False")
    except ValueError:
        pass


