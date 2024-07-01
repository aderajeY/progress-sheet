class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
    
        # Initialize an empty queue
        queue = deque()

        # Process the cards from the largest to the smallest
        for card in reversed(deck):
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)

        return list(queue) 