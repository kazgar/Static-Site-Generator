from textnode import TextNode

def main():
    textnode = TextNode("This is a text node", "bold", "fake.url.address")

    print(textnode.__repr__())


main()