#include "Node.h"

Node::UP_Node Node::init_new_node(const std::string& value) {
    UP_Node node(new Node());
    node->value(value);
    return std::move(node);
}

Node::UP_Node Node::init_from_json(const json& input_json) {
    UP_Node node(new Node());
    return std::move(node);
}

Node::UP_Node Node::intersection(const Node& other) const
{
    UP_Node intersection(new Node());
    return std::move(intersection);
}

Node::json Node::to_json() const {
    json json_data;
    return json_data;
}