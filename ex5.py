def count_descendants(person: str, children: dict) -> int:
  
    """
    Recursively counts the number of descendants (children, grandchildren, etc.) 
    for the specified person.
    Args:
        person (str): person's name
        children (dict): dictionary with parent's name and a person's name
    Returns:
        int: The number of descendants
    """
  
    if person not in children:
        return 0   
    total = 0
    for child in children[person]:
        total += 1
        total += count_descendants(child, children)
    return total


def solve_family_tree() -> None:
  
    """
    Main function: Reads input data, builds a parent-child dictionary, 
    determines the searched name and prints the number of all its descendants.
    Args:
        None
    Returns:
        None
    """
  
    n = int(input())
    children = {}
    for i in range(n):
        line = input().strip()
        parent, child = line.split()
        if parent not in children:
            children[parent] = []
        children[parent].append(child)
    target = input().strip()
    result = count_descendants(target, children)
    print(result)


if __name__ == "__main__":
    solve_family_tree()
