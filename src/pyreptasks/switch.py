# Class Switch: Defines a switch that may be executed as many times as needed.
class Switch:
    """
    This class creates a switch structure in Python. It may be configured to manage a default case if necessary.

    An object of type Switch must be declared using at least two arguments: the key values for the switch and the actions to perform.
    Both arguments must be lists of the same length. REMARK: The orders of the lists are important, the first key will execute the first action,
    the second key will execute the second action, and so on.

    There are also two optional arguments that may be provided when creating the object:

     - use_default_case: <class 'bool'>. Used to determine if a default case is necessary for the switch. By default its value is False.
     - default_case: The action to perform in the default case if use_default_case == True.

    ATTRIBUTES:

     - options: A dictionary containing the pairs keys/values.
     - use_default_case: A boolean used to indicate if an action should be performed in a default case.
     - default_case: If use_default_case == True, the action to perform in the default case.

    METHODS:

     - exec: This method takes the desired choice as argument and returns the corresponding switch value.
    """

    def __init__(
        self,
        keys: list,
        actions: list,
        use_default_case: bool = False,
        default_case=None,
    ) -> None:
        # Check that the type of the arguments are correct.
        if keys.__class__ != list:
            raise ValueError("switch keys must be specified using a list.")
        if actions.__class__ != list:
            raise ValueError("switch actions must be specified using a list.")
        if use_default_case.__class__ != bool:
            raise ValueError(
                "set use_default_case = True if you are interested in using a default case for the switch."
            )
        # Check that there are as much actions as keys for the switch.
        if len(keys) != len(actions):
            raise ValueError(
                "the length of the list of keys and actions must be the same."
            )
        # Definition of the object attributes.
        self.options = dict.fromkeys(keys)
        for i in range(len(actions)):
            self.options[list(self.options.keys())[i]] = actions[i]
        self.use_default_case = use_default_case
        self.default_case = default_case

    def exec(self, choice):
        """
        Returns the selected choice of the switch.
        """
        if self.use_default_case:
            return self.options.get(choice, self.default_case)
        else:
            return self.options.get(choice)
