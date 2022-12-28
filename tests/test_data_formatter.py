# These test are designed to proof that the DataFormatter class acts as it is attended.

# Import of the class

from pyreptasks import DataFormatter

# We create the object each time inside the funcionts in order it delete it after each function. We do this basically to avoid weird performances due to we forget there is something already defined.

######################################################
# CORRECT PERFORMANCE TESTS
######################################################

# Test 1: Correct formatting of each field separately


def test_1():
    # We are going to create a DataFormatter object containing the following data and formats:

    # - Name: alphabetic field admitting spaces, the first letter of each name should be capital.
    # - Last Name: alphabetic field admitting spaces, the first letter of each name should be capital.
    # - Short Description: alphabetic field of length at most 50 characters, admitting spaces, dots and commas, the first letter of the field should be capital
    # - Contact number: integer field of lenght exactly 9.
    # - Contact mail: alphanumeric field, admitting @(once),_,.,-
    # - Age: integer field, value must be in the range 18 -> 90
    # - Country: Alphabetic field, upper case for each letter.
    # - City: Alphabetic field, lower case for each letter.
    # - Monthly contribution: float field, not higher than 30.5
    # - Hash: No format

    my_formatter = DataFormatter()
    my_formatter.add_field(
        "Name", style="title", alphabetic_field=True, admitted={" ": True}
    )
    my_formatter.add_field(
        "Last Name", style="title", alphabetic_field=True, admitted={" ": True}
    )
    my_formatter.add_field(
        "Short Description",
        style="capitalize",
        alphabetic_field=True,
        length_range=[0, 50],
        admitted={" ": True, ".": True, ",": True},
    )
    my_formatter.add_field("Contact number", int_field=True, length_range=[9, 9])
    my_formatter.add_field(
        "Contact mail",
        alphanumeric_field=True,
        admitted={"@": 1, "_": True, ".": True, "-": True},
    )
    my_formatter.add_field("Age", int_field=True, value_range=[18, 90])
    my_formatter.add_field(
        "Country", alphabetic_field=True, style="upper", admitted={" ": True}
    )
    my_formatter.add_field(
        "City", alphabetic_field=True, style="lower", admitted={" ": True}
    )
    my_formatter.add_field(
        "Monthly contribution", float_field=True, value_range=[0.0, 30.5]
    )
    my_formatter.add_field("Hash")
    # Tests start here
    assert my_formatter.single_data_to_format("  john   ", "Name") == "John"
    assert (
        my_formatter.single_data_to_format(" rodriguez  pErez", "Last Name")
        == "Rodriguez Perez"
    )
    assert (
        my_formatter.single_data_to_format(
            "hi THIS IS my Description", "Short Description"
        )
        == "Hi this is my description"
    )
    assert (
        my_formatter.single_data_to_format(" 123456789", "Contact number")
        == "123456789"
    )
    assert (
        my_formatter.single_data_to_format(" john_test_mail@gmail.com", "Contact mail")
        == "john_test_mail@gmail.com"
    )
    assert my_formatter.single_data_to_format(" 43 ", "Age") == "43"
    assert (
        my_formatter.single_data_to_format("united kingdom", "Country")
        == "UNITED KINGDOM"
    )
    assert my_formatter.single_data_to_format("London", "City") == "london"
    assert (
        my_formatter.single_data_to_format("12.99", "Monthly contribution") == "12.99"
    )
    assert (
        my_formatter.single_data_to_format("ksncpdcn344nsmdcpecped243m", "Hash")
        == "ksncpdcn344nsmdcpecped243m"
    )  ## Obviously this hash is invented btw


# Test 2: Correct formatting of every fields together


