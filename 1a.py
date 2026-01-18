from collections import defaultdict
from math import gcd

def maxPoints(customer_locations):
    n = len(customer_locations)
    if n <= 2:
        return n

    max_points = 0

    for i in range(n):
        slope_count = defaultdict(int)
        x1, y1 = customer_locations[i]

        for j in range(i + 1, n):
            x2, y2 = customer_locations[j]
            dx = x2 - x1
            dy = y2 - y1
            
            if dx == 0:
                slope = ('inf', 0)    
            elif dy == 0:
                slope = (0, 0)         
            else:
                g = gcd(dx, dy)
                slope = (dy // g, dx // g)

            slope_count[slope] += 1

        current_max = max(slope_count.values(), default=0) + 1
        max_points = max(max_points, current_max)
    return max_points


if __name__ == "__main__":
    test_locations = [[1,1], [2,2], [3,3], [1,5], [4,1]]
    result = maxPoints(test_locations)
    
    print("-" * 30)
    print(f"RESULT: {result}")
    print("-" * 30)