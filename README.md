<div style="text-align:center"><img src="https://static1.fjcdn.com/comments/Ahh+yes+_d951bbee810ba54ba379ec286a57a073.png"
alt="drawing" width="400"/>

### What does it do?
Downloads every image it can find on Rule34 that matches the tags you search for. 

## Dependencies
- Python3.5+
- [My Rule34 API wrapper](https://github.com/LordOfPolls/Rule34-API-Wrapper)

## How do i use it?

- Clone the repository
- Navigate to the root directory (the one with ``requirements.txt`` in)
- Run ``pip install -r requirements.txt``
  - This will install all dependencies
- Run main.py and follow on screen instructions
- Enjoy your excessive amount of porn

### FAQ

**Can I search for more than one tag at once?**

> Yes, the program treats each word as a tag; so ``gay furry`` is
> treated as two tags; ``gay`` and ``furry``

**What about multi-word tags?** 

>The program treats them the same way rule34 does, usually with
>underscores. Id suggest searching on rule34 first to make sure its a
>real tag. 

**Can i download a specific amount of images?**

>Not yet...

**Whats this ``cachedsearch.r34`` file?**

>The program stores all the files it could find in this file. Should the
>program close before the download is complete; it can use this file to
>resume the download. Then when the download completes, the file gets
>deleted. If youre curious, open it in notepad

**Why doesnt it have a popper gui?** 

>I really dont see the point in implementing one, there is only one way
>to go through this program. Plus, a fully fledged GUI would just make
>the program more resource intensive, and not add anything truly useful.

# Like what I do?

Why not buy me a coffee? [https://paypal.me/LordOfPolls](https://paypal.me/LordOfPolls)