# Cabizares_Jr_Ronald_T._Coding-activity-3

1. Conceptual Distinction
  Encapsulation vs. Abstraction
  Encapsulation - Keeps data protected inside a class and controls how it can be accessed.
  Abstraction - Hides complicated details and only shows the important parts.

  Why is _attribute not strictly private?
  A single underscore, like _score, means "this is for internal use."
  It is called convention-based because it is mainly a programmer's rule or warning.
  Python does not actually prevent you from accessing it.

  What happens with __attribute?
  Two underscores, like __score, trigger name mangling.
  Python changes the attribute's name to make accidental access harder.

2. Final Reflection Question
    1. When trying to access atm.__pin directly, an AttributeError occurred because Python uses name mangling for attributes with two underscores. Python changes __pin into something like _ATM__pin to make it harder to access accidentally from outside the class.
    2. Using @property allowed the programmer to control and validate data while keeping the same way of accessing it. This means the caller can still use something simple like atm.pin, even if the internal code or data structure changes.
    3. The ATM class demonstrated abstraction by hiding the complicated BankAccount logic from the user. The user only needs to perform simple actions like checking the balance or withdrawing money without knowing how the bank account works internally.
