---
layout: templ
title: extend
module: bed
---
    
    Extends BED regions (3' only)
    
    Usage: bedutils extend {+}SIZE bedfile
    
    SIZE is what the total size of the region should be.  The size of the region
    will be extended or reduced to make the total length exactly SIZE. The region
    is always adjusted at the 3' end, respective to the given strand.
    
    If the first character of SIZE is '+', then the region is extended
    SIZE bases, regardless of how long it is to start with.
    
    
    
