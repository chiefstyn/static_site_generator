from textnode import TextType, TextNode



def main():

    node = TextNode("This is a test", TextType.BOLD, "https:/www.test.com")
    print(node)

if __name__ == "__main__":
    main()