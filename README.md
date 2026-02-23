# CBZ to PDF Converter

This is still a work in progress. The objective of this code is to successfully convert any type of manga/comic compressed file (`.cbz, .cbr, .zip, etc...`) to a pdf.

A cbz file normally consists of all the pages of the comic and a xml file which contains all the metadata about it, like:
- Author
- Penciller
- Title
- Series
- Chapter
- Genre (normally includes a lot of tags)
- some other informations... (like where you downloaded it)

This metadata does not apply very well to the pdf, so you have to convert it.

## Instructions

To initialize the project, make sure you have:
- A `bash terminal`
- [`python >= 3.14`](https://www.python.org/downloads/)
- The [`make`](https://www.gnu.org/software/make/) command

Then all you have to do is create the enviroment and run the program, which can be done by using the following commands:

```bash
    make venv
    make run
```
Or just use `make all` to do both of those commands. Just **be careful** to not use this all the time, use just `make run` after you created the enviroment. 
