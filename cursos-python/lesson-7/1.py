def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    # Complete steps 2 and 3 here
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")

graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph

print(prettify_graph())