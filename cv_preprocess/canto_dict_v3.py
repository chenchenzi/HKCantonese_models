# canto_dict_v3.py
# By Chenzi Xu 2024
# Tidy the affricates and secondary articulation w

import re
import pandas as pd
import sys

# Define regex patterns for affricates, glides, and codas
affricates = re.compile(r"t sʰ|t s")
glides = re.compile(r"kʰ w|k w")


# Define transformation functions
def tidy_affricates(pron):
    return affricates.sub(
        lambda match: "tsʰ" if match.group(0) == "t sʰ" else "ts", pron
    )


def tidy_w(pron):
    return glides.sub(lambda match: "kʷʰ" if match.group(0) == "kʰ w" else "kʷ", pron)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(
            "Usage: python canto_dict_v3.py <input_dictionary.txt> <output_dictionary.txt>"
        )
        sys.exit(1)

    dict_input_path = sys.argv[1]
    dict_output_path = sys.argv[2]

    df = pd.read_csv(
        dict_input_path, sep="\t", header=None, names=["Character", "Pronunciation"]
    )

    df["Pronunciation"] = df["Pronunciation"].apply(tidy_affricates).apply(tidy_w)

    df.to_csv(dict_output_path, sep="\t", index=False, header=False, encoding="utf-8")

    print(
        f"All transformations and variants have been applied and saved to '{dict_output_path}'."
    )
