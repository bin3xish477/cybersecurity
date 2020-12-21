# Hashing
**Fun Fact**: MD5 can express `2^128` unique values which is equivalent to `340,282,366,920,938,463,463,374,607,431,768,211,456`. *Yikes*.

**What makes a good cryptographic hash function?**
1. Preimage resistance
2. Second-preimage
3. Collision resistance

### Preimage Resistance
The preimage for a hash function, H, and a message digest, m, is equal to the set of inputs, x, passed to the hash function that will yield the value m: `H(x) = m`.
 - the process of obtaining an input value that will produce a known message digest is called **inverting**.
 - a good hash function ensures that the amount of computation required to obtain a value of x that will produce the known message digest is infinite. In other words, as of today's computing capability, it's nearly impossible to obtain a value for x that will result in the value of m.
 
### Second-preimage Resistance
Second-preimage resistance means that if you already possess an input and know it's corresponding digest, it will be nearly impossible to obtain another value from the preimage that will produce the same digest. 

### Collision Resistance
To say a hash function is collision resistant means that it is hard to find any two inputs that will result in the same message digest. The **avalanche property** ensures that an alteration to the initial input to hash functions and other cryptographic ciphers will result in a drastically different output. For example: the MD5 hash of the string "aa" is `4124bc0a9335c27f086f24ba207a4912` and the MD5 hash for the string "ab" is `187ef4436122d1cc2f40dc2b92f0eba0`. As shown, a single character changed in the string "aa" to "ab" yielded a completely unpredictable and diverse output. 
