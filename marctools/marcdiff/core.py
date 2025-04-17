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


def get_value(record, field):
    f = record[field]
    if f is not None:
        return f.value()


def data_from_file(f, matchpoint):
    data = {"problems": {"missing matchpoints": [], "duplicate matchpoints": []}}
    for rec in f:
        rec_id = get_value(rec, matchpoint)
        if rec_id is None:
            data["problems"]["missing matchpoints"].append(rec)
        elif rec_id in data:
            data["problems"]["duplicate matchpoints"].append(rec)
        else:
            data[rec_id] = rec
    return data


def html_compare(file1, file2, outfile, matchpoint):
    """Compare 2 files of MARC records and write HTML diff"""
    with open(file1, "rb") as f1, open(file2, "rb") as f2, open(
        outfile, "w", encoding="utf-8"
    ) as out:
        out.write(FILE_START)
        r1 = pymarc.MARCReader(f1)
        r2 = pymarc.MARCReader(f2)

        data_1 = data_from_file(r1, matchpoint)
        data_2 = data_from_file(r2, matchpoint)

        for rec_id in data_1:
            if rec_id == "problems":
                continue
            if rec_id in data_2:
                out.write(
                    difflib.HtmlDiff(wrapcolumn=85).make_table(
                        str(data_1[rec_id]).splitlines(),
                        str(data_2[rec_id]).splitlines(),
                        context=True,
                    )
                )
                del data_2[rec_id]
            else:
                out.write(
                    difflib.HtmlDiff().make_table(
                        str(data_1[rec_id]).splitlines(), ["No match"], context=True
                    )
                )
        for rec_id in data_2:
            if rec_id == "problems":
                continue
            out.write(
                difflib.HtmlDiff().make_table(
                    ["No match"], str(data_1[rec_id]).splitlines(), context=True
                )
            )

        for problem_type in data_1["problems"]:
            for rec in data_1["problems"][problem_type]:
                out.write(
                    difflib.HtmlDiff().make_table(
                        str(rec).splitlines(),
                        [f"PROBLEM: {problem_type}"],
                        context=True,
                    )
                )
        for problem_type in data_2["problems"]:
            for rec in data_2["problems"][problem_type]:
                out.write(
                    difflib.HtmlDiff().make_table(
                        [f"PROBLEM: {problem_type}"],
                        str(rec).splitlines(),
                        context=True,
                    )
                )

        out.write(FILE_END)
