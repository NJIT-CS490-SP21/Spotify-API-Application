
# Joseph Stapleton - CS490 - Project 1
This project uses spotify api and genius api to find popular artist song information, display the information, and a way to access their lyrics.
## Requirements

1. ```pip install python-dotenv ```
2. ```pip install requests ```
3. ```pip install flask ```

## Setup
1. Create ```.env ``` file in your directory
2. Add your Spotify Developer ```client-id``` and ```client-secret``` keys with:
   *  ``` export client-id = 'your-client-id ``` and 
   *  ``` export client-secret = 'your-client-secret' ```
3. Add your Genius Developer Authentication Token key into your ```.env``` file:
   *  ``` export genius-access-token = "your-genius-access-token" ```

## Run Application
1. Run ```python app.py``` in command terminal

## Additional Features
I have no known ploblems currently, but I have some new features I was thinking of implementing in my code:
1. One was to have all of the artists on the html and when clicked it would show songs of that artist. I would do this by:
    * having the artists in an array, and display those artists within individual text boxes
    * clicking on the textbox would grab a random song, from that artist.
    * I would only need to manipulate my code a little to get rid of randomly choosing an artist and send the data back from the web app using Java Objects, json/arrays, and then go through the process of finding the songs again
    * Work would be needed to display the intial page and then connect the variables to the textboxes
2.  Another was to have albums displayed and when clicked would show all of the songs in that album.  I would do this by:
    *  having the album cover image clickable using html and send back the album information when clicked
    *  I would need to do some work to make the inital page but once I get the variable to connect it would be very simple.
    *  The hard part would be displaying everything without it looking bad
3.  I could also combine these two thoughts and have artists displayed and when clicked, show popular albums by this artists. Then when clicking an album show songs in that album and then you might be actually able to play the song instead of just the preview.
    * This would require connecting the two pages of the previous suggestion, but if the two parts are done, it would be very simple to just connect the pages.

## Technical Issues
One specific problem I had was that I was recieving random errors when accessing the JSON. 
* Sometimes my JSON would give an error saying 'tracks' is not a valid key. I believe that when grabbing the top tracks from a specific artist, the JSON did not actually have the 'tracks' key.
*I fixed this by doing a try/except around all of the lines of code that require me to go through the JSON. I had a while loop around that code anyways and would just continue if there is an error.
* In the while loop I also had the code to grab the api, so everytime I get an error in my JSONI would just grab a new one and check again.
* This does not explain why I got the error but I was able to solve the problem with minimal lines of code, I believe.

Another specific problem I had was in the begining with the GET request.

*  I basically copied and pasted from hw5 but it didn't work.
*  I was able to get to the Spotify Developers page from the link you gave us and I was able to figure out that I needed another parameter to account for the market.
*  I then tried market='US' given in the link on the Developers page about this parameter, but it did not work.
*  I tried multiple different ways but could not figure it out until I got to a page that did that specific request.
*  It didn't need market='US', it needed params='ES' as 'US' is not on the market for most songs for some reason.

Another specfic problem I ran into was displaying the preview audio.  Most of the songs I encountered did not have a preview audio.
*  The first thing I thought of was that I need to know the what information I am showing in the html.
*  I made an array with a random 0 or 1 for every variable I had.  
*  I then checked if the number corresponding to the preview audio was 1, meaning that we are displaying it.
*  After grabbing the information form the JSON, I checked if the preview audio actually exists and isn't None.  
*  If it doesn't exist and I am supposed to show it, I would go through my while loop again and grab information on a different artist and song, and check again.
*  Once that is done I know that I can display all the information I am supposed to and would then send it to the html to show.