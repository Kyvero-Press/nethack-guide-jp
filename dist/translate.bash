for filename in ./*.png.txt; do
    echo "translating $filename"
    deepl -t en -o $(basename "$filename" .txt).eng.txt $filename
done
