for i in $(seq 1 5);
do
    # Testing Base encodings 
    echo hello world | ./pycook -b85 -b64 -b32 -b16;
    echo ""

    # Testing hex encodings
    echo hello world | ./pycook -hex -hexd;
    echo ""
    
done
