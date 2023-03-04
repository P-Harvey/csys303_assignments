import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

def get_word_count(df: pd.DataFrame):
    array = df.to_numpy().flatten()
    array = array[array != '']
    words = set(array)
    return {word : np.count_nonzero(array == word) for word in words}, array

def load_data(user: str = '/plharvey_15/data/'):
    path = os.getcwd() + user
    df = pd.read_csv(f'{path}Blood_Meridian_McCarthy.csv', dtype = str, encoding='utf-8')
    df.fillna('', inplace=True)
    return get_word_count(df)

def plot_zipf(word_frame = None, word_array = None):
    if word_frame is None or word_array is None:
        word_frame, word_array = load_data()
    x = np.linspace(1,len(word_frame.values())+1, len(word_frame.values()))
    y = sorted(word_frame.values(), reverse=True)
    fig, ax = plt.subplots(figsize=(4, 4), dpi=1080)
    sns.scatterplot(x=x, y=y, size=1, alpha=.5, legend=False, ax=ax)
    ax.set_xlabel('Rank')
    ax.set_ylabel('Frequency')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_title('Zipf\'s Law for\nBlood Meridian by Cormac McCarthy')
    import matplotlib as mpl
    mpl.rcParams['figure.constrained_layout.use'] = True
    fig.savefig('zipf.png')
    fig.show()
    return pd.DataFrame.from_dict(word_frame, orient='index', columns=['count']), word_array

def main():
    pd_word_counts, np_word_counts = load_data()
    plot_zipf(pd_word_counts, np_word_counts)

if __name__ == "__main__":
    main()

else:
    print('Please run as main.')

# Path: plharvey_15/data/zipf.png