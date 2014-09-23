---
layout: templ
title: split
module: fastqutils
---
    
    Splits a FASTQ file into multiple smaller files
    
    Output is a set of gzip compressed FASTQ files
    
    Usage: fastqutils split {opts} filename.fastq{.gz} out_template num_chunks
    
    Options:
      -ignorepaired    Normally for paired-end samples, each read of the pair is
                       written to the same file. With this option, paired reads
                       can be written to any file. This is useful for splitting a
                       paired FASTQ file back into separate files for each
                       fragment. (Only for interleaved paired-end files).
    
      -gz              gzip compress the output FASTQ files
    
    
    
