from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi import APIRouter
import pandas as pd
import json

router = APIRouter()

@router.post("/upload/", summary= "Upload CSVs", description="Uploads input.csv and reference.csv for processing.")
async def upload_files(input_file: UploadFile = File(...), reference_file: UploadFile = File(...)):
    
    input_path = f"app/sample_input/{input_file.filename}"
    reference_path = f"app/sample_input/{reference_file.filename}"

    with open(input_path, "wb") as f:
        f.write(await input_file.read())

    with open(reference_path, "wb") as f:
        f.write(await reference_file.read())

    return {"message": "Files uploaded successfully"}

@router.get("/generate-report/", summary= "Generate report CSVs", description="Generate report.csv's for download.")
def generate_report():
    with open("app/config.json") as f:
        rules = json.load(f)

    input_df = pd.read_csv("app/sample_input/input.csv")
    ref_df = pd.read_csv("app/sample_input/reference.csv")

    merged_df = pd.merge(input_df, ref_df, on=["refkey1", "refkey2"], how="left")

    # Apply transformation rules
    merged_df["outfield1"] = merged_df["field1"] + merged_df["field2"]
    merged_df["outfield2"] = merged_df["refdata1"]
    merged_df["outfield3"] = merged_df["refdata2"] + merged_df["refdata3"]
    merged_df["outfield4"] = merged_df["field3"] * merged_df[["field5", "refdata4"]].max(axis=1)
    merged_df["outfield5"] = merged_df[["field5", "refdata4"]].max(axis=1)

    merged_df[["outfield1", "outfield2", "outfield3", "outfield4", "outfield5"]].to_csv("output/output.csv", index=False)
    
    return {"message": "Report generated successfully"}

@router.get("/download-report/", summary= "Download CSVs", description="Downoads report.csv's.")
def download():
    return FileResponse("output/output.csv", filename="output.csv", media_type="text/csv")

@router.get("/rules/", summary= "Future enhancements.", description="In here for Future enhancements.")
def get_rules():
    with open ("app/config.json") as f:
        return json.load()
    
@router.post("/rules/", summary= "Future enhancements.", description="In here for Future enhancements.")
def update_rules(new_rules:dict):
    with open("app/config.json", "w") as f:
        json.dump(new_rules,f,indent=4)
    return {"message" : "rules updated"}