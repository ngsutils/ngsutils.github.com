---
layout: templ
title: sort
module: fastqutils
---
    
    Sort a FASTQ file by name or sequence.
    
    This sorts a FASTQ file into a number of smaller chunks. These chunks are then merged
    together into one output written to stdout. Chunks are written to the same directory
    as the original file (unless otherwise specified).
    
    
    Usage: fastqutils sort {opts} filename.fastq
    
    Options:
        -seq      Sort by read sequence (by default it sorts by name)
    
        -T dir    Use this directory for temporary output
        -cs num   Output this many reads in each temporary file (default: 1000000)
        -nogz     Don't compress temporary files
    
    
