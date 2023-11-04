#pragma once

namespace demo
{
class foo
{
public:
    explicit foo();
    void print() const;
    int get() const;
    
private:
    int _x {123};
};

}