---
layout: templ
title: extend
module: bedutils
---
    
    Extends BED regions (5' and 3')
    
    Usage: bedutils extend {opts} bedfile
    
    Options:
        -5 SIZE     Extend the region SIZE bases in the 5' direction
        -3 SIZE     Extend the region SIZE bases in the 5' direction
    
    SIZE is how much the region should be extended in the corresponding
    direction. If the first character of SIZE is '=', then the region is
    extended in the corresponding direction and the length of the region
    is set to be exactly SIZE. Only one direction is allowed when SIZE
    starts with "=".
    
    Note: using an exact size may make a region smaller!
    
    
    
