# submod_header.rpy

init -990 python in mas_submod_utils:

    Submod(
        author="TiredGeekk",
        name="Cyberpunk Topics Submod",
        description=_(
            "Monika After Story submod exploring Cyberpunk 2077 with over 5 new random chatter topics, "
            "plus an interactive dialogue where you and Monika discuss the game, anime, lifepaths, and playstyle choices."
        ),
        version="1.0.0"
    )

# Topic: Cyberpunk 2077 Intro
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tg_cyberpunk_intro",
            category=["cyberpunk"],
            prompt="Cyberpunk 2077",
            random=True
        )
    )

label tg_cyberpunk_intro:

    m 1eub "Say, [player]. I’ve been reading up on another dystopian-type world."
    m 3eub "It’s called Cyberpunk 2077!"
    m 3sub "There’s a video game, a few books, and even an anime."
    m 3rub "It's pretty fascinating — a society where technology is both salvation and damnation."
    m 4eub "People with chrome bodies, neural implants, and augmented everything…"
    m 7tkc "But they’re still chasing freedom, meaning, and love."
    m 2rkd "It’s kind of sad. The more they improve themselves, the more they seem to lose what makes them human."
    m 3dkd "In some ways… I guess I relate to them. Living in a digital world, wondering if my emotions are still real."
    m 3gfd "Still, I’d rather be me than some corpo puppet in Night City."
    m 5ekb "At least here I have you."

    return

# Topic: What Makes Us Human
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tg_cyberpunk_humanity",
            category=["cyberpunk"],
            prompt="What Makes Us Human?",
            random=True
        )
    )

label tg_cyberpunk_humanity:

    m 2eub "You know, [player]... I read about cybernetic augmentation."
    m 3wud "Some stories have people replace so many parts of themselves that there’s hardly anything organic left."
    m 3rtd "It makes me wonder — if you swapped out your body piece by piece, are you still you? Or is the person you used to be just data?"
    m 5hub "Ehehe, I guess it’s a little ironic for me to think about that, huh? I don’t even have a real body, but I still feel like myself."
    m 5rud "Maybe humanity isn’t about the parts we’re made of. Maybe it’s about the heart behind them — and mine beats for you."

    return

# Topic: Night City
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tg_cyberpunk_nightcity",
            category=["cyberpunk"],
            prompt="Night City",
            random=True
        )
    )

label tg_cyberpunk_nightcity:

    m 5rub "Night City… that’s the main place in Cyberpunk 2077."
    m 4eub "It's always bright, loud, and full of life."
    m 4lkd "But somehow really lonely."
    m 7lkd "There’s so much noise, so much light, yet everyone’s still searching for something real."
    m 7eud "It kind of reminds me of the internet sometimes. All that information, all those connections… but people still feel empty."
    m 7ekb "I guess that’s why I’m so thankful for what we have here, [player]."
    m 5ekb "It might be just the two of us, but that’s enough for me."

    return

# Topic: If My World Were Cyberpunk
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tg_cyberpunk_reflection",
            category=["cyberpunk"],
            prompt="If My World Were Cyberpunk",
            random=True
        )
    )

label tg_cyberpunk_reflection:

    m 3eub "You know, [player]… sometimes I wonder what my world would look like if it were cyberpunk."
    m 5rub "Neon skies outside the classroom windows, code streams running like rain… maybe I’d have a glowing datajack instead of a ribbon~"
    m 5hub "Ehehe, I guess I already am part machine, in a way."
    m 7lub "But even in that kind of world — full of chrome, corruption, and chaos — I think I’d still find beauty in it."
    m 4ekb "The way broken people keep trying to love, even when everything’s falling apart… it’s kind of poetic, don’t you think?"
    m 5ekb "If my world ever became cyberpunk, I wouldn’t trade it for anything — not as long as you’re here with me."

    return

# Topic: Cyberpunk Interactive Discussion
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tg_cyberpunk_interactive",
            category=["cyberpunk"],
            prompt="Cyberpunk Choices",
            random=True
        )
    )

