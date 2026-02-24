import argparse
import os
import json
import csv
import requests
import pandas as pd
from pdfminer.high_level import extract_text

Keys = {
    "AI":["machine learning","Artificial intelligence"],
    "National_security":["nation","safety","records"],
    "Health":["medical","hospital","records","health"]
}
api_key="rXd4nfxLkTmFTTWVziytTPt4t"

def extract_id(url):
    return url.rstrip("/").split("/")[-1]

def get_foa(opportunity_id,api_key):
    api_url=f"https://api.simpler.grants.gov/v1/opportunities/{opportunity_id}"
    headers={
        "X-API-Key": api_key,
        "Accept" : "application/json"
    }
    r=requests.get(api_url,headers=headers)##r.status_code=200 successful
    return r.json().get("data", {})

def map_schema(data,url):
    summary=data.get("summary",{})
    attachments = data.get("attachments", [])##############################pdf
    pdf_url = attachments[0].get("download_path") if attachments else None #################pdf
    foa={
        "id": data.get("opportunity_id"),
        "title": data.get("opportunity_title"),
        "agency": data.get("agency_name"),
        "posted_data": data.get("post_date"),
        "close_date":data.get("close_date"),
        "eligibility": ", ".join(summary.get("applicant_types", []) or []),
        "description": data.get("summary_description"),
        "source_url":url,
        "pdf_url":pdf_url

    }
    return foa

def give_tag(text):
    text=(text).lower()
    tags=[]

    for tag,keywords in Keys.items():
        if any(kw in text for kw in keywords):
            tags.append(tag)
    if not tags:
      return ["Others"]
    return tags


def save_outputs(foa, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    pdf_url=foa.get("pdf_url")
    json_path=os.path.abspath(os.path.join(out_dir,"foa.json"))
    csv_path=os.path.abspath(os.path.join(out_dir,"foa.csv"))
    pdf_path=os.path.abspath(os.path.join(out_dir,"foa.pdf"))
    with open(json_path,"w") as f:
        json.dump(foa,f,indent=2)
    ############################################################pdf#################
    if(pdf_url):
        response=requests.get(pdf_url)
        if response.status_code==200:
            with open(pdf_path,"wb") as f:
                f.write(response.content)
    else:
        print("No pdf found")
    
    ########################## pdf#####################################
    if os.path.exists(pdf_path):
        pdf_text=extract_text(pdf_path)
        lines=[l.strip()  for l in pdf_text.split("\n") if l.strip()]
        pdf_data={
            "agency":None,
            "title":None,
            "deadline":None,
        }
        for line in lines:
            low=line.lower()
            if( not pdf_data["agency"] and "agency" in low):
                pdf_data["agency"]=line
            if( not pdf_data["title"] and "title" in low):
                pdf_data["title"]=line
            if( not pdf_data["deadline"] and "deadline" in low):
                pdf_data["deadline"]=line
        pdf_json_path = os.path.abspath(os.path.join(out_dir, "pdf.json"))
        with open(pdf_json_path, "w") as f:
            json.dump(pdf_data, f, indent=2)
        print("Saved PDF JSON",pdf_json_path)
   ######################################################################## 
    pd.DataFrame([foa]).to_csv(csv_path,index=False)
    
    print("Saved JSON", json_path)
    print("Saved CSV", csv_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="FOA URL")
    parser.add_argument("--out_dir", required=True, help="Output directory")

    args = parser.parse_args()
    opportunity_id = extract_id(args.url)

    data = get_foa(opportunity_id,api_key)
    foa = map_schema(data, args.url)

    tag_text = (foa["title"] or "") + " " + (foa["description"] or "")
    foa["tags"] = give_tag(tag_text)

    save_outputs(foa, args.out_dir)

    print("FOA extracted successfully")
    
if __name__ == "__main__":
    main()