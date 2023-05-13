# Project_comp
A repository for watchlist organization; love mangas/manhwas but dont know which one is good to start, thought maybe have an organization tool would help

# Overview
### [Compare.py](compare.py)
- Takes in two `.txt` files, gathers the unique items/lines are puts them in a 3rd `.txt`;
    - Input in `text1.txt`, `text2.txt`; output in `text3.txt`
    - Change separator accordingly; right now separator is just new line;
- 3rd `.txt` will be all items with no repeat;
- Could be use for 2 watchlists

### [watchlist_gui.py](watchlist_gui.py)
- GUI for watchlist organization, and continuously add new items onto old watchlist (dung beetle logic)
- Saves old watchlist as `.sqlite` instead of `.txt` -> Easier organization

# Future development plan/ideas/improvements
- Old list be in a table showing rating (Web scraping? MAL?)
    - Periodic update?
- Table could have <br>
| name | Rating | Status |
- In the new pop-up window, have box to update whether or not the item has been watched/read
- Organization: Show only read/unread; order by rating

