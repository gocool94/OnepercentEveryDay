import heapq
from collections import Counter


def rearrange_string(s):
    # Count character frequencies
    char_count = Counter(s)

    # Create a max-heap of tuples (frequency, character)
    max_heap = [(-freq, char) for char, freq in char_count.items()]
    heapq.heapify(max_heap)

    result = []

    while max_heap:
        # Extract the character with the highest frequency
        freq, char = heapq.heappop(max_heap)

        # If result is empty or the last character appended is different
        if not result or result[-1] != char:
            result.append(char)
            # Decrease the frequency and push back into the heap
            if freq + 1 < 0:
                heapq.heappush(max_heap, (freq + 1, char))
        else:
            # If the heap is empty, return since further rearrangement is not possible
            if not max_heap:
                return ""
            # Extract the next highest frequency character
            freq_next, char_next = heapq.heappop(max_heap)
            result.append(char_next)
            # Decrease the frequency and push back into the heap
            if freq_next + 1 < 0:
                heapq.heappush(max_heap, (freq_next + 1, char_next))
            # Push the original character back into the heap
            heapq.heappush(max_heap, (freq, char))

    return "".join(result)


# Example usage
s = "aabb"
print(rearrange_string(s))  # Output: "abab"
