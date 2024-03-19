from random import choice

capital = "Topeka"
bird = "Western Bird"
flower = "Sunflower"

def randomfunfact():
    funfacts = [
        "Kansas is considred flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas city is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")
    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()