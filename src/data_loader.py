import pandas as pd

def load_quran_data():

    df = pd.read_excel("data/quran.xlsx")

    # Select required columns
    df = df[
        [
            "SurahNo",
            "AyahNo",
            "SurahNameEnglish",
            "EnglishTranslation",
            "ArabicText"
        ]
    ]

    # Remove missing values
    df = df.dropna()

    # Rename columns
    df.rename(
        columns={
            "SurahNo": "surah",
            "AyahNo": "ayah",
            "SurahNameEnglish": "surah_name",
            "EnglishTranslation": "translation",
            "ArabicText": "arabic",
        },
        inplace=True,
    )

    return df


if __name__ == "__main__":

    df = load_quran_data()

    print(df.head())
    print("Total verses:", len(df))