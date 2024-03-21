from rich import print

print("Enter the title")
title = input(">")
print("Enter the content")
lis = ""
while True:
    content = input(">")
    if content == "":
        content = "<br>\n"
    elif content == "-":
        break
    else:
        content += "<br>\n"
    lis += content
exlpln = ""
while True:
    content = input(">")
    if content == "":
        content = "<br>"
    elif content == "-":
        break
    else:
        content += "<br>"
    exlpln += content


print(lis)
print("enter the date")
date = input(">")
sheet = f"""<div class="card">
        <div>
            <h2 class="card_title">{title}</h2>

            <p class="content">
            {lis}
            </p>
            <p class="date">{date}</p>
        </div>
        <span class="line"></span>

        <div class="meaning">

            <div class="summary">
                <h2 class="card_title">Explaination</h2>
                <div class="inline"></div>
                <p class="content">
                {exlpln}
                </p>
            </div>
        </div>
    </div>"""

print(sheet)
