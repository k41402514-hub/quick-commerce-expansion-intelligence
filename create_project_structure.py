from pathlib import Path

root = Path(".")

folders = [
    "data/raw",
    "data/api/raw_json",
    "data/api/csv",
    "data/api/logs",
    "data/clean",
    "data/integrated",

    "notebooks",

    "scripts/collection",
    "scripts/api",
    "scripts/cleaning",
    "scripts/integration",
    "scripts/synthetic",

    "sql",

    "dashboards",

    "docs",

    "metadata",

    "outputs/figures",
    "outputs/reports",
    "outputs/exports",
]

files = [
    "README.md",

    "notebooks/01_data_collection.ipynb",
    "notebooks/02_data_cleaning.ipynb",
    "notebooks/03_data_integration.ipynb",
    "notebooks/04_eda.ipynb",
    "notebooks/05_dashboard.ipynb",

    "docs/business_problem.md",
    "docs/project_scope.md",
    "docs/source_inventory.md",
    "docs/data_dictionary.md",
    "docs/methodology.md",

    "metadata/metadata_registry.csv",
]

for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

for file in files:
    path = root / file
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

print("\nProject structure created successfully!\n")
print("Folder:", root.resolve())