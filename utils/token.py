import nltk


def tokenize_frequency(df, column, row):
    """Tokenize text in dataframe

    Args:
        df (pandas df): dataframe with the text
        column (str): daframe column 
        row (int): number of row to access the text

    Returns:
        nltk.probability.FreqDist: words frequency distribution
    """
    tokens_frequency = nltk.tokenize.word_tokenize(
        df[column][row]
    )
    word_frequency = nltk.FreqDist(tokens_frequency)
    return word_frequency
