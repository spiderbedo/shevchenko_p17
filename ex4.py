def find_shape() -> None:
    
    """
    Reads the lines, then determines the shape of this item and displays it.
    If the item is not found, the word itself is displayed.
    Args:
        None
    Returns: 
        None
    """
  
    n = int(input())
    object_shape = {}
    for i in range(n):
        line = input().strip()
        parts = line.split()
        shape = parts[0]
        items = parts[1:]
        for it in items:
            object_shape[it] = shape
    target = input().strip()
    result = object_shape.get(target, target)
    print(result)


if __name__ == "__main__":
    find_shape()
