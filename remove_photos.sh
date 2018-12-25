for pic in $(find . \( -name "*.png" -o -name "*.jpg" \));
do
    rm "$pic"
done
