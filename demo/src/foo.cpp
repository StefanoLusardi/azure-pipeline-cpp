#include <demo/foo.hpp>
#include <spdlog/spdlog.h>

namespace demo
{
foo::foo()
{
}

void foo::print() const
{
    spdlog::info("Hello! This is a simple CMake project.");
}

int foo::get() const
{
    return _x;
}

}