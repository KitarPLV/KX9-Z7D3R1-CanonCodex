
import os
from datetime import datetime

def convert_master_memory_to_html(md_path="MasterMemory.md", output_html="dashboard.html"):
    if not os.path.exists(md_path):
        print("❌ MasterMemory.md not found.")
        return

    with open(md_path, "r") as f:
        lines = f.readlines()

    html = "<html><head><title>CanonCodex Dashboard</title><style>body{font-family:sans-serif;}table{border-collapse:collapse;width:100%;}th,td{padding:8px;border:1px solid #ccc;text-align:left;}thead{background:#f0f0f0;}</style></head><body>"
    html += "<h1>🧠 CanonCodex Dashboard</h1><p>Updated: {}</p>".format(datetime.utcnow().isoformat())

    table_started = False
    for line in lines:
        if line.startswith("|") and not table_started:
            html += "<table><thead><tr>"
            headers = [h.strip() for h in line.strip().split("|") if h]
            for h in headers:
                html += f"<th>{h}</th>"
            html += "</tr></thead><tbody>"
            table_started = True
        elif table_started and line.startswith("|"):
            html += "<tr>"
            cells = [c.strip() for c in line.strip().split("|") if c]
            for cell in cells:
                html += f"<td>{cell}</td>"
            html += "</tr>"
    if table_started:
        html += "</tbody></table>"

    html += "</body></html>"

    with open(output_html, "w") as f:
        f.write(html)

    print(f"✅ Dashboard generated at {output_html}")

if __name__ == "__main__":
    convert_master_memory_to_html()
