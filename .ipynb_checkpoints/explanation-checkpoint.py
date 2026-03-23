def generate_explanation(query, image_path, score):
    return (
        f"The image '{image_path}' is relevant to the query '{query}' "
        f"with a similarity score of {score}. It likely contains visual elements, "
        f"scenes, or objects associated with '{query}', making it a strong match."
    )