from main import Trie




def add_all_keys(values):
    the_trie = Trie()
    for value in values:
        print(value)
    the_trie.add_keys(values)
    for value in values:
        found = the_trie.find(value)
        print("finding value {value}, results in {found}".format(value=value, found=found))
    return the_trie