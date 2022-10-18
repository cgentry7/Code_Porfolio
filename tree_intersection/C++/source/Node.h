#ifndef TREE_INTERSECTION_NODE_H
#define TREE_INTERSECTION_NODE_H

#include <vector>
#include <string>
#include <memory>
#include <nlohmann/json.hpp>

/**
 * This is the base class from which tree structures can be built
 * 
 * This probably could have used a full composite pattern, but we're just
 * going to use a simplified form of that here
 * 
 * @brief  A tree node along with its children
 */
class Node {
public:

    using UP_Node = std::unique_ptr<Node>;
    using Nodes = std::vector<UP_Node>;
    using json = nlohmann::json;

    Node() = default;
    ~Node() = default;
    Node(const Node&) = delete;            // Remove default copy constructor
    Node& operator=(const Node&) = delete; // Remove default assignment via reference

    /**
     * @brief Initializes a new node
     * @param value The value of the new node
     * @return The created Node
     */
    static UP_Node init_new_node(const std::string& value);

    /**
     * @brief Initializes a node using a JSON data structure to build out its tree structure
     * @param input_json JSON data structure with which to fully construct the node and its children
     * @return The Node created from the JSON data structure
     */
    static UP_Node init_from_json(const json& input_json);

    /**
     * @brief Getter for the Node value
     * @return  The value of the Node
     */
    const std::string& value() const { return this->_value; }

    /**
     * @brief Setter for the Node value
     * @param  The value with which to set the Node to
     */
    void value(const std::string& value) { this->_value = value; }

    /**
     * @brief Getter for the Node children
     * @return  The children of the Node
     */
    Nodes& children() { return this->_children; }

    /**
     * @brief Indicator of whether or not a Node is a Leaf (i.e. has no children)
     * @return  True if Node is Leaf, False otherwise
     */
    bool is_leaf() const { return this->_children.empty();}

    /**
     * @brief Checks for equality between two nodes
     * @param other The other node to compare against
     * @return  True if the two nodes are equivalent, False otherwise
     */
    bool operator==(const Node& other) const { return this->to_json() == other.to_json();}

    /**
     * @brief Adds a child node
     * @param child The child node to be added
     */
    void add_child(UP_Node child) { this->_children.push_back(std::move(child));}

    /**
     * @brief Determine the intersection of the node tree structure and some other node tree structure
     * @param other The other node tree structure to compare against for the intersection
     * @return  The intersection of the two node trees structures
     */
    UP_Node intersection(const Node& other) const;

    /**
     * @brief Returns the node tree structure as a JSON data structure
     * @return  The JSON data structure form of the node tree structure
     */
    json to_json() const;


private:
    std::string _value;    /*!< The value of the Node*/
    Nodes _children;       /*!< The children of the Node*/
};

#endif //TREE_INTERSECTION_NODE_H