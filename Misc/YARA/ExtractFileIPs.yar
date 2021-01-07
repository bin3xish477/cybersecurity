rule ExtractFileIPs
{
    meta:
        description = "This Yara rule extracts IP addresses located within a file"
        author = "Alexis Rodriguez"
        date = "2020-10-12"

    strings:
        // the wide modifier means to search for strings that                                                                                                                                                                  
        // are encoded with two bytes per character (utf-16, etc)                                                                                                                                                              
        // the ascii is the default modifier for strings                                                                                                                                                                       
        // so the ascii modifier is implicitly used when the wide                                                                                                                                                              
        // modifier is not used
        $ip = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/ wide ascii

    condition:
        $ip and filesize < 10MB
}
