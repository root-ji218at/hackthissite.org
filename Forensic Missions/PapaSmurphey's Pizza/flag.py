f = open("flashdrive/shh.jpg", "rb")
r = f.read()
f.close()

File_List = ["rar", "jpg"]
Header_Array = []
Trailer_Array = []
start = 0
File_Number = 0

for fi in range(start, len(File_List)):

    if (File_List[fi] == "jpg"):
        Header_Array = [255, 216, 255, 224]
        Trailer_Array = [255, 217]
    else:
        Header_Array = [82, 97, 114, 33]
        Trailer_Array = [0, 64, 7, 0]

    Key_List = []
    for i in range(start, len(r)):
        try:
            if (r[i+1] == Header_Array[1] and r[i+2] == Header_Array[2] and r[i+3] == Header_Array[3]):
                Key_List.append(i)
        except IndexError:
            pass
    for j in range(start, len(Key_List)):
        Byte_List = []
        for i in range(Key_List[j], len(r)):
            Byte_List.append(r[i])
            try:
                if (i > 0):
                    if (File_List == "jpg"):
                        if (r[i-1] == Trailer_Array[0] and r[i] == Trailer_Array[1]):
                            break
                    else:
                        if (r[i-3] == Trailer_Array[0] and r[i-2] == Trailer_Array[1] and r[i-1] == Trailer_Array[2] and r[i] == Trailer_Array[3]):
                            break
            except IndexError:
                pass
        Byte_List[0] = Header_Array[0]
        file = open("Extracted_files/"+str(File_Number)+"."+File_List[fi], "wb")
        file.write(bytearray(Byte_List))
        file.close()
        File_Number += 1
