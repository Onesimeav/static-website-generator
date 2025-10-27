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

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is a bold text", TextType.BOLD)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value,"This is a bold text")
        self.assertEqual(html_node.props,None)

    def test_italic_text(self):
        node = TextNode("This is some italic text",TextType.ITALIC)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value,"This is some italic text")
        self.assertEqual(html_node.props,None)
    
    def test_code_text(self):
        node = TextNode("This is some code text",TextType.CODE)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag,"code")
        self.assertEqual(html_node.value,"This is some code text")
        self.assertEqual(html_node.props,None)
    
    def test_link_text(self):
        node = TextNode("This is some link text",TextType.LINK, "url")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value,"This is some link text")
        self.assertEqual(html_node.props,{"href":"url"})

    def test_image_text(self):
        node = TextNode("This is some image text",TextType.IMAGE,"url")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.value,"")
        self.assertEqual(html_node.props_to_html(),' src="url" alt="This is some image text"')


if __name__ == "__main__":
    unittest.main()