import fresh_tomatoes
import media

get_the_gringo = media.Movie("Get The Gringo",
                        "A story of a bank robber vacationing in Mexico",
                        "http://www.gstatic.com/tv/thumb/movieposters/9134074/p9134074_p_v8_ae.jpg",
                        "https://www.youtube.com/watch?v=pi1eoi5uP-s")
#print(toy_story.storyline)
gran_torino = media.Movie("Gran Torino",
                     "A story of a Korean War Vet that has to make nice with the neighbors",
                     "https://upload.wikimedia.org/wikipedia/en/c/c6/Gran_Torino_poster.jpg",
                     "https://www.youtube.com/watch?v=AUiU42iOi4M")
#print(avatar.storyline)
#avatar.show_trailer()
the_big_short = media.Movie("The Big Short",
                     "The Story of the 2008 housing crash and how a couple funds profited",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcTXyM8ObeZ-zWDqxf0Q40iOeWw26uXJ7CTfGVoxyez5PVokMYqB",
                     "https://www.youtube.com/watch?v=5Zhy1NQf2NM")
safe_house = media.Movie("Safe House",
                     "Ex CIA operative is hunted by the CIA",
                     "https://upload.wikimedia.org/wikipedia/en/d/d0/Safe_House_Poster.jpg",
                     "https://www.youtube.com/watch?v=mMf4N4TonhQ")

borne_ultimatum = media.Movie("Borne Ultimatum",
                     "Jason Borne is hunted by the Agency",
                     "http://img.goldposter.com/2015/04/The-Bourne-Ultimatum_poster_goldposter_com_9.jpg",
                     "https://www.youtube.com/watch?v=N6J2oiKJr-A")
october_sky = media.Movie("October Sky",
                     "A few boys living in a rural mining community build rockets and beat the odds",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcQzuXaV2cKW7z_N2_-7hc8WizhSAdKalq31RVCunHP3PV_-65aJ",
                     "https://www.youtube.com/watch?v=3eXPBhy7i10")

movies = [get_the_gringo, gran_torino, the_big_short, safe_house, borne_ultimatum, october_sky]
fresh_tomatoes.open_movies_page(movies)
