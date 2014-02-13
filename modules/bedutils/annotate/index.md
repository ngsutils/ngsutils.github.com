---
layout: templ
title: annotate
module: bedutils
---
    
    Convert a BED3 file to a BED6 file with constant name, score, and strand.
    This can also be used to replace values in a BED6 file, or add RGB colors based 
    on the "name" field of a region.
    
    If you add an RGB column, then the thickStart and thickEnd columns will also be
    added and set to the region start and end respectfully (if they are missing).
    
    Usage: bedutils annotate {-name val} {-score val} {-strand val} {-rgb name value} bedfile
    
    
    
