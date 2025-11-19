from textnode import TextNode, TextType


def main():
    TestNode = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(TestNode)


main()
