---
layout: templ
title: readfilepos
module: bam
---
    
    Finds the realtive position of a read or reference:position in a BAM file.
    This is returned as a line number out of the total number of lines in the
    file.
    
    This is useful for estimating the amount of time required for certain types
    of processing.
    
    
    Usage: bamutils readfilepos {-read read_name} {-pos chr:pos}  bamfile
    
    
