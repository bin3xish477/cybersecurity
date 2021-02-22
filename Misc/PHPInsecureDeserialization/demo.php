<?php

include 'logging.php';

class User
{
    public $username;
    public $isAdmin;

    public function IsUserAdmin()
    {
        if ($this->isAdmin)
        {
            echo $this->username . " is an admin user\n";
        } else {
            echo $this->username . " is not an admin user\n";
        }
    }
}

class ReadFile
{
    // the `__tostring` appears to be invoked when we use
    // the `echo` keyword which is what triggers the exploit
    // in the if statement inside the `IsUserAdmin` function
    public function __tostring()
    {
        return file_get_contents($this->filename);
    }

    public function __destruct()
    {
        $this->pwnobj->pwn();
    }
}

class Pwned
{
    public function pwn()
    {
        system($this->command);
    }
}

//$user = new User();
//$user->username = "binexishatt";
//$user->isAdmin = True;

// serializing object
// O:4:"User":2:{s:8:"username";s:11:"binexishatt";s:7:"isAdmin";b:1;}

// O = object
// s = string
// b = boolean
//echo serialize($user);

// running php server ```php -S 127.0.0.1:80```
$user = unserialize($_POST['param']);
$user->IsUserAdmin();

?>
