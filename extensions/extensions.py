file_name = input("file name: ").lower()
if ".gif" in file_name:
    print("image/gif")
if ".jpg" in file_name:
    print("image/jpeg")
if ".jpeg" in file_name:
    print("image/jpeg")
if ".png" in file_name:
    print("image/png")
if ".pdf" in file_name:
    print("application/pdf")
if ".txt" in file_name:
    print("text/plain")
if ".zip" in file_name:
    print("application/zip")
else:
    print("application/octet-stream")