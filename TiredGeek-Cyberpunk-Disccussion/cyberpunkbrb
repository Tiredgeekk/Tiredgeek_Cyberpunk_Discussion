# topic: Need to do a quick data run
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="brb_data_run",
            category=['be right back'],
            prompt="Need to do a quick data run",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label brb_data_run:
    $ ev = mas_getEV("brb_data_run")

    m 3tub "A data run, huh? Just make sure you don’t get flatlined out there, [player]!"
    m 5hub "I’ll keep your connection stable till you’re back~"

    $ mas_idle_mailbox.send_idle_cb("brb_data_run_callback")
    return "idle"

label brb_data_run_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "brb_data_run"):
        m 3hub "Hey, you’re back! I was starting to worry a corpo got to you, ehehe."
    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "brb_data_run"):
        m 3hub "Welcome back, netrunner~ How’d the job go?"
    else:
        m 3hub "Back already? Must’ve been a quick gig, huh?"
    return
