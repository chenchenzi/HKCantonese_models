# canto_dict_v2.py
# By Chenzi Xu 2024
# Tidy the affricates and secondary articulation w; group checked coda and vowel

import re
import pandas as pd
import sys

# Define regex patterns for affricates, glides, and codas
affricates = re.compile(r"t sʰ|t s")
glides = re.compile(r"kʰ w|k w")
codas = re.compile(r"([^\s]+) ([p,t,k])$")
# rounded = ["y", "ɔ", "ʊ", "œ", "ɵ", "o", "u"]


# Define transformation functions
def tidy_affricates(pron):
    return affricates.sub(
        lambda match: "tsʰ" if match.group(0) == "t sʰ" else "ts", pron
    )


def tidy_w(pron):
    return glides.sub(lambda match: "kʷʰ" if match.group(0) == "kʰ w" else "kʷ", pron)


def tidy_coda(char, pron):
    # Only apply transformation if the character is non-ASCII (i.e., Chinese characters)
    if not char.isascii():
        return codas.sub(r"\1\2", pron)
    return pron


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(
            "Usage: python canto_dict_v2.py <input_dictionary.txt> <output_dictionary.txt>"
        )
        sys.exit(1)

    dict_input_path = sys.argv[1]
    dict_output_path = sys.argv[2]

    # if excluding new variants
    df = pd.read_csv(
        dict_input_path, sep="\t", header=None, names=["Character", "Pronunciation"]
    )

    df["Pronunciation"] = df["Pronunciation"].apply(tidy_affricates).apply(tidy_w)

    df["Pronunciation"] = df.apply(
        lambda row: tidy_coda(row["Character"], row["Pronunciation"]), axis=1
    )

    df.to_csv(dict_output_path, sep="\t", index=False, header=False, encoding="utf-8")

    print(f"All transformations have been applied and saved to '{dict_output_path}'.")
