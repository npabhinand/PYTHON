PLACEHOLDER="[name]"
with open("C:/Users/npabh/OneDrive/Desktop/project/python/udemy/files/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as f:
    letters=f.read()
with open("C:/Users/npabh/OneDrive/Desktop/project/python/udemy/files/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as f:
    names=f.readlines()
for name in names:
    new_letters=letters.replace(PLACEHOLDER,name.strip())
    with open(f"Output/ReadyToSend/letter_to_{name.strip()}.txt",mode="w") as file:
        file.writelines(new_letters)
    # letter[]