# Runtime Complexity

*What is the runtime complexity of this solution you just did?*
*Then, How can identify the runtime complexity?*

How much more processing power/time is required to run your algorithm if we double the inputs?

```javascript
function reverse(str) {
    let reversed = '';
    for (let character of str){
        reversed = character + reversed;
        debugger;
    }
    return reversed 
}
```
In this function:
- Each additional character (involves)=> 1 step through 1 loop;
- n step through n loop.

- 
1. Constant Time ; 1   
- No matter how many elements we're working with,   
- the algorithm/operation/whatever... will always take the same amount of time
- ex) Accessing a specific element in an array

2. Logarithmic Time ; logn   
- Dobling the number of elements does not double the amount of work.
- Common in searching algorithms like binary search.
You have this if doubling the number of elements you are iterating over doesn't double the amount of work. Always assume that searching operations are logn

3. Linear Time : n   
Iterating through all elements in a collection of data. If you see a for loop spanning from '0' to 'array.length', you probably have 'n', or linear runtime.
- ex) Iterating through all elements in an array

4. Quasilinear Time : n*logn  
You have this if doubling the number of elements you are iterating over doesn't double the amount of work. Always assume that any sorting operation is n*log(n)

5. Quadratic Time : n^2  
Every element in a collection has to be compared to every other element. 
very easy way to identify algorithm.
- ex) Bubble sort, insertion sort


6. Exponential Time : 2^n
If you add a 'single' element to a collection, the processing power required doubles.
- Common in algorithms solving problems with recursive branching


### Big 'O' Notation
To describe the efficiency of an algorithm. 

### Identifying Runtime Complexity
for n loop ? O(n)  
for n/2 loop ? O(n)  
for n loop and then for m loop ? O(n+m)  
for n loop in for n loop ? O(n\*n) = O(n^2)  
for n loop in for m loop ? O(n\*m)  
Sorting ? O(n\*logn)  
Searching a sorted array? O(logn)  

### Space Complexity 



