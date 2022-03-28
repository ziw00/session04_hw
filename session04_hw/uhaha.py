def extract_info(comics_list):
    result = []
    

    for comics in comics_list:
        title = comics.find("dt").find("a").string
        artist = comics.find("dd",{"class":"desc"}).find("a").string
        grade = comics.find("div",{"class":"rating_type"}).find("strong").string

        comics_info = {
            'title':title,
            'artist':artist,
            'grade':grade
        }
        result.append(comics_info)
    return result