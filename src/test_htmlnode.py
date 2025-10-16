import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_html(self):
        node1 = HTMLNode("div",None,None,{"class":"part","id":"part-2"})
        props =  ' class="part" id="part-2"'

        self.assertEqual(node1.props_to_html(),props)