import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_equal_different_url_none_vs_string(self):
        """Test inequality when one url is None and the other is a string."""
        node = TextNode("Same link text", TextType.LINK, url=None)
        node2 = TextNode("Same link text", TextType.LINK, url="https://example.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()