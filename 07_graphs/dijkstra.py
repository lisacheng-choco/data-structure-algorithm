import collections
import heapq

def dijkstra(edges, n, start_v):
    '''
    use BFS + priority queue (instead of queue)

    - time complexity: O(E+ElogV)
    - space complexity: O(E+V)
    '''
    dist = [0 for i in range(n+1)]
    adjMap = collections.defaultdict(list) #S: O(E)
    visited = set()

    for u, v, w in edges: # T: O(E)
        adjMap[u].append((v, w))
    
    minHeap = [(0, start_v)] # S: O(S)
    while minHeap:
        w, n = heapq.heappop(minHeap)
        if n in visited:
            continue

        dist[n] = w
        for nv, nw in adjMap[n]: # T: O(E)
            if nv in visited:
                continue
            heapq.heappush(minHeap, (nw+w, nv)) # T: O(logV)
        
    return dist[1:]
    


if __name__ == "__main__":
    edges = [[2,1,1],[2,3,1],[3,4,1]] #[start_v, end_v, weight]
    n = 4 # vertices are from 1 to n
    start_v = 2
    print(f"distance: {dijkstra(edges, n, start_v)}")
    '''
    answer: [1, 0, 1, 2]
    '''