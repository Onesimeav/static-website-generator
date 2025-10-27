import unittest
from textnode import TextNode,TextType
from utils import split_nodes_delimiter

class TestUtils(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,[TextNode("This is text with a ", TextType.PLAIN),TextNode("code block", TextType.CODE),TextNode(" word", TextType.PLAIN),])

    
    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle",TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.PLAIN),TextNode("bolded phrase", TextType.BOLD),TextNode(" in the middle", TextType.PLAIN),])

    def test_italic(self):
        node = TextNode("This is text with an _italic marker_",TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node],"_",TextType.ITALIC)
        self.assertEqual(new_nodes,[TextNode("This is text with an ", TextType.PLAIN),TextNode("italic marker", TextType.ITALIC)])
    
    def test_multiple_markers(self):
        node = TextNode("This is a text with **multiple** _markers_ and **we** only want _some of them_",TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node],"_",TextType.ITALIC)
        self.assertEqual(new_nodes,[TextNode("This is a text with **multiple** ",TextType.PLAIN),TextNode("markers",TextType.ITALIC),TextNode(" and **we** only want ",TextType.PLAIN),TextNode("some of them",TextType.ITALIC)])
    
    def test_multiple_nodes(self):
        node1 = TextNode("This is a text with **multiple** _markers_ and **we** only want _some of them_",TextType.PLAIN)
        node2 = TextNode("This is text with an _italic marker_",TextType.PLAIN)
        node3 = TextNode("This is text with a **bolded phrase** in the middle",TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node1,node2,node3],"_",TextType.ITALIC)
        self.assertEqual(new_nodes,[TextNode("This is a text with **multiple** ",TextType.PLAIN),TextNode("markers",TextType.ITALIC),TextNode(" and **we** only want ",TextType.PLAIN),TextNode("some of them",TextType.ITALIC),
                                   TextNode("This is text with an ", TextType.PLAIN),TextNode("italic marker", TextType.ITALIC),
                                    TextNode("This is text with a **bolded phrase** in the middle",TextType.PLAIN) ])
