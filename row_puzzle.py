# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/16/2022
# Description: Attempts to solve a row puzzle. Returns True is solvable, False otherwise.

def rec_row_puzzle(num_row, token, visited):
    """Helper function for row_puzzle."""
    if token + 1 == len(num_row):
        return True

    if token + num_row[token] + 1 <= len(num_row):
        new_token = token + num_row[token]
        if new_token not in visited:
            visited.append(new_token)
            stepping = rec_row_puzzle(num_row, new_token, visited)
            if stepping is not False:
                token += num_row[token]
                return stepping

    if token - num_row[token] >= 0:
        new_token = token - num_row[token]
        if new_token not in visited:
            visited.append(new_token)
            stepping = rec_row_puzzle(num_row, new_token, visited)
            if stepping is not False:
                token -= num_row[token]
                return stepping

    return False

def row_puzzle(num_row):
    """Attempts to solve a row puzzle. Returns True is solvable, False otherwise."""

    return rec_row_puzzle(num_row, 0, [])
