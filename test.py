import re
from collections import defaultdict

def get_tokens(file_path):
    def read_log_file(file_path):
        with open(file_path, 'r') as file:
            logs = file.readlines()
        return logs

    def preprocess_logs(logs):
        # Tokenize each log entry into words
        tokenized_logs = [re.findall(r'\b\w+\b', log.lower()) for log in logs]
        return tokenized_logs


    logs = read_log_file(file_path)
    tokenized_logs = preprocess_logs(logs)

    # Print the first few tokenized logs
    return tokenized_logs

file_path = "C:/Users/sashinag/OneDrive - Cisco/Desktop/log_test.txt"
tokens = get_tokens(file_path)
# print(tokens)




def get_stats(vocab):
    """
    Given a vocabulary (dictionary mapping words to frequency counts), returns a 
    dictionary of tuples representing the frequency count of pairs of characters 
    in the vocabulary.
    """
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    """
    Given a pair of characters and a vocabulary, returns a new vocabulary with the 
    pair of characters merged together wherever they appear.
    """
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

def get_vocab(data):
    """
    Given a list of strings, returns a dictionary of words mapping to their frequency 
    count in the data.
    """
    # print(data)

    vocab = defaultdict(int)
    for line in data:
        word = line
        vocab[' '.join(list(word)) + '</w>'] += 1

    print(vocab)    
    return vocab

def byte_pair_encoding(data, n):
    """
    Given a list of strings and an integer n, returns a list of n merged pairs
    of characters found in the vocabulary of the input data.
    """
    vocab = get_vocab(data)
    for i in range(n):
        pairs = get_stats(vocab)
        best = max(pairs, key=pairs.get)
        vocab = merge_vocab(best, vocab)
    return vocab

# Example usage:
data = [j for i in tokens for j in i]
# print(tokens)

n = 10
bpe_pairs = byte_pair_encoding(data, n)
print(bpe_pairs)
