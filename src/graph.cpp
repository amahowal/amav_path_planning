#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

// Include your own C++ library headers
#include "astar.h"

int generate(int node_number, int strategy) {
    return 1000*node_number;
}

int describe(int node_number, int strategy) {
    return 1000*node_number;
}

namespace py = pybind11;

PYBIND11_MODULE(graph, m) {
    m.doc() = R"pbdoc(
        Path Planning
        -----------------------

        .. currentmodule:: path_planning

        .. autosummary::
           :toctree: _generate

           generate
           describe
           generate_nodes
           describe_nodes
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

    // Bindings for A*
    m.def("generate_nodes", &generate_nodes);
    // py::class_<ClassFromLibA>(m, "ClassFromLibA")
    //    .def(py::init<>())
    //    .def("method", &ClassFromLibA::method);

    // Bindings for Library B
    // m.def("function_from_lib_b", &function_from_lib_b);
    // py::class_<ClassFromLibB>(m, "ClassFromLibB")
    //     .def(py::init<>())
    //     .def("method", &ClassFromLibB::method);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
