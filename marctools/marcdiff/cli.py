import click

import marctools.marcdiff.core


@click.command(
    help="""Compare 2 files of MARC records. file2 must be a subset of the records
in file1, with existing records in the same order in both files. If OUTFILE is not given,
output will be written to 'marcdiff_output.html' in the working directory."""
)
@click.argument("file1", type=click.Path())
@click.argument("file2", type=click.Path())
@click.argument("outfile", type=click.Path(), default="marcdiff_output.html")
def run(file1, file2, outfile):
    marctools.marcdiff.core.html_compare(file1, file2, outfile)
