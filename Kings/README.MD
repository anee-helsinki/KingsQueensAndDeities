## Data used for creating networks between kings and deities

<b>Collocates_Kings.csv:</b> The connections between kings and deities with the bigram frequencies extracted from the Collocates_Kings.tsv file.

<b>Collocates_Kings.tsv:</b> The file produced with Pmizer (https://github.com/asahala/Pmizer). Shows the bigram frequences and PMI scores of co-occurring kings and deities.

<b>Duplicates:</b> A list of duplicate texts omitted from analysis. The duplicates were removed at the beginning of data processing. Thus some SAAo texts may have been omitted as duplicates although the duplicate we kept belonged to a project other than RINAP, RIAo, RIBo, and SAAo and was not included in our final dataset.

<b>Frequencies_Deities_K:</b> List of all deities and their frequencies in the 576 texts which contain at least one king and one deity in a window of 10 words.

<b>Frequencies_Kings:</b> List of all kings and their frequencies in the 576 texts which contain at least one king and one deity in a window of 10 words.

<b>Frequencies_Words:</b> List of all words and their frequencies in the 576 texts which contain at least one king and one deity in a window of 10 words.

<b>Genre_KingsTexts:</b> Genre distribution of the 576 texts which contain at least one king and one deity in a window of 10 words.

<b>Kings_gender.csv:</b> List showing the gender of the deities co-occurring with kings.

<b>RIAoKings:</b> List of the kings whose texts are analyzed from the RIAo project.

<b>RIBoKings:</b> List of the kings whose texts are analyzed from the RIBo project. All the kings attested in the RINAP and SAAo projects were included in the analysis.

<b>RoyalDeitySNA_extractor.py:</b> The script used for starting Pmizer.

<b>Texts_Kings.tsv:</b> A list of 816 texts which refer to at least one king and one deity, including some metadata.

<b>Texts_KingsInWindow.tsv:</b> A list of 576 texts which contain at least one king and one deity in a window of 10 words, including some metadata.

<b>Texts_analyzed:</b> The text file composed of 576 texts from which we extracted all connections between kings and deities within a window of 10 words.

<b>WantedKingsDeities:</b> A list of the names of kings and deities extracted.

<b>WeightedDegree_Deities_Kings:</b> Shows the weighted degree of deities, i.e. how many times each deity co-occurs with a king in a window of 10 words. The deities have to be attested five times or more in the dataset of 576 texts which contain at least one king and one deity in a window of 10 words.

<b>WeightedDegree_Kings_Deities:</b> Shows the weighted degree of kings, i.e. how many times each king co-occurs with a deity in a window of 10 words. The deities have to be attested five times or more in the dataset of 576 texts which contain at least one king and one deity in a window of 10 words.
