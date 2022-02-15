#!/usr/bin/env bash
# must set VT_API_KEY for script to work successfully
# must install jq, json parser with `sudo apt install jq`


function usage() {
    echo "export VT_API_KEY='[YOUR_VIRUSTOTAL_API_KEY]'"
    echo "usage: $0 <file_to_upload_to_virustotal>"
    
    exit 1
}

function get_results() {
    echo "[*] Getting results ..."
    url="https://www.virustotal.com/api/v3/files/$1"
    echo "[+] File URL: $url"
    curl --request GET \
        --url $url \
        --header "x-apikey: $VT_API_KEY"

    echo -e "\n\n[*] Complete !!!"
}

function upload() {
    echo "[*] Uploading file to Virustotal..."
    resp=$(curl --request POST \
        --no-progress-meter \
        --url 'https://www.virustotal.com/api/v3/files' \
        --header "x-apikey: $VT_API_KEY" \
        --form file=@"$1"
    )
    sleep 1
    file_hash=$(sha256sum $1 | cut -d" " -f1)
    echo "[+] File Hash: $file_hash"
    get_results $file_hash
}

function main() {
    jq_installed=$(jq --help)
    if [[ $? -ne 0 ]]
    then
        echo "[-] Please install 'jq' with : sudo apt install jq"
        exit 1
    fi

    file=$1
    if [[ -z $file ]]
    then
        usage
    else
        if [[ -f $file && -s $file ]]
        then
            upload $file
        else
            echo "$file does not exists or is empty!"
        fi
    fi
}

main $1
