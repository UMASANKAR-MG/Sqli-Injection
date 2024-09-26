import requests
from includes import write


def sqlscan(url,output):
    try:
        res= requests.get(url+ "'")
        print(f"\n Checking ====> {url}\n")
        resp = res.text
        if "error" not in resp or "SQL" not in resp:
            print("[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]")
            outputprint = (f"[Vulnerable] ====> {url}\n")
            print(outputprint)
            print("[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]")
            if output is not None:
                write.write(output, f"{url}\n")
        else:
            print("No SQL injection vulnerability found")

    except requests.exceptions.RequestException as e:
        print("invalid url {url}",e)
        
        
        

