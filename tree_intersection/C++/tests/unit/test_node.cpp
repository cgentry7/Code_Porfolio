#include "gtest/gtest.h"
#include "Node.h"
#include <memory>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

TEST(TestNode, test1) {
/*
    Test Trees:
       A            A                A
    ┌─────┐         │                │
    │     │         │                │
    B   ┌─C─┐     ┌─C─┐     ─────►   C
        │   │     │   │              │
        │   │     │   │              │
        E   D     F   E              E
 */

    // Manually Constructe Trees
    Node::Nodes trees;
    trees.push_back(Node::init_new_node("A"));
    trees[0]->add_child(Node::init_new_node("B"));
    trees[0]->add_child(Node::init_new_node("C"));
    trees[0]->children()[1]->add_child(Node::init_new_node("E"));
    trees[0]->children()[1]->add_child(Node::init_new_node("D"));

    trees.push_back(Node::init_new_node("A"));
    trees[1]->add_child(Node::init_new_node("C"));
    trees[1]->children()[0]->add_child(Node::init_new_node("F"));
    trees[1]->children()[0]->add_child(Node::init_new_node("E"));


    // Test tree construction via JSON
    auto tree_0_json = json::parse(R"(
        {"A" :
            {"B" : "Leaf",
             "C" : 
                {"E" : "Leaf",
                 "D" : "Leaf"
                }
            }
        }
    )");

    EXPECT_EQ (*trees[0], *Node::init_from_json(tree_0_json));


    // Test intersection method
     auto expected_intersection_json = json::parse(R"(
        {"A" :
            {"C" : 
               {"E" : "Leaf"
               }
            }
        }
    )");
    auto expected_intersection = Node::init_from_json(expected_intersection_json);
    auto intersection = trees[0]->intersection(*trees[1]);
    EXPECT_EQ (*intersection, *expected_intersection);

    // Test to_json method
    EXPECT_EQ (intersection->to_json(), expected_intersection_json);
}