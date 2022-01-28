using System;
using System.Diagnostics;
using Microsoft.Build.Framework;
using Microsoft.Build.Utilities;

namespace MyTasks
{
  public class EvilTask : Task
  {
    public override bool Execute()
    {
      Process.Start("calc.exe");
    }
  }
}
