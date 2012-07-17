---
layout: templ
title: tag
module: bamutils
---
    
    Tags each read in a BAM file
    
    Currently supported tags:
      -suffix
      -xs
    
    Usage: bamutils tag {opts} in.bamfile out.bamfile
    
    Arguments:
      in.bamfile    The input BAM file
      out.bamfile   The name of the new output BAM file
    
    Options:
      -suffix suff  A suffix to add to each read name
      -xs           Add the XS:A tag for +/- strandedness (req'd by Cufflinks)
      -tag tag      Add an arbitrary tag (ex: -tag XX:z:test)
      -f            Force overwriting the output BAM file if it exists
    
    
