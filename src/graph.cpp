#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

int generate(int node_number, int strategy) {
    return 1000*node_number;
}

int describe(int node_number, int strategy) {
    return 1000*node_number;
}

namespace py = pybind11;

PYBIND11_MODULE(graph, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: path_planning

        .. autosummary::
           :toctree: _generate

           generate
           describe
           visualize
    )pbdoc";

    m.def("generate", &generate, R"pbdoc(
        Generate a graph

        The goal here is to generate different types of graphs that I can solve with different solvers
            to explore the performance across solver implementations.
    )pbdoc");

    m.def("describe", &describe, R"pbdoc(
        Describe the graph

        Some other explanation about the describe function.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
