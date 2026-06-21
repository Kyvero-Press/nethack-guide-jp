for filename in ./cropped_*.png; do
    echo "doing ocr on $filename"
    tesseract "$filename"  "$filename" -l jpn+eng
done
## uncomment to ocr the whole book into one pdf afterwards
# tesseract ./pdforder.txt ocr_nethack_guide -l jpn+eng pdf
