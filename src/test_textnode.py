import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK,"url")
        node2 = TextNode("This is a plain text",TextType.PLAIN)
        self.assertNotEqual(node,node2)
    
    def test_undefined_url(self):
        node = TextNode("This is link node",TextType.LINK)
        node2 = TextNode("This is link node",TextType.LINK,None)

        self.assertEqual(node,node2)

    def test_not_equal_content(self):
        node = TextNode("This is is my life not yours",TextType.PLAIN)
        node2 = TextNode("This is a book",TextType.PLAIN)

        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()