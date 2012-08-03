---
layout: templ
title: fromfasta
module: fastq
---
    
    Merges a (cs)fasta file and a qual file into a FASTQ file (on stdout)
    
    This assumes that the fasta and qual files have the same reads in the same
    order (so we don't have to load all the data and merge it).
    
    
    Usage: fastqutils fromfasta {opts} filename.[cs]fasta [filename.qual]
    
    Options:
      -q val       Use a constant value for quality (Phred char; e.g. '*' = 10)
      -tag tag     add a tag as a suffix to all read names like: readname:suffix
    
    
