

Linked List Intersection 2024
Programming challenge description:
-> Please read the following description carefully and think about edge cases.

You are given a collection of singly-linked lists (SLLs) and several sets of starting nodes. Each starting node is pointing at a node which is part of an SLL.

Your program should traverse each set of starting nodes and detect, whether any list in is cyclic, or any two lists in the set are intersecting.

Using recursion is not allowed. Aim to be as efficient as possible from a time complexity perspective, assume that the SLLs may be large in length (in the millions). You may use as much space as required, to build a time-efficient solution. Think carefully about edge-cases.

Input:
Your program should read lines of text from the standard input. The input consists of two subsequent blocks: the first one describes SLLs, the second on described sets of starting nodes. Example input:

a->b
r->s
b->c
s->t
q->r
a,r
b
s,b,c
We advise that you draw a diagram to help you understand the example more clearly.

An SLL is a directed graph, the out degree of each node in the graph is either zero or one, i.e. each node is pointing at most at one other node. Each line describes a directed connection between two nodes, in the form a->b, which means a is pointing at b.

Following the SLLs are sets of starting nodes. A sets of starting nodes contains a comma-separated list of nodes to start traversing from. The line a,b,c means start traversing from nodes a, b and c.

You may assume that all inputs are syntactically and semantically correct.

Constraints

->Please think about edge cases in your program that may result from the following constraints.

The out degree of a node is either zero or one. This means, for example, that a->b and a->c will not occur in the same input, because the out degree of a would be two. However, a->b and b->a may well occur in the same input, i.e. two nodes pointing at each other.

An SLL contains one or more nodes.

The input contains one or more sets of starting nodes.

A set of starting nodes contains one or more distinct and valid nodes, i.e. nodes which are part of at least one SLL.

Node identifiers are strings consisting only of a-z, A-Z and 0-9.

Output:
Traverse all sets of starting nodes. For each set of starting nodes, print the following to stdout:

CYCLE if any list in the set is cyclic
INTERSECTION if any two lists in the set intersect
OK otherwise
If you detect a cycle or an intersection in the current set of starting nodes, stop processing immediately, and continue with the next set of starting nodes.

Test 1
Test Input
Download Test 1 Input
a->b
b->c
x->y
y->z
a,x
a,b
Expected Output
Download Test 1 Output
OK
INTERSECTION
Test 2
Test Input
Download Test 2 Input
a->b
b->c
f->g
x->y
c->d
r->s
z->s
y->z
d->a
t->u
s->t
e->f
a,b
x,e
t,f
e,y,r
Expected Output
Download Test 2 Output
CYCLE
OK
OK
INTERSECTION



````
import sys

def detect_cycle(graph, start):
    slow = fast = start
    while True:
        slow = graph.get(slow)
        fast = graph.get(graph.get(fast, None), None)
        if slow is None or fast is None:
            return False
        if slow == fast:
            return True

def get_tail_path(graph, start):
    visited = set()
    current = start
    while current and current not in visited:
        visited.add(current)
        current = graph.get(current)
    return visited

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    
    # Parse input
    graph = {}
    sets = []
    parsing_edges = True

    for line in lines:
        if '->' in line:
            src, dst = map(str.strip, line.split('->'))
            graph[src] = dst
        else:
            parsing_edges = False
            sets.append([node.strip() for node in line.split(',')])

    for start_nodes in sets:
        # 1. Check for cycle in any list
        cycle_found = False
        for node in start_nodes:
            if detect_cycle(graph, node):
                print("CYCLE")
                cycle_found = True
                break
        if cycle_found:
            continue

        # 2. Check for intersection
        all_visited = set()
        intersection_found = False
        for node in start_nodes:
            path = get_tail_path(graph, node)
            if any(n in all_visited for n in path):
                print("INTERSECTION")
                intersection_found = True
                break
            all_visited.update(path)

        if not intersection_found:
            print("OK")

if __name__ == "__main__":
    main()
```