def test_2():
    # We reuse the same formatter used in test_1
    my_formatter = DataFormatter()
    my_formatter.add_field(
        "Name", style="title", alphabetic_field=True, admitted={" ": True}
    )
    my_formatter.add_field(
        "Last Name", style="title", alphabetic_field=True, admitted={" ": True}
    )
    my_formatter.add_field(
        "Short Description",
        style="capitalize",
        alphabetic_field=True,
        length_range=[0, 50],
        admitted={" ": True, ".": True, ",": True},
    )
    my_formatter.add_field("Contact number", int_field=True, length_range=[9, 9])
    my_formatter.add_field(
        "Contact mail",
        alphanumeric_field=True,
        admitted={"@": 1, "_": True, ".": True, "-": True},
    )
    my_formatter.add_field("Age", int_field=True, value_range=[18, 90])
    my_formatter.add_field(
        "Country", alphabetic_field=True, style="upper", admitted={" ": True}
    )
    my_formatter.add_field(
        "City", alphabetic_field=True, style="lower", admitted={" ": True}
    )
    my_formatter.add_field(
        "Monthly contribution", float_field=True, value_range=[0.0, 30.5]
    )
    my_formatter.add_field("Hash")
    # Tests start here
    data = [
        "  john  ",
        " rodriguez pErez",
        "hi THIS  IS my Description",
        "   123456789  ",
        "john_test_mail@gmail.com",
        " 43 ",
        "united kingdom",
        "London",
        "12.99",
        "ksncpdcn344nsmdcpecped243m",
    ]
    assert my_formatter.to_format(data) == [
        "John",
        "Rodriguez Perez",
        "Hi this is my description",
        "123456789",
        "john_test_mail@gmail.com",
        "43",
        "UNITED KINGDOM",
        "london",
        "12.99",
        "ksncpdcn344nsmdcpecped243m",
    ]


# Test 3: Fields modifications working well


def test_3():
    # We reuse the same formatter used in the previous tests
    my_formatter = DataFormatter()
    my_formatter.add_field(
        "Name", style="title", alphabetic_field=True, admitted={" ": True}
    )
    my_formatter.add_field(
        "Last Name", style="title", alphabetic_field=True, admitted={" ": True}
    )
    my_formatter.add_field(
        "Short Description",
        style="capitalize",
        alphabetic_field=True,
        length_range=[0, 50],
        admitted={" ": True, ".": True, ",": True},
    )
    my_formatter.add_field("Contact number", int_field=True, length_range=[9, 9])
    my_formatter.add_field(
        "Contact mail",
        alphanumeric_field=True,
        admitted={"@": 1, "_": True, ".": True, "-": True},
    )
    my_formatter.add_field("Age", int_field=True, value_range=[18, 90])
    my_formatter.add_field(
        "Country", alphabetic_field=True, style="upper", admitted={" ": True}
    )
    my_formatter.add_field(
        "City", alphabetic_field=True, style="lower", admitted={" ": True}
    )
    my_formatter.add_field(
        "Monthly contribution", float_field=True, value_range=[0.0, 30.5]
    )
    my_formatter.add_field("Hash")
    # Tests start here
    assert my_formatter.show_fields() == [
        "Name",
        "Last Name",
        "Short Description",
        "Contact number",
        "Contact mail",
        "Age",
        "Country",
        "City",
        "Monthly contribution",
        "Hash",
    ]  ## Check that the defined fields are actually the ones we added using add_field
    my_formatter.delete_field("Hash")  ## Delete hash field
    assert my_formatter.show_fields() == [
        "Name",
        "Last Name",
        "Short Description",
        "Contact number",
        "Contact mail",
        "Age",
        "Country",
        "City",
        "Monthly contribution",
    ]  ## Check the hash field is well deleted


###################################
# EXCEPTIONS TESTS
###################################

# Now we test that te exceptions are well catched.

# Test 4: add_field method exceptions


