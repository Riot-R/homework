def heapify(list, n, i):
    head = i 
    left = 2*i+1 
    right = 2*i+2  

    if left < n and list[i] < list[left]:
        head = left
    
    if right < n and list[head] < list[right]:
        head = right
    
    if head != i:
        list[i], list[head] = list[head], list[i] 
        heapify(list, n, head)

def heap_sort(list):
    n=len(list)
   
    for i in range(n // 2 , 0, -1):
        heapify(list, n, i)

    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i] 
        heapify(list, i, 0)

list = []
while True:
    n = input("Enter number (enter 'stop' to quit the loop): ")
    if n=="stop":
        break
    if n.isdigit():
        i = int(n)
        list.append(i)
    else:
        print("Input is 1not valid")

print(list)
heap_sort(list)
print(f"New list:\n{list}")