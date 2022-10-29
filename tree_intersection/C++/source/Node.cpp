#include "Node.h"
#include <assert.h>


Node::UP_Node Node::init_new_node(const std::string& value) {
    UP_Node node(new Node());
    node->value(value);
    return std::move(node);
}

Node::UP_Node Node::init_from_json(const json& input_json) {
    UP_Node node(new Node());
    assert(input_json.size() == 1);
    for (auto& [key, value] : input_json.items()) {
        assert((value.type() == json::value_t::object) || (value.type() == json::value_t::string));
        node->value(key);
        if (value.type() == json::value_t::object) {
            for (auto& [child_key, child_value] : value.items()) {
                json child_json;
                child_json[child_key] = child_value;
                node->add_child(init_from_json(child_json));
            }
        }
        if (value.type() == json::value_t::string) {
            assert(value == "Leaf");
        }
    }
    return std::move(node);
}

Node::UP_Node Node::intersection(Node& other) const
{
    UP_Node node(new Node());
    if (this->value() == other.value()) {
        if (this->is_leaf() && other.is_leaf()) {
            node->value(this->value());
        }
        else {
            Nodes intersecting_children;
            for (auto& self_child : _children) {
                for (auto& other_child : other.children()) {
                    auto intersection_node = self_child->intersection(*other_child);
                    bool children_intersect = !(intersection_node->value().empty());
                    if (children_intersect){
                        intersecting_children.push_back(std::move(intersection_node));
                    }
                }
            }

            if (intersecting_children.size() > 0){
                node->value(this->value());
                for (auto& child : intersecting_children) {
                    // This prevents repeating intersections if they're already accounted for
                    bool repeated_intersection = false;
                    for (const auto& other_child : node->children()) {
                        if (*child == *other_child) {repeated_intersection = true;}
                    }
                    if (repeated_intersection) {
                        continue;
                    }                    
                    node->children().push_back(std::move(child));
                }
            }
        }
    }
    return std::move(node);
}

Node::json Node::to_json() const {
    json output_json;
    if (!(this->value().empty())) {
        auto& key = this->value();
        if (this->is_leaf()) {
            output_json[key] = "Leaf";
        }
        else {
            json value;
            for (const auto& child : _children) {
                auto child_json = child->to_json();
                for (auto& [child_key, child_value] : child_json.items()) {
                    value[child_key] = child_value;
                }
            }
            output_json[key] = value;
        }

    }
    assert((output_json.size() == 0) || (output_json.size() == 1));
    return output_json;
}