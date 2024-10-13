def add_commas(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write('[')
        lines = infile.readlines()
        
        print(f"Total lines: {len(lines)}")  # Kiểm tra số dòng trong tệp

        for i, line in enumerate(lines):
            cleaned_line = line.strip()
            print(f"Processing line {i + 1}: {cleaned_line}")  # In ra từng dòng đang xử lý
            
            if i < len(lines) - 1:
                outfile.write(f"{cleaned_line},\n")
            else:
                outfile.write(f"{cleaned_line}\n")
        outfile.write(']')
        print("Finished writing to output file")

# Gọi hàm
add_commas('/Users/nguyenvandunghaha/Desktop/ImageCV/videos.json', '/Users/nguyenvandunghaha/Desktop/ImageCV/fix2.json')

        