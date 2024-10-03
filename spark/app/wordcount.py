from pyspark import SparkContext

def main():
    # Tạo SparkContext
    sc = SparkContext(appName="WordCount")
    
    # Đọc file đầu vào
    input_file = "/usr/local/spark/resources/data/haha.txt"
    text_file = sc.textFile(input_file)
    
    # Thực hiện tính toán WordCount
    counts = text_file.flatMap(lambda line: line.split(" ")) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)
    
    # Lưu kết quả ra file
    counts.saveAsTextFile("/usr/local/spark/resources/data/output")

    # Dừng SparkContext
    sc.stop()

if __name__ == "__main__":
    main()
