import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that comes to life",
	"https://en.wikipedia.org/wiki/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

legally_blonde = media.Movie("Legally Blonde", "Fashion merchandising student goes to Harvard Law School", 
	"https://en.wikipedia.org/wiki/Legally_Blonde#/media/File:Legally_blonde.jpg", "https://www.youtube.com/watch?v=E8I-Qzmbqnc")

wonder_woman = media.Movie("Wonder Woman", "Diana Prince arrives to London leaving her home to fight God Zeus", 
	"https://en.wikipedia.org/wiki/File:Wonder_Woman_(2017_film).jpg", "https://www.youtube.com/watch?v=VSB4wGIdDwo")

baywatch = media.Movie("Baywatch", "Story about the lifeguards and how far they go to protect beach from dangerous crimes", 
	"https://en.wikipedia.org/wiki/Baywatch_(film)#/media/File:Baywatch_poster.jpg", "https://www.youtube.com/watch?v=TDteZ0YrhSU")

baby_driver = media.Movie("Baby Driver", "Talented gateway driver tries to leave his shady life but couldn't get out due to other villains", 
	"https://en.wikipedia.org/wiki/Baby_Driver#/media/File:Baby_Driver_poster.jpg", "https://www.youtube.com/watch?v=D9YZw_X5UzQ")

dunkirk = media.Movie("Dunkirk", "Story revolves around May 1940 where French and German troops fight on the land of Dunkirk", 
	"https://en.wikipedia.org/wiki/Dunkirk_(2017_film)#/media/File:Dunkirk_Film_poster.jpg", "https://www.youtube.com/watch?v=F-eMt3SrfFU")


#import fresh_tomaotoes from the repository which will help in calling the function open_movies_page 
#open_movies_page takes one argument as list of movies, and it creates HTML file which will display all the favorite movies
#Make sure the 	website renders correctly when attempted to load in browser

movies_list = [toy_story, legally_blonde, wonder_woman, baywatch, baby_driver, dunkirk]

fresh_tomaotoes.open_movies_page(movies_list)

