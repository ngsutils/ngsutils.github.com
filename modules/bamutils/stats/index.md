---
layout: templ
title: stats
module: bamutils
---
    
    Calculates simple stats for a BAM file
    
    
    Usage: bamutils stats in.bam {options} {region}
    
    If a region is given, only reads that map to that region will be counted.
    Regions should be be in the format: 'ref:start-end' or 'ref:start' using
    1-based start coordinates.
    
    Options:
        -tags   tag_name{:sort_order},tag_name{:sort_order},...
    
                For each tag that is given, the values for that tag will be
                tallied for all reads. Then a list of the counts will be presented
                along with the mean and maximum values. The optional sort order
                should be either '+' or '-' (defaults to +).
    
                There are also special case tags that can be used as well:
                    MAPQ     - use the mapq score
                    LENGTH   - use the length of the read
                    MISMATCH - use the mismatch score (# mismatches) + (# indels)
                               where indels count for 1 regardless of length
    
                               Note: this requires the 'NM' tag (edit distance)
                               to be present
    
                Common tags:
                    AS    Alignment score
                    IH    Number of alignments
                    NM    Edit distance (each indel counts as many as its length)
    
                For example, to tally the "IH" tag (number of alignments) and the
                read length:
                    -tags IH,LENGTH
    
    
        -delim  char
    
                If delimiter is given, the reference names are split by this
                delimiter and only the first token is summarized.
    
        -gtf model.gtf
    
                If a GTF gene model is given, counts corresponding to exons,
                introns, promoters, junctions, intergenic, and mitochondrial
                regions will be calculated.
    
    