def test_4():
    my_formatter = DataFormatter()
    # name type error
    try:
        my_formatter.add_field(34)
    except ValueError:
        pass
    # style type error
    try:
        my_formatter.add_field("Name", style="Capital letters")
    except ValueError:
        pass
    # alphabetic_field type error
    try:
        my_formatter.add_field("Name", alphabetic_field="True")
    except ValueError:
        pass
    # int_field type error
    try:
        my_formatter.add_field("Name", int_field="34")
    except ValueError:
        pass
    # float_field type error
    try:
        my_formatter.add_field("Name", float_field=[True])
    except ValueError:
        pass
    # alphanumeric_field type error
    try:
        my_formatter.add_field("Name", alphanumeric_field=1)
    except ValueError:
        pass
    # Simultaneously alphabetic, integer, float and/or alphanumeric field declaration error

    # List containing all the wrong configurations. There are (4 4)+ (4 3) + (4 2) = 11 possibilities, where (a b) represents the binomial coefficient.
    wrong_configurations = [
        [True, True, True, True],
        [True, True, True, False],
        [True, True, False, True],
        [True, False, True, True],
        [True, True, False, False],
        [True, False, True, False],
        [True, False, False, True],
        [False, True, True, True],
        [False, False, True, True],
        [False, True, False, True],
        [False, True, True, False],
    ]
    errors_encountered = 0
    for configuration in wrong_configurations:
        try:
            my_formatter.add_field(
                "Name",
                alphabetic_field=configuration[0],
                int_field=configuration[1],
                float_field=configuration[2],
                alphanumeric_field=configuration[3],
            )
        except ValueError:
            errors_encountered += 1
    assert (
        errors_encountered == 11
    )  # Check that for each wrong configuration a ValueError exception has been thrown

    try:  # admitted type error
        my_formatter.add_field("Name", alphabetic_field=True, admitted=[" "])
    except ValueError:
        pass
    # admitted only allowed if alphabetic or alphanumeric field
    errors_encountered = 0
    try:
        my_formatter.add_field("Age", int_field=True, admitted={".": True})
    except ValueError:
        errors_encountered += 1
    try:
        my_formatter.add_field(
            "Monthly contribution", float_field=True, admitted={".": True}
        )
    except ValueError:
        errors_encountered += 1
    try:
        my_formatter.add_field("Monthly contribution", admitted={".": True})
    except ValueError:
        errors_encountered += 1
    assert errors_encountered == 3  # Check that the exception is thrown in both cases.

    # admitted containing a non-string key
    try:
        my_formatter.add_field("Name", alphabetic_field=True, admitted={3: 1})
    except ValueError:
        pass
    # admitted containing a string key longer than 1 character
    try:
        my_formatter.add_field("Name", alphabetic_field=True, admitted={" .": 2})
    except ValueError:
        pass
    # admitted containing an entry with not valid value
    try:
        my_formatter.add_field("Name", alphabetic_field=True, admitted={".": "3"})
    except ValueError:
        pass
    # length_range type error
    try:
        my_formatter.add_field("Name", length_range=23)
    except ValueError:
        pass
    # length_range not well-formed error
    try:
        my_formatter.add_field("Name", length_range=[2])
    except ValueError:
        pass
    # value_range type error
    try:
        my_formatter.add_field("Name", int_field=True, value_range=32)
    except ValueError:
        pass

    # value_range declared out of a numeric field
    try:
        my_formatter.add_field("Name", value_range=[0, 2])
    except ValueError:
        pass
    # value_range not well_formed error
    try:
        my_formatter.add_field("Name", int_field=True, value_range=[2])
    except ValueError:
        pass

    # field duplication error
    try:
        my_formatter.add_field("Name")
        my_formatter.add_field("Name")
    except NameError:
        pass


# Test 5: delete_field method exceptions


def test_5():
    my_formatter = DataFormatter()
    # field_name type error
    try:
        my_formatter.delete_field(22)
    except ValueError:
        pass
    # field_name does not match a defined field
    try:
        my_formatter.delete_field("Name")
    except NameError:
        pass


# Test 6: single_data_to_format method exceptions


def test_6():
    my_formatter = DataFormatter()
    # field_name type error
    try:
        my_formatter.single_data_to_format("Name", 23)
    except ValueError:
        pass
    # data type error
    try:
        my_formatter.single_data_to_format(23, "Name")
    except ValueError:
        pass

    # field_name does not match a defined field
    try:
        my_formatter.single_data_to_format("Name", "Name")
    except NameError:
        pass


# Test 7: to_format method exceptions


def test_7():
    my_formatter = DataFormatter()
    # data type error
    try:
        my_formatter.to_format("Name")
    except ValueError:
        pass
    # data length is not equal to the number of defined fields
    try:
        my_formatter.to_format(["Name"])
    except ValueError:
        pass


