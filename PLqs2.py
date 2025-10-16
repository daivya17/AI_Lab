import itertools

# Logical operations
def implies(a, b):
    return not a or b

def or_operator(a, b):
    return a or b

def not_operator(a):
    return not a

# Construct truth table for all combinations of A, B, C
def construct_truth_table():
    truth_values = [True, False]
    truth_table = []
    
    for values in itertools.product(truth_values, repeat=3):
        A, B, C = values
        
        alpha = or_operator(A, B)                 # alpha = A ∨ B
        kb = or_operator(A, C) and or_operator(B, not_operator(C))  # KB = (A ∨ C) ∧ (B ∨ ¬C)
        
        truth_table.append((
            A, B, C,
            alpha,
            kb
        ))
    return truth_table

# Print full truth table nicely
def print_full_truth_table(truth_table):
    header = ["A", "B", "C", "alpha (A ∨ B)", "KB ((A ∨ C) ∧ (B ∨ ¬C))"]
    print("Full Truth Table:")
    print(" | ".join(header))
    print("-" * 50)
    
    for row in truth_table:
        formatted_row = [("T" if val else "F") for val in row]
        print(" | ".join(formatted_row))
    print("\n")

# Check if KB entails alpha
def check_entailment(truth_table):
    for row in truth_table:
        kb = row[4]
        alpha = row[3]
        if kb and not alpha:
            return False
    return True

# Print filtered truth table for sub-question showing relevant columns
def print_subquestion_tt(truth_table, col_indices, col_names):
    print(" | ".join(col_names))
    print("-" * (4 * len(col_indices) + 3 * (len(col_indices)-1)))
    for row in truth_table:
        vals = [row[i] for i in col_indices]
        formatted_vals = [("T" if v else "F") for v in vals]
        print(" | ".join(formatted_vals))
    print("\n")

# Main execution
truth_table = construct_truth_table()
print_full_truth_table(truth_table)

# Entailment question: Does KB entail alpha?
print("Does KB entail alpha (A ∨ B)?")
entails_alpha = check_entailment(truth_table)
print(f"Answer: {entails_alpha}\n")

