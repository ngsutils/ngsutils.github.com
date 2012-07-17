---
layout: templ
title: bfq
module: fastqutils
---
    
    Converts to/from BFQ (binary-compressed FASTQ format)
    
    This stores the name/seq/qual information for a FASTQ file in a highly compact
    binary format. This stores the sequence + qual in an 8-bit encoded format. It
    can store more than one sequence+qual fragments for each read, meaning that it
    efficiently deals with paired-end data (with support for upto 256 fragments).
    
    To save paired end data, include one file for each fragment, or use a single
    FASTQ file with one record for each fragment (consecuatively using the same
    name for each fragment).
    
    BFQ also compresses the read data with zlib, so it is very compact. (This can
    be turned off for faster processing).
    
    Finally, the file includes an MD5 checksum at the end so that file integrity
    be confirmed at any point.
    
    Usage: fastqutils bfq {opts} infile1.fastq {infile2.fastq ... }
           fastqutils bfq -d {opts} filename.bfq
           fastqutils bfq -t filename.bfq
    
    Options:
        -d              Decode BFQ file to stdout in FASTQ format (one-file)
        -t              Test file integrity
        -i              Display information about the file and fragments
    
        -h              Display this message
    
    Encoding options:
        -c              Output to stdout
        -f              Force overwriting existing files
        -fn             Include a name for a fragment (there can be as
                        many of these are there are fragments)
        -desc text      Include a description of the file
        -descf fname    The contents of the file fname will be used as the
                        description (this can be a binary file)
        -nc             Disable compression
        -o fname        Name of the output file
                        (defaults to input filename.bfq)
        -q              Quiet (no progress bar)
    
    Decoding options:
        -desc           Extract the description only (to stdout)
    
    
    
