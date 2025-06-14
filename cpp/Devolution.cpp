#include "Devolution.h"

Devolution::Devolution() {
    books = {
        "Dom Quixote",
        "1984",
        "O Pequeno Príncipe",
        "Cem Anos de Solidão",
        "A Revolução dos Bichos",
        "O Senhor dos Anéis",
        "Harry Potter e a Pedra Filosofal",
        "Orgulho e Preconceito",
        "O Hobbit",
        "O Código Da Vinci"
    };
}

std::string Devolution::toLower(const std::string& str) const {
    std::string lower = str;
    std::transform(lower.begin(), lower.end(), lower.begin(),
                   [](unsigned char c) { return std::tolower(c); });
    return lower;
}

bool Devolution::verifyIfBookExists(const std::string& bookName) const {
    for (const auto& book : books) {
        if (toLower(book) == toLower(bookName)) {
            return true;
        }
    }
    return false;
}
