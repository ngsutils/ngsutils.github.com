---
layout: templ
title: basecall
module: bamutils
---
    
    Base caller
    
    Given a BAM file and a genomic reference, for each position covered in the
    BAM file, show the reference base, and the number of A/T/C/G's and InDels.
    
    You can also optionally filter out all bases whose quality score is below a
    threshold, bases that aren't covered by enough reads, bases that have no
    variation compared to reference, or bases whose variation is too low.
    
    The output is a tab-delimited file that contains the following for each base:
    
    chromosome
    position (1-based)
    reference base
    # reads that contain this base
    Consensus call
    Minor call
    Average mappings (number of mappings each read covering this base has)
    Entropy
    # A calls
    # C calls
    # G calls
    # T calls
    # deletions
    # gaps
    # inserts
    
    If -showstrand is applied, a minor strand percentage is also calculated.p This
    is calculated as:
        pct = (# reads with base on plus/ # reads with base total)
        if pct > 0.5,
            pct = 1-pct
    
    Entropy is sum(a..t) { p log2 p } where p = freq(+pseudocount) / genomic freq.
    pseudo count = genomic freq * sqrt(N)
    
    We use the following genomic frequencies: A 0.3, C 0.2, G 0.2, T 0.3
    
    
    Usage: bamutils basecall {opts} in.bam {chrom:start-end}
    
    Options:
    -ref   fname   Include reference basecalls from this file
    -qual  val     Minimum base-quality level to use in calculations
                   (numeric, Sanger scale) (default 0)
    
    -count val     Report only bases with this minimum number of read-coverage
                   (matches, inserts, deletions counted) (default 0)
    
    -mask  val     The bitmask to use for filtering reads by flag
                   (default 1540 - see SAM format for details)
    
    -minorpct pct  Require a minor call to be within [pct] percent of the
                   consensus call. Calculated as #minor / #consensus.
                   (0.0 -> 1.0, default 0.01)
    -showgaps      Report gaps/splice-junctions in RNA-seq data
    -showstrand    Show the minor-strand percentages for each call
                   (0-0.5 only shows the minor strand %)
    
    