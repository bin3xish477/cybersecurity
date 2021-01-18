event zeek_init()
    {
    local v: vector of string = {"v1", "v2", "v3"};
    
    # print first element of vector
    print v[0];

    # append value to the end of vector using length operator "||"
    v[|v|] = "v4";

    # print all elements of vector
    for (e in v)
        {
        print e
        }
    }
