# Day 4: Giant Squid

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

## Utilities and tools

- VSCode
- Python 3.11.0

## My solution - in words

This one was pretty easy with how I set up the rest of the code. I just needed to change my win condition to keep track of the last card that won. In my case, all cards were guranteed to win. In the event that this wasn't the case, my implementation would need to be upated to handle when the draw order has been exhausted. I'm also assuming that only one card can win at a time. If two cards tied at the end, I would be chosing the card at the bottom of the stack as the last winner.
