#!/usr/bin/python3
"""
This module contains the function island_perimeter which
calculates the perimeter of an island represented in a grid.
"""


def island_perimeter(grid):
    """
    calculate the perimeter of an island in a grid.
    Args:
    grid (list of list of int): A rectangular grid where 0
    represents water and 1 represents land. The grid is completely
    surrounded by water and contains exactly one island.
    Returns:
    int: The perimeter of the island.
    """
    width = len(grid[0])
    height = len(grid)
    shared_edges = 0
    land_cells = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                land_cells += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    shared_edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    shared_edges += 1

    return land_cells * 4 - shared_edges * 2
