init 5 python:
    # --- Cyberpunk Compliment ---
    
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_chrome_shine",
            category=['mas_compliment'],
            prompt="You look like you just stepped out of Night City",
            unlocked=True
        ), code="CMP"
    )

label mas_comp_chrome_shine:
    m 1tub "Haha, you think so? Maybe I’ve got that cyber-chic look down!"
    m 3hub "Or maybe it’s just because you make me glow like neon~"
    $ mas_gainAffection(3, bypass=False)
return "love"
