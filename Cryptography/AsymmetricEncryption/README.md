# Asymmetric Encryption

### Applications

Asymmetric encryption is commonly used to provide widely distributable encryption keys for those who wish to set up secure communications channels with another party. Because a public key can be placed in any public place, anyone who wishes to create a secure communication channel with another party, can simply utilize the public key of the opposite party in order to ensure secure comms. This also means that there are less keys that need to be generated because keys no longer need to be generate for each person who wishes to setup a secure communication channel with someone else.

Asymmetric encryption is also used to provide **cryptographic signatures**. Cryptographic signatures allow two parties the verify the identity of the opposite party by confirming that the opposite party is in possession of the private key associated with the public key. 

Another benefit of using asymmetric encryptions is that two communicating parties no longer have to meet to exchange key information. The publicly available public keys allows for both parties to setup secure communication channels whenever they desire. This tackled the **key distribution** problem issue that was concerned with symmetric encryption.

### RSA

RSA is an outdated asymmetric algorithm that uses extremely large prime numbers to create two asymmetric keys: a private key and a public key. Each key can be used individually to encrypt and decrypt data but one key alone cannot perform both operations, hence their being asymmetric. They are also asymmetric key because the public key can be extracted from the private key and not vice versa.

RSA is a deterministic algorithm meaning that if the same values are used over and over again, the same output can be predicted because the output won't change unless the initial arguments to algorithm change. In terms of RSA, provided a key and plaintext, the generated ciphertext will always be equivalent if the keys and messages do not change. This is an issue that also occurs with AES ECB, where each block of plaintext encrypted when encrypted with the same key will also produce the same encrypted block. This is why AES CBC and AES CTR, utilize the Initialivatin Vector - to remove the deterministic property of raw AES (ECB).

### Identity Confirmation

One major difference between asymmetric encryption and symmetric encryption is that symmetric encryption has inherent trust because both communication parties know and have one preshared key. Because there is only one key that both communications parties possesses, both parties can trust each other assuming they are the only ones in possession of the symmetric key. Asymmetric encryption does not permit either parties to confirm the identities of the each party because everyone has access to either parties public key and therefore anyone can encrypt messages and send them to either party, thus neither party can confirm that the messages they receive actually came from the intended senders. This is disadvantage that asymmetric encryption has over symmetric encryption but which is solved by using **digital certificates**.

