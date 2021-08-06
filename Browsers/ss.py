import time

def screenshot(d):

    folder ="C:\Users\harsh\Desktop\testing\screenshot\\"
    time_string = time.asctime().replace(":"," ")
    file_name = folder + time_string + ".jpg"
    d.save_screenshot(file_name)
