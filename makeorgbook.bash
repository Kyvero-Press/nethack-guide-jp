makepage () {
    cat <( [[ "cropped_nethack_uncropped_cover.png" == "$filename" ]] && echo "" || echo "[[$PREV_FILE][previous page]]") <(echo "[[../$filename]]" ) "$filename.txt" <( [[ $PAGE_NUM -gt "267" ]] && echo "" || echo "[[$NEXT_FILE][next page]]" ) > orgbook/$filename.org
}

filename="cropped_nethack_uncropped_cover.png"
PAGE_NUM=0
TEXT=$(cat "$filename.txt")
NEXT_FILE="cropped_nethack_uncropped_openpages_1_2_3-1_left.png"
makepage
filename="cropped_nethack_uncropped_openpages_1_2_3-1_left.png"
PAGE_NUM=0
TEXT=$(cat "$filename.txt")
NEXT_FILE="cropped_nethack_uncropped_openpages_1_2_3-1_right.png"
makepage
filename="cropped_nethack_uncropped_openpages_1_2_3-1_right.png"
PAGE_NUM=0
TEXT=$(cat "$filename.txt")
NEXT_FILE="cropped_nethack_uncropped_openpages_1_2_3-2.png"
makepage
filename="cropped_nethack_uncropped_openpages_1_2_3-2.png"
PAGE_NUM=0
TEXT=$(cat "$filename.txt")
NEXT_FILE="cropped_nethack_uncropped_both_sides_ordered-001.png"
makepage

for filename in ./cropped_nethack_uncropped_both_sides_ordered*.png; do
    PAGE_NUM=$( grep -o '[0-9]\+' <(echo $filename) )
    TEXT=$(cat "$filename.txt")
    NEXT_PAGE_NUM=$(expr $PAGE_NUM + 1)
    PREV_PAGE_NUM=$(expr $PAGE_NUM - 1)
    if [[ $PAGE_NUM -eq "001" ]]; then
        PREV_FILE='cropped_nethack_uncropped_tocpage-2.png'
    else
        PREV_FILE=$( echo $filename | sed -E "s/[[:digit:]]{1,3}/$NEXT_PAGE_NUM/" )
    fi
    NEXT_FILE=$( echo $filename | sed -E "s/[[:digit:]]{1,3}/$NEXT_PAGE_NUM/" )
    
    makepage
done
