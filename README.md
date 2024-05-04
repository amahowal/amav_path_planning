# Graph-Based Path Planning

[![Gitter][gitter-badge]][gitter-link]

|      CI              | status |
|----------------------|--------|
| conda.recipe         | [![Conda Actions Status][actions-conda-badge]][actions-conda-link] |
| pip builds           | [![Pip Actions Status][actions-pip-badge]][actions-pip-link] |


A project for generating various graphs and testing performance for various graph traversal algorithms. Uses [pybind11][] for C+    + graph traversal and [scikit-build-core][]. Python for generating test graphs.

[actions-badge]:           https://github.com/pybind/scikit_build_example/workflows/Tests/badge.svg
[actions-pip-link]:        https://github.com/pybind/scikit_build_example/actions?query=workflow%3APip
[actions-pip-badge]:       https://github.com/pybind/scikit_build_example/workflows/Pip/badge.svg
[actions-wheels-link]:     https://github.com/pybind/scikit_build_example/actions?query=workflow%3AWheels
[actions-wheels-badge]:    https://github.com/pybind/scikit_build_example/workflows/Wheels/badge.svg

## Test Graph Generation

**Directed Acyclic Graphs (DAGs):** Graphs with directed edges and no cycles. Number of nodes, max number of edges, and seed for random generation.
`python generate_graph.py --nodes 10 --edges 15 --graph_type DAG --weighted --weight_strategy uniform --filename "dag.json"`
`python visualize_graph.py dag.json`
    Generate nodes.
    Add edges ensuring no cycles are formed. This can be done by maintaining a topological order or using a method that connects nodes from earlier to later in a predefined order.

**Undirected Graphs:** Graphs where edges have no direction. Number of nodes, max number of edges, and connectivity requirements.
`python generate_graph.py --nodes 10 --edges 15 --graph_type undirected --weighted --weight_strategy uniform --filename "undirected.json"`
`python visualize_graph.py undirected.json`
    Generate nodes.
    Randomly connect nodes ensuring each edge is bidirectional.

**Directed Cyclic Graphs:** Graphs with directed edges that may contain cycles. Number of nodes, max number of edges.
`python generate_graph.py --nodes 10 --edges 15 --graph_type directed_cyclic --weighted --weight_strategy uniform --filename "directed_cyclic.json"`
`python visualize_graph.py undirected.json`
Similar to DAG, but allow edges that create cycles, ensuring that the graph remains connected.

**Weighted Graphs:** Graphs where edges have associated weights, which can be applied to any of the above types.

## Graph Representations
adjacency list, adjacency matrix, edge list, etc

## Installation

- Clone this repository
- `pip install .`
- `pytest`

## Example call

```python
from path_planning import graph
graph.generate_nodes(1,5)
```

## Files

This example has several files that are a good idea, but aren't strictly
necessary. The necessary files are:

* `pyproject.toml`: The Python project file
* `CMakeLists.txt`: The CMake configuration file
* `src/main.cpp`: The source file for the C++ build
* `src/path_planning/__init__.py`: The Python portion of the module. The root of the module needs to be `<package_name>`, `src/<package_name>`, or `python/<package_name>` to be auto-discovered.

These files are also expected and highly recommended:

* `.gitignore`: Git's ignore list, also used by `scikit-build-core` to select files for the SDist
* `README.md`: The source for the PyPI description
* `LICENSE`: The license file

* `.github`: configuration for [Dependabot][] and [GitHub Actions][]
* `tests/`: Tests go here

And some optional files:

* `.pre-commit-config.yaml`: Configuration for the fantastic static-check runner [pre-commit][].

This is a simplified version of the recommendations in the [Scientific-Python
Development Guide][], which is a _highly_ recommended read for anyone
interested in Python package development (Scientific or not). The guide also
has a cookiecutter that includes scikit-build-core and pybind11 as a backend
choice.

### CI Examples

There are examples for CI in `.github/workflows`. A simple way to produces
binary "wheels" for all platforms is illustrated in the "wheels.yml" file,
using [cibuildwheel][].

## License

pybind11 is provided under a BSD-style license that can be found in the LICENSE
file. By using, distributing, or contributing to this project, you agree to the
terms and conditions of this license.

[cibuildwheel]: https://cibuildwheel.readthedocs.io
[scientific-python development guide]: https://learn.scientific-python.org/development
[dependabot]: https://docs.github.com/en/code-security/dependabot
[github actions]: https://docs.github.com/en/actions
[pre-commit]: https://pre-commit.com
[pybind11]: https://pybind11.readthedocs.io
[scikit-build-core]: https://scikit-build-core.readthedocs.io
