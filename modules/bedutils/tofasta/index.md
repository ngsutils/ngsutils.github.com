---
layout: templ
title: tofasta
module: bedutils
---
    
    Extract BED regions from a reference FASTA file
    
    Usage: bedutils tofasta {-min size} {-ns} bedfile ref.fasta
    
    Outputs the sequences of each BED region to FASTA format.
    
    Option:
    -min  The minumum size of a region
    -ns   Ignore the strand of a region (always return seq from the + strand)
    
    
