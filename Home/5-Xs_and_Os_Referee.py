#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-18 22:46:42
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

def checkio(game_result):
	for row in game_result:
		if row[0] == row[1] == row[2] and row[0] != ".":
			if row[0] == "O":
				return "O"
			elif row[0] == "X":
				return "X"
	for col in range(3):
		if game_result[0][col] == game_result[1][col] == game_result[2][col] and game_result[0][col] != ".":
			if game_result[0][col] == "O":
				return "O"
			elif game_result[0][col] == "X":
				return "X"
	if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != ".":
		if game_result[0][0] == "O":
				return "O"
		elif game_result[0][0] == "X":
				return "X"
	if game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] != ".":
		if game_result[0][2] == "O":
				return "O"
		elif game_result[0][2] == "X":
				return "X"
	return "D"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
