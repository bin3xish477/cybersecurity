---
-- @usage
--
-- @output
--
-- @args
--
---

local shortPort = require "shortport"
local ipOps = require "ipOps"
local http = require "http"
local stdNse = require "stdnse"
local b64 = require "base64"

description = [[
An example NSE script that simply makes an HTTP request to
any HTTP(S) ports it finds while echoing the request status line
to stdout
]]

author = {"Alexis Rodriguez"}
license = "Same as Nmap--See http://nmap.org/book/man-legal.html"
categories = {
  "safe"
}

function hostrule(host)
  -- checks if IP address is local, if not,
  -- script won't run
  return ipOps.isPrivate(host)
end

function portrule()
  -- returns a function that matches on ports, services, protocol, and state
  return shortPort.port_or_service({80, 443}, {"http", "https"}, "tcp", "open")
end

function action(host, port)
  -- debug logs
  stdNse.debug(1, "IP::%s", host.ip)
  stdNse.debug(1, "PORT::%s", port.number)

  opts = {}
  local resp = http.get(host, port, "/", opts)

  return stdNse.format_output(
    true, string.format("Server Header ==> %s", resp.header["server"])
  )
end
