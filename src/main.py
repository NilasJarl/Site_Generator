import os, shutil
from generate_page import static_to_public, generate_page_recursive



 



def main():
    static_to_public("static", "public")
    generate_page_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()