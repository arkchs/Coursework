#include <bits/stdc++.h>
using namespace std;
struct Node
{
    int data;
    char ch;
    Node *left;
    Node *right;
    Node()
    {
        data = 0;
        ch = '-';
        left = NULL;
        right = NULL;
    }
    Node(int val, char alpha)
    {
        data = val;
        ch = alpha;
        left = NULL;
        right = NULL;
    }
    Node(int val, char alpha, Node *leftChild, Node *rightChild)
    {
        data = val;
        ch = alpha;
        left = leftChild;
        right = rightChild;
    }
};
class Solution
{
public:
    priority_queue<Node *, vector<Node *>, greater<Node *>> minHeap;
    unordered_map<char, int> freq_list;
    unordered_map<char, string> codes;
    void init() // pushes elements into the minHeap to initialize it
    {
        for (auto p : freq_list)
        {
            minHeap.push(new Node(p.second, p.first));
        }
    }
    void freq_map(string s) // lists the frequencies of appearence of the characters
    {
        for (const char &ch : s)
        {
            freq_list[ch]++;
        }

        for (auto p : freq_list)
        {
            cout << p.first << " " << p.second;
            cout << endl;
        }
    }
    void encode()
    {
        while (minHeap.size() > 1)
        {
            Node *leftChild = minHeap.top();
            minHeap.pop();
            Node *rightChild = minHeap.top();
            minHeap.pop();
            Node *parent = new Node(leftChild->data + rightChild->data, '*', leftChild, rightChild);
            minHeap.push(parent);
        }
        varLenCode(minHeap.top(), "");
    }

    void varLenCode(Node *root, string s)
    {
        if (root == NULL)
            return;
        if (root->ch != '*')
        {
            codes[root->ch] = s;
        }
        varLenCode(root->left, s + '0');
        varLenCode(root->right, s + '1');
    }
    void displayCodes()
    {
        for (auto p : codes)
        {
            cout << p.first << " " << p.second;
            cout << endl;
        }
    }
    string extract_to_code()
    {
        ifstream fileInput;

    }

    string fileOpen()
    {
        string str;
        ifstream fileInput;
        fileInput.open("sample.txt");
        char ch;
        while (fileInput)
        {
            fileInput.get(ch);
            str += ch;
        }
        return str;
    }
};
int main()
{
    Solution obj;
    string s = "AKSHAT";
    obj.freq_map(s);
    obj.init();
    obj.encode();
    obj.displayCodes();
}