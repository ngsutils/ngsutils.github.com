---
layout: templ
title: peakheight
module: bamutils
---
    
    Find the size of a set of defined peaks (BED) in a BED file.
    
    If you have a set of defined peak regions (in the form of a BED file), this
    will return the size characteristics of the region for a given BAM file.
    
    The following fields will be added to the BED file:
        maximum peak size
        total unique reads
        total coverage (sum of coverage over each base)
        coverage density (total coverage / length)
    
    Usage: bamutils peakheight {options} bamfile peaks.bed
    
    
