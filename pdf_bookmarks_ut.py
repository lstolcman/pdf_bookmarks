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

        self.test_files = {
                1 : ('example-tabs.txt', 'example-bookmarks-tabs.pdf'),
                2 : ('example-2spaces.txt', 'example-bookmarks-2spaces.pdf'),
                4 : ('example-4spaces.txt', 'example-bookmarks-4spaces.pdf'),
                8 : ('example-8spaces.txt', 'example-bookmarks-8spaces.pdf')
                }

    def testAddBookmarks(self):
        for i in self.test_files:
            with open('example-bookmark-in.pdf', 'rb') as input_file,\
            open(self.test_files[i][0], 'r', encoding='utf-8') as bookmarks_file,\
            open(self.test_files[i][1], 'wb') as output_file:
                pdf_bookmarks.process(input_file, bookmarks_file, output_file, i)

if __name__ == "__main__":
    unittest.main()

