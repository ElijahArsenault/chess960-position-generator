import random

# Assigning characters to piece variables
queen = "Q"
king = "K"
rook1 = "R"
rook2 = "r"
bishop_light = "B"
bishop_dark = "b"
knight1 = "n"
knight2 = "N"


# Loop to keep trying combinations until a legal position is reached
while True:
    position = [queen, king, rook1, rook2, bishop_light, bishop_dark, knight1, knight2]
    random.shuffle(position)
    # To insure bishops are on opposite colors
    if (position.index(bishop_dark) - position.index(bishop_light)) % 2 == 0:
        continue
    # Checks if king is between rooks
    elif position.index(rook1) > position.index(king) and position.index(rook2) > position.index(king):
        continue
    elif position.index(rook1) < position.index(king) and position.index(rook2) < position.index(king):
        continue
    else:
        break

position = str(position)
print("Chess960 position:")
# Prints position in a more readable way
print(position.strip("[").strip("]").replace("'", "").replace(",", ""))
