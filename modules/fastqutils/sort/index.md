---
layout: templ
title: sort
module: fastqutils
---
    
    Sort a FASTQ file by name or sequence.
    
    This sorts a FASTQ file into a number of smaller chunks. These chunks are then merged
    together into one output written to stdout. Chunks are written to the same directory
    as the original file (unless otherwise specified).
    
    fastqutils sort [-name | -seq] {-T dir} filename.fastq
    
