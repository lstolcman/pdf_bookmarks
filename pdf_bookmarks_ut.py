#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import pdf_bookmarks

class TestBookmark(unittest.TestCase):
    def setUp(self):
        writer = PdfFileWriter()
        for i in range(40):
            writer.addBlankPage(210, 297)
        with open('example-bookmark-in.pdf', 'wb') as f:
            writer.write(f)

    def testAddBookmarks(self):
        with open('example-bookmark-in.pdf', 'rb') as input_file,\
        open('example.txt', 'r', encoding='utf-8') as bookmarks_file,\
        open('example-bookmark-out.pdf', 'wb') as output_file:
            pdf_bookmarks.process(input_file, bookmarks_file, output_file)


if __name__ == "__main__":
    unittest.main()

