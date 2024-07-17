# purifytext

purifytext is a flexible and customizable text preprocessing package designed to clean and prepare text data for natural language processing (NLP) tasks. It includes various text preprocessing steps such as removing HTML tags, lowercasing text, removing URLs, emojis, punctuation, special characters, numbers, expanding contractions, removing stopwords, stemming, and lemmatizing.

## Installation

You can install purifytext and its dependencies using pip:

```bash
pip install purifytext
```

This command will automatically install the required dependencies: `numpy`, `pandas`, `nltk`, `beautifulsoup4`, and `contractions`.

Additionally, ensure that you download the necessary NLTK data:

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

## Usage

Here's an example of how to use the purifytext package:

```python
import pandas as pd
from purifytext import clean_text

# Example DataFrame
data = {
    'text_column': [
        '<p>Hello World! Visit http://example.com 😊</p>',
        'Python is awesome!!! 123456'
    ]
}

df = pd.DataFrame(data)

# Cleaning the text
df_cleaned = clean_text(df, 'text_column', remove_HTML=True, lowercase=True, remove_urls=True,
                        remove_emojis=True, remove_punctuation=True, remove_special_characters=True,
                        remove_numbers=True, remove_whitespace=True, expand_contractions=True,
                        remove_stopwords=True, stemming=False, lemmatizing=True)

print(df_cleaned)
```

## Functions

- `text_lower(text)`: Lowercases the input text.
- `remove_punctuation(text)`: Removes punctuation from the text.
- `remove_number(text)`: Removes numbers from the text.
- `remove_whitespace(text)`: Removes extra whitespace from the text.
- `remove_contractions(text)`: Expands contractions in the text.
- `remove_HTML_tag(text)`: Removes HTML tags from the text.
- `remove_stopwords(text)`: Removes stopwords from the text.
- `lemmatize_words(text)`: Lemmatizes the words in the text.
- `stem_words(text)`: Stems the words in the text.
- `remove_urls(text)`: Removes URLs from the text.
- `remove_emojis(text)`: Removes emojis from the text.
- `remove_special_characters(text)`: Removes special characters from the text.

## Cleaning Options

The `clean_text` function allows you to specify which cleaning steps to perform using the following parameters (default values are shown):

- `remove_HTML=True`: Remove HTML tags.
- `lowercase=True`: Lowercase the text.
- `remove_urls=True`: Remove URLs.
- `remove_emojis=True`: Remove emojis.
- `remove_punctuation=True`: Remove punctuation.
- `remove_special_characters=True`: Remove special characters.
- `remove_numbers=True`: Remove numbers.
- `remove_whitespace=True`: Remove extra whitespace.
- `expand_contractions=True`: Expand contractions.
- `remove_stopwords=True`: Remove stopwords.
- `stemming=False`: Stem words.
- `lemmatizing=True`: Lemmatize words.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This package is developed by Aman Kumar Jha. For any questions or suggestions, please contact us at [vats.amankumarjha2002@gmail.com](vats.amankumarjha2002@gmail.com).
