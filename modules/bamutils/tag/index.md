---
layout: templ
title: tag
module: bamutils
---
    
    Tags each read in a BAM file
    
    Currently supported tags:
      -suffix
      -xs
      -orig-ref
      -orig-pos
      -orig-cigar
      -junction
    
    Usage: bamutils tag {opts} in.bamfile out.bamfile
    
    Arguments:
      in.bamfile    The input BAM file
      out.bamfile   The name of the new output BAM file
    
    Options:
      -suffix suff     A suffix to add to each read name
    
      -xs              Add the XS:A tag for +/- strandedness (req'd by Cufflinks)
    
      -tag tag         Add an arbitrary tag (ex: -tag XX:Z:test)
    
      -junction tag    Predicts junction spans from CIGAR alignment
    
      -orig-ref tag    Add a new tag with the original reference name (For
                       example, in a region-based BAM will be converted to
                       standard coordinates)
    
      -orig-pos tag    Add a new tag with the original reference pos
    
      -orig-cigar tag  Add a new tag with the original CIGAR alignment
    
      -f               Force overwriting the output BAM file if it exists
    
    
