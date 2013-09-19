---
layout: templ
title: bamutils
module: bamutils
---
<table cellpadding="4"><tr><td colspan="3"><h3>DNA-seq</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/basecall">basecall</a></td><td>Base/variant caller</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/minorallele">minorallele</a></td><td>Find potential minor allele frequency (experimental)</td></tr>
<tr><td colspan="3"><h3>RNA-seq</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/cims">cims</a></td><td>Finds regions of unusual deletions (CLIP-seq) (experimental)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/count">count</a></td><td>Calculates counts/RPKM for genes/BED regions/repeats (also CNV)</td></tr>
<tr><td colspan="3"><h3>General</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/convertregion">convertregion</a></td><td>Converts region mapping to genomic mapping</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/export">export</a></td><td>Export reads, mapped positions, and other tags</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/expressed">expressed</a></td><td>Finds regions expressed in a BAM file</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/extract">extract</a></td><td>Extracts reads based on regions in a BED file</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/filter">filter</a></td><td>Removes reads from a BAM file based on criteria</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/innerdist">innerdist</a></td><td>Calculate the inner mate-pair distance from two BAM files</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/keepbest">keepbest</a></td><td>Parses BAM file and keeps the best mapping for reads that have multiple mappings</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/merge">merge</a></td><td>Combine multiple BAM files together (taking best-matches)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/nearest">nearest</a></td><td>Find the nearest annotated BED region for each read (experimental)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/pcrdup">pcrdup</a></td><td>Find and mark PCR duplicates (experimental)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/removeclipping">removeclipping</a></td><td>Postprocesses a BAM file to remove all clipping from reads and alignments (experimental)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/renamepair">renamepair</a></td><td>Postprocesses a BAM file to rename pairs that have an extra /N value</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/split">split</a></td><td>Splits a BAM file into smaller pieces</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/stats">stats</a></td><td>Calculates simple stats for a BAM file</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/tag">tag</a></td><td>Update read names with a suffix (for merging)</td></tr>
<tr><td colspan="3"><h3>Conversion</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/tobed">tobed</a></td><td>Convert BAM reads to BED regions</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/tobedgraph">tobedgraph</a></td><td>Convert BAM coverage to bedGraph (for visualization)</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/tofasta">tofasta</a></td><td>Convert BAM reads to FASTA sequences</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/tofastq">tofastq</a></td><td>Convert BAM reads back to FASTQ sequences</td></tr>
<tr><td colspan="3"><h3>Misc</h3></td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/check">check</a></td><td>Checks a BAM file for corruption</td></tr>
<tr><td>&nbsp;</td><td><a href="/modules/bamutils/cleancigar">cleancigar</a></td><td>Fixes BAM files where the CIGAR alignment has a zero length element</td></tr>
</table>