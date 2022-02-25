import pymarc
import difflib

FILE_START = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type"
          content="text/html; charset=UTF-8" />
    <title></title>
    <style type="text/css">
    table.diff {font-family:Courier; border:medium;}
        .diff_header {background-color:#e0e0e0}
        td.diff_header {text-align:right}
        .diff_next {background-color:#c0c0c0}
        .diff_add {background-color:#aaffaa}
        .diff_chg {background-color:#ffff77}
        .diff_sub {background-color:#ffaaaa}
    </style>
</head>
<body>"""

FILE_END = """
</body>
</html>
"""

def html_compare(file1, file2, outfile):
    """Compare 2 files of MARC records and write HTML diff"""
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(outfile, 'w', encoding='utf-8') as out:
        out.write(FILE_START)
        r1 = pymarc.MARCReader(f1)
        r2 = pymarc.MARCReader(f2)

        rec2 = next(r2)
        for rec1 in r1:
            rec_id = rec1['001'].data

            if rec2['001'].data != rec_id:
                pass
                #out.write(difflib.HtmlDiff().make_table(str(rec1).splitlines(), ['']))
            else:
                out.write(difflib.HtmlDiff(wrapcolumn=85).make_table(str(rec1).splitlines(), str(rec2).splitlines(), context=True))
                try:
                    rec2 = next(r2)
                except StopIteration:
                    pass
        out.write(FILE_END)


