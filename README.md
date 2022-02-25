# marctools
Command line tools for MARC21 records


marccount - counts the MARC records in a file.

marcpager - page through MARC records

marcdiff:

**marcdiff** generates an HTML diff of files containing MARC21 records.

Currently, the files must use field 001 as a consistent record ID between
the files, and all records in the second file must be present in the first 
file.

Records present in the first file and not the second file will not be displayed.

    Usage: marcdiff [OPTIONS] FILE1 FILE2 [OUTFILE]
    
      Compare 2 files of MARC records. file2 must be a subset of the records in
      file1, with existing records in the same order in both files. If OUTFILE
      is not given, output will be written to 'marcdiff_output.html' in the
      working directory.
    
    Options:
      --help  Show this message and exit.
