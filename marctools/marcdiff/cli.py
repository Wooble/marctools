import click

import marctools.marcdiff.core


@click.command(
    help="""Compare 2 files of MARC records. If OUTFILE is not given,
output will be written to 'marcdiff_output.html' in the working directory."""
)
@click.argument("file1", type=click.Path())
@click.argument("file2", type=click.Path())
@click.argument("outfile", type=click.Path(), default="marcdiff_output.html")
@click.option(
    "-m", "--matchpoint", default="001", help="MARC tag to match on (default 001)"
)
def run(file1, file2, outfile, matchpoint):
    marctools.marcdiff.core.html_compare(file1, file2, outfile, matchpoint)


if __name__ == "__main__":
    run()
