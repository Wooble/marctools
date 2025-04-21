# marctools
Command line tools for MARC21 records


marccount - counts the MARC records in a file.

marcpager - page through MARC records

marcdiff:

**marcdiff** generates an HTML diff of files containing MARC21 records.

Records that exist in only one of the files will be listed at the end of 
the file, along with any records that did not contain the matchpoint
MARC tag (defaults to 001).


    Usage: marcdiff [OPTIONS] FILE1 FILE2 [OUTFILE]
    
      Compare 2 files of MARC records. If OUTFILE is not given, output will be 
      written to 'marcdiff_output.html' in the working directory.
    
    Options:
      --help  Show this message and exit.
      -m TAG, --matchpoint=[TAG]    use MARC tag TAG as matchpoint. Defaults to 001
