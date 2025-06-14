#include <iostream>
#include <string>
#include "Devolution.h"

int main() {
    std::string nome;
    std::string bookName;

    std::cout << "Digite seu nome: ";
    std::getline(std::cin, nome);

    std::cout << "Olá, " << nome << ". Qual livro deseja buscar?.\n";
    std::getline(std::cin, bookName);

    Devolution devolution;
    
    if (devolution.verifyIfBookExists(bookName)) {
        std::cout << "O livro " << bookName << " está na lista.\n";
    } else {
        std::cout << "O livro "  << bookName << " NÃO está na lista.\n";
    }
    
    return 0;
}
