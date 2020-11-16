def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return email


print(replace_domain('shafan@gmail.com', "gmail.com", "hotmail.com"))


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return print(result)

count_letters("aaaaaaaallllllllllllll")
count_letters("A really long run on sentence, with many words and repeated letters.")

# With this same concept make a function that checks error logs, using error messages.
