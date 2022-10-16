#include "gtest/gtest.h"
#include "Node.h"
#include <nlohmann/json.hpp>

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
    trees.pushback(Node());
    trees.pushback(Node());

    trees[0].value("A");
    trees[0].add_child(Node());
    trees[0].children[0].value("B");
    trees[0].add_child(Node());
    trees[0].children[1].value("C");
    trees[0].children[1].add_child(Node());
    trees[0].children[1].children[0].value("E");
    trees[0].children[1].add_child(Node());
    trees[0].children[1].children[1].value("D");

    trees[1].value("A");
    trees[1].add_child(Node());
    trees[1].children[0].value("C");
    trees[1].children[0].add_child(Node());
    trees[1].children[0].children[0].value("F");
    trees[1].children[0].add_child(Node());
    trees[1].children[0].children[1].value("E");

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

    EXPECT_EQ (trees[0], Node::init_from_json(tree_0_json));


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
    auto intersection = trees[0].intersection(trees[1]);
    EXPECT_EQ (intersection, expected_intersection);

    // Test to_json method
    EXPECT_EQ (intersection.to_json(), expected_intersection_json);
}