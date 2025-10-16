import itertools

# Logical operations
def implies(a, b):
    return not a or b

def or_operator(a, b):
    return a or b

def not_operator(a):
    return not a

# Constructing the truth table
def construct_truth_table():
    truth_values = [True, False]
    truth_table = []
    
    # Generate all combinations for Q, P, R
    for values in itertools.product(truth_values, repeat=3):
        Q, P, R = values
        
        # Evaluate KB sentences
        q_implies_p = implies(Q, P)
        p_implies_not_q = implies(P, not_operator(Q))
        q_or_r = or_operator(Q, R)
        
        # KB = (Q → P) ∧ (P → ¬Q) ∧ (Q ∨ R)
        kb_is_true = q_implies_p and p_implies_not_q and q_or_r
        
        # Entailment expressions
        entail_r = R
        entail_r_implies_p = implies(R, P)
        entail_q_implies_r = implies(Q, R)
        
        # Add row to truth table
        truth_table.append((
            Q, P, R,
            q_implies_p, p_implies_not_q, q_or_r,
            kb_is_true,
            entail_r, entail_r_implies_p, entail_q_implies_r
        ))
    return truth_table

# Print the truth table nicely
def print_truth_table(truth_table):
    header = [
        "Q", "P", "R",
        "Q → P", "P → ¬Q", "Q ∨ R",
        "KB (all true)",
        "R", "R → P", "Q → R"
    ]
    print(" | ".join(header))
    print("-" * 85)
    
    for row in truth_table:
        # Format True/False as T/F for compactness
        formatted_row = [("T" if val else "F") for val in row]
        print(" | ".join(formatted_row))

# Generate and print truth table
truth_table = construct_truth_table()
print_truth_table(truth_table)

# Additionally, check entailment by verifying if for all models where KB is true, entailment is true

def check_entailment(truth_table, entailment_index):
    for row in truth_table:
        kb_true = row[6]
        entailment_val = row[entailment_index]
        if kb_true and not entailment_val:
            return False
    return True

print("\nEntailment Results:")
print(f"Does KB entail R? {check_entailment(truth_table, 7)}")
print(f"Does KB entail R → P? {check_entailment(truth_table, 8)}")
print(f"Does KB entail Q → R? {check_entailment(truth_table, 9)}")
