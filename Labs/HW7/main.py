"""
Lab 07 - HW7
65.2 Out and Back with Bellman-Ford
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

from edgegraph import *
import sys


def weight(edge):
    """ Returns the weight of an edge. """
    return edge.get_value()


def no_relaxation_possible(graph: GraphEL, distances):
    """ Returns true if no relaxation is possible. i.e.
    there is no directed edge whose distance can be improved. """
    result = True
    for dir_edge in graph.edges():
        u = dir_edge.tail()
        z = dir_edge.head()
        # check if relaxation operation on (u,z) possible
        edge_weight = weight(dir_edge)
        if distances[str(u)] + edge_weight < distances[str(z)]:
            result = False
            break
    return result


def lookup_edge(lookup_graph: GraphEL, v1: VertexEL, v2: VertexEL) -> EdgeEL:
    """ Returns an edge from the graph if it exists, or None if none exists. """
    result = None
    # lookup by one end then the other.
    edge = lookup_graph.get_edge_with_ends(v1, v2)
    if edge is None:
        edge = lookup_graph.get_edge_with_ends(v2, v1)
    if edge is not None:
        result = edge
    return result 


def convert_list_vertices_to_edges(items: list, lookup_graph: GraphEL = None) -> list:
    """ Returns a list of edges looked up in the graph from a list of vertices. """
    result = []
    if items is None or len(items) == 0:
        return result
    
    v1 = items[0]
    for vertex in items[1:]:
        v2 = VertexEL(str(vertex))
        
        edge = lookup_edge(lookup_graph, v1, v2)
        if edge is None:
            edge_name = str(v1) + "-" + str(v2)
            edge = EdgeEL(edge_name, v1, v2)

        if edge is not None:
            result.append(edge)
        v1 = v2
    return result


def get_next_vertex_no_excluded(paths, current, exclude_edges):
    """ Checks each element in the paths[current] entry's list
    starting with last index to first index, if the edge from
    current to vertex is excluded and returns the non-excluded
    element or None if no non-excluded list item exists. """
    next = None
    for index in range(len(paths[current]) - 1, -1, -1):
        vertex = paths[current][index]
        if not is_excluded(exclude_edges, VertexEL(current), VertexEL(vertex)):
            next = vertex
            break
    return next


def get_next_last_path_vertex(paths, current, exclude_edges):
    """ Returns the next non-excluded vertex from the
    paths[current] entry's ordered list of vertices. """
    next = None
    if current in paths and len(paths[current]) > 0:
        next = get_next_vertex_no_excluded(paths, current, exclude_edges)
    return next


def package_result_end_to_start_chain(graph: GraphEL, distances: dict, 
                                      paths: dict, start, end, exclude_edges):
    """ Returns the result as a tuple of edges. """
    result = None
    # return the label D[u] of each vertex u
    vertices = []
    current = None
    if str(end) in paths and len(paths[str(end)]) > 0:
        current = paths[str(end)][len(paths[str(end)]) - 1]
    if current is not None:
        vertices.append(VertexEL(str(end)))
        vertices.insert(0, VertexEL(current))
    while (current is not None and current != str(start)):
        current = get_next_last_path_vertex(paths, current, exclude_edges)
        if current is not None:
            vertices.insert(0, VertexEL(current))

    if current is not None and current == str(start):
        result = tuple(convert_list_vertices_to_edges(vertices, graph))
    
    return result


def is_end_a_match(edge, v1, v2):
    """ Returns True if v1 and v2 are both ends of edge. """
    ends = edge.ends()
    is_start_end = (ends[0] == v1 and ends[1] == v2)
    is_end_start = (ends[0] == v2 and ends[1] == v1)
    return is_start_end or is_end_start


def is_vertex_edges_excluded(exclude_edges, the_vertex, other_vertex):
    """ Returns true if any exclude_edges[the_vertex] edge entries
    match the_vertex and other_vertex."""
    result = False
    if str(the_vertex) in exclude_edges:
        for edge in exclude_edges[str(the_vertex)]:
            if is_end_a_match(edge, the_vertex, other_vertex):
                result = True
                break
    return result


