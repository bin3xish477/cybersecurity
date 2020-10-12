rule DetectExe
{
    meta:
        description = "This Yara rule simply detects an exe file using magic byte identification"
        author = "Alexis Rodriguez"
        date = "2020-10-12"

	strings:
		$exe_magic_bytes = {4D 5A}

	condition:
		$exe_magic_bytes 
}
