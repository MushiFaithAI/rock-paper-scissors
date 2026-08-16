def player(prev_play, opponent_history=[]):

    if prev_play:
        opponent_history.append(prev_play)

    if not opponent_history:
        return "R"

    # Track what the opponent does after our previous moves.
    # Abbey uses patterns based on our play, so predict her response.

    # Look for repeated sequences in the opponent's history.
    for n in [4, 3, 2, 1]:
        if len(opponent_history) <= n:
            continue

        pattern = opponent_history[-n:]
        counts = {"R": 0, "P": 0, "S": 0}

        for i in range(len(opponent_history) - n):
            if opponent_history[i:i+n] == pattern:
                following = opponent_history[i+n]
                counts[following] += 1

        if sum(counts.values()) > 0:
            predicted = max(counts, key=counts.get)

            if predicted == "R":
                return "P"
            elif predicted == "P":
                return "S"
            else:
                return "R"

    # If there isn't enough history, counter the last move.
    if prev_play == "R":
        return "P"
    elif prev_play == "P":
        return "S"
    else:
        return "R"