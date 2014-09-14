About
=====

Detector is an algorithm that learns to detect patters within images that would be deemed inappropriate, or pornographic. I don't have much knowledge in machine learning prior to this project, but from what I can see the algorithm was capable of distinguishing appropriate from inappropriate images fairly well. It did take quite a bit of time for the algorithm to "learn" though, and I still have it learning as I am writing this.


How to use
==========

Get the algoithm learning automatically with

    python detector.py autolearn

WARNING: This will download inappropriate images and save them briefly.



This repo does not contain my detector.db file which is essentially the "brain" of this algorithm. Without the .db file the algorithm is dumb and has to learn again. Autolearn will generate this file and fill it with useful RGB values.

You can also import detector


    import detector
    d = detector.detector()
    check = d.check("image.jpg")
    # Check returns True or False
