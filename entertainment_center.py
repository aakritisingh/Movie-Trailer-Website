import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that comes to life",
	"http://images.fanpop.com/images/image_uploads/Toy-Story-2-pixar-116966_1024_768.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

legally_blonde = media.Movie("Legally Blonde", "Fashion merchandising student goes to Harvard Law School", 
	"https://upload.wikimedia.org/wikipedia/en/a/ac/Legally_blonde.jpg", "https://www.youtube.com/watch?v=E8I-Qzmbqnc")

wonder_woman = media.Movie("Wonder Woman", "Diana Prince arrives to London leaving her home to fight God Zeus", 
	"http://cdn.collider.com/wp-content/uploads/2017/03/justice-league-wonder-woman-poster.jpg", "https://www.youtube.com/watch?v=VSB4wGIdDwo")

baywatch = media.Movie("Baywatch", "Story about the lifeguards and how far they go to protect beach from dangerous crimes", 
	"https://i.ytimg.com/vi/gUFgJ8f9slo/maxresdefault.jpg", "https://www.youtube.com/watch?v=TDteZ0YrhSU")

baby_driver = media.Movie("Baby Driver", "Talented gateway driver tries to leave his shady life but couldn't get out due to other villains", 
	"https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg", "https://www.youtube.com/watch?v=D9YZw_X5UzQ")

dunkirk = media.Movie("Dunkirk", "Story revolves around May 1940 where French and German troops fight on the land of Dunkirk", 
	"https://m0.joe.ie/wp-content/uploads/2017/07/07151915/Dunkirk-poster-2.jpg", "https://www.youtube.com/watch?v=F-eMt3SrfFU")


#import fresh_tomaotoes from the repository which will help in calling the function open_movies_page 
#open_movies_page takes one argument as list of movies, and it creates HTML file which will display all the favorite movies
#Make sure the 	website renders correctly when attempted to load in browser

movies_list = [toy_story, legally_blonde, wonder_woman, baywatch, baby_driver, dunkirk]

fresh_tomatoes.open_movies_page(movies_list)

