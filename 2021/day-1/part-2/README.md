# [Day 1: Sonar Sweep](https://adventofcode.com/2021/day/1)

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

``` text
199  A
200  A B
208  A B C
210    B C D
200  E   C D
207  E F   D
240  E F G
269    F G H
260      G H
263        H
```

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

```text
A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
```

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

## Utilities and tools

VSCode
Python 3.9.8

## My solution - in words

Looking at the examples given, it looks like I will be managing several objects at a time, assuming I don't calculate the values of every triplet first, then compare later. I'd like to try to do this in a single loop, because why not?

My first thought is to try looping over each line, then add the value of that line to each appropriate index in that list. This feels overly complicated and I can't come up with a simple way to keep this intuitive and readable, so let's not do that.

The other option would be to loop over each line, keeping track of the last 3 values I've looped over. Once I have my first 3 values, adding them together would give me `A`. On the next loop, I could pop the oldest value, append the next one, then that value would be `B`. From there I just need to compare and add to my counter if necessary, and keep chugging along each line until the file closes.

### Issues

On my first attempt, I forgot that `list.pop()` removes `list[-1]` and not `list[0]`. I did catch this before submitting, since my answer seemed a bit high.

This did not work either. I thought about how I was handling initilizing my list of values, and realized I was skipping the first value in my file:

```python
for line in open('input.txt', 'r'):
    depth = int(line)

    if len(window) < 3:
        window.append(depth)
    else:
        # Store the current window and compare
        this_sum = sum(window)
        window.pop(0)
```

I realized that once there were 2 values in my list, I was adding the next line to the list, then completely ignoring my initialized window, since now it had 3. Fixing this gave me the correct answer.
