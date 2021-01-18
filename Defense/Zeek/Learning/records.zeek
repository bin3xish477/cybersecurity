type Person: record {
    fname: string;
    lname: string;
    age: int;
    is_student: bool &default = T;
    is_married: bool &optional;
    };

event zeek_init()
    {
    local p = Person(
                    $fname="John",
                    $lname="Wick",
                    $age=40,
                    $is_student=F);

    # checking if value is set
    if ( p?$fname )
        {
        print fmt("Name: %s", p$fname);
        }
    }
