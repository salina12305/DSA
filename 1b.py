def keyword_segmentation(query, keywords):
    memo = {}

    def split(text):
        if text in memo:
            return memo[text]

        if text == "":
            return [""]

        result = []

        for word in keywords:
            if text.startswith(word):
                rest = text[len(word):]

                for sentence in split(rest):
                    if sentence == "":
                        result.append(word)
                    else:
                        result.append(word + " " + sentence)
        memo[text] = result
        return result

    return split(query)

if __name__ == "__main__":
    query = "organicsearchmarketing"
    dictionary = ["organic", "search", "marketing", "organ", "ic", "searchmarketing"]

    answers = keyword_segmentation(query, dictionary)

    print("-" * 40)
    print("User Query:", query)
    print("Possible Segmentations:")
    for i, ans in enumerate(answers, 1):
        print(f"{i}. {ans}")
    print("-" * 40)