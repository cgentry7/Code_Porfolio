#include <iostream>
#include <vector>
#include <string>
#include <nlohmann/json.hpp>
#include <fstream>
#include "Node.h"


using json = nlohmann::json;

int main(int argc, char** argv) {

    if (argc != 2) {
        std::cout << std::endl;
        std::cout << "tree_intersection called incorrectly!"   << std::endl;
        std::cout << "Correct Usage Example:"                  << std::endl;
        std::cout << "    tree_intersection <input_file_name>" << std::endl << std::endl;
        return -1;
    }

    std::string input_file_name = argv[1];

    Node::Nodes trees;
    std::ifstream input_file(input_file_name);
    auto json_data = json::parse(input_file);
    input_file.close();

    for (int i = 0; i < 2; ++i) {
        trees.push_back(Node::init_from_json(json_data[i]));
    }

    auto intersection = trees[0]->intersection(*trees[1]);
    std::ofstream output_file("output.json");
    output_file << intersection->to_json().dump(4);
    output_file.close();

    return 0;
}