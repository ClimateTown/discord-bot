## NOTES
# For now this is in debug mode and not meant to be used as discord bot but like any other python program
# I'm sure that with proper url libs we can handle this more elegantly, this is just the simplest form, eventually we will probably upgrade it to proper libraries
# These variables are useful to make the text colored for better debugging, but they will be removed alongside most of the print() functions once the testing is complete
red = "\033[31;1m"
yellow = "\033[33;1m"
green = "\033[32;1m"
reset = "\033[0m"

## Funcitons
# Here I shall put the functions the bot will call.

# This function identifies what type of link it's dealing with so other functions act accordingly
# It should also identify if embedding is necessary
def identifier(link):
    # Youtube links do not need further embedding
    if "youtu.be" in link or "youtube" in link:
        id_link = "yt"
        needs_embed = False
        print(f"{green}Link type: {id_link}{reset}")
        print(f"{green}Needs embed: {needs_embed}{reset}")
        return id_link, needs_embed
    # Instagram is handled differently than YT and it only needs embedding if it's the default link
    elif "instagram" in link:
        id_link = "ig"
        if "dd" in link or "ez" in link or "kk" in link: # dd, ez and kk are the most used embedders, idk if there's others, might change this
            needs_embed = False
        else:
            needs_embed = True
        print(f"{green}Link type: {id_link}{reset}")
        print(f"{green}Needs embed: {needs_embed}{reset}")
        return id_link, needs_embed
    else:
        print(f"{red}This link is currently unsupported or not recognized. Quitting.{reset}")
        quit()

# This removes tracking strings
def sanitizer(link, id_link):
    print(f"{yellow}Sanitizing {link}...{reset}")
    # For youtube we need to just remove "?si=" and the string that follows.
    if id_link == "yt":
        # Because often the timestamp (&t=) is after ?si but we might wanna keep it I parse it then add it back on the link.
        # The if statement exists because if there's no &t= the bot crashes.
        if "&t=" in link:
            timestamp = link.split("&t=")[1]
            sanitized_link = link.split("?si=")[0]
            sanitized_link = f"{sanitized_link}&t={timestamp}"
        else:
            sanitized_link = link.split("?si=")[0]
    # For instagram we generally want to remove everything after "/?" but IG stories have a different URL with just "?igsh=" hence the double delete.
    elif id_link == "ig":
        sanitized_link = link.split("/?")[0]
        sanitized_link = sanitized_link.split("?igsh=")[0]
    return sanitized_link

# This will make links embed
def embedder(link, id_link):
    print(f"{yellow}Embeddizing {link}...{reset}")
    # For now only IG is supported and I'm using ez since it usually has the least amoung of embed fails.
    if id_link == "ig":
        embedder_link = link.replace("instagram", "instagramez")
    return embedder_link

## Code execution
# This is where the code is actually ran

# First we'd want to grab links from text.
# Eventually we want to support more links and actually parsing inks from text.
# For now we manually input a link to test if the sanitizer and embedder functions work.
link = input("Please insert link: ")
link.strip()

# Once we add support for multiple links we might want to put the code below into its own function!

# Identify the link and if it needs embedding
id_link, needs_embed = identifier(link)

# Sanitize the link
sanitized_link = sanitizer(link, id_link)
print(f"{green}Sanitized link: {sanitized_link}{reset}")

# Make link embed better
# note: we should ensure that if the parsed link in the text is between < > we should override identifier()'s needs_embed
if needs_embed:
    embedder_link = embedder(sanitized_link, id_link)
    print(f"{green}Embedder link: {embedder_link}{reset}")
else:
    print(f"{red}Embedder not necessary.{reset}")
