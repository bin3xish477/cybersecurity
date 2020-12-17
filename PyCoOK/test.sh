for i in $(seq 1 2);
do
    # Testing Base encodings 
    pycook base -85 -64 -32 -16 "Hello, World!"
    pycook base -85 -64 -32 -16 setup.sh
    echo ""

    # Testing binary conversion
    pycook bin -b "Hello, World!"
    pycook bin -f "0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100"
    echo ""

    # Testing hex encodings
    pycook hex -x "Hello, World!";
    pycook hex -f "74657374696e672074657374696e67" 
    echo ""

    # Testing URL stuff
    pycook url -e "q=testing&r=true&name=john wick"
    pycook url -d "q%3Dtesting%26r%3Dtrue%26name%3Djohn%20wick" 
    pycook url -dp "q%3Dtesting%26r%3Dtrue%26name%3Djohn+wick"
    pycook url -ep "q=test&r=true&name=john wick"
    pycook url -pq "q=test&r=true&name=john wick"
    echo ""

    # Testing Hashing Stuff
    #   - testing hashes for file
    echo -e "\nTesting hashes for file argument\n"
    pycook hash /etc/passwd -a md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_512 blake2b blake2s
    #   - testing hashes for string
    echo -e "\nTesting hashes for string argument\n"
    pycook hash "Hello, World!" -a md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_512 blake2b blake2s

    # Testing Pattern Stuff
    pycook ptn -c -l 100
    pycook ptn -g -m "61543061"

    # Testing Reverse Shells generation
    pycook revs -s bash_tcp_1 -p 1234 10.10.10.1
    pycook revs -s py_ip4_1 192.168.10.45
    pycook revs -l 192.168.10.45

    echo "---------------------------------------------------------------------------------------"
done
