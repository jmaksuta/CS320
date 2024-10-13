"""
Lab 06 - HW6
64.2 Depth-First Traversal
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

from edgegraph import VertexEL, EdgeEL, GraphEL, parse_graph_file

# 64.2 Depth-First Traversal
# In this lab, you are tasked with writing a Depth-First traversal (see textbook section 14.3) using the course-provided edgegraph library. Download the edgegraph.py file below. (This version of edgegraph.py may be improved from the version you downloaded from canvas. Make sure you use the one provided with this assignment).

# Specifically, you will write a routine dfs(graph, start) which accepts a graph (GraphEL) and a start vertex (VertexEL) and returns a tuple of vertices in a valid DFS order.

# Some details:
# You may assume that graph is not a forest.
# If graph is None, return an empty tuple (())
# If start is None, return an empty tuple (())
# If start is not in graph, return an empty tuple(())
# Performance
# Your implementation should run in time O(n+m), where n is the number of vertices and m is the number of edges.
def _internal_dfs(graph, start):
    pass

def validate(graph, start):
    """ Validates the input argments. """
    # You may assume that graph is not a forest.
    # If graph is None, return an empty tuple (())
    # If start is None, return an empty tuple (())
    # If start is not in graph, return an empty tuple(())
    assert graph is not None
    assert start is not None
    assert start in graph.vertices()
    
def dfs(graph, start):
    result = (())
    try:
        validate(graph, start)
        result = _internal_dfs(graph, start)

    except Exception as e:
        # result = None
        pass
    return result

# picking up tomorrow!