#%%
import wikipedia

def get_page_content(page_name):
    try:
        return wikipedia.page(page_name).content
    except wikipedia.exceptions.DisambiguationError as e:
        try:
            return wikipedia.page(e.options[0]).content 
        except Exception as e:
            return ""
    except Exception as e:
        return ""


#%%
with open('wiki.txt', 'w') as f:
    for _ in range(2500):
        text = get_page_content(wikipedia.random(1))
        f.write(text)
        f.write('\n\n')

        if _ % 25 == 0:
            print(f"Writing aricle {_}...")
print("Finished writing.")
# %%
