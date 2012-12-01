---
layout: templ
title: csencode
module: fastqutils
---
    
    Convert color-space FASTQ file to encoded color-space.
    
    This is required for some tools that don't natively support color-space
    files, such as BWA. For these tools, the color-space 01234 must be converted
    into an encoded ACGTN.
    
    0 -> A
    1 -> C
    2 -> G
    3 -> T
    4,5,6,. -> N
    
    Usage: fastqutils csencode filename.fastq{.gz}
    
