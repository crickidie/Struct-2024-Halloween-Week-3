##############################################################
# created by: Deborah Sanchez
# email: debsanchez.business@outlook.com
# date: 9-27-2024
# desc: This sample Python project teaches you how to parse
# html from a website or api. This project is week 3 of a 5 week 
# project which can be downloaded at https://github.com/crickidie.
##############################################################

##############################################################
# This sample code uses the 'html.parser' object.
# To install this object, open terminal within
# your python session and run 'pip install html.parser'
##############################################################

import os
from html.parser import HTMLParser

dataArray = []

class HTMLParserCls(HTMLParser):
    inTag = False

    def handle_starttag(self, tag, attrs):
        if (tag != 'div' or attrs.count == 0):
            return

        for a in attrs:
            if (a[1] == 'the_class'):
                self.inTag = True

    def handle_endtag(self, tag):
        if (tag == 'div' and self.inTag == True):
            self.inTag = False

    def handle_data(self, data):
        if (self.inTag):
            dataArray.append(data)


def parse_html():
    parser = HTMLParserCls()
    html = "<html><head><title>Sample Parser</title></head><body><div class='the_class'>The quick brown fox</div><div class='another_class'>This should not be returned</div><div class='the_class'>jumps over the lazy dog.</div></body></html>"

    parser.feed(html)
    return dataArray

def main():
    os.system('cls')

    rtn = parse_html()

    print(rtn)

    input("Press enter to exit.")

if __name__ == "__main__":
    main()
