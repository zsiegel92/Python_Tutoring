poem_template = "\n\nMy {relationship} {name} is {description}.\n{pronoun} is kind to me, but so prefers {favorite_thing}.\nIf I turned into {favorite_thing}\n{pronoun} would spend all {possessive_pronoun} time with {favorite_thing}.\nThankfully, {pronoun} spends some time with me.\n\n"

#Dad
print(poem_template.format(relationship="Dad",name="Lawrence",description="a really nice guy",pronoun="he",possessive_pronoun="his",favorite_thing="wonton soup"))

#Sister
print(poem_template.format(relationship="sister",name="Alison",description="an amazing artist",pronoun="she",possessive_pronoun="her",favorite_thing="colored pencils"))

#Me
print(poem_template.format(relationship="self",name="Zach",description="a silly but nice teacher",pronoun="he",possessive_pronoun="his",favorite_thing="writing tutorials"))
