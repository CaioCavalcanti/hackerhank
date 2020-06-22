"""
Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies.
More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords.
All edges along the path to a character contain a code digit.
If they are on the left side of the tree, they will be a 0 (zero).
If on the right, they'll be a 1 (one).
Only the leaves will contain a letter and its frequency count.
All other nodes will contain a null instead of a character, and the count of the frequency of all of it and its descendant characters.

For instance, consider the string ABRACADABRA. There are a total of 11 characters in the string.
This number should match the count in the ultimately determined root of the tree.
Our frequencies are A=5, B=2, R=2, C=1 and D=1.
The two smallest frequencies are for C and D, both equal to 1, so we'll create a tree with them.
The root node will contain the sum of the counts of its descendants, in this case 1+1=2.
The left node will be the first character encountered, C, and the right will contain D.
Next we have 3 items with a character count of 2: the tree we just created, the character B and the character R.
The tree came first, so it will go on the left of our new root node.
B will go on the right. Repeat until the tree is complete, then fill in the 1's and 0's for the edges.
The finished graph looks like:

    ϕ,11
   /    \
 A,5    ϕ,6
       /   \
     R,2   ϕ,4
          /   \
        ϕ,2   B,2
       /   \
     C,1   D,1

Input characters are only present in the leaves.
Internal nodes have a character value of ϕ (NULL).
We can determine that our values for characters are:
A - 0
B - 111
C - 1100
D - 1101
R - 10

Our Huffman encoded string is:
A B    R  A C     A D     A B    R  A
0 111 10 0 1100 0 1101 0 111 10 0
or
01111001100011010111100

To avoid ambiguity, Huffman encoding is a prefix free encoding technique.
No codeword appears as a prefix of any other codeword.
To decode the encoded string, follow the zeros and ones to a leaf and return the character there.
You are given pointer to the root of the Huffman tree and a binary coded string to decode.
You need to print the decoded string.

Complete the function decode_huff in the editor below. It must return the decoded string.
decode_huff has the following parameters:
    - root: a reference to the root node of the Huffman tree
    - s: a Huffman encoded string

Input:
There is one line of input containing the plain string, s.
Background code creates the Huffman tree then passes the head node and the encoded string to the function.
        ϕ,5
       /   \
     ϕ,2   A,3
    /   \
  B,1   C,1
s="1001011"

Output:
Output the decoded string on a single line.
ABACA
"""

import queue as Queue

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


def decodeHuff(root, s):
    current = root
    for i in range(len(s)):
        char = s[i]
        if char == "0":
            current = current.left
        else:
            current = current.right

        if current.data is not "\0":
            print(current.data, end="")
            current = root


ip = input()
freq = {}  # maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch] += 1

root = huffman_hidden()  # contains root of huffman tree

code_hidden = {}  # contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:  # if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
    toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
