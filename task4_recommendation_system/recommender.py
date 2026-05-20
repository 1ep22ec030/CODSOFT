MOVIES = [
    {"title": "Interstellar", "genres": {"sci-fi", "adventure", "drama"}},
    {"title": "Inception", "genres": {"sci-fi", "action", "thriller"}},
    {"title": "The Dark Knight", "genres": {"action", "crime", "drama"}},
    {"title": "Finding Nemo", "genres": {"animation", "adventure", "family"}},
    {"title": "The Social Network", "genres": {"biography", "drama", "technology"}},
    {"title": "Toy Story", "genres": {"animation", "comedy", "family"}},
    {"title": "Avengers: Endgame", "genres": {"action", "sci-fi", "adventure"}},
    {"title": "A Beautiful Mind", "genres": {"biography", "drama"}},
    {"title": "Coco", "genres": {"animation", "family", "music"}},
    {"title": "The Martian", "genres": {"sci-fi", "adventure", "comedy"}},
]


def recommend_movies(preferred_genres, limit=5):
    scored_movies = []

    for movie in MOVIES:
        matches = preferred_genres.intersection(movie["genres"])
        if matches:
            score = len(matches) / len(movie["genres"])
            scored_movies.append((score, len(matches), movie, matches))

    scored_movies.sort(reverse=True, key=lambda item: (item[0], item[1], item[2]["title"]))
    return scored_movies[:limit]


def display_movies():
    print("Available movies:")
    for number, movie in enumerate(MOVIES, start=1):
        genres = ", ".join(sorted(movie["genres"]))
        print(f"{number}. {movie['title']} ({genres})")


def main():
    print("Content-Based Movie Recommendation System")
    print()
    display_movies()
    print()

    raw_input = input("Enter your preferred genres separated by commas: ")
    preferred_genres = {genre.strip().lower() for genre in raw_input.split(",") if genre.strip()}

    if not preferred_genres:
        print("Please enter at least one genre.")
        return

    recommendations = recommend_movies(preferred_genres)

    print()
    if not recommendations:
        print("No exact matches found. Try genres like sci-fi, action, drama, family, or comedy.")
        return

    print("Top recommendations:")
    for rank, (score, matches_count, movie, matches) in enumerate(recommendations, start=1):
        matched_text = ", ".join(sorted(matches))
        genre_text = ", ".join(sorted(movie["genres"]))
        print(f"{rank}. {movie['title']} - score {score:.2f}")
        print(f"   Genres: {genre_text}")
        print(f"   Matched your preference: {matched_text}")


if __name__ == "__main__":
    main()

