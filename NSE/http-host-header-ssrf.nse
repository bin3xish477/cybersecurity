---
-- @usage nmap --script http-host-header-ssrf --script-args "oob.server='<oob_server>'" <host>
-- 
-- @output
-- PORT     STATE SERVICE
-- 3000/tcp open  ppp
-- | http-host-header-ssrf:
-- |   Location: None
-- |   Injected-Host-Header: faljfqp141laafa.interact.sh
-- |   Response-Code: 404
-- |_  Verdict: Non-200/301 status codes may mean no SSRF is present but check your server logs anyways
--
-- @args oob.server    The hostname of the server to listen for connection
--
---

description = [[
Attempts to detect Server-Side Request Forgery (SSRF) by injecting
an attacker-controlled server into the Host header of an HTTP GET request

An Out of Band detection tool like Project Discovery's interactsh or
Burp's collaborator client can be used for the detection
]]

author = "Alexis Rodriguez"
license = "Same as Nmap--See http://nmap.org/book/man-legal.html"
categories = {
  "safe",
  "default"
}

local stdNse    = require "stdnse"
local http      = require "http"
local shortPort = require "shortport" 
local rand      = require "rand"
local b64       = require "base64"
local ipOps     = require "ipOps"

local debug = stdNse.debug

function hostrule(host)
  -- return not ipOps.isPrivate(host)
  return ipOps.isPrivate(host)
end

function portrule(host, port)
  return shortPort.port_or_service(
      {80, 443, 3000, 5000, 8080, 8443, 8888},
      {"http", "https"},
      "tcp", "open"
    )
end

local function getHeaders(host, port, server)
  local agent    = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
  local referer  =  "http://" .. host.ip .. port.number

  local headers = {}
  headers["Host"] = server
  headers["User-Agent"] = agent
  headers["Referer"] = referer

  return headers
end

-- performs the actual enumeration or exploit
function action(host, port)
  debug(1, "Port::%d", port.number)
  local oobServer = stdNse.get_script_args("oob.server")
  debug(1, "OOB_Server::%s", oobServer)

  local output = stdNse.output_table()

  local opts = {}
  opts["header"] = getHeaders(host, port, oobServer)

  local path = "/" .. b64.enc(rand.random_alpha(8))

  local resp = http.get(host, port, path, opts)

  if resp.header["location"] == nil then
    output["Location"] = "None"
  else
    output["Location"] = resp["header"]["location"]
  end

  output["Injected-Host-Header"] = oobServer
  output["Response-Code"]        = resp.status

  if resp.status ~= 200 or resp.status ~= 301 then
    output["Verdict"] = "Non-200/301 status codes may mean no SSRF is present but check your server logs anyways"
  else
    output["Verdict"] = "*** Potential SSRF detected ***"
  end

  return output
end
