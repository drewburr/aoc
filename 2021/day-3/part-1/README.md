# Day 3: Binary Diagnostic

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

```text
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

## Utilities and tools

- VSCode
- Python 3.10.6

## My solution - in words

I think a class is the way to go on this one. Provide a way to stream in each line of binary, then have the class keep track of the number of lines, as well as the number of `1`s that appear in each index. Both pieces of data together will tell me whether there were more ones or zeroes in each index.

I originally ran into issues with programmatically converting binary to base 10. I probably could have used an online converter, but that'd be too easy. I also had to change up the way I was importing data, due to newlines being a problem. My solution would not work well for very large data sets because I am importing all data at once, then streaming it into my diagnostic class. It would be relatively simple to convert this into something that reads in one line at a time, severely reducing the overall memory load.
