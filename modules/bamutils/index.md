---
layout: templ
title: bam
module: bam
---
<table cellpadding="4"><tr><td colspan="3"><h3>DNA-seq</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/basecall">basecall</a></td><td>Base caller</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/minorallele">minorallele</a></td><td>Find potential minor allele frequency (experimental)</td></tr>
<tr><td colspan="3"><h3>RNA-seq</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/cims">cims</a></td><td>Finds regions of unusual deletions (CLIP-seq)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/count">count</a></td><td>Calculates counts/RPKM for genes/BED regions/repeats</td></tr>
<tr><td colspan="3"><h3>General</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/convertregion">convertregion</a></td><td>Converts region mapping to genomic mapping</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/export">export</a></td><td>Export reads, mapped positions, and other tags</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/expressed">expressed</a></td><td>Finds regions expressed in a BAM file</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/extract">extract</a></td><td>Extracts reads based on regions in a BED file</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/filter">filter</a></td><td>Removes reads from a BAM file based on criteria</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/merge">merge</a></td><td>Combine multiple BAM files together (taking best-matches)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/removeclipping">removeclipping</a></td><td>Postprocesses a BAM file to remove all clipping from reads and alignments (experimental)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/split">split</a></td><td>Splits a BAM file into smaller pieces</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/stats">stats</a></td><td>Calculates simple stats for a BAM file</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/tag">tag</a></td><td>Update read names with a suffix (for merging)</td></tr>
<tr><td colspan="3"><h3>Conversion</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/tobed">tobed</a></td><td>Convert BAM reads to BED regions</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/tobedgraph">tobedgraph</a></td><td>Convert BAM coverage to bedGraph (for visualization)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/tofasta">tofasta</a></td><td>Convert BAM reads to FASTA sequences</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/tofastq">tofastq</a></td><td>Convert BAM reads back to FASTQ sequences</td></tr>
<tr><td colspan="3"><h3>Misc</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/check">check</a></td><td>Checks a BAM file for corruption</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/cleancigar">cleancigar</a></td><td>Fixes BAM files where the CIGAR alignment has a zero length element</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bam/readfilepos">readfilepos</a></td><td>Finds the position of a read in a BAM file</td></tr>
</table>