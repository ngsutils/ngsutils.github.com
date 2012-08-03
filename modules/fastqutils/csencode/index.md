---
layout: templ
title: csencode
module: fastq
---
    
    Convert color-space FASTQ file to encoded color-space.
    
    This is required for some tools that don't natively support color-space
    files, such as BWA. For these tools, the color-space 01234 must be converted
    into an encoded ACGTN.
    
    Usage: fastqutils csencode filename.fastq{.gz}
    
