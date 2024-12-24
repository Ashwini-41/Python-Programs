animals_and_sounds = {
    "Duck": "quack",
    "Turkey": "gobble",
    "Cow": "moo",
    "Cat": "meow",
    "Dog": "bow wow",
    "Turtle": "nerp"
}

with open("File_IO\poem.txt", "r") as file:
    template_poem = file.read()

completed_poem = ""
for animal, sound in animals_and_sounds.items():
    animal_poem = template_poem.replace("%ANIMAL%", animal).replace("%SOUND%", sound)
    completed_poem += animal_poem + "\n"  

with open("File_IO\completed_poem.txt", "w") as file:
    file.write(completed_poem)

print("The completed poem has been written to 'completed_poem.txt'.")