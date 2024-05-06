from __future__ import annotations

from path_planning import graphing

def test_generate_dag():
    graphing.generate_graph(15, 10, "DAG")

def test_generate_undirected():
    graphing.generate_graph(15, 10, "undirected")

def test_generate_directed_cyclic():
    graphing.generate_graph(15, 10, "directed_cyclic")
