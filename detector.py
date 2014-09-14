import sqlite3
import sys
import Image
import os
import urllib
import re

class detector:
    def __init__(self):
        self.db = sqlite3.connect("detector.db")
        self.db.execute("CREATE TABLE IF NOT EXISTS rgb(r INT, g INT, b INT)")

    def check(self, image, auto=False):
        try:
            picture = Image.open(image).resize((50, 50)).getcolors(maxcolors=100000)
        except:
            print "Can't read that image."
            return

        print "Scanning image..."

        new = []
        for x,y in picture:
            new.append(y)
        
        bad = self.db.execute("SELECT * FROM rgb").fetchall()
          
        yes = []
        no = []
        
        for colors in new:
            if colors in bad:
                yes.append(colors)
            else:
                no.append(colors)
        
        if __name__ == "__main__":
            print "Yes votes {}".format(len(yes))
            print "No votes {}".format(len(no))
        
        if len(yes) >= len(no) or len(yes) > 1000:
            
            if not __name__ == "__main__":
                return True
            
            if not auto:
                check = raw_input("This picture is pornographic right?: ")
            elif auto:
                check = "yes"
            if check == "no" or check == "n":
                print "Oh.... awkward"
                for new in yes:
                    self.db.execute("DELETE FROM rgb WHERE r=? AND g=? AND b=?", new)

                self.db.commit()

            else:
                print "Oh, okay, I'll add it to the database"
                for new in yes:
                    if not self.db.execute("SELECT * FROM rgb WHERE r=? AND g=? AND b=?", new).fetchall():
                        self.db.execute("INSERT INTO rgb (r, g, b) VALUES (?, ?, ?)", new)
                for x in no:
                    self.db.execute("DELETE FROM rgb WHERE r=? AND g=? AND b=?", x)
                self.db.commit()

        else:
            if not __name__ == "__main__":
                return False

            if not auto:
                check = raw_input("This picture isn't pornograpic right?: ")
            elif auto:
                check = "no"
            if check == "no" or check == "n":
                print "Oh... wow, okay I'll add it to the database"
                for new in no:
                    x = self.db.execute("SELECT * FROM rgb WHERE r=? AND g=? AND b=?", new).fetchall()
                    if not x:
                        self.db.execute("INSERT INTO rgb (r, g, b) VALUES (?, ?, ?)", new)
                for x in yes:
                    self.db.execute("DELETE FROM rgb WHERE r=? AND g=? AND b=?", x)
                self.db.commit()
            else:
                print "Wow, I am good."
    
    



if __name__ == "__main__":
    d = detector()
    if sys.argv[1] == "auto":

        for x in os.listdir(os.getcwd()):
            if x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".png"):
                d.check(x, auto=True)
    
    if sys.argv[1] == "autolearn":
        
        # Good old 4chan, it finally came in handy for something.
        
        while True:
            pictures = "http://4chan.org/hc/"
            
            print pictures
            data = urllib.urlopen(pictures).read()
            links = re.findall("src=\"(.*?)\"", data)
            for y in links:
                if y.endswith(".jpg"):
                    with open("picture.jpg", 'wb') as file:
                        print y
                        try:
                            file.write(urllib.urlopen("http:"+y).read())
                        except:
                            continue
                    d.check("picture.jpg", auto=True)
    else:
        d.check(sys.argv[1])
