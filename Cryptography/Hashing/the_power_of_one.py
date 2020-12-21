#!/usr/bin/env python3
from hashlib import md5, sha256
from random import choice
from string import ascii_lowercase, ascii_uppercase, printable
from time import perf_counter

average_times = []

def the_power_of_one():
    print("1 letter input, MD5, 26 possible inputs")
    times = []
    for _ in range(10):
        preimage_seed = choice(ascii_lowercase)
        target_hash = md5(preimage_seed.encode("utf-8")).hexdigest()
        start = perf_counter()
        for c in ascii_lowercase:
            char_hash = md5(c.encode("utf-8")).hexdigest()
            if char_hash == target_hash:
                break
        end = perf_counter()
        times.append(end-start)
        print(f"Number of seconds to find target hash: {end-start:0.15f}")
    t_sum = sum(times) 
    average_time = t_sum / len(times) 
    average_times.append(average_time)
    print(f"Average time to find target hash = {average_time:0.15f}")

def the_power_of_one_but_bigger():
    print("1 letter input, MD5, all printable characters: len = 100") 
    times = []
    for _ in range(10):
        preimage_seed = choice(printable)
        target_hash = md5(preimage_seed.encode("utf-8")).hexdigest()
        start = perf_counter()
        for c in printable:
            char_hash = md5(c.encode("utf-8")).hexdigest()
            if char_hash == target_hash:
                break
        end = perf_counter()
        times.append(end-start)
        print(f"Number of seconds to find target hash: {end-start:0.15f}")
    t_sum = sum(times) 
    average_time = t_sum / len(times) 
    average_times.append(average_time)
    print(f"Average time to find target hash = {average_time:0.15f}")

# using sha256 increases the average time it takes
# to find an input that will equal the target hash.
# Using hash functions that require more computational
# time can slow down and thwart brute force attacks.
def the_power_of_one_with_sha256():
    print("1 letter input, SHA256 , 26 possible inputs")
    times = []
    for _ in range(10):
        preimage_seed = choice(ascii_lowercase)
        target_hash = md5(preimage_seed.encode("utf-8")).hexdigest()
        start = perf_counter()
        for c in ascii_lowercase:
            char_hash = sha256(c.encode("utf-8")).hexdigest()
            if char_hash == target_hash:
                break
        end = perf_counter()
        times.append(end-start)
        print(f"Number of seconds to find target hash: {end-start:0.15f}")
    t_sum = sum(times) 
    average_time = t_sum / len(times) 
    average_times.append(average_time)
    print(f"Average time to find target hash = {average_time:0.15f}")

if __name__ == "__main__":
    the_power_of_one()
    print("-"*60)
    the_power_of_one_but_bigger()
    print("-"*60)
    lowercase_printable_time_difference = average_times[1] - average_times[0]
    print(f"Compute time difference {lowercase_printable_time_difference}")

    print("-"*60)
    the_power_of_one_with_sha256()
