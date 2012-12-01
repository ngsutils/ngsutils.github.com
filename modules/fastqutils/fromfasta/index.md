---
layout: templ
title: fromfasta
module: fastqutils
---
    
    Merges a (cs)fasta file and a qual file into a FASTQ file (on stdout)
    
    This assumes that the fasta and qual files have the same reads in the same
    order (so we don't have to load all the data and merge it). If there is a
    constant quality value, this will automatically determine if a FASTA file is
    in base-space or color-space. If the FASTA file is in color-space, the read
    sequence will be examined to determine if there is a base-space prefix and the
    length of the quality string adjusted accordingly.
    
    Any '_F3' or '_R3' suffixes at the end of the read names will be removed.
    
    
    Usage: fastqutils fromfasta {opts} filename.[cs]fasta [filename.qual]
    
    Options:
      -q val       Use a constant value for quality (Phred char; e.g. '*' = 10)
      -tag tag     add a tag as a suffix to all read names
    
                     Example:
                        -tag '_foo'
    
                     Yields:
                        @read1_foo
                        @read2_foo
                        etc...
    
    
