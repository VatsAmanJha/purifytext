from .text_preprocessing import *

def clean_text(dataframe, column_name, remove_HTML=True, lowercase=True, remove_urls=True, 
               remove_emojis=True, remove_punctuation=True, remove_special_characters=True, 
               remove_numbers=True, remove_whitespace=True, expand_contractions=True, 
               remove_stopwords=True, stemming=False, lemmatizing=True):
    
    dataframe_copy = dataframe.copy()
    print("\n=== Cleaning Process ===")

    if remove_HTML:
        print("\n⬇️ Removing HTML Tags ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_HTML_tag)

    if lowercase:
        print("\n⬇️ Lowercasing Text ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_text_lower)

    if remove_urls:
        print("\n⬇️ Removing URLs ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_urls)

    if remove_emojis:
        print("\n⬇️ Removing Emojis ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_emojis)

    if remove_punctuation:
        print("\n⬇️ Removing Punctuation ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_punctuation)

    if remove_special_characters:
        print("\n⬇️ Removing Special Characters ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_special_characters)

    if remove_numbers:
        print("\n⬇️ Removing Numbers ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_number)

    if remove_whitespace:
        print("\n⬇️ Removing Whitespace ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_whitespace)

    if expand_contractions:
        print("\n⬇️ Expanding Contractions ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_contractions)

    if remove_stopwords:
        print("\n⬇️ Removing Stopwords ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_remove_stopwords)

    if stemming:
        print("\n⬇️ Stemming Words ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_stem_words)
    if lemmatizing:
        print("\n⬇️ Lemmatizing Words ⬇️")
        dataframe_copy[column_name] = dataframe_copy[column_name].apply(func_lemmatize_words)

    print("\n=== Cleaning Completed ===\n")
    return dataframe_copy

if __name__ == "__main__":
    pass
