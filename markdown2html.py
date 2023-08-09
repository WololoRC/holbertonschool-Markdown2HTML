#!/usr/bin/python3
"""
Parse a Markdown file and turns into HTML
"""
import sys


if __name__ == "__main__":

    def un_list(lines):
        """ Gives a ul tags to lines and wraps with <ul> """

        wrap = ["<ul>\n",]

        for item in lines:
            text = item.replace('-', '')
            text.strip()
            wrap.append(f"<li>{text.strip()}</li>\n")

        wrap.append("</ul>\n")

        return "".join(wrap)

    def headings(lines):
        """ Gives a headings tags to lines """

        wrap = []

        for item in lines:
            lvl = item.count('#')
            text = item.replace('#', '')
            wrap.append(f"<h{lvl}>{text.strip()}</h{lvl}>\n")

        return "".join(wrap)

    def read_file(src, dest):
        """
        Parse Mardown and saves as HTML.

        Each line is goona be wraped by his own specific tag function
        and returned as a string saved on @render list, then each item
        on render was goona be write in @dest as a string.

        attrs:
            src: source file.
            dest: destination of source file.
        """
        fun_dic = {
            '#': headings,
            '-': un_list
        }

        aux = []
        render = []

        try:
            with open(f"{src}", 'r', encoding='utf-8') as file:
                content = file.read()
        except FileNotFoundError:
            sys.stderr.write(f"Missing {src}\n")
            sys.exit(1)

        for mark in fun_dic:
            aux.clear()
            for line in content.split('\n'):
                if mark in line:
                    aux.append(line)
            render.append(fun_dic.get(mark)(aux))

        with open(f"{dest}", 'w', encoding='utf-8') as to_html:
            for line in render:
                to_html.write("".join(line))

    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    elif sys.argv[1].endswith('.md'):
        read_file(sys.argv[1], sys.argv[2])
        sys.exit()

    else:
        sys.exit(0)
