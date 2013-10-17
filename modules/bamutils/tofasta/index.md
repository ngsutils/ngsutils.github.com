---
layout: templ
title: tofasta
module: bamutils
---
    
    Convert BAM reads back to FASTA/FASTQ sequences (mapped or unmapped)
    
    Usage: bamutils tofastq {opts} file.bam
    
    Options:
        -cs        Output color-space sequences
        -mapped    Only output mapped sequences
        -unmapped  Only output unmapped sequences
    
        -read1     Only output the first read (paired-end)
        -read2     Only output the second read (paired-end)
        -proper    Only output proper-pairs (both mapped)
    
    
