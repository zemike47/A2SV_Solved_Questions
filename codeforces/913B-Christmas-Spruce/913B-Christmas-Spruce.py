# print(children)

for child in range(2, n + 1):
    parent = int(input())
    children[parent].append(child)

# print(children)

for node in range(1, n + 1):

    # non-leaf node
    if children[node]:

        leaf_children = 0

        for child in children[node]:
            # print(child)
            if len(children[child]) == 0:
                leaf_children += 1
                
        

        if leaf_children < 3:
            print("No")
            exit()

print("Yes")