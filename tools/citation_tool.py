def extract_citations(results):

    citations = []

    for item in results:

        citations.append(
            {
                "title": item.get("title"),
                "url": item.get("url")
            }
        )

    return citations