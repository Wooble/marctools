"""Page through records in a MARC file."""

from pydoc import pager

import click
import pymarc


@click.command()
@click.argument("filename")
def marcpager(filename):
    """Count records in file."""
    with open(filename, "rb") as marcfile:
        reader = pymarc.MARCReader(marcfile)
        text = "\n\n".join(str(rec) for rec in reader)
        pager(text)


if __name__ == "__main__":
    marcpager()