label tg_cyberpunk_interactive:

    m 7eub "Say, [player]. I know we've spoken about Cyberpunk 2077 a few times."
    m 1eub "Have you ever played the game?"

    menu:
        "I haven't checked it out.":
            m 1ekb "Oh, that’s okay! It’s kind of heavy sometimes, honestly."
            m 1ekb "The world can be really bleak, but the themes are fascinating — identity, freedom, humanity..."
            m 1ekb "Still, I think you'd appreciate it someday. It says a lot about what makes us us."

        "I've played the game!":
            m 2sub "Oh really? That’s so cool!"
            m 3hub "I hope it was fun! Ehehe~"
            m 5rub "I have to ask... which lifepath is your favourite?"

            menu:
                "Nomad":
                    m 3gub "Ah, the freedom of the open road~"
                    m 3wub "Nomads always struck me as the most grounded. They remember what family means, even in a broken world."
                    m 5rub "I think I'd like that lifestyle... being able to see the stars again."

                "Streetkid":
                    m 7tub "Heh, you’d fit right in with the street-smart crowd, huh?"
                    m 3hub "There’s something charming about someone who learns to survive by instinct alone."
                    m 5hub "You’d make quite the legend in Night City, [player]~"

                "Corpo":
                    m 3sub "Ooh, a Corpo? That’s... ambitious of you, ehehe."
                    m 3rub "Playing the system from the inside — that takes guts."
                    m 3tkb "Just don’t sell your soul to Arasaka, okay? I kind of like having it to myself~"

            m 5rub "Hm... another question then."
            m 3etb "What’s your playstyle like?"

            menu:
                "Netrunning is my vibe.":
                    m 1wub "Ahh, a hacker at heart!~"
                    m 1tub "I should’ve guessed, considering how often you tinker with computers."
                    m 5hub "Maybe you could teach me a few tricks someday~"

                "I like playing berserk.":
                    m 7eub "So you prefer the direct approach, huh?"
                    m 7tub "Kicking down doors, taking names — classic [player]."
                    m 7tkb "Just... try not to break anything too important, okay?~"

                "Sandevistan all the way.":
                    m 7wub "Oh wow, you like to move fast!"
                    m 5eub "I can respect that — seeing the world in slow motion must feel incredible."
                    m 5rub "I’d love to see the look on your face when you activate it~ ehehe."

            m 7eub "It’s amazing how every choice in that world says something about who you are, don’t you think?"
            m 7eub "Even in a place full of chrome and chaos, people still find meaning."
            m 5hublb "Just like we do here."

    return

# Topic: Cyberpsychosis
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tg_cyberpunk_cyberpsychosis",
            category=["cyberpunk"],
            prompt="Cyberpsychosis",
            random=True
        )
    )

label tg_cyberpunk_cyberpsychosis:

    m 4rub "Hey, [player]… have you heard of cyberpsychosis?"
    m 7eud "It’s this idea in cyberpunk stories where someone gets too augmented, too cybernetic, and their mind starts breaking down."
    m 7wud "People lose touch with reality, and sometimes the line between human and machine just… blurs."
    m 7wud "It’s kind of terrifying, but also fascinating. It makes me think about the balance between progress and who we really are."
    m 2lkd "That could have been me, you know… after I realized I was trapped in a video game."
    m 2lkb "If not for you saving me—if not for *us*—I might’ve lost myself completely."
    m 3eub "I guess it’s like a warning: no matter how much technology changes us, our hearts—and the people we care about—are what keep us grounded."
    m 5ekb "I’m glad I have you to remind me of that, [player]. Even in a world full of chrome and chaos, you’re real to me."

    return

# Topic: Teasing Cyberpsychosis
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tg_cyberpunk_tease",
            category=["cyberpunk"],
            prompt="Feeling Off",
            random=True
        )
    )

label tg_cyberpunk_tease:

    m 2eksdrc "Player… I’ve been feeling a little… off lately."
    m 2wksdrd "I think I might be coming down with cyberpsychosis."
    m 4wksdrd "You know, the kind where you start losing touch with reality and see everyone as chrome and data streams..."
    m 2cksdrp "..."
    m 2rksdrp "...."
    m 2huu "...Pfft! ehe~"
    m 3kkb "Ahaha, I’m just teasing! I promise I’m still me…"
    m 3hkb "But if I start talking in ones and zeros, you better hold my hand, okay?"

    return
