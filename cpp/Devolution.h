#ifndef DEVOLUTION_H
#define DEVOLUTION_H

#include <vector>
#include <string>
#include <algorithm> 

class Devolution {
private:
    std::vector<std::string> books;
    std::string toLower(const std::string& str) const;

public:
    Devolution();
    bool verifyIfBookExists(const std::string& bookName) const;

};

#endif
