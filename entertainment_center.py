# imports fresh_tomatoes for HTML / CSS layout and open functions
import fresh_tomatoes
import media  # imports media class file to call it in this file

get_the_gringo = media.Movie("Get The Gringo",  # calls an instance movie class
                             "A story of a bank robber vacationing in Mexico",
                             "http://bit.ly/2bCwTBQ",
                             "https://www.youtube.com/watch?v=pi1eoi5uP-s")

gran_torino = media.Movie("Gran Torino",  # calls another instance of movie
                          "Korean War Vet has to make nice with the neighbors",
                          "http://bit.ly/2bhmBEY",
                          "https://www.youtube.com/watch?v=AUiU42iOi4M")

the_big_short = media.Movie("The Big Short",
                            "The Story of the 2008 housing crash",
                            "http://bit.ly/1M59Zvw",
                            "https://www.youtube.com/watch?v=5Zhy1NQf2NM")
safe_house = media.Movie("Safe House",
                         "Ex CIA operative is hunted by the CIA",
                         "http://bit.ly/2bopZgp",
                         "https://www.youtube.com/watch?v=mMf4N4TonhQ")

borne_ultimatum = media.Movie("Borne Ultimatum",
                              "Jason Borne is hunted by the Agency",
                              "http://bit.ly/2boqlU3",
                              "https://www.youtube.com/watch?v=N6J2oiKJr-A")
october_sky = media.Movie("October Sky",
                          "Boys in rural mining community build rockets",
                          "http://bit.ly/2bQ8QfY",
                          "https://www.youtube.com/watch?v=3eXPBhy7i10")

"""Not enough time to fix the 79 charachter length thing."""

movies = [get_the_gringo, gran_torino, the_big_short,
          safe_house, borne_ultimatum, october_sky]
# queries all of the different instances into one variable to call

fresh_tomatoes.open_movies_page(movies)
# calls the open_movies_page function from fresh tomatoes and inputes the list
# webpage is opened!!
