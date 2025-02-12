
#include <stdlib.h>
#include <stdio.h>
// An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
//
// If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

// I will start with just implementing a regular linked list...

// Create node
struct node {
    int data;
    struct node *both;
};

// Returns the xor of two node adresses
struct node* xor(struct node *a, struct node *b) {
    return (struct node*) ((uint64_t) (a) ^ (uint64_t) (b));
}

// Get node at given index
struct node* get(int index, struct node *head) {
    if (index == 0) {
        return head;
    }
    struct node *prev = NULL;
    struct node *next = NULL;
    struct node *current = head;
    int j = 0;
    // Traverse down to last element
    while(j < index+1 && current) {
        next = xor(prev, current->both);
        prev = current; //When this loop ends, we know prev is the last element in the list
        current = next;
        j++;
    }
    return prev;
}

// Append element to end of list
void add(struct node *element, struct node *head) {
    struct node *prev = NULL;
    struct node *next = NULL;
    struct node *current = head;
    // Traverse down to last element
    while(current) {
        next = xor(prev, current->both);
        prev = current; //When this loop ends, we know prev is the last element in the list
        current = next;
    }
    prev->both = xor(prev->both, element);
    element->both = xor(prev, NULL);
}

// Print content of linked list
void printLinkedList(struct node *p) {
    printf("Printing list:\n");
    struct node *prev = NULL;
    struct node *next = NULL;
    struct node *current = p;
    while(current) {
        printf("%d\n", current->data);
        next = xor(prev, current->both);
        prev = current;
        current = next;
    }
}

int main() {
    // Initialize nodes
    struct node *head;
    struct node *one = NULL;
    struct node *two = NULL;
    struct node *three = NULL;
    struct node *four = NULL;

    // Allocate memory
    one = malloc(sizeof(struct node));
    two = malloc(sizeof(struct node));
    three = malloc(sizeof(struct node));
    four = malloc(sizeof(struct node));

    // Assign data values
    one->data = 1;
    two->data = 2;
    three->data = 3;
    four->data = 4;

    //Connect node
    one->both = xor(NULL, two);
    two->both = xor(one, three);
    three->both = xor(two, NULL);

    // Save address of first node in head
    head = one;

    // Print the thing:
    printLinkedList(head);
    // Add #4
    add(four, head);
    // Print it again:
    printLinkedList(head);
    // Get node at index = 2
    int index = 2;
    printf("Value of node at index: %d, value: %d", index, get(index, head)->data);

    // Free the memory
    free(one);
    free(two);
    free(three);
    free(four);
}
