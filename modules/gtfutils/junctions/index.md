---
layout: templ
title: junctions
module: gtfutils
---
    
    Takes a GTF gene model and a genome FASTA file and produces a splice-
    junction library in FASTA format.
    
    This will build junctions of a minimum size with a minimum overlap. Meaning,
    if the size of an exon is smaller than the minumum size, the next splice-site
    will be appended. This can result in more than one potential junction being
    included. This way potential RNA reads can be properly mapped across as many
    splice sites as is needed. The longer the reads, the more junctions that may
    be potentially included. (Maximum of 5)
    
    This will also take into account the sides of a junction to include so that
    sufficient overlap with the junction is established when reads are mapped.
    
    Usage: gtfutils junctions {opts} genes.gtf{.gz} genome.fasta
    
    Arguments
      genes.txt       Gene model in GTF format
      genome.fasta    Reference genome in FASTA or RAGZ format
                      (samtools indexed ref.fasta.fai req'd)
    
    Options
      -frag size        Number of bases on either side of the junction to include
                        [default 46]
      -min size         Minimum size of a junction
                        [default 50]
      -known            Only export known junctions
    
      -scramble         Include potential circular junctions
      -retain-introns   Include retained introns (retains introns from both the 
                        5' and 3' splice side)
    
                            ________           _______
                        ---|        |---------|       |---
                            --------           -------
                                  ******   ++++++
    
    
    
