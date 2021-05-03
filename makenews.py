#%%
from nltk.corpus import reuters


# %%
articles = [" ".join(reuters.words(f)) for f in reuters.fileids()]
with open('reuters.txt', 'w') as f:
    for article in articles:
        f.write(article)
        f.write('\n\n')

# %%
fileids = reuters.fileids()
with open('reuters.txt', 'w') as f:
    for file_id in reuters.fileids():
        f.write(reuters.raw(file_id))
        f.write('\n\n')

# %%
from nltk.corpus import brown
print(brown.raw(categories='learned'))
# %%
