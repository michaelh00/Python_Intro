"""
Generates the sample_data/ folder used throughout Sessions 2 and 3.

Run this once before either notebook:

    python setup_sample_data.py

The folder is already included alongside the notebooks in the course
materials, so most students will never need to run this directly. It's
here mainly so the dataset is reproducible rather than a mystery folder
that appeared from nowhere, and so it's easy to regenerate if it ever
gets modified during an exercise and needs a clean reset.

The filenames simulate what a trade-law researcher's downloads folder
tends to look like after a while: some files still carry a recognisable
WTO document symbol (slashes swapped for dashes or underscores, since
slashes aren't valid in filenames), others have clearly been renamed by
a person along the way.
"""

from pathlib import Path

SAMPLE_FILES = {
    "WT-DS316-AB-R.txt":
        "Appellate Body Report, European Communities and Certain Member States "
        "- Measures Affecting Trade in Large Civil Aircraft.",
    "AB_2019_7_footwear_import.txt":
        "Appellate Body report note regarding footwear import measures, 2019.",
    "ds58_shrimp_turtle_AB.txt":
        "Appellate Body report, United States - Import Prohibition of Certain "
        "Shrimp and Shrimp Products.",
    "WT-DS58-AB-R_shrimp_turtle.txt":
        "Appellate Body report, United States - Shrimp/Turtle, alternate filename copy.",
    "panel report DS412 Canada FIT programme.txt":
        "Panel Report, Canada - Certain Measures Affecting the Renewable "
        "Energy Generation Sector.",
    "WT-DS135-R_asbestos.txt":
        "Panel Report, European Communities - Measures Affecting Asbestos "
        "and Asbestos-Containing Products.",
    "ds379_china_auto_parts_panel.txt":
        "Panel Report, China - Measures Affecting Imports of Automobile Parts.",
    "ab_report_ds135_asbestos.txt":
        "Appellate Body report note, DS135, asbestos dispute.",
    "G_MA_TAR_RS_70_Argentina.csv":
        "commodity_code,description,tariff_rate\n0101,Live horses,5.0\n1006,Rice,10.0",
    "Costa Rica - Tariff Schedule (revised) FINAL v3.csv":
        "commodity_code,description,tariff_rate\n0201,Beef,14.0\n0901,Coffee,0.0",
    "tariff_schedule_brazil_2021.csv":
        "commodity_code,description,tariff_rate\n2709,Crude petroleum oils,0.0",
    "G_MA_TAR_RS_45_Japan.csv":
        "commodity_code,description,tariff_rate\n1001,Wheat,7.5",
    "wt_min17_w_8.txt":
        "Ministerial Conference working document, 2017 session, paper 8.",
    "WT-MIN11-W-2.txt":
        "Ministerial Conference working document, eleventh session, paper 2.",
    "TN_MA_W_103.txt":
        "Negotiating Group on Market Access, working document 103.",
    "Understanding_DSU_consolidated_1994.txt":
        "Understanding on Rules and Procedures Governing the Settlement of "
        "Disputes, consolidated text, 1994.",
    "GATT_1994_consolidated.txt":
        "General Agreement on Tariffs and Trade 1994, consolidated text.",
    "Agreement_on_Safeguards.txt":
        "Agreement on Safeguards, consolidated text.",
    "report(draft)v2.txt":
        "Draft notes, untitled, version 2.",
    "notes_meeting_march.txt":
        "Personal notes from a meeting held in March.",
    "untitled_document_3.txt":
        "Untitled document, content unclear.",
    "scan0001.txt":
        "Scanned document, OCR placeholder text.",
    "Copy of Copy of report.txt":
        "Duplicate copy of an earlier report, content unclear.",
    "final_final_v2.txt":
        "Draft document, likely superseded, version 2.",
}


def main():
    data_dir = Path(__file__).parent / "sample_data"
    data_dir.mkdir(exist_ok=True)
    for name, content in SAMPLE_FILES.items():
        (data_dir / name).write_text(content, encoding="utf-8")
    print(f"Created {len(SAMPLE_FILES)} files in {data_dir.resolve()}")


if __name__ == "__main__":
    main()
