# AmazeFileSearch
Trying to implement efficient searching for text in files.

# GEt it over with Hash
Time complexity analysis of first approach usign just dictionaries.

First time the program executes, we store everythin parent dictionary with key value pairs of filenames(keys) and set values(words in files).

Time complexity which we might think usually -> O(max(N1, N2, N2 ...)) => O(N) assuming each insertion into set takes O(1) time and O(Nx) to insert Nx elements into set. But Wrong!

set implementation can take O(N) time to hash the string itself. So, Worst case Time complexity could go upto -> O(max(Nx.(O(max(Wi))))) => O(N.W)

Space complexity is O(Files.max(words in files))

Optimizations:

Once dictionary is computed, no need for creation of dictionary everytime the program runs! Save it!

Now, for searching in worst case as mentioned above the program could be hit by a worst case time complexity of O(N.W)! as we are searching for a word(W) in files of size(N).

# Trying Trie
More optimizations(Dictionary Trie), this program is stored in trie.py:

Different characters in our list:

[' ', '&', "'", '(', ')', ',', '-', '.', '/', ';', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '\ufeff']

total chars: 37

ord values (ele-'a')
sorted_ords
[-65, -59, -58, -57, -56, -53, -52, -51, -50, -38, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 65182]

normal_ords
[32, 38, 39, 40, 41, 44, 45, 46, 47, 59, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65279]

Sample Input:
["north america", "grand view-on-hudson", "yunlin county", "south east", "a.t.", "building cnstrctn - general contractors", "engineering, accounting, research, management & related svcs", "refrigeration", "connecticut"]


Time complexity analysis with trie:
O(max(len(input[i])))
Space O()
