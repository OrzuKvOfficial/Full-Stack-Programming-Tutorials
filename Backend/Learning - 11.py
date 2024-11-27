import heapq

def dijkstra(graph, start):
    # Har bir tugunga eng qisqa masofani boshlang'ich qiymat bilan o'rnatamiz
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    
    # Tugunlarni tekshirish uchun prioritet navbat (heapq) ishlatiladi
    priority_queue = [(0, start)]  # (masofa, tugun)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Agar navbatdagi masofa avval qayd etilgan masofadan katta bo'lsa, uni o'tkazib yuboramiz
        if current_distance > shortest_distances[current_node]:
            continue
        
        # Qo'shni tugunlarni tekshiramiz
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Agar yangi masofa kichikroq bo'lsa, yangilaymiz
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_distances

# Grafikni aniqlaymiz
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Boshlang'ich tugun
start_node = 'A'

# Algoritmni ishga tushiramiz
result = dijkstra(graph, start_node)

# Natijani chop etamiz
print("Eng qisqa masofalar:")
for node, distance in result.items():
    print(f"{start_node} → {node}: {distance}")
