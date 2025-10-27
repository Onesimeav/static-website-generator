import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("b","first child",{"id": "title", "class":"Heading"})
        child2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        child3 = LeafNode("p","Some paragraph too")
        parent = ParentNode("div",[child1,child2,child3],{"class":"body"})
        self.assertEqual(
            parent.to_html(),
            '<div class="body"><b id="title" class="Heading">first child</b><a href="https://www.google.com">Click me!</a><p>Some paragraph too</p></div>'
        )