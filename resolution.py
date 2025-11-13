from sympy import symbols
from sympy.logic.boolalg import Implies, And, Or, Not, to_cnf
from sympy.logic.inference import satisfiable

# Define symbols
Food = symbols('Food')
Apple = symbols('Apple')
Vegetables = symbols('Vegetables')
Peanuts = symbols('Peanuts')
John_likes_x = symbols('John_likes_x')
Anil_eats_x = symbols('Anil_eats_x')
Harry_eats_x = symbols('Harry_eats_x')
Alive_x = symbols('Alive_x')
Killed_x = symbols('Killed_x')

# Knowledge Base in propositional logic
# a. John likes all kind of food -> For each food x, John_likes_x if Food(x)
kb = And(
    Implies(Food, John_likes_x),  # a
    Implies(Or(Apple, Vegetables), Food),  # b
    Implies(And(Anil_eats_x, Not(Killed_x)), Food),  # c
    And(Anil_eats_x, Alive_x),  # d
    Implies(Anil_eats_x, Harry_eats_x),  # e
    Implies(Alive_x, Not(Killed_x)),  # f
    Implies(Not(Killed_x), Alive_x)  # g
)

# We want to prove: John likes peanuts -> John_likes_x for Peanuts
# Assume the negation of the goal for resolution
goal_negation = Not(John_likes_x)

# Combine KB with negated goal
combined = And(kb, goal_negation)

# Check satisfiability
sat_result = satisfiable(combined)

if sat_result:
    print("The negation is satisfiable. Cannot prove John likes peanuts from KB.")
else:
    print("The negation is unsatisfiable. By resolution, John likes peanuts is proven!")
