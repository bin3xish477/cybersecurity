---
-- @usage nmap --script shodan-ip-info --script-args 'shodan.api-key=<api_key>' <host>
-- 
-- @output
--
-- @args shodan.api-key   Shodan API key
--
---

local ipOps  = require "ipOps"
local stdNse = require "stdnse"
local http   = require "http"
local json   = require "json"

description = [[
]]

author = ""
license = "Same as Nmap--See http://nmap.org/book/man-legal.html"
categories = {
  "safe",
  "discovery",
  "default"
}

local SHODAN_API_BASE = "https://api.shodan.io/shodan/host/"
local SHODAN_API_KEY = ""

function init()
  SHODAN_API_KEY = stdNse.get_script_args("shodan.api-key")
end

function hostrule(host)
  -- checks if ip is external
  return not ipOps.isPrivate(host)
end

function action(host, port)
  init()
  output = stdNse.output_table()

  local url = SHODAN_API_BASE..host.ip.."?key="..SHODAN_API_KEY.."&minify=True"
  stdNse.debug(1, "SHODAN_REQ_URL: %s", url)

  local resp = http.get_url(url)
  
  if resp.status ~= 200 then
    output["Results"] = "No data was found for the IP: " .. host.ip
    return output
  end

  local ok, respJson = json.parse(resp.body)

  if ok then
    output["IP"] = host.ip
    output["Hostnames"] = respJson["hostnames"]
    output["Country"] = respJson["country_name"]
    output["Organization"] = respJson["org"]
    output["ASN"] = respJson["asn"]
  else
    output["Error"] = "Could not parse JSON response from Shodan API..."
  end


  return output
end