# Test 8: __alpha_formatter private method exceptions (they would be thrown from a public method)


def test_8():
    my_formatter = DataFormatter()
    my_formatter.add_field("Name", alphabetic_field=True)
    # Input string type error
    try:
        my_formatter.to_format([3])
    except ValueError:
        pass

    # non-alphabetic character introduced + only alphabetic characters admitted
    try:
        my_formatter.to_format(["john doe"])
    except ValueError:
        pass
    my_formatter.delete_field("Name")

    # alphabetic field only contains non-alphabetic characters, but admitted by the configuration
    my_formatter.add_field(
        "email",
        alphabetic_field=True,
        admitted={"@": 1, ".": True, ",": True, "-": True},
    )
    try:
        my_formatter.single_data_to_format("...@.", "email")
    except ValueError:
        pass

    # non-alphabetic character introduced + some special characters allowed
    try:
        my_formatter.to_format(["john.'doe'@gmail.com"])  # the problem is with the '
    except ValueError:
        pass
    my_formatter.delete_field("email")

    # length data does not fit the specifications
    my_formatter.add_field(
        "Name", alphabetic_field=True, length_range=[2, 10], admitted={" ": True}
    )
    counter = 0
    try:
        my_formatter.single_data_to_format("h", "Name")
    except ValueError:
        counter += 1
    try:
        my_formatter.single_data_to_format("hello world", "Name")
    except:
        counter += 1
    assert counter == 2
    assert (
        my_formatter.single_data_to_format("he", "Name") == "he"
        and my_formatter.single_data_to_format("hello worl", "Name") == "hello worl"
    )  # Extreme cases testes
    my_formatter.delete_field("Name")


# Test 9: __int_formatter private method exceptions (they would be thrown from a public method)


def test_9():
    my_formatter = DataFormatter()
    my_formatter.add_field("Age", int_field=True)
    # Input string type error
    try:
        my_formatter.to_format([3])
    except ValueError:
        pass

    # Input string is not convertible to an integer
    try:
        my_formatter.to_format(["hello"])
    except ValueError:
        pass
    my_formatter.delete_field("Age")

    # length data does not fit the specifications
    my_formatter.add_field("Contact number", int_field=True, length_range=[7, 9])
    counter = 0
    try:
        my_formatter.single_data_to_format("123456", "Contact number")
    except ValueError:
        counter += 1
    try:
        my_formatter.single_data_to_format("0123456789", "Contact number")
    except ValueError:
        counter += 1
    assert counter == 2
    assert my_formatter.single_data_to_format(
        "  123456789", "Contact number"
    ) == "123456789" and my_formatter.to_format(["1234567"]) == [
        "1234567"
    ]  ##Extreme cases tested
    my_formatter.delete_field("Contact number")

    # value does not fit the specifications
    my_formatter.add_field("Age", int_field=True, value_range=[18, 90])
    counter = 0
    try:
        my_formatter.to_format(["17"])
    except ValueError:
        counter += 1
    try:
        my_formatter.to_format(["91"])
    except ValueError:
        counter += 1
    assert counter == 2
    assert my_formatter.to_format(["18"]) == ["18"] and my_formatter.to_format(
        ["  90"]
    ) == [
        "90"
    ]  # Extreme cases tested
    my_formatter.delete_field("Age")


# Test 10: __float_formatter private method exceptions (they would be thrown from a public method)


