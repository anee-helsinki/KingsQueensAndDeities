# KingsQueensAndDeities

This repository contains the data used for and generated during our research for the article "The Relationships of Neo-Assyrian Kings and Queens to the Divine: A Study of Texts, Images, and Social Network Analysis".

In the article we study the networked relationship among Neo-Assyrian deities, kings, and queens. For studying the kings and deities, our text data comes from Open Richly Annotated Cuneiform Corpus (Oracc). From the texts in the Oracc projects RINAP, RIAo, RIBo, and SAAo, we used 816 texts that contain references to at least one king and one deity after we had processed the dataset. The connections between queens and deities were collected manually.

The folder in this repository contain the following:

<b>Kings:</b> The text file from which we extracted all connections between kings and deities within a window of ten words from each other. A list of the names of kings and deities extracted. A list of the texts used.

<b>Queens:</b> A listing of queens and the deities mentioned in the same text. A list of pairs of queens and deities with the number of times they were mentioned together in all the texts studies. A list of the texts used.

<b>Networks:</b> The gexf files used to create the graphs in Gephi. The Gephi project with the original graphs from which the pictures in the folder *Visualization* have been extracted/modified.

<b>lists:</b> Lists used for preprocessing of the data. Frequency lists of the words analyzed.

<b>OraccData:</b> The words extacted from the JSON files available from Oracc.
