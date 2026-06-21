# for filename in ./*.png.txt; do
#     echo "translating $filename"
#     deepl -t en -o $(basename "$filename" .txt).eng.txt $filename
# done
for filename in ./*.png.txt; do
    echo "translating $filename"
    trans ja:en --brief -i $filename -o $(basename "$filename" .txt).eng2.txt

done