def test_10():
    my_formatter = DataFormatter()
    my_formatter.add_field("Contribution", float_field=True)
    # Input string type error
    try:
        my_formatter.to_format([3])
    except ValueError:
        pass

    # Input string is not convertible to a float
    try:
        my_formatter.to_format(["hello"])
    except ValueError:
        pass
    my_formatter.delete_field("Contribution")

    # length data does not fit the specifications
    my_formatter.add_field("Contribution", float_field=True, length_range=[4, 5])
    counter = 0
    try:
        my_formatter.single_data_to_format("122.10", "Contribution")
    except ValueError:
        counter += 1
    try:
        my_formatter.single_data_to_format("9.9", "Contribution")
    except ValueError:
        counter += 1
    assert counter == 2
    assert (
        my_formatter.single_data_to_format("20", "Contribution") == "20.0"
        and my_formatter.single_data_to_format(" 89.99 ", "Contribution") == "89.99"
    )  # Extreme cases tested
    ##In the previous assert, we used 20 to test the minimum length case (4) but it has length 2! Apparently yes, but the formatter convert it to 20.0, so it is ok to test length 4 :)
    my_formatter.delete_field("Contribution")

    # value does not fit the specifications
    my_formatter.add_field("Contribution", float_field=True, value_range=[19.32, 90.21])
    counter = 0
    try:
        my_formatter.single_data_to_format("90.22", "Contribution")
    except ValueError:
        counter += 1
    try:
        my_formatter.single_data_to_format("19.31", "Contribution")
    except:
        counter += 1
    assert counter == 2
    assert (
        my_formatter.single_data_to_format("90.21", "Contribution") == "90.21"
        and my_formatter.single_data_to_format("19.32", "Contribution") == "19.32"
    )  # Extreme cases tested
    my_formatter.delete_field("Contribution")


# Test 11: __alphanum_formatter private method exceptions (they would be thrown from a public method)


def test_11():
    my_formatter = DataFormatter()
    my_formatter.add_field("email", alphanumeric_field=True)
    # Input string type error
    try:
        my_formatter.to_format([3])
    except ValueError:
        pass

    # non-alphanumeric character introduced + only alphabetic characters admitted
    try:
        my_formatter.to_format(["john doe3"])
    except ValueError:
        pass
    my_formatter.delete_field("email")

    # alphanumeric field only contains non-alphanumeric characters, but admitted by the configuration
    my_formatter.add_field(
        "email",
        alphanumeric_field=True,
        admitted={"@": 1, ".": True, ",": True, "-": True},
    )
    try:
        my_formatter.single_data_to_format("...@.", "email")
    except ValueError:
        pass

    # non-alphanumeric character introduced + some special characters allowed
    try:
        my_formatter.to_format(["john'-doe3'@gmail.com"])
    except ValueError:
        pass
    my_formatter.delete_field("email")

    # length data does not fit the specifications
    my_formatter.add_field(
        "Name", alphanumeric_field=True, length_range=[2, 10], admitted={" ": True}
    )
    counter = 0
    try:
        my_formatter.single_data_to_format("h", "Name")
    except ValueError:
        counter += 1
    try:
        my_formatter.single_data_to_format("hello world", "Name")
    except:
        counter += 1
    assert counter == 2
    assert (
        my_formatter.single_data_to_format("he", "Name") == "he"
        and my_formatter.single_data_to_format("hello worl", "Name") == "hello worl"
    )  # Extreme cases testes
    my_formatter.delete_field("Name")


# Test 12: __default_formatter private method exceptions (they would be thrown from a public method)


def test_12():
    my_formatter = DataFormatter()
    my_formatter.add_field("Name")
    # Input string type error
    try:
        my_formatter.to_format([3])
    except ValueError:
        pass
    my_formatter.delete_field("Name")

    # length data does not fit the specifications
    my_formatter.add_field("Name", length_range=[2, 10])
    counter = 0
    try:
        my_formatter.single_data_to_format("h", "Name")
    except ValueError:
        counter += 1
    try:
        my_formatter.single_data_to_format("hello world", "Name")
    except:
        counter += 1
    assert counter == 2
    assert (
        my_formatter.single_data_to_format("he", "Name") == "he"
        and my_formatter.single_data_to_format("hello worl", "Name") == "hello worl"
    )  # Extreme cases testes
    my_formatter.delete_field("Name")


# Test 13: __remove_admitted private method exceptions (they would be thrown from a public method)
def test_13():
    my_formatter = DataFormatter()
    # An admitted character appears in the input, but it overtake the allowed amount
    my_formatter.add_field(
        "email",
        alphanumeric_field=True,
        admitted={"@": 1, ".": True, ",": True, "-": True},
    )
    try:
        my_formatter.to_format(["john.doe3@@gmail.com"])
    except ValueError:
        pass
    my_formatter.delete_field("email")


## The private method __string_cleaner does not need specific tests because it has been used several times above.
