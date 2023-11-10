#!/bin/bash

if ! command -v go &> /dev/null
then
  echo "[x] missing go installation..."
  exit 1
fi

tools=(
  "httpx"
  "asnmap"
  "subfinder"
  "interactsh-client"
  "mapcidr"
  "cdncheck"
  "tlsx"
  "proxify"
  "dnsx"
)

for tool in ${tools[@]}
do
  if [[ $tool = "interactsh-client" ]]
  then
    # interactsh-client lives as a sub tool of the interactsh repo
    go install -v "github.com/projectdiscovery/interactsh/cmd/${tool}@latest"
  else
    go install -v "github.com/projectdiscovery/${tool}/cmd/${tool}@latest"
  fi
done
