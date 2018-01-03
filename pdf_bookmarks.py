#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse


def process(input_file, bookmarks_file, output_file, tab_spaces):
    writer = PdfFileWriter()
    reader = PdfFileReader(input_file)
    writer.appendPagesFromReader(reader)
    writer.addMetadata(reader.getDocumentInfo())

    bookmarks = {}
    for line in bookmarks_file:
        if not line.strip():
            continue
        commaIndex = line.rfind(' ')
        title = line[:commaIndex]
        pageNo = int(line[commaIndex+1:].strip())
        level = int((len(line)-len(line.lstrip()))/tab_spaces)

        parent = None
        if level > 0:
            parent = bookmarks[level-1]
        bookmarks[level] = writer.addBookmark(title, pageNo-1, parent)

    writer.write(output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add bookmarks to pdf file')
    parser.add_argument('input_pdf', metavar='input_pdf',type=argparse.FileType('rb'))
    parser.add_argument('bookmarks_file', metavar='bookmarks_file', type=argparse.FileType('r', encoding='utf-8'))
    parser.add_argument('output_pdf', metavar='output_pdf', type=argparse.FileType('wb'))
    parser.add_argument('--spaces', '-s', default=1, type=int, help='determines how many spaces should be used instead of tab, if intended by spaces')
    args = parser.parse_args()
    process(args.input_pdf, args.bookmarks_file, args.output_pdf, args.spaces)

