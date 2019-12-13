#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)this code snippet is running a loop and has a runtime complexity of O(n)

b)this code snippet runs a loop until we get back the value of 'n' which then kicks us out of the loop. Giving us a runtime Complexity of O(n)

c)this recursive function is using bunnies - q or (n-1) recursive calls until the base case it triggered and with no other logic to increase the space or time complexity we get O(n)

## Exercise II

Divide and conquer / Binary search would be the strategy I would use for this algorithm. We need to find the midpoint of the building and drop the egg. If the egg breaks then we start at the bottom and make our old mid point the new top. If the egg does not break then the current mid point becomes our bottom and the end of the building is our new top. We would continue that halving approach until we found the lowest floor that the egg dropped would no longer break. This approach is O( log n ) runtime complexity.
