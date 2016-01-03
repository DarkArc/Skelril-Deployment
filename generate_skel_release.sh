#!/bin/bash

VERSION=$(python3 get_cur_version.py)

echo "Creating release version" $VERSION"..."

markdown_py --output_format=html5 news.md > news-raw.txt
python3 converter.py
java -jar Tools/Launcher\ Builder.jar --version $VERSION --input Packs/SkelCore --output Active --manifest-dest "Active/SkelCore.json" --pretty-print
