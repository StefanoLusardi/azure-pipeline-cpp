#include <demo/foo.hpp>
#include <iostream>

int main(int, char**)
{
    demo::foo f;

    f.print();
    std::cout << f.get() << std::endl;
    
    return 0;
}