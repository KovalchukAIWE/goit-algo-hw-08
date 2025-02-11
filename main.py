import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # З'єднуємо їх
        combined = first + second
        total_cost += combined
        
        # Додаємо результат назад у купу
        heapq.heappush(cables, combined)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables)}")
