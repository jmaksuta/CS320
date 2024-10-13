"""
Lab 06 - HW6
64.2 Depth-First Traversal
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

from edgegraph import VertexEL, EdgeEL, GraphEL, parse_graph_file

EXPLORED = 1
UNEXPLORED = 2


def get_end_vertex(edge, start):
    """ Returns the end vertex of edge that is opposite of start. """
    end_vertex = None
    ends = edge.ends()
    if ends[0] == start:
        end_vertex = ends[1]
    if ends[1] == start:
        end_vertex = ends[0]
    return end_vertex


def is_unexplored(paths, edge):
    return (paths.get(str(edge)) != EXPLORED)


def _internal_dfs(graph, start, paths=None, depth=0):
    discover_path = []
    if paths is None:
        paths = dict()
    paths[str(start)] = EXPLORED
    discover_path.append(start)
    for edge in graph.incident(start):
        if is_unexplored(paths, edge):
            end_vertex = get_end_vertex(edge, start)

            if is_unexplored(paths, end_vertex):
                paths[str(edge)] = "Discovery"
                route, paths = _internal_dfs(graph, end_vertex, paths, depth + 1)
                discover_path += route
            else:
                paths[str(edge)] = "Back"

    if depth == 0:
        result = tuple(discover_path)
    else:
        result = (discover_path, paths)
    return result


def validate(graph, start):
    """ Validates the input argments. """
    assert graph is not None
    assert start is not None
    assert start in graph.vertices()
    
    
def dfs(graph, start):
    result = (())
    try:
        validate(graph, start)
        result = _internal_dfs(graph, start)
        
    except Exception as e:
        result = (())
    return result
