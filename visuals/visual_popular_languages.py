import plotly.express as px
import requests
import urllib.parse

# import fetch_github_repos from visual_main to reuse logic
# from visuals.visual_main import fetch_github_repos

def fetch_language_stars(language, min_stars=1000, top_n=30):
    """
    Fetch the total stars for the top repositories of a given language.
    Args:
        language (str): Programming language to search for.
        min_stars (int): Minimum stars for repositories to be included.
        top_n (int): Number of top repositories to consider.
    Returns:
        int: Total stars for the language's top repositories.
    """
    encoded_lang = urllib.parse.quote(language)
    url = f"https://api.github.com/search/repositories?q=language:{encoded_lang}+sort:stars+stars:>{min_stars}&per_page={top_n}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    print(f"Requesting: {url}")
    response = requests.get(url, headers=headers)
    print(f"Status code for {language}: {response.status_code}")
    if response.status_code != 200:
        print(f"GitHub API error for {language}: {response.status_code}")
        return 0
    data = response.json()
    items = data.get('items', [])
    print(f"{language}: found {len(items)} repos with >{min_stars} stars")
    if len(items) == 0:
        print(f"Raw response for {language}: {data}")
    return sum(repo.get('stargazers_count', 0) for repo in items)


def compare_languages(languages, min_stars=1000, top_n=30):
    """
    Compare total stars for a list of programming languages.
    Returns:
        dict: {language: total_stars}
    """
    stars_by_language = {}
    for lang in languages:
        print(f"Fetching stars for {lang}...")
        stars = fetch_language_stars(lang, min_stars=min_stars, top_n=top_n)
        stars_by_language[lang] = stars
    return stars_by_language


def plot_language_comparison(stars_by_language):
    """
    Plot a bar chart comparing languages by total stars.
    """
    langs = list(stars_by_language.keys())
    stars = list(stars_by_language.values())
    fig = px.bar(x=langs, y=stars, title='Most Popular Backend Languages on GitHub (by Stars)',
                 labels={'x': 'Programming Language', 'y': 'Total Stars'})
    fig.update_layout(title_x=0.5, title_font_size=24, xaxis_title_font_size=20, yaxis_title_font_size=20)
    fig.update_traces(marker_color='rgb(60, 100, 150)', marker_opacity=0.7)
    fig.show()


def main():
    # Only backend languages for comparison
    languages = [
    'python', 'java', 'go', 'c', 'c++', 'c#', 'ruby', 'php', 'rust', 'kotlin']
    stars_by_language = compare_languages(languages, min_stars=1000, top_n=30)
    print("\nTotal stars by language:")
    for lang, stars in stars_by_language.items():
        print(f"{lang}: {stars}")
    plot_language_comparison(stars_by_language)


if __name__ == "__main__":
    main() 