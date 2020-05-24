import datetime
import os
import pickle


class TrieNode:
    def __init__(self):
        self.chars = [None] * 37
        self.which_files = set()
        self.isEnd = False


class AmazeFileSearchTrie:

    def __init__(self):
        """
        Timer setup and runs the run, lol!
        """
        start = datetime.datetime.now()
        self.run()
        end = datetime.datetime.now()
        print("The total execution time is ",
              (end - start).total_seconds()% 86400, "sec")

    def run(self):
        """
        Our run function sets up the trie and
        this also handles input and output function,
        until you want them to be abstracted out!
        """
        self.trie_setup()
        yo_input = self.input_handler()
        self.output_handler(yo_input)

    def trie_setup(self):
        """
        This function handles trie itself.
        If trie exists then we use it else,
        we create a new one!(Time consuming brughh!)
        """
        list_of_files = self.get_files_list()
        self.root = self.get_trie()
        if not self.root:
            self.root= TrieNode()
            self.initialize_trie(list_of_files)
            self.save_trie(self.root)

    def get_files_list(self):
        """
        Lets get out files in given folder
        """
        list_of_files = os.listdir(os.getcwd() + "/dictionary")
        return list_of_files

    def get_trie(self):
        """
        If dict exists return dict else return None
        """
        if os.path.exists("data_trie.pkl"):
            a_file = open("data_trie.pkl", "rb")
            output = pickle.load(a_file)
            a_file.close()
            return output
        return None

    def save_trie(self, mytrie):
        """
        Saving the dict for saving time
        """
        a_file = open("data_trie.pkl", "wb")
        pickle.dump(mytrie, a_file)
        a_file.close()

    def initialize_trie(self, list_of_files):
        """
        Creating the trie for first time
        """
        for file in list_of_files:
            with open(os.getcwd() + "/dictionary/" + str(file), "r+", encoding='utf-8') as read_file:
                file_name = os.path.basename(read_file.name)
                list_of_lines = read_file.read().splitlines()
                for line in list_of_lines:
                    self.insert(line, file_name)

    def insert(self, word, file_name):
        """
        Trie insertion function! cool bruh!
        """
        temp = self.root
        for w in range(len(word)):
            idx = self.getCharMap(word[w])
            if temp.chars[idx] == None:
                temp.chars[idx] = TrieNode()
            temp = temp.chars[idx]
        temp.isEnd = True
        temp.which_files.add(file_name)

    def input_handler(self):
        """
        Takes input and returns it
        """
        print("Input: ")
        yo_input = eval(input())
        return yo_input

    def output_handler(self, yo_input):
        """
        runs the search and outputs the result
        """
        startF = datetime.datetime.now()
        print("Output: ")
        for ele in yo_input:
            found = self.lets_search_trie(ele)
            if len(found):
                print(ele + " is available in " + " and ".join(found)+".")
            else:
                print(ele + " not found! or check input!")
        endF = datetime.datetime.now()
        print("The test case execution time is ",
              (endF - startF).total_seconds()% 86400, "sec")


    def lets_search_trie(self, ele):
        """
        heart of the search
        """
        output = []
        temp = self.root 
        for w in range(len(ele)): 
            idx = self.getCharMap(ele[w]) 
            if not temp.chars[idx]: 
                return []
            temp = temp.chars[idx] 
  
        if temp != None and temp.isEnd:
            output = temp.which_files
        return output



    def getCharMap(self, c):
        """
        Mapping characters to store in trie
        """
        out = ord(c)-ord('a')
        if out == -65:
            return 26
        if out == -59:
            return 27
        if out == -58:
            return 28
        if out == -57:
            return 29
        if out == -56:
            return 30
        if out == -53:
            return 31
        if out == -52:
            return 32
        if out == -51:
            return 33
        if out == -50:
            return 34
        if out == -38:
            return 35
        if out == 65182:
            return 36
        return out

afst = AmazeFileSearchTrie()
