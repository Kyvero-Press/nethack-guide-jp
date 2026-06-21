for filename in ./nethack_uncropped_both_sides_ordered-*.png; do
    echo "$filename"
    magick "$filename" -crop 1788x2512+376+0 cropped_$(basename "$filename")
done
