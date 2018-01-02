#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader
import pdf_bookmarks

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox



class BookmarksGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        parent.title('PDF Bookmarks writer')
        self.pdf_fn = ''
        self.bookmarks_fn = ''
        self.output_fn = ''
        self.parent = parent

        self.pdf= tk.Text(self.parent, height=1, width=50, state=tk.DISABLED)
        self.txt = tk.Text(self.parent, height=1, width=50, state=tk.DISABLED)

        self.pdf.grid(row=0, column=0)
        self.txt.grid(row=1, column=0)
        tk.Button(self.parent, text='Select pdf file', width=20, command=self.load_pdf).grid(row=0, column=1, padx=3,pady=2)
        tk.Button(self.parent, text='Select bookmark file', width=20, command=self.load_bookmark).grid(row=1, column=1, padx=3)
        tk.Button(self.parent, text='Select output file', width=20, command=self.save_pdf).grid(row=2, column=1, padx=3, pady=2)

    def load_pdf(self):
        fn = filedialog.askopenfilename(filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
        if fn:
            self.pdf_fn = fn
            self.pdf.config(state=tk.NORMAL)
            self.pdf.delete(1.0, tk.END)
            self.pdf.insert(tk.END, self.pdf_fn)
            self.pdf.config(state=tk.DISABLED)

    def load_bookmark(self):
        fn = filedialog.askopenfilename(filetypes=(("Bookmarks files", "*.txt"), ("All files", "*.*")))
        if fn:
            self.bookmarks_fn = fn
            self.txt.config(state=tk.NORMAL)
            self.txt.delete(1.0, tk.END)
            self.txt.insert(tk.END, self.bookmarks_fn)
            self.txt.config(state=tk.DISABLED)

    def save_pdf(self):
        if self.pdf_fn and self.bookmarks_fn:
            fn = filedialog.asksaveasfilename(filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
            if fn:
                if not fn.endswith('.pdf'):
                    fn = fn + '.pdf'
                self.output_fn = fn
                with open(self.pdf_fn, 'rb') as pdf_in,\
                open(self.bookmarks_fn, 'r', encoding='utf-8') as bookmarks,\
                open(self.output_fn, 'wb') as pdf_out:
                    pdf_bookmarks.process(pdf_in, bookmarks, pdf_out)
        else:
            tk.messagebox.showwarning("Warning", "Select input pdf and/or bookmarks file")


if __name__ == '__main__':
    root = tk.Tk()
    BookmarksGUI(root)
    root.mainloop()

