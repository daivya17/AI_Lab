def alpha_beta(node, depth, alpha, beta, maximizing_player, path):
    # Base case: if node is a leaf (integer), return its value and path
    if isinstance(node, int):
        return node, path

    if maximizing_player:
        value = float('-inf')
        best_path = None
        
        for i, child in enumerate(node):
            child_value, child_path = alpha_beta(
                child, depth + 1, alpha, beta, False, path + [i]
            )
            
            if child_value > value:
                value = child_value
                best_path = child_path
            
            # Artifact '62' removed here
            alpha = max(alpha, value)
            
            if alpha >= beta:
                print(f"  [PRUNE] MAX (Depth {depth}): Alpha ({alpha}) >= Beta ({beta})")
                break
                
        return value, best_path

    else:
        value = float('inf')
        best_path = None
        
        for i, child in enumerate(node):
            child_value, child_path = alpha_beta(
                child, depth + 1, alpha, beta, True, path + [i]
            )
            
            if child_value < value:
                value = child_value
                best_path = child_path
            
            beta = min(beta, value)
            
            if beta <= alpha:
                print(f"  [PRUNE] MIN (Depth {depth}): Beta ({beta}) <= Alpha ({alpha})")
                break
                
        return value, best_path

if __name__ == "__main__":
    # Tree structure with artifact '63' removed
    tree = [
        [
            [
                [10, 11],
                [9, 12]
            ],
            [
                [14, 15],
                [13, 14]
            ],
        ],
        [
            [
                [5, 2],
                [4, 1] 
            ],
            [
                [3, 22],
                [20, 21]
            ],
        ]
    ]

    print("Starting Alpha-Beta Pruning...\n" + "-"*30)
    
    value, best_path = alpha_beta(tree, 0, float('-inf'), float('inf'), True, [])
    
    print("-" * 30)
    print(f"FINAL MINIMAX VALUE AT ROOT: {value}")
    print(f"BEST PATH INDICES: {best_path}")
