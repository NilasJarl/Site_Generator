import sys
from generate_page import static_to_public, generate_page_recursive



 



def main(basepath):
    static_to_public("static", "docs")
    generate_page_recursive(basepath,"content", "template.html", "docs")

if __name__ == "__main__":
    basepath = "/"
    if sys.argv[1]:
        basepath = sys.argv[1]
    
    main(basepath)