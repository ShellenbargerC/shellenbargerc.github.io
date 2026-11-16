import csv 
from pathlib import Path

csv_file = Path("assets.csv")
with csv_file.open("r", encoding="utf-8-sig", newline= "") as file: 

    reader = csv.DictReader(file)
    print("CSV Headers:", reader.fieldnames)
    
    #This creates a folder for HTML pages
    output_folder = Path("docs")
    output_folder.mkdir(exist_ok=True)

    for asset in reader:
        asset_id = asset["asset_id"]
        asset_name = asset["asset_name"]
        asset_type = asset["asset_type"]
        location = asset["location"]
        owner = asset["owner"]

        # Create HTML webpage
        from html import escape

        webpage = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, initial-scale=1">
            <title>{escape(asset_id)}</title>
        </head>
        <body>
            <h1>Asset: {escape(asset_id)}</h1>
            <hr>
            <p><b>Asset Name:</b> {escape(asset_name)}</p>
            <p><b>Asset Type:</b> {escape(asset_type)}</p>
            <p><b>Location:</b> {escape(location)}</p>
            <p><b>Owner:</b> {escape(owner)}</p>
        </body>
        </html>
        """

        # Save each asset webpage
        filename = output_folder / f"{asset_id}.html"
        filename.write_text(webpage, encoding="utf-8")

        print(f"Created webpage for {asset_id}")
        
