# Day 7: The Treachery of Whales

A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

`16,1,2,0,4,2,7,1,2,14`

This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

- Move from 16 to 2: 14 fuel
- Move from 1 to 2: 1 fuel
- Move from 2 to 2: 0 fuel
- Move from 0 to 2: 2 fuel
- Move from 4 to 2: 2 fuel
- Move from 2 to 2: 0 fuel
- Move from 7 to 2: 5 fuel
- Move from 1 to 2: 1 fuel
- Move from 2 to 2: 0 fuel
- Move from 14 to 2: 12 fuel

This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

## Utilities and tools

- VSCode
- Python 3.11.0

## Initial thoughts

At first, I wondered if this could be solvable by calculating the mean or the median of the crab positions, but quickly realized this wouldn't work. For example, if 999 crabs were at position 1 and 1 crab was at position 2000, we'd end up rounding to a solution of 3 for the mean and the median would be heavily skewed to the right, which is definitely *not* right. In that situaton, we'd want the single crab in position 2000 to be the only crab to move.

I second thought, if we sorted the data, we shoud see a parabola shape form, with our answer at the bottom. Knowing this, we can conduct a binary search by selecting the middle two points from our list, then comparing the slope, or the size of each. Whichever is bigger, we know the answer is not on that side, so we can eliminate that half of the data set. Rinse and repeat until there is only one answer.

## Issues

I ran into two issues:

1. I originally only considered the cost of positions the crabs were currently in, and not every position they could be in. This means if a crab was not in position 50, I wasn't considering it as a possible solution. Because of this, I switched to using ranges based on the min and max crab positions.

2. I was mishandling range indexes. Because I was using ranges and not a list containing every possible solution, I ran into issues surrounding the behavior of ranges. Say we have `range(0, 10)`, and I select position 4 and 5 for my test. Position 4 wins, so my resulting range would be set to `range(0, 4)`. The problem is, the number 4 doesn't exist in `range(0, 4)`, so I was accidentally removing values. Fixing this led me to the correct answer.
