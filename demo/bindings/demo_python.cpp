#include <pybind11/pybind11.h>
#include <demo/foo.hpp>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace bindings
{
PYBIND11_MODULE(pydemo, m) {
    m.doc() = "Demo module docs";

    pybind11::class_<demo::foo>(m, "create")
    .def(pybind11::init<>())
    .def("get", &demo::foo::get)
    .def("print", &demo::foo::print)
    ;

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY((VERSION_INFO));
#else
    m.attr("__version__") = "dev";
#endif
}

}