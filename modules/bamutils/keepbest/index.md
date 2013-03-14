---
layout: templ
title: keepbest
module: bamutils
---
    
    Parses BAM file and keeps the best mapping for reads that have multiple
    mappings. If an aligner outputs multiple mappings for each read, this will
    remove mappings, keeping only the best one.
    
    Usage: bamutils keepbest {-tag tag} infile.bam outfile.bam
    
    Options:
       -tag tag    Use {tag} to determine which mappings to keep. This can be any
                   tag present in the BAM file or "MAPQ" (default: AS).
    
    
    
