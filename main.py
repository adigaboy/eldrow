from typing import List, Optional
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/options", response_class=HTMLResponse)
def options(
    request: Request,
    characters: List[Optional[str]] = Form(...),
    excludedChars: List[Optional[str]] = Form(...),
    unboundChars: List[Optional[str]] = Form(...)
):
    if not characters:
        raise HTTPException(status_code=400, detail="At least one character must be entered")
    regex_exp = build_regex_exp(characters)
    all_options = get_all_options(regex_exp, len(characters))
    partial_options = filter_unbound_characters([char for char in unboundChars[0]], all_options)
    filtered_options = filter_excluded_characters(excludedChars, partial_options)

    return templates.TemplateResponse(
        "options.html",
        context={
            "request": request,
            "char_request": characters,
            "perms": filtered_options,
            "excluded_chars": excludedChars,
            "unbound_chars": unboundChars,
        }
    )

def build_regex_exp(chars: List[str]) -> str:
    """
    Build a regex pattern from a list of characters.
    
    Args:
        chars (List[str]): A list where each member is either a character or an empty string.
        
    Returns:
        str: A regex pattern that matches a string based on the provided list.
    """
    # Start with an empty pattern
    pattern = ''
    
    for char in chars:
        if char == '':
            pattern += '.'  # Use '.' to match any character
        else:
            pattern += re.escape(char)  # Escape the character to avoid special regex interpretation
    
    return '^' + pattern + '$'  # Match the whole string

def build_exclude_regex(chars: str) -> str:
    # Escape any special regex characters in the chars list
    escaped_chars = [re.escape(char) for char in chars]
    # Join escaped characters with '|' to match any of them
    regex_pattern = f"[{''.join(escaped_chars)}]"
    return regex_pattern

def get_all_options(characters: str, chars_count: int) -> set[str]:
    options = set()
    with open('words_alpha.txt', mode='r') as words_file:
        for word in words_file.read().splitlines():
            if len(word) == chars_count:
                res = re.search(characters, word)
                if res:
                    options.add(res.string)
    return options

def filter_unbound_characters(unbound_chars: List[str], words: List[str]) -> List[str]:
    if unbound_chars == ['']:
        return words
    correct_words = []
    for word in words:
        word_set = set(word)
        if all(char in word_set for char in unbound_chars):
            correct_words.append(word)
    return correct_words

def filter_excluded_characters(excluded_chars: List[str], words: List[str]) -> List[str]:
    if excluded_chars == ['']:
        return words
    correct_words = []
    for word in words:
        if not re.search(build_exclude_regex(excluded_chars[0]), word):
            correct_words.append(word)
    return correct_words


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
