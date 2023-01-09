import matplotlib.pyplot as plt
from wordcloud import WordCloud


def plot_wordcloud(text, title):
    """Plot word cloud

    Args:
        text (str): text with tokenized words.
            
    Returns:
        Figure containing the word cloud
    """

    # Building the word cloud plot with only single words (collocations=False)
    wordcloud_pt = WordCloud(width= 800, height= 500,
                      max_font_size = 110,
                      collocations = False).generate(text)

    # Plotting the figure, setting interpolation = "bilinear" for a better 
    # figure constrast
    plt.figure(figsize=(10,7))
    plt.imshow(wordcloud_pt, interpolation='bilinear')
    plt.title(title)
    plt.axis("off")
    plt.show()
    