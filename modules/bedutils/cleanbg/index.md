---
layout: templ
title: cleanbg
module: bedutils
---
    
    Cleanup a bedgraph file, ensuring that the coordinates are w/in the same
    range as the associated chrom.sizes file.
    
    Usage: bedutils cleanbg bedfile chrom.sizes
    
    Note: a samtools faidx (.fai) file also works as a chrom.sizes file
    
    
    
