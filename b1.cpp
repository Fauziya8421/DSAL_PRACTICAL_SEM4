// Beginning with an empty binary search tree, 
// Construct binary search tree by inserting the values in the order given. 
// After constructing a binary tree -
        // i. Insert new node, 
        // ii. Find number of nodes in longest path from root, 
        // iii. Minimum data value found in the tree, 
        // iv. Change a tree so that the roles of the left and right pointers are swapped at every node,
        // v. Search a value

#include<iostream>
using namespace std;
// binary search tree 
struct Node{
    int data;
    Node* left;
    Node* right;

    Node(int value){
        data = value;
        left = nullptr;
        right = nullptr;
    }
};
// function to insert a new node
Node* insertNode(Node* root, int value){
    if(root == nullptr){
        return new Node(value);
    }

    if(value < root->data){
        root->left = insertNode(root->left, value);
    }else if(value > root->data) {
        root -> right = insertNode(root->right, value);
    }
    return root;
}

// time complexity is O(h) -best case {h is height} O(n) -worst case

// function to find the number of nodes in the longest pathfrom root

int findLongestPath(Node *root){
    if(root == nullptr){
        return 0;
    }

    int leftPath = findLongestPath(root->left);
    int rightPath = findLongestPath(root-> right);

    return 1 + max(leftPath, rightPath);
}

// function to find the minimum data value in the tree 

int findMinimunValue(Node* root){
    if(root == nullptr){
        cout<<" Error tree is empty"<<endl;
        return -1;
    }

    while(root->left != nullptr){
        root = root->left;
    }

    return root->data;
}


// function to change the tree so that it swap 
void swapLeftnRight(Node *root){
    if (root == nullptr){
        return;
    }

    swapLeftnRight(root->left);
    swapLeftnRight(root->right);

    swap(root->left , root->right);
}

// search for the value
bool searchValue(Node *root , int value){
    if(root == nullptr){
        return false;
    }

    if(value == root->data){
        return true;
    }
    else if(value < root->data){
        return searchValue(root->left , value);
    }
    else {
        return searchValue(root->right , value);
    }
}

void displayInorder(Node* root){
    if (root == nullptr){
        return;
    }
    displayInorder(root->left);
    cout<<root->data<<" ";
    displayInorder(root->right);
}

void displayPreorder(Node* root){
    if (root == nullptr){
        return;
    }
    cout<<root->data<<" ";
    displayInorder(root->left);
    displayInorder(root->right);
}

void displayPostorder(Node* root){
    if (root == nullptr){
        return;
    }
    displayInorder(root->left);
    displayInorder(root->right);
    cout<<root->data<<" ";
}

int main(){
    int v,data;
    Node *root = nullptr;
    cout<<"how many value";
    cin>>v;
    cout<<"enter the value";
    for(int i =0 ; i<v ; i++){
        cin>>data;
        root = insertNode(root, data);
    }
    // constructing the bonary tree
  
    // root = insertNode(root, 3);
    // root = insertNode(root, 8);
    // root = insertNode(root, 2);
    // root = insertNode(root, 4);
    // root = insertNode(root, 7);
    // root = insertNode(root, 9);
    // root = insertNode(root, 1);
    // root = insertNode(root, 6);

    // insert new node
    // root = insertNode(root , 10);

    // find the number of nodes
    int longestPath = findLongestPath(root);
    cout<<"\n longest path is "<<longestPath<<"\n";

    // min value
    int minvalue = findMinimunValue(root);
    cout << "\n min value"<<minvalue<<"\n";


 // v. Search for a value
    int valueToSearch = 6;
    bool isValueFound = searchValue(root, valueToSearch);
    if (isValueFound) {
        std::cout << "Value " << valueToSearch << " is found in the tree." << std::endl;
    } else {
        std::cout << "Value " << valueToSearch << " is not found in the tree." << std::endl;
    }

    cout<<"befor swap";
    cout<<"\n inorder ";
    displayInorder(root);
    cout<<" \n Preorder ";
    displayPreorder(root);
    cout<<"\n postorder ";
    displayPostorder(root);

    swapLeftnRight(root);
    cout<<"\n after swap";
    cout<<"\n inorder ";
    displayInorder(root);
    cout<<"\n Preorder ";
    displayPreorder(root);
    cout<<"\n postorder ";
    displayPostorder(root);
}