using System;
using System.Management.Automation;
namespace Powershell
{
	class Program
	{
		static void Main(string[] args)
		{
			PowerShell ps = PowerShell.Create();
			ps.AddCommand("Invoke-Expression");
			ps.AddArgument("<PAYLOAD>");
			ps.Invoke();
		}
	}
}
