from Graph import Graph


def draw_edge(vertex_from, vertex_to, weight):
    edge_str = f'{vertex_from} -> {vertex_to} [ label="{weight}" ];\n'
    return edge_str


def render_dot(graph):
    graph = graph.graph
    render_accumulator = "digraph G {\n"

    for vertex, top in graph.items():
        for edge in top.edges:
            to = edge['edgeName']
            weight = edge['weight']
            render_accumulator += draw_edge(vertex, to, weight)

    render_accumulator += '}'
    return render_accumulator


if __name__ == '__main__':
    graph = Graph()
    graph.read()
    print(render_dot(graph))
