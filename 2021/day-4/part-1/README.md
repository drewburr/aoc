# Day 4: Giant Squid

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

```text
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
```

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

```text
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

```text
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```

Finally, 24 is drawn:

```text
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: `14 21 17 24 4`).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

## Utilities and tools

- VSCode
- Python 3.10.6

## Initial thoughts

My immediate thought is to create an object to define each card, which includes each space on the card, its marking status, and methods used to determine both a win condition and the final answer.

I could also create another object to define the game, which will orchestrate the process of telling every card about the number that was drawn. That game could have a 'play' method that's called for every number drawn, and it can return true or false to communicate if there is a winning card.

## My solution - in words

For the card objects, I chose to pull inspiration from game design by storing the card data and marking statuses in separate logical objects called bitmaps. These are identically-sized multi-domentional arrays where each array (or list, in Python) holds a single set of data. In my case, I used a 5x5 list of strings to store the values of each cell on the bingo card, and another 5x5 list of booleans to store each cell's marking status. When checking for match, I keep track of the x, y coorinates on the values bitmap, then use those coordinates on the marking status bitmap to update the boolean.

Now, given that I had to go out of my way to keep track of indexes and learn how to use `zip()` to its full potential, it's safe to say this kind of unnecessary. A much simpler solution would have been to create a Cell object whose attributes would store both of these pieces of information together. I wanted to try to make use of some theoretical knowledge I've been holding on to, and overall, I'd say it was pretty successful

Normally it's valuable to use a bitmap when storing a many sets of independent data. A simple example might be a checkers game, where a bitmap could define the three important elements of the game: The player's pieces on the board, the opponent's pieces on the board, and the location of kings. If a player moves a piece, we can use the source and destination coordinates across all three bitmaps to determine everything we need to know about that move. Did they move to a free space or an opponent? Did they actually jump the opponent? Can this piece move backwards? Can it jump again? We could also choose leverage one or an additional bitmap to define the checkerboard pattern, to help ensure player A will never arrive on player B's spaces. All of these bitmaps are also elements that must be rendered to the screen, and this format can greatly simplify that logic.

In addition to developing an appreciation for this format, I was also able to learn more about why `zip()` is useful and how it can be leveraged to simplify some very daunting join operations. For example, if our bingo card bitmaps were 3x3 lists, we might see a card in this state:

```python
>>> values
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> marked
[[True, True, False], [False, True, False], [False, True, False]]
```

Here we can see that values 1, 2, 5, and 8 are all marked. This is a win condition, the middle vertical column is complete! But how are we supposed to determine this, especially once we scale up to the 5x5 cards?

One way of doing this might be by looping over each row and column index seprately, to determine if all cells in that set are set to True. For example:

```python
# Check rows for win
for x in range(len(marked)):
    win = True
    for y in range(len(marked)):
        if not marked[x][y]:
            win = False
    if win:
        print('Win found!')

# Check columns for win
for y in range(len(marked)):
    win = True
    for x in range(len(marked)):
        if not marked[x][y]:
            win = False
    if win:
        print('Win found!')
```

This definitely works, but it's a lot of code and can be hard to follow.

We could simplify this a ton by adding a filter to the rows search, but this doesn't work for columns because we can't address just the y value.

```python
# Check rows for win
for row in marked:
    marked_cells = list(filter(None, row)) # Filter out all False cells
    if len(marked_cells) == 3:
        print('Win found!')

# Check columns for win
for y in range(len(marked)):
    win = True
    for x in range(len(marked)):
        if not marked[x][y]:
            win = False
    if win:
        print('Win found!')
```

One way to get around this limitation is by inverting or rotating the array using `zip()`. We can effectively 'flip' the x and y axis by leveraging `zip()` to perform a horizontal reflection of the list. Let's use this on our marked list:

```shell
>>> marked
[[True, True, False], [False, True, False], [False, True, False]]
>>> list(zip(*marked))
[(True, False, False), (True, True, True), (False, False, False)]
```

And that's it! To better explain, we just took the X and Y axis and swapped them. We can see our win condition moved from (0,1) (1,1) (2,1) over to (1,0) (1,1) (1,2).

> Note: The astrisk (*) in `zip(*marked)` is used to separate each element in the list into arguments. In our case, this is the same as `zip(marked[0], marked[1], marked[2])`.

By doing this, the code we're using for the rows now works with our columns. We could even use a function to check for either win:

```python
def check_win(data):
    for row in data:
        marked_cells = list(filter(None, row)) # Filter out all False cells
        if len(marked_cells) == 3:
            return True
    return False

if check_win(marked) or check_win(zip(*marked)):
    print('Win found!')
```

Another problem `zip()` solved for me was the final soution, where we needed to add all unmarked cells together. To do this, I was able to double zip both the values and marked lists together, resulting in a series of Tuples with the matching elements from each list

```shell
>>> values
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> marked
[[True, True, False], [False, True, False], [False, True, False]]
```

```python
for join in zip(values, marked):
    for val, marked in zip(*join):
            print(val, marked)
```

```text
1 True
2 True
3 False
4 False
5 True
6 False
7 False
8 True
9 False
```

Overall, this was a very fun challenge for me. It was great to explore a different type of data structure and the challenges it brings.