def is_excluded(exclude_edges, v1, v2):
    """ Returns True if the exclude_edges entry for
    either vertex contains an edge of both vertices. """
    result = False
    if exclude_edges is None:
        return False
    result = is_vertex_edges_excluded(exclude_edges, v1, v2)
    if result is False:
        result = is_vertex_edges_excluded(exclude_edges, v2, v1)
    return result


def package_result(graph: GraphEL, distances: dict, paths: dict, start, end, exclude_edges):
    """ Returns the result as a tuple of edges. """
    result = []
    # return the label D[u] of each vertex u
    path_to_end = [str(start)] + paths[str(end)] + [str(end)]
    vertices = []
    for key in path_to_end:
        vertices.append(VertexEL(key))
    result = convert_list_vertices_to_edges(vertices, graph)
    return tuple(result)


def _bellman_ford_relaxation(dir_edge, distances, paths):
    """ Performs the Bellman-Ford relaxation operation and
    returns distances and paths. """
    u = dir_edge.tail()
    z = dir_edge.head()

    edge_weight = weight(dir_edge)
    if edge_weight <= 0:
        raise Exception("negative weight encountered.")
    
    if distances[str(u)] + edge_weight < distances[str(z)]:
        distances[str(z)] = distances[str(u)] + edge_weight
        paths[str(z)] = paths[str(z)] + [str(u)]

    return distances, paths


def _bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL,
                  exclude_edges: dict = None) -> list:
    """ Performs the bellman-ford algorithm given a weighted
    directed graph with n vertices, and a vertex v of G. """
    distances = dict()
    distances[str(start)] = 0
    paths = dict()
    num_vertices = len(graph.vertices())

    for vertex in graph.vertices():
        if vertex != start:
            distances[str(vertex)] = sys.maxsize
            paths[str(vertex)] = []
    
    for iteration in range(0, num_vertices - 1):
        for dir_edge in graph.edges():
            distances, paths = _bellman_ford_relaxation(dir_edge, distances, paths)

    if no_relaxation_possible(graph, distances):
        # if there are no edges left with potential relaxation operations then
        # return the label D[u] of each vertex u
        return package_result_end_to_start_chain(graph, distances, paths, start, end, exclude_edges)
    else:
        return None
    

def validate_start_and_end(start_to_end, end_to_start):
    """ Validates the start and end entries. Returns False
    if they have the same exact entries. """
    result = True
    if start_to_end is None or end_to_start is None:
        return result
    if len(start_to_end) != len(end_to_start):
        return result
    for index in range(0, len(end_to_start)):
        if start_to_end[index] == end_to_start[index]:
            result = False
            break
    return result


def build_exclude_dict(path):
    """ Returns a dictionary of excluded edges
    relevant to a given vertex key in the dictionary. """
    result = None
    if path is not None:
        result = dict()
        for edge in path:
            ends = edge.ends()
            result[str(ends[0])] = []
            result[str(ends[1])] = []
        for edge in path:
            ends = edge.ends()
            result[str(ends[0])] += [edge]
            result[str(ends[1])] += [edge]
    return result


def _internal(graph: GraphEL, start: VertexEL, end: VertexEL):
    """ This is the main runner of the application. """
    start_to_end = _bellman_ford(graph, start, end)
    exclude_edges = build_exclude_dict(start_to_end)
    # exclude_edges = None
    end_to_start = _bellman_ford(graph, end, start, exclude_edges)
    if not validate_start_and_end(start_to_end, end_to_start):
        end_to_start = None
    if start_to_end is not None and len(start_to_end) == 0:
        start_to_end = None
    if end_to_start is not None and len(end_to_start) == 0:
        end_to_start = None
    return (start_to_end, end_to_start)


def validate(graph: GraphEL, start: VertexEL, end: VertexEL):
    """ Validates the input arguments, throws exception if
    there are invalid arguments."""
    assert graph is not None
    assert start is not None
    assert end is not None
    assert graph.find_vertex(start) is not None
    assert graph.find_vertex(end) is not None
    return


def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    """ Returns a tuple of two tuples of edges, the first is the
    shortest path from start to end, and the second is the shortest
    path from end to start."""
    result = (), ()
    try:
        validate(graph, start, end)
        result = _internal(graph, start, end)

    except Exception as e:
        print(e)
        result = None, None
    return result
