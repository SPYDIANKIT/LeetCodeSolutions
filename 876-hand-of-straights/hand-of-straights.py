class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        # Count frequencies
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1
        
        # Sort the unique cards
        unique_cards = sorted(card_count.keys())
        
        for card in unique_cards:
            while card_count[card] > 0:
                for i in range(card, card + groupSize):
                    if i not in card_count or card_count[i] == 0:
                        return False
                    card_count[i] -= 1
        
        return True
