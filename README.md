# Better names

A really simple webapp to generate Icelandic names. It fuzzy matches two names (the user's and the user's father's names) with Icelandic names (it fuzzy matches their slugs to account for different alphabets).

The webapp is at [http://my-icelandic-name.is/](http://my-icelandic-name.is/).

## Webapp technology

Webapp uses [Fuse.js](http://kiro.me/projects/fuse.html) for fuzzy matching and [JSunidecode](https://github.com/xen0n/jsunidecode/) for slugifying names. Thanks to those developers for making this a quick hack.

## Datasets

Uses a list of Icelandic names <a href="https://opingogn.is/dataset/mannanafnaskra">released as open data</a> by <a href="http://skra.is">Registers Iceland</a>.

Uses data from the <a href="http://bin.arnastofnun.is/>The Database of Modern Icelandic Inflection</a> to find the genetive form of the father's name (so it'll be correct). Correct reference would is: Beygingarlýsing íslensks nútímamáls. [The Database of Modern Icelandic Inflection.]   (n.d.) Kristín Bjarnadóttir, editor. The Árni Magnússon Institute for Icelandic Studies. Accessed 01.07.2016 from [bin.arnastofnun.is](http://bin.arnastofnun.is).

Both datasets need to be downloaded before the script can be run. The DMII should be in "Sigrúnarsnið".

## Origin story

Based on [Aure Moser's suggestion](https://twitter.com/auremoser/status/748326674572390400) I included an [ORIGINSTORY](ORIGINSTORY.md).
