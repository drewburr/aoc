import re


class BingoCard():
    def __init__(self, data: list[list[str]]):
        BingoCard.validate_data(data)
        self.data = data
        self.mark_map: list[list[bool]] = list()

        for _ in range(5):
            self.mark_map.append([False]*5)

    @staticmethod
    def validate_data(data):
        if len(data) != 5:
            raise Exception(f'Invalid number of rows: {len(data)}')

        for i, row in enumerate(data):
            if len(row) != 5:
                raise Exception(
                    f'Invalid number of columns: {len(row)}. Row: {i}')

    def check_draw(self, draw):
        """
        Check if draw is on the board.
        Returns self if card has won.
        """
        for x, col in enumerate(self.data):
            for y, val in enumerate(col):
                if val == draw:
                    self.mark_map[x][y] = True
                    return self.check_win()

        return False

    def check_win(self):
        """
        Checks if any rows or columns are fully marked.
        Returns self if won.
        """
        for row in self.mark_map:
            marked_cells = list(filter(None, row))
            if len(marked_cells) == 5:
                return self

        # Invert the map (rows, cols -> cols, rows)
        for col in list(zip(*self.mark_map)):
            marked_cells = list(filter(None, col))
            if len(marked_cells) == 5:
                return self

        return False

    def get_score(self):
        """
        Returns the sum of all unmarked cells
        """
        total = 0
        # Zip each value to its respective mark map
        for join in zip(self.data, self.mark_map):
            for val, marked in zip(*join):
                if not marked:
                    total += int(val)

        return total


class BingoGame():
    def __init__(self):
        self.cards: list[BingoCard] = []
        self.draw_order: list[str] = []
        self.last_draw = ''
        self.winning_card: BingoCard = None

    def add_card(self, data: list[list[str]]):
        self.cards.append(BingoCard(data))

    def play(self):
        """
        Play a single draw.
        Returns true when the game is over
        """
        draw = self.draw_order.pop(0)
        self.last_draw = draw

        # Add draw to all cards
        results = map(lambda c: c.check_draw(draw), self.cards)

        # Check for win condition
        winning_cards = list(filter(None, results))
        if winning_cards:
            print(f'{len(winning_cards)} card(s) have won!')
            print(f'Winning draw: {self.last_draw}')
            self.winning_card = winning_cards[0]
            return True

        return False

    def calculate_score(self):
        """
        Calculates the final score of the game
        """
        card_score = self.winning_card.get_score()
        return card_score * int(self.last_draw)


def setup_game():
    game = BingoGame()
    card_data = []  # A 2D list of a card's cell values

    for line in open('input.txt', 'r'):
        # Remove newlines
        l = line.strip()

        if not game.draw_order:
            # First line is a CSV of the draw order
            game.draw_order = l.split(',')
        elif not l and card_data:
            # Save card if empty line is hit
            game.add_card(card_data)
            card_data = list()
        elif l:
            # Handle whitespace before appending
            card_data.append(re.split('[ ]+', l))

    # Catch the last card
    if card_data:
        game.add_card(card_data)

    return game


def main():
    game = setup_game()

    while not game.play():
        pass

    print(game.calculate_score())


if __name__ == "__main__":
    main()
