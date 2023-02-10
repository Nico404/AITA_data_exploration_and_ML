def count_occurrences(df, categories):
    result = {}
    for i, row in df.iterrows():
        post_id = row["post_id"]
        comment_content = row["comment_content"]
        counts = result.get(post_id, {})
        for category in categories:
            if category in comment_content:
                counts[category] = counts.get(category, 0) + 1
                break
        result[post_id] = counts

    for post_id, counts in result.items():
        for category in categories:
            counts[category] = counts.get(category, 0)

        result[post_id] = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

    return result
