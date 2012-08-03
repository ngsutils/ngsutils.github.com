---
layout: templ
title: reduce
module: bed
---
    
    Reduces BED regions to overlap them. The BED file *must* be sorted in order
    to merge them.
    
    Usage: bedutils reduce {opts} bedfile
    
    -extend num{,num}   Extend the BED region {num} bases 5' and 3'
                        Can either a single number (extend the same in both
                        direction) or a comma delimited pair of numbers where the
                        first number extends the region in the 5' direction and
                        the second number extends the region in the 3' direction.
    
    -clip               Only extend the reads to find overlapping regions, don't
                        extend the edges of the regions.
    
    -c                  Output the number of regions merged as the score (count).
                        Otherwise, the scores for all of the regions are added
                        together.
    
    -nostrand           Ignore strand information when merging regions
    
    Unknown option: -h
    
    Reduces BED regions to overlap them. The BED file *must* be sorted in order
    to merge them.
    
    Usage: bedutils reduce {opts} bedfile
    
    -extend num{,num}   Extend the BED region {num} bases 5' and 3'
                        Can either a single number (extend the same in both
                        direction) or a comma delimited pair of numbers where the
                        first number extends the region in the 5' direction and
                        the second number extends the region in the 3' direction.
    
    -clip               Only extend the reads to find overlapping regions, don't
                        extend the edges of the regions.
    
    -c                  Output the number of regions merged as the score (count).
                        Otherwise, the scores for all of the regions are added
                        together.
    
    -nostrand           Ignore strand information when merging regions
    
    
