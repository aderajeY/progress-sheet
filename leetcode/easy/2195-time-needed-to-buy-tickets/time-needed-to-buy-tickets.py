class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(i, tickets[i]) for i in range(len(tickets))])
        time = 0

        while queue:
            index, ticket_count = queue.popleft()
            time += 1
            ticket_count -= 1

            if index == k and ticket_count == 0:
                return time

            if ticket_count > 0:
                queue.append((index, ticket_count))
        