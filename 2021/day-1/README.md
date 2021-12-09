# [Day 1: Sonar Sweep](https://adventofcode.com/2021/day/1)

You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 stars.

Your instincts tell you that in order to save Christmas, you'll need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

```text
199
200
208
210
200
207
240
269
260
263
````

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

```text
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
```

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

## Utilities and tools

VSCode
Python 3.9.8

## My solution - in words

My first thought is to open the data file, then loop over each line. Because of this, we know what line 1 is before line 2, meaning we'll be comparing each line with the line **before** it.

We'll be storing the line we're looping on in a variable at the end of the loop, so that way we can access it on the next loop. We'll also need to check if this variable has a value from the file in it, so we'll need to initialize it with a value that won't be in that file before starting the loop. `None` is uaually a good option.

```python
last_val = None

for line in file:
    if last_val is not None:
        if line > last_val:
            ## The depth has incremented
```

This should be good enough scaffolding to get us in the right place. It doesn't read from the file or actually count each value, but I think it's the right idea.

### Issues

The assumtion I went into this with was that strings and integers could be used identially when comparing values, but there is a difference. For example, alphabetically, '1016' comes before '996', but the integer value 1016 is greater than 996. Converting my strings to integers before comparison resulted in a correct answer.
