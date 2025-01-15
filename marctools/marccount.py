"""Counts the MARC records in a file."""
import click
import pymarc


def do_count(filename):
    with open(filename, "rb") as marcfile:
        reader = pymarc.MARCReader(marcfile)
        count = sum(1 for _ in reader)
        return count


@click.command()
@click.argument("filename")
def marccount(filename):
    """Count records in file."""
    count = do_count(filename)
    click.echo(count)


if __name__ == "__main__":
    marccount()
