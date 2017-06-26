import media
import fresh_tomatoes

# List of all the movies and their links and info       
shrek = media.Movie("Shrek",
                    "An ogre stumbles upon a princess and falls in love",
                    "http://www.impawards.com/2001/posters/shrek_ver2_xlg.jpg",
                    "https://www.youtube.com/watch?v=W37DlG1i61s")

bill = media.Movie("Kill Bill Vol. 1",
                     "A highly trained assasin is on a mission for revenge",
                     "https://s-media-cache-ak0.pinimg.com/originals/41/1a/18/411a18522a6a79bb3a040eeeac422852.jpg", # noqa
                     "https://www.youtube.com/watch?v=ot6C1ZKyiME")

pilgrim = media.Movie("Scott Pilgrim vs The World",
                "Scott must fight to be with Romona",
                "http://img.moviepostershop.com/scott-pilgrim-vs-the-world-movie-poster-2010-1020561018.jpg", # noqa
                "https://www.youtube.com/watch?v=8NUBVcit5VM")

schindler = media.Movie("Schindler's List",
                  "A man saves hundreds of Jews from death",
                  "https://images-na.ssl-images-amazon.com/images/I/517nCQA7%2B%2BL.jpg", # noqa
                  "https://www.youtube.com/watch?v=M5FpB6qDGAE")

scream = media.Movie("Scream",
               "A masked serial killer is on the loose",
               "https://www.movieposter.com/posters/archive/main/199/MPW-99549", # noqa
               "https://www.youtube.com/watch?v=AWm_mkbdpCA")

wolf = media.Movie("The Wolf of Wall Street",
             "Jordan Belford is making a fortune selling pitty stocks",
             "http://cdn2.gbtimes.com/cdn/farfuture/7ioYXeoP0jyN23yX7PM0Bu7wi0A-YBwhSbkwUtH2wFA/mtime:1390289000/sites/default/files/styles/1280_wide/public/2014/01/20/thewolfofwallstreet.jpg?itok=gHJUwj_1", # noqa
             "https://www.youtube.com/watch?v=iszwuX1AK6A")

# array of the movies and their order to be displayed
# the fresh tomatoes know that these are the movies             
movies = [shrek, bill, pilgrim, schindler, wolf, scream]

# Program now opens the movies page and calls on the previous array
fresh_tomatoes.open_movies_page(movies)
         
