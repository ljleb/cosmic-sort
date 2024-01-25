from collections import Counter
import random
import math


def cosmic_sort(a, *, redundancy: int = 1, simulate_corruption: bool = False):
    redundancy = 2 * redundancy + 1
    original_copies = [list(a) for _ in range(redundancy)]

    while True:
        if simulate_corruption:
            corrupt_random_bits(a)
            for i in range(redundancy):
                corrupt_random_bits(original_copies[i])

        majority_freq_map = get_majority_freq_map(original_copies)
        correct_to_frequency_map(a, majority_freq_map)
        for i in range(redundancy):
            correct_to_frequency_map(original_copies[i], majority_freq_map)

        if is_sorted(a):
            return a


def is_sorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def get_majority_freq_map(copies):
    majority_freq = Counter()
    for items_i, items in enumerate(zip(*copies)):
        majority_freq += {Counter(items).most_common(1)[0][0]: 1}

    return majority_freq


def correct_to_frequency_map(l, majority_freqs):
    freqs = Counter(l)
    freqs[next(iter(freqs.keys()))] += majority_freqs.total() - freqs.total()
    freqs_diff = freqs.copy()
    freqs_diff.subtract(majority_freqs)
    missing = iter({v: c for v, c in freqs_diff.items() if c < 0}.items())
    extra = iter({v: c for v, c in freqs_diff.items() if c > 0}.items())
    try:
        e_m, c_m = 0, 0
        e_x, c_x = 0, 0
        while True:
            if c_m <= 0:
                e_m, c_m = next(missing)
            if c_x <= 0:
                e_x, c_x = next(extra)
            l[l.index(e_x)] = e_m
            c_m -= 1
            c_x -= 1
    except StopIteration:
        pass


def corrupt_random_bits(l):
    selector = -1
    for _ in range(math.ceil(1.5*math.log2(len(l) + 1))):
        selector &= random.getrandbits(len(l))

    if selector < 0:
        return

    for i in range(math.ceil(math.log2(selector + 1))):
        if selector & (1 << i):
            bits_count = math.ceil(math.log2(l[i] + 1))
            bits_to_flip = -1
            for _ in range(math.ceil(1.5*math.log2(bits_count + 1))):
                bits_to_flip &= random.getrandbits(bits_count)
            if bits_to_flip > 0:
                l[i] ^= bits_to_flip


print(cosmic_sort([2, 1], redundancy=4, simulate_corruption=True))
