# Jarvis March (Gift Wrapping Algorithm)
The Jarvis March, often referred to as the gift wrapping algorithm, starts by identifying the leftmost point and progressively wrapping the set of points, much like string wrapping around an object. This method is intuitive and mimics the process of manually tracing out the outer boundary of a shape.

- Complexity: The algorithm operates in O(nh) time, where n is the number of points and h is the number of points on the convex hull. This efficiency can degrade if the number of points on the hull is large, making it less suitable for larger datasets.

# Graham's Scan
Graham's Scan is a more efficient and commonly used method for computing the convex hull. The steps involved in Graham's Scan include:

1. Choosing the Origin: Identify the point with the lowest y-coordinate as the reference. If multiple points have the same y-coordinate, the one with the lowest x-coordinate is chosen. This point serves as a starting point for the sorting process.
2. Sorting Points: Sort all points based on the polar angle relative to the reference point. This angle measures how far each point is from a direct horizontal line extending to the right from the reference point.
3. Stack Initialization: Initialize the process with the first two sorted points placed on a stack.
4. Processing Remaining Points: As each new point is considered, check whether the path from the two topmost stack points to this new point makes a left or a right turn. Points that result in a right turn are not part of the convex hull and are removed from the stack.
5. Scanning the Upper and Lower Hull: The algorithm completes a full cycle around the points, effectively scanning for both the lower and upper parts of the hull if the dataset requires such treatment.

### Implementation Considerations
- Efficiency: Graham's scan is generally more efficient than the Jarvis March for larger datasets, primarily due to its O(n log n) complexity driven by the sorting step, followed by a linear sweep to form the hull.
- Robustness: Implementing Graham's Scan requires attention to detail, especially in handling cases with collinear points and selecting the correct initial point.


CHT 문제
좌표상의 많은 정점들의 가장 바깥쪽에 있는 정점을 잇는 정점을 을 구하라. 
나무들의 좌표가 주어지고 나무들의 최소한의 정점을 구하라 …. 

- 자비스 마치 : 시간복잡도가 안좋고
- 그레이엄의 스캔 : 
원점과 기준으로 정렬 … 각이 가장 작은 것부터? 
첫  두점을 스택에 추가하여 스택 초기화 
나머지두 점을 추가하면서 새로 추가된 것이 시계방향인지 아닌지, 

upper hull, lower hull 두번 스캔한다.