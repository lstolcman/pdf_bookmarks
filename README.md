# pdf_bookmarks

pdf_bookmarks is simple app designed to help with maintaining bookmarks in PDF files.

![Sample output](example_bookmarks.png)

## Running

`python pdf_bookmarks.py <input-pdf> <bookmarks-file> <output-pdf>`

## Bookmarks file format
```
First level page_num
<tab>First sublevel page_num
<tab><tab>First sub-sublevel page_num
<tab>Second sublevel page_num
Second level page_num
```
Example file is `example.txt`

## Testing

`python pdf_bookmarks_ut.py`

Script should produce two pdf files - input without bookmarks and output with bookmarks based on `example.txt`

## Building standalone executable with PyInstaller

`pyinstaller --onefile --noconsole pdf_bookmarks_gui.py`

`pyinstaller --onefile pdf_bookmarks.py`

