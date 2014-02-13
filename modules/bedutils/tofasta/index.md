---
layout: templ
title: tofasta
module: bedutils
---
    
    Extract BED regions from a reference FASTA file.
    
    Note: Sequences that are extracted will be in the same orientation as the
    BED region, unless the {-ns} option is given.
    
    Usage: bedutils tofasta {-min size} {-name} {-ns} bedfile ref.fasta
    
    Outputs the sequences of each BED region to FASTA format.
    
    Option:
    -min    The minumum size of a region
    
    -name   Include the name field of the BED region in the FASTA sequence name
            If used, the final name will be in the form:
                name|chrX:start-end[strand]
    
            The default is to not include the BED region name (only the genomic
            coordinates will be exported).
    
    -ns     Ignore the strand of a region (always return seq from the + strand)
    
    
