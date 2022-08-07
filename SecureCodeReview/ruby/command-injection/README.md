# Ruby Command Injection Functions

The following Ruby functions can be used to execute system commands and should be avoided if possible:

```ruby
eval("ruby code here")
system("os command here")
`ls -al /` # (backticks contain os command)
exec("os command here")
spawn("os command here")
open("| os command here")
Process.exec("os command here")
Process.spawn("os command here")
IO.binread("| os command here")
IO.binwrite("| os command here", "foo")
IO.foreach("| os command here") {}
IO.popen("os command here")
IO.read("| os command here")
IO.readlines("| os command here")
IO.write("| os command here", "foo")
```
