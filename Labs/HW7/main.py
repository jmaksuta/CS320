"""
Lab 06 - HW6
64.2 Depth-First Traversal
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

from edgegraph import *
import math

def _bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    """ A weighted directed graph with n vertices, and a vertex v of G. """
    # input
    path = dict()
    path[start] = 0
    # D[v] = 0
    # for each vertex u != v of G do
        # D[u] = positive infinity
    # for i = 1 to n-1 do
        # for each (directed) edge (u, z) outgoing from u do
            # Perform the relax ation operation on (u,z)
            # if D[u] + w((u, z)) < D[z] then
                # D[z] = D[u] + w((u, z))
    # if there are no edges left with potential relaxation operations then
        # return the label D[u] of each vertex u
    # else
        # return "Graph contatins a negative-weight cycle"


def validate(graph: GraphEL, start: VertexEL, end: VertexEL):
    assert graph is not None
    assert start is not None
    assert end is not None
    assert graph.find_vertex(start) is not None
    assert graph.find_vertex(end) is not None
    return

def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    result = (),()
    try:
        validate(graph, start, end)
        _bellman_ford(graph, start, end)

    except Exception as e:
        result = None, None
    return result