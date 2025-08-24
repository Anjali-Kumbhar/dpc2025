from collections import defaultdict

def groupAnagrams(strs):
    group_anagram = defaultdict(list)

    for word in strs:
        s_word = ''.join(sorted(word))
        group_anagram[s_word].append(word)

    # Return the values (groups of anagrams)
    return list(group_anagram.values())
