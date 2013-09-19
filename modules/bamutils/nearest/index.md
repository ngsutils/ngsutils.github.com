---
layout: templ
title: nearest
module: bamutils
---
    
    For each read, find the nearest annotated region from a BED file.
    
    For example, if you have a BED file with the transcription starting site (TSS)
    for all genes in the genome, this will find the nearest TSS for each read, and
    report the distance to the site.
    
    Usage: bamutils nearest {-max val} filename.bam regions.bed
    
    Options:
      -max    The maximal distance to look for a nearest region
              (default: 100K)
    
    
