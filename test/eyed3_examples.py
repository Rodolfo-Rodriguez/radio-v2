import eyed3


# audiofile = 'Ginm4a'

# audiofile = eyed3.load(f_name)
# audiofile.initTag()

# tag_u = ('Title').decode('utf-8')
# audiofile.tag.title = tag_u

# tag_u = ('Buitres').decode('utf-8')
# audiofile.tag.artist = tag_u

# tag_u = ('Album').decode('utf-8')
# audiofile.tag.album = tag_u

# audiofile.tag.track_num = 1

#imagedata = open(image_f,"rb").read()
#audiofile.tag.images.set(3,imagedata,"image/jpeg",u"description")

audiofile.tag.save()