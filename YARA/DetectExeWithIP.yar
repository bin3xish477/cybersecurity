rule DetectExe {
	meta:
		description: "This Yara rule detects an exe files with IP addresses"
		author: "Alexis Rodriguez"
		date: "2020-10-12"

	strings:
		$exe_magic_bytes = {4D 5A}
		// the wide modifier means to search for strings that
		// are encoded with two bytes per character (utf-16, etc)
		// the ascii is the default modifier for strings
		// so the ascii modifier is implicitly used when the wide
		// modifier is not used
		$ip = /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/ wide ascii 

	condition:
		$exe_magic_bytes and $ip and filesize < 10KB
}