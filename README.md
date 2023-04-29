# Project_comp
A repository for watchlist organization; love mangas/manhwas but dont know which one is good to start, thought maybe have an organization tool would help

# Overview
- Takes in two `.txt` files, gathers the unique items/lines are puts them in a 3rd `.txt`;
    - Input in `text1.txt`, `text2.txt`; output in `text3.txt`
    - Change separator accordingly; right now separator is just new line;
- 3rd `.txt` will be all items with no repeat;
- Could be use for 2 watchlists

# Future development plan/ideas
- Set up GUI so that multiple watchlists could be entered instead of one (use textbox?)
    - New window for every new watchlist, and just continuously add new items onto old watchlist (dung beetle logic)
- Multiple separators (Anything that is not whitespace/alphabet/number?)
    - Could have user specify in GUI (entry box)
- Saves old watchlist as `.sqlite` instead of `.txt` -> Easier organization
- Old list be in a table showing rating (Web scraping? MAL?)
    - Periodic update?
- Table could have 
| name | Rating | Status |

