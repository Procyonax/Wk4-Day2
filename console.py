import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()

# artist1 = Artist("Deftones")
# artist_repository.save(artist1)
# artist2 = Artist("Queen")
# artist_repository.save(artist2)


# album = Album("Adrenaline", artist1, "Nu Metal")
# album_repository.save(album)

result1 = artist_repository.select(21)
print(result1)

result = artist_repository.select_all()

for artist in result:
    print(artist.__dict__)

result = album_repository.select_all()

for album in result:
    print(album.__dict__)

# pdb.set_trace()