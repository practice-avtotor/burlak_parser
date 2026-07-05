from setuptools import find_packages, setup

setup(
    name="burlak_parser",
    version="0.1.0",
    description="Heuristic parser for BOM and operational card comparison",
    packages=find_packages(),
    python_requires=">=3.12",
    install_requires=[
        "openpyxl>=3.1.0",
        "xlsxwriter>=3.1.0",
        "xlrd>=2.0.0",
        "tqdm>=4.65.0",
        "lxml>=5.0.0",
    ],
)
