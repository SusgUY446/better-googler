def generate_prompt():

    print("INFO")
    print("Leave options empty to not specify that parameter")
    print("------------------------------------------------------")

    print("Search for:")
    search_for = input()

    print("Site:")
    site = input()

    print("Filetype:")
    filetype = input()

    print("In URL:")
    inurl = input()

    print("in text:")
    intext = input()

    print("before date:")
    before_date = input()

    print("after date:")
    after_date = input()

    
    # this logic is needed to leave empty parameters out of the prompt
    if site != None:
        site_true = True
    else:
        site_true = False

    
    if filetype != None:
        filetype_true = True
    else:
        filetype_true = False

    if  inurl != None:
        inurl_true = True
    else:
        inurl_true = False

    if  intext != None:
        intext_true = True
    else:
        intext_true = False

    if before_date != None:
        before_date_true = True
    else:
        before_date_true = False

    if  after_date != None:
        after_date_true = True
    else:
        after_date_true = False


    # make the prompt
    prompt = f"{search_for}"

    if site_true:
        prompt = f"{search_for} SITE:{site}"

    if filetype_true:
        prompt = f"{search_for} SITE:{site} FILETYPE:{filetype}"
    
    if inurl_true:
        prompt = f"{search_for} SITE:{site} FILETYPE:{filetype} INURL:{inurl}"

    if intext_true:
        prompt = f"{search_for} SITE:{site} FILETYPE:{filetype} INURL:{inurl} INTEXT:{intext}"

    if before_date_true:
        prompt = f"{search_for} SITE:{site} FILETYPE:{filetype} INURL:{inurl} INTEXT:{intext} BEFORE:{before_date}"

    if after_date_true:
        prompt = f"{search_for} SITE:{site} FILETYPE:{filetype} INURL:{inurl} INTEXT:{intext} BEFORE:{before_date} AFTER:{after_date}"

    
    print("------------------------------------------")
    print("PROMPT:")
    print(prompt)


generate_prompt()
