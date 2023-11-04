#include <gtest/gtest.h>
#include <demo/foo.hpp>

namespace demo::tests
{
TEST(demo_foo, get)
{ 
    demo::foo f;
    ASSERT_EQ(f.get(), 123);
}

}
