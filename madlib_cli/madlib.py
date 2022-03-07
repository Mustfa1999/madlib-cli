def read_template(path):
    """
    This function takes a relative path, open it,
    delete the leading and trailing spaces, then 
    return it.

    It's also able to handle I/O errors.
    """
    try:
        return open(path).read().strip()
    except FileNotFoundError:
        raise(FileNotFoundError)


def parse_template(script):
    """
    This function takes a template(string) and extract all the
    phrases within any two curly brackets {}. It also delete those 
    phrases from the original script.
    
    It returns the modifyed script besides the tuple of phrases.
    """
    lower, upper, parts = 0, len(script)-1, []
    
    for _ in range(script.count("{")):
        left, right = script.find("{", lower, upper), script.find("}", lower, upper)
        parts.append(script[left+1:right])
        script = script[:left+1] + script[right:]
        lower = left + 2

    return script, tuple(parts)


def merge(script, answers):
    """
    This function takes a "bare" script (a string with empty 
    curly brackets) and a tuple of phrases. It insert the phrases 
    respectively inside the curly brackets on the script and return 
    the result.
    """
    return script.format(*answers)


def mad_lib_game():
    print("Greetings .. Welcome to the Madlib game !!!\nPlease answer the next questions with whatever you feel funny ^_^\n")
    template = read_template(r"assets/dark_and_stormy_night_template.txt")
    script, choices = parse_template(template)
    answers = [input(f"\nChoose a {i}: ") for i in choices]
    return merge(script, answers)

