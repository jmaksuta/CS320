"""
Lab 06 - HW6
64.2 Depth-First Traversal
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

from edgegraph import *
# import math
import sys


def weight(edge):
    return edge.get_value()


def relaxation(distances, edge):
    u = edge.head()
    z = edge.tail()
    edge_weight = weight(edge)
    if distances[str(u)] + edge_weight < distances[str(z)]:
        distances[str(z)] = distances[str(u)] + edge_weight
    return distances


def get_other_end(edge, vertex):
    result = None
    pair = edge.ends()
    if pair[0] == vertex:
        result = pair[1]
    elif pair[1] == vertex:
        result = pair[0]
    return result


def no_relaxation_possible(graph: GraphEL, distances):
    result = True
    for dir_edge in graph.edges():
        u = dir_edge.head()
        z = dir_edge.tail()
        # check if relaxation operation on (u,z) possible
        edge_weight = weight(dir_edge)
        if distances[str(u)] + edge_weight < distances[str(z)]:
            result = False
            break
    return result


def convert_list_vertices_to_edges(items: list, lookup_graph: GraphEL = None) -> list:
    result = []

    if items is None or len(items) == 0:
        return result
    
    v1 = items[0]
    for vertex in items[1:]:
        v2 = VertexEL(str(vertex))
        edge = None
        # lookup edge
        if lookup_graph is not None:
            edge = lookup_graph.get_edge_with_ends(v1, v2)

        # if edge is None:
        #     edge_name = str(v1) + "-" + str(v2)
        #     edge = EdgeEL(edge_name, v1, v2)

        if edge is not None:
            result.append(edge)
        v1 = v2
    return result


def package_result(graph: GraphEL, distances: dict, paths: dict, end):
    """ Returns the result as a tuple of edges. """
    result = []
    # return the label D[u] of each vertex u

    path_items = []
    for key, value in paths.items():
        # add end point
        paths[key] = paths[key] + [key]

    path_to_end = paths[str(end)]

    vertices = []
    for key in path_to_end:
        vertices.append(VertexEL(key))

    result = convert_list_vertices_to_edges(vertices, graph)
    
    return tuple(result)


def _bellman_ford_relaxation(dir_edge, distances, paths):
    """ Performs the Bellman-Ford relaxation operation and
    returns distances and paths. """
    u = dir_edge.head()
    z = dir_edge.tail()

    edge_weight = weight(dir_edge)
    if edge_weight <= 0:
        raise Exception("negative weight encountered.")
    
    if distances[str(u)] + edge_weight < distances[str(z)]:
        distances[str(z)] = distances[str(u)] + edge_weight
        paths[str(z)] = paths[str(z)] + [str(u)]
    return distances, paths


def _bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    """ A weighted directed graph with n vertices, and a vertex v of G. """
    distances = dict()
    distances[str(start)] = 0
    paths = dict()
    num_vertices = len(graph.vertices())

    for vertex in graph.vertices():
        if vertex != start:
            distances[str(vertex)] = sys.maxsize
            paths[str(vertex)] = [str(start)]
    
    for iteration in range(0, num_vertices - 1):
        for dir_edge in graph.edges():
            distances, paths = _bellman_ford_relaxation(dir_edge, distances, paths)

    if no_relaxation_possible(graph, distances):
        # if there are no edges left with potential relaxation operations then
        # return the label D[u] of each vertex u
        return package_result(graph, distances, paths, end)
    else:
        return None
    

def validate_start_and_end(start_to_end, end_to_start):
    result = True
    if start_to_end is None or end_to_start is None:
        return result
    for index in range(0, len(end_to_start)):
        if start_to_end[index] == end_to_start[index]:
            result = False
            break
    return result


def _internal(graph: GraphEL, start: VertexEL, end: VertexEL):
    start_to_end = _bellman_ford(graph, start, end)
    end_to_start = _bellman_ford(graph, end, start)
    if not validate_start_and_end(start_to_end, end_to_start):
        end_to_start = None
    return (start_to_end, end_to_start)


def validate(graph: GraphEL, start: VertexEL, end: VertexEL):
    assert graph is not None
    assert start is not None
    assert end is not None
    assert graph.find_vertex(start) is not None
    assert graph.find_vertex(end) is not None
    return


def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    result = (), ()
    try:
        validate(graph, start, end)
        result = _internal(graph, start, end)

    except Exception as e:
        print(e)
        result = None, None
    return result
