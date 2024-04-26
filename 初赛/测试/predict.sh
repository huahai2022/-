#本文件仅为示意
predict_file=$1
predict_result=$2
cat $predict_file | python predict.py > $predict_result
