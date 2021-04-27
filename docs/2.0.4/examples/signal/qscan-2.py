from gwpy.segments import Segment
search = Segment(gps-0.25, gps+0.25)
qgram = data.q_gram(qrange=(4, 150), search=search, mismatch=0.35)