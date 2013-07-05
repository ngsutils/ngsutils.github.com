---
layout: templ
title: tile
module: fastqutils
---
    
    For each read in a FASTQ file, split it into smaller (overlapping) chunks.
    Fragments are defined by their length and offset. For example, if the length
    is 35 and the offset is 10, sub-reads will be 1->35, 11->45, 21->55, etc... If
    the offset and the length are the same, then the fragments will not overlap.
    
    Output is a set of (gzip compressed) FASTQ files
    
    Usage: fastqutils tile {opts} filename.fastq{.gz} out_template
    
    Options:
      -len val         Length of each fragment (default: 35)
      -offset val      Offset for each fragment (default: 10)
    
      -gz              gzip compress the output FASTQ files
    
    
    
