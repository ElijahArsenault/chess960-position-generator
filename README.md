# chess960-position-generator
A Python program that generates a legal Chess960 starting position.

Chess960 (also known as Fischer Random Chess, among other nanes) is a variant of chess where the back row of pieces is shuffled. Its name is derived from the 960 possible positions that can be generated.

The starting positions have to follow two rules:
- The bishops must be on the opposite colors
- The king must be between the rooks

This program follows these two rules.
To insure the bishops are on different colors:
```
    if (position.index(bishop_dark) - position.index(bishop_light)) % 2 == 0:
        continue
```
To insure that the king is between the rooks:
```
    elif position.index(rook1) > position.index(king) and position.index(rook2) > position.index(king):
        continue
    elif position.index(rook1) < position.index(king) and position.index(rook2) < position.index(king):
        continue
```
The program prints the position left-to-right like this: "n B R Q b K r N" where the letter represents the piece in standard chess notation.
