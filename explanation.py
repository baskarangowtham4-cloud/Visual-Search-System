def generate_explanation(query, image_id, score):
    return (
        f"The image '{image_id}' is relevant to the query '{query}' "
        f"with a similarity score of {score}. It likely contains visual elements "
        f"or scenes associated with '{query}'."
    )