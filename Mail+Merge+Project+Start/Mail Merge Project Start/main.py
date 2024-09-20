PLACEHOLDER = "[name]"

with open(r"Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt") as name_file:
    # "readlines" convert all the lines into a item and place in inside a list
    names = name_file.readlines()

with open(r"Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"C:\\Users\\aanand2\\OneDrive - Capgemini\\Desktop\\Python\\Codes\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Output\\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)