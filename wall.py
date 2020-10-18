import os
import requests
import wget
import time
import platform
import ctypes
import threading
import shutil
def main():
    access_key='sxKc8gQqH9v8Go4rDVLXXs8kR1mC4nE_WZj9J-JN7X0'
    url= 'https://api.unsplash.com/photos/random?client_id='+access_key
    params = {
        'query': 'HD wallpapers',
        'orientation': 'landscape'
    }
    try:
        response=requests.get(url,params).json()

        image_source = response['urls']['full']


        directory = os.getcwd() + "/.unsplash"

        if os.path.exists(directory):
            shutil.rmtree(directory,ignore_errors=True)

        if not os.path.exists(directory):
            os.makedirs(directory)



        filepath = directory + "/" + str(time.time()) + ".jpg"
        wget.download(image_source,filepath)


        osvar = platform.system()

        if osvar == "Windows":

            try:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
                threading.Timer(10.0, main()).start()
            except:
                print(f"\r[-] Status: Error - Couldn't set your wallpaper.", end="")
        else:
            print("Supported fo Windows environment only")

    except:
        print("\nThe API limit has exceeded , kindly try after one hour",end="")


if __name__=='__main__':
    main()
