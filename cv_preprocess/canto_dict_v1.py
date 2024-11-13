# canto_dict_v1.py
# By Chenzi Xu 2024
# Tidy the affricates and secondary articulation w; group checked coda and vowel; add HK Cantonese new variants
import re
import pandas as pd
import sys

# Define regex patterns for affricates, glides, and codas
affricates = re.compile(r"t sʰ|t s")
glides = re.compile(r"kʰ w|k w")
codas = re.compile(r"([^\s]+) ([p,t,k])$")
rounded = ["y", "ɔ", "ʊ", "œ", "ɵ", "o", "u"]


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


# Function to add variants based on pronunciation rules
def add_variants(row):
    char, pron = row["Character"], row["Pronunciation"]
    variants = [[char, pron.strip()]]  # Start with the original entry

    if char.isascii():
        return variants

    # 1. Initial ng-/null-
    if pron.startswith("ŋ "):
        variants.append([char, pron[2:]])

    # 2. Final -ng/-n
    if pron.endswith(" ŋ"):
        variants.append([char, pron[:-2] + " n"])

    # 3. n-/l-
    if pron.startswith("n "):
        variants.append([char, "l" + pron[1:]])

    # 4. Final -m/-n
    # if pron.endswith(" m"):
    #     variants.append([char, pron[:-2] + " n"])

    # 5. s-/sh-
    if pron.startswith("s "):
        for vowel in rounded:
            if pron[2:].startswith(vowel):
                variants.append([char, "ʃ " + pron[2:]])
                break

    # 6. kw-/k- followed by /ɔ:/ or /ɔ/
    if pron.startswith("k w "):
        for vowel in rounded:
            if pron[4:].startswith(vowel):
                variants.append([char, "k " + pron[4:]])
                break

    # 7. ng/m
    if pron == "ŋ":
        variants.append([char, "m̩"])

    # 8. Specific transformation for 佢 only
    if char == "佢":
        variants.append([char, "h ɵy"])

    # Return all variants as new DataFrame rows
    return variants


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(
            "Usage: python canto_dict_v1.py <input_dictionary.txt> <output_dictionary.txt>"
        )
        sys.exit(1)

    dict_input_path = sys.argv[1]
    dict_output_path = sys.argv[2]

    # Expand with variants
    df_dict = pd.read_csv(
        dict_input_path, sep="\t", header=None, names=["Character", "Pronunciation"]
    )
    variant_rows = []
    for _, row in df_dict.iterrows():
        variant_rows.extend(add_variants(row))

    df = pd.DataFrame(variant_rows, columns=["Character", "Pronunciation"])

    # if excluding new variants
    # df = pd.read_csv(
    #     dict_input_path, sep="\t", header=None, names=["Character", "Pronunciation"]
    # )

    df["Pronunciation"] = df["Pronunciation"].apply(tidy_affricates).apply(tidy_w)
    # coda part can be commented out
    df["Pronunciation"] = df.apply(
        lambda row: tidy_coda(row["Character"], row["Pronunciation"]), axis=1
    )

    df.to_csv(dict_output_path, sep="\t", index=False, header=False, encoding="utf-8")

    print(
        f"All transformations and variants have been applied and saved to '{dict_output_path}'."
    )
