"""
Lab 06 - HW6
64.2 Depth-First Traversal
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

from edgegraph import *
import math
import sys

def weight(edge):
    return 1

def relaxation(distances, edge):
    u = edge.head
    z = edge.tail
    edge_weight = weight(edge)
    if distances[str(u)] + edge_weight < distances[str(z)]:
    # if D[u] + w((u, z)) < D[z] then
        distances[str(z)] = distances[str(u)] + edge_weight
        #D[z] = D[u] + w((u, z))
    return distances

def get_other_end(edge, vertex):
    result = None
    pair = edge.ends()
    if pair[0] == vertex:
        result = pair[1]
    elif pair[1] == vertex:
        result = pair[0]
    return result


def no_relaxation_possible(graph: GraphEL):
    return True

def package_result(distances: dict, paths: dict):
    result = []
    # return the label D[u] of each vertex u
    for key, value in distances.items():
        result.append(key)
    return result


def _bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    """ A weighted directed graph with n vertices, and a vertex v of G. """
    # TODO: Idea is that as we get the shortest distance that ends with end,
    # we find the shortest paths at the same time as the distances, by
    # concatenating the end vertex onto the path list onto the paths dict.

    # input
    distances = dict()
    paths = dict()
    distances[str(start)] = 0
    paths[str(start)] = [start]
    # D[v] = 0
    for vertex in graph.vertices():
        if vertex is not start:
            distances[str(vertex)] = sys.maxsize
            paths[str(vertex)] = [vertex]
    
    for u in graph.vertices():
        for dir_edge in graph.out_incident(u):
            z = dir_edge.tail
            # Perform the relaxation operation on (u,z)
            distances = relaxation(dir_edge)
            edge_weight = weight(dir_edge)
            if distances[str(u)] + edge_weight < distances[str(z)]:
            # if D[u] + w((u, z)) < D[z] then
                distances[str(z)] = distances[str(u)] + edge_weight
                paths[str(u)] = paths[str(u)] + distances[str(z)]
                # D[z] = D[u] + w((u, z))
    if no_relaxation_possible(graph):
    # if there are no edges left with potential relaxation operations then
        # return the label D[u] of each vertex u
        return package_result(distances, paths)
    else:
    # else
        return None
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