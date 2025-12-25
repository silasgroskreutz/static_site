import unittest
from extract_links import extract_markdown_images, extract_markdown_links

class TestInlineMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Check out this ![cat photo](https://example.com/cat.jpg) and that ![dog image](https://example.com/dog.png)"
        )
        self.assertListEqual([
            ("cat photo", "https://example.com/cat.jpg"),
            ("dog image", "https://example.com/dog.png")
        ], matches)

    def test_extract_markdown_images_no_images(self):
        matches = extract_markdown_images(
            "This is plain text without any images or links."
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_with_spaces_in_alt(self):
        matches = extract_markdown_images(
            "Here's a photo of a ![sunset over the ocean](https://i.imgur.com/sunset.jpg)"
        )
        self.assertListEqual([("sunset over the ocean", "https://i.imgur.com/sunset.jpg")], matches)

    def test_extract_markdown_images_at_start(self):
        matches = extract_markdown_images(
            "![logo](https://company.com/logo.svg) Welcome to the site!"
        )
        self.assertListEqual([("logo", "https://company.com/logo.svg")], matches)

    def test_extract_markdown_links_single(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com/page)"
        )
        self.assertListEqual([("link", "https://example.com/page")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "Check out this [cat page](https://example.com/cat.html) and that [dog site](https://example.com/dog.html)"
        )
        self.assertListEqual([
            ("cat page", "https://example.com/cat.html"),
            ("dog site", "https://example.com/dog.html")
        ], matches)

    def test_extract_markdown_links_with_image(self):
        matches = extract_markdown_links(
            "Text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)