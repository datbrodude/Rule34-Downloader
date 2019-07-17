"""
Name: Rule34 Downloader
Author: Daniel Allen -- LordOfPolls - https://github.com/LordOfPolls
Version: 0.01
Date: 17/07/2019
"""
import rule34
import time
import os
from timeit import default_timer as timer
import urllib.request

Rule34 = rule34.Sync()

class Downloader:
    def __init__(self):
        self.downloading = False  # Are we downloading right now?
        self.empty = True  # Is the queue of files empty?
        self.connection = False  # Do we have an internet connection
        self.webm = False
        self.silent = False  # Run the script silently
        self.debug = True

        self.commandLineParse()  # process command line args if any
        self.checkConnection()  # validate that we have an internet connection

    def debugPrint(self, string):
        if self.debug:
            print(string)

    def commandLineParse(self):
        # todo: Parse command line arguments
        return None

    def response(self, prompt):
        """Wrapper for input() allowing the result to be normalised to a boolean"""
        prompt += " (y/n) "
        for i in range(3):
            resp = input(prompt).lower()
            if "y" in resp:
                return True
            elif "n" in resp:
                return False
            else:
                print("Invalid response")
        print("Too many invalid responses, quiting")
        time.sleep(1)
        exit(0)


    def checkConnection(self):
        try:
            self.debugPrint("Checking Google for response")
            urllib.request.urlopen('http://216.58.192.142', timeout=1)  # Check google for a response
            self.debugPrint("Google responded")
            self.debugPrint("Checking Rule34 for response")
            urllib.request.urlopen('https://rule34.xxx/', timeout=1)  # Check rule34 for a response
            self.debugPrint("Rule34 responded")
            self.connection = True
        except urllib.request.URLError as err:
            self.connection = False

    def download(self, images):
        # todo: Add progress bar

        times = []
        print("Sorting list...")
        webmList = []
        for image in images:
            if "webm" in image:
                if self.webm:
                    webmList.append(image)
                images.remove(image)

        for video in webmList:
            images.append(video)

        numDownloaded = 0
        print("Downloaded {}/{}".format(numDownloaded, len(images)))
        for image in images:
            try:
                name = "{}/{}".format("images", image.split("/")[-1])
                if os.path.isfile(name):
                    print(image, "Already exists")
                else:
                    if "webm" in name:
                        print("Downloading a webm... this will take longer")
                    start = timer()
                    with urllib.request.urlopen(image) as f:
                        imageContent = f.read()
                        with open(name, "wb") as f:
                            f.write(imageContent)
                        numDownloaded = numDownloaded + 1
                        end = timer()
                        times.append(end - start)
                        times = times[-30:]
                        average = (sum(times) / len(times))
                        ETA = average * (len(images) - numDownloaded)
                        print("Downloaded {0}/{1} -- ETA: {2:.3g}s @ {3:.3g}s/image".format(numDownloaded, len(images),
                                                                                            ETA, average))
            except Exception as e:
                print("Skipping image due to", e)
        return None

    def menu(self):
        query = input("Search Term: ")
        self.debugPrint("Querying Rule34...")
        totalImages = Rule34.totalImages(query)
        print("{} images expected!".format(totalImages))
        if self.response("Would you like to download?"):
            if self.response("Would you like to download videos too?"):
                self.webm = True
            print("Gathering Data from rule34, this is predicted to take {0:.3g} seconds".format(0.002*totalImages))
            start = timer()
            images = Rule34.getImageURLS(query, singlePage=False)
            end = timer()
            total = end-start
            print(total/totalImages)
            if images is None:
                print("No images found... this shouldnt happen")
            else:
                print("Download commencing")
                self.download(images)

        self.debugPrint("EOF")
        return True


if __name__ == "__main__":
    main = Downloader()
    main.menu()