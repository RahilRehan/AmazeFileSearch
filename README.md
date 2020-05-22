# AmazeFileSearch
Trying to implement efficient searching for text in files.

## Get over with it with Hash
Create a dictionary with keys as file names and values as set of words/paras in each file.

Dict = {file1Name:set(word1, word2, ...), file2Name:set(word1, word2, ...), ...}

### Time complexity analysis with dictionaries.

Ni represents files N1, N2, N3 ....
Wi represents words in Ni

Time complexity: we might think usually -> O(max(N1, N2, N2 ...)) => O(N) assuming each insertion into set takes O(1) time and O(Ni) to insert Nx elements into set. But Wrong!

Creation time complexity: set(hash) implementation can take O(N) time to hash the string itself. So, Worst case time complexity could be -> O(max(Ni).O(max(Wi))) => O(N.W)

Search time complexity: O(N.W)

Space complexity is O(max(Ni).max(Wi)) -> O(N.W)

Optimizations:

First time the program executes, we create the dictionary from scratch and store that dictionary in file for loading next time and saving time of creation from scratch each time. So, we can eliminate overhead of creation time at every initialization.

Now, for searching in worst case as mentioned above the program could be hit by a worst case time complexity of O(N.W) as we are searching for a word(W) in files of size(N).

## Trying to Trie
This program is stored in trie.py

Read the preprocessing section to know how characters are stored in trie

Huge advantage is that, let's say if we have "amaze" and "amazing" then in our trie we just have "amazing" stored! Now, that's amazing

If you think about it, we are eliminating lot of repeating characters when storing in trie.

Time complexity for creation: O(N.W) but with many optimizations!

Search time complexity: O(Wi) where W is input.

Space complexity: O(N.W) with huge space optimizations.



## Preprocessing:

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

