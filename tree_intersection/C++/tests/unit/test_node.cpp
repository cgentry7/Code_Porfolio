#include "gtest/gtest.h"
#include "Node.h"

TEST(blaTest, test1) {

    EXPECT_EQ (Node::bla (0),  0);
    EXPECT_EQ (Node::bla (10), 20);
    EXPECT_EQ (Node::bla (50), 100);
}