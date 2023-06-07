def health(character):
    health_lost = 10 - character.health
    health_display = chr(0x2588) + chr(0x2502)
    dash_display = chr(0x2591) + chr(0x2502)
    display_health = health_display * character.health
    dash_zero = dash_display * health_lost
    console.print(display_health + dash_zero, style="failure")

health()